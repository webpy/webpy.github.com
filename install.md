---
layout: default
title: Install
---

# Install

To install web.py, download:
    
    http://webpy.org/web.py-0.2.tar.gz

extract it and copy the _web_ folder into a directory where your application is. Or, to make it accessible to all applications, run:
    
    python setup.py install

Note: on some unix like systems you may need to switch to root or run:

    sudo python setup.py install

see [recomended setup](/recommended_setup).

## Development

webpy comes with a built-in webserver.  Learn how write an application by following the [tutorial](http://webpy.infogami.com/tutorial2).  When you have an application written, put your code into `code.py` and start the server like this:

     python code.py

Open your browser and go to [http://localhost:8080/](http://localhost:8080/) to view the page. To specify another port, use `python code.py 1234`.

## Production

The web server that gets started when you run a web.py program is nice, but for popular sites you're going to want something a little more serious. web.py implements [WSGI](http://www.python.org/dev/peps/pep-0333/) and runs with everything that is compatible to it. WSGI is a common API between web servers and applications, analogous to Java's Servlet Interface. To run web.py with CGI, FastCGI or SCGI you will need to install [flup](http://www.saddi.com/software/flup/dist/), which provides WSGI interfaces for those APIs.

For all the CGI variants, add this to the top of your `code.py`:

    #!/usr/bin/env python

And run `chmod +x code.py` to make it executable.

### LightTPD

#### .. with FastCGI

FastCGI with lighttpd is the recommended way of using web.py in production. [reddit.com][3] handles millions of hits this way.

   [3]: http://reddit.com/

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

If you get error messages about not being able to import flup, install it by typing "easy_install flup" at the command line.

### Apache

#### .. with CGI

CGI is easy to configure, but is not suitable for high-performance websites.
Add this to your `.htaccess`:

    Options +ExecCGI
    AddHandler cgi-script .py

and point your browser to `http://example.com/code.py/`. Don't forget the trailing slash, otherwise you'll see a `not found` message (because the `urls` list you defined do not match anything). To make things work without having to enter `code.py`, enable mod_rewrite rules (see below).

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

#### .. with FastCGI

FastCGI is easy to configure and performs as well as mod_python.

Add this to your `.htaccess`:
    
    <Files code.py>      SetHandler fastcgi-script
    </Files>
Unfortunately, unlike lighttpd, Apache gives no hint that it wants your web.py script to act as a FastCGI server so you have to tell web.py explicitly. Add this to `code.py`:
    
    web.runwsgi = web.runfcgi
    
and point your browser to `http://example.com/code.py/`. Don't forget the trailing slash, otherwise you'll see a `not found` message (because the `urls` list you defined do not match anything). To make things work without having to enter `code.py`, enable mod_rewrite rules (see below).

[Walter has some additional advice](http://lemurware.blogspot.com/2006/05/webpy-apache-configuration-and-you.html).

#### .. with SCGI
https://www.mems-exchange.org/software/scgi/
download `mod_scgi` source here: http://www.mems-exchange.org/software/files/mod_scgi/
windows apache user: 
edit your httpd.conf:

    LoadModule scgi_module Modules/mod_scgi.so
    SCGIMount / 127.0.0.1:8080

restart apache and then start your code.py in the command below:

    python code.py 127.0.0.1:8080 scgi

and open you browser,visit 127.0.0.1
It's ok! 

#### .. with mod_python

mod_python performs as well as FastCGI, but is not as straight-forward to configure.

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

#### mod_rewrite Rules for Apache

Add the following rules to the `.htaccess` file:

    <IfModule mod_rewrite.c>      RewriteEngine on
      RewriteBase /
      RewriteCond %{REQUEST_URI} !^/icons
      RewriteCond %{REQUEST_URI} !^/favicon.ico$
      RewriteCond %{REQUEST_URI} !^(/.*)+code.py/
      RewriteRule ^(.*)$ code.py/$1 [PT]
    </IfModule>
If the `code.py` is in the subfolder `myapp/`, adjust the RewriteBase to `RewriteBase /myapp/`. If you have static files like CSS files and images to pass through, duplicate the line with the icons for each path you want to allow.
