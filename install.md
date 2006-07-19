---
layout: default
title: Install
---

# Install

To install web.py, download:
    
    http://webpy.org/web.py

into the directory where your application is. Or, to make it accessible to all applications, to your Python site-packages directory. To find where that is, run:
    
    python -c "import sys; print[x for x in sys.path if x.endswith('site-packages')][-1]"
## Development

webpy comes with a built-in webserver. Put your code into `code.py` and start the server like this:

     $ python code.py
     Launching server: http://0.0.0.0:8080/

Open your browser and go to [http://localhost:8080/](http://localhost:8080/) to view the page. To specify another port, use `python code.py 1234`. 

## Production

The web server that gets started when you run a web.py program is nice, but for popular sites you're going to want something a little more serious.

web.py implements [WSGI](http://www.python.org/dev/peps/pep-0333/) and runs with everything that is compatible to it. WSGI is a common API between web servers and applications, much like Java Servlets. To run web.py with FastCGI, SCGI or AJP, you will need to install [flup](http://www.saddi.com/software/flup/dist/), which provides WSGI interfaces for those APIs.

### FastCGI

FastCGI with lighttpd is the recommended way of using web.py in production. [reddit.com][3] handles millions of hits this way.

   [3]: http://reddit.com/

To the top of your `code.py` add:
    
    #!/usr/bin/env python

And run `chmod +x code.py`

#### lighttpd

Your lighttpd config can be something like:
    
     server.modules = ("mod_fastcgi", "mod_rewrite")
     server.document-root = "/path/to/root/"     fastcgi.server = ( "/code.py" =>     (( "socket" => "/tmp/fastcgi.socket",
        "bin-path" => "/path/to/root/code.py",
        "max-procs" => 1
     ))
     )
    
     url.rewrite-once = (
       "^/favicon.ico$" => "/static/favicon.ico",
       "^/static/(.*)$" => "/static/$1",
       "^/(.*)$" => "/code.py/$1",
     )
    
With some versions of lighttpd, it is important to ensure the "check-local" property of the fastcgi.server entry is set to "false", especially if your `code.py` is located outside of the document root.

#### Apache

If you want to use FastCGI with Apache instead, just install `mod_fastcgi` and use a `.htaccess` like:
    
    
    <Files code.py>    SetHandler fastcgi-script
    </Files>    

Unfortunately, unlike lighttpd, Apache gives no hint that it wants your web.py script to act as a FastCGI server so you have to tell web.py explicitly. Add this to `code.py`:
    
    
    web.runwsgi = web.runfcgi
    

[Walter has some additional advice](http://lemurware.blogspot.com/2006/05/webpy-apache-configuration-and-you.html).

### mod_python

mod_python installs are a little more complicated:
    
    
    svn co svn://svn.eby-sarna.com/svnroot/wsgiref/
    cd wsgiref
    python setup.py install # as root
    cd /usr/lib/python2.3/site-packages/wsgiref/ # or whatever the path
    wget -O modpython_gateway.py http://projects.amor.org/misc/browser/modpython_gateway.py?format=raw
    

(Note: be sure not to install wsgiref as an easy_install egg or Apache won't be happy.)

Rename your `code.py` to something like `codep.py` and add:
    
    main = web.wsgifunc(web.webpyfunc(urls))

In your `.htaccess`, add:
    
    
    AddHandler python-program .py
    PythonHandler wsgiref.modpython_gateway::handler
    PythonOption wsgi.application codep::main
    

You also probably want to add a `RewriteRule` pointing `/` to `/codep.py/`

Be sure to visit `/codep.py/` with the extra `/` on the end. Otherwise, you'll see an error message like `A server error occurred. Please contact the administrator.`

### CGI

Note: You'll still need `flup` installed.

Note: The way `web.py` is implemented breaks the `cgitb` module because it captures `stdout`. I worked around the issue by using this:
    
    import cgitb; cgitb.enable()
    import sys
    
    # ... import web etc here...
    
    def cgidebugerror():
        """                                                                         
        """        _wrappedstdout = sys.stdout
    
        sys.stdout = web._oldstdout
        cgitb.handler()
    
        sys.stdout = _wrappedstdout
    
    web.internalerror = cgidebugerror
