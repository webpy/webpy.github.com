---
layout: default
title: Deployment
---

# Deployment

The web server that gets started when you run a web.py program is nice, but for popular sites you're going to want something a little more serious. web.py implements WSGI and runs with everything that is compatible to it. WSGI is a common API between web servers and applications, analogous to Java's Servlet Interface. To run web.py with CGI, FastCGI or SCGI you will need to install flup (download here), which provides WSGI interfaces for those APIs.

For all the CGI variants, add this to the top of your `code.py`:

    #!/usr/bin/env python

And run `chmod +x code.py` to make it executable.

### LightTPD

#### .. with FastCGI

FastCGI with lighttpd is the recommended way of using web.py in production. [reddit.com][3] handles millions of hits this way.

   [3]: http://reddit.com/

Your lighttpd config can be something like:
    
     server.modules = ("mod_fastcgi", "mod_rewrite")
     server.document-root = "/path/to/root/"     
     fastcgi.server = ( "/code.py" =>     
     (( "socket" => "/tmp/fastcgi.socket",
        "bin-path" => "/path/to/root/code.py",
        "max-procs" => 1
     ))
     )
    
     url.rewrite-once = (
       "^/favicon.ico$" => "/static/favicon.ico",
       "^/static/(.*)$" => "/static/$1",
       "^/(.*)$" => "/code.py/$1"
     )
    
With some versions of lighttpd, it is important to ensure the "check-local" property of the fastcgi.server entry is set to "false", especially if your `code.py` is located outside of the document root.

If you get error messages about not being able to import flup, install it by typing "easy_install flup" at the command line.

Since revision 145, it is necessary to set a bin-environment variable on the fastcgi configuration if your code uses redirects.  If when your code redirects to http://domain.com/ and in the url bar you see http://domain.com/code.py/, you'll need to set the environment variable. This will cause your fastcgi.server configuration above to look something like this:
     
    fastcgi.server = ( "/code.py" =>
    ((
       "socket" => "/tmp/fastcgi.socket",
       "bin-path" => "/path/to/root/code.py",
       "max-procs" => 1,
       "bin-environment" => (
         "REAL_SCRIPT_NAME" => ""
       ),
       "check-local" => "disable"
    ))
    )
    

### Apache

#### .. with CGI


Add the following to `httpd.conf` or `apache2.conf`.

    Alias /foo/static/ /path/to/static
    ScriptAlias /foo/ /path/to/code.py


#### .. with CGI using .htaccess

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

Unfortunately, unlike lighttpd, Apache gives no hint that it wants your web.py script to act as a FastCGI server so you have to tell web.py explicitly. Add this to `code.py` before your `if __name__ == "__main__":` line:
    
    web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    
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

For Python 2.5 do this:

    cd /usr/lib/python2.5/wsgiref
    # or in windows: cd /python2.5/lib/wsgiref
    wget -O modpython_gateway.py http://projects.amor.org/misc/browser/modpython_gateway.py?format=raw
    # or fetch the file from that address using your browser

For Python <2.5 do this:

    cd /usr/lib/python2.4/site-packages
    # or in windows: cd /python2.4/lib/site-packages
    svn co svn://svn.eby-sarna.com/svnroot/wsgiref/wsgiref
    cd wsgiref
    wget -O modpython_gateway.py http://projects.amor.org/misc/browser/modpython_gateway.py?format=raw
    # or fetch the file from that address using your browser  


Rename your `code.py` to something like `codep.py` and add:
    
    main = web.wsgifunc(web.webpyfunc(urls, globals()))

In your `.htaccess`, add:
    
    
    AddHandler python-program .py
    PythonHandler wsgiref.modpython_gateway::handler
    PythonOption wsgi.application codep::main
    

You also probably want to add a `RewriteRule` pointing `/` to `/codep.py/`

Be sure to visit `/codep.py/` with the extra `/` on the end. Otherwise, you'll see an error message like `A server error occurred. Please contact the administrator.`

#### .. with mod_wsgi

mod\_wsgi is a new Apache module which [typically outperforms mod_python](http://code.google.com/p/modwsgi/wiki/PerformanceEstimates) for hosting WSGI applications, and is very easy to set up.

At the end of your `code.py`, add:

    app = web.application(urls, globals(), autoreload=False)
    application = app.wsgifunc()

mod\_wsgi offers [many possible ways](http://code.google.com/p/modwsgi/wiki/ConfigurationDirectives) to expose a WSGI application in Apache's URL hierarchy, but one simple way would be to add the following to your .htaccess:

    <Files code.py>
        SetHandler wsgi-script
        Options ExecCGI FollowSymLinks
    </Files>

If you get an "ImportError: No module named web" in your apache error.log file, you could try setting the absolute path in code.py before importing web:

    import sys, os
    abspath = os.path.dirname(__file__)
    sys.path.append(abspath)
    os.chdir(abspath)
    import web

Also, you might want to read the "Application Working Directory" section from [Common problems with WSGI application](http://code.google.com/p/modwsgi/wiki/ApplicationIssues).

It should then be accessible at `http://example.com/code.py/` as usual.

#### mod_rewrite Rules for Apache

If you want web.py to be accessible at 'http://example.com' instead of 'http://example.com/code.py/' add the following rules to the `.htaccess` file:

    <IfModule mod_rewrite.c>      
      RewriteEngine on
      RewriteBase /
      RewriteCond %{REQUEST_URI} !^/icons
      RewriteCond %{REQUEST_URI} !^/favicon.ico$
      RewriteCond %{REQUEST_URI} !^(/.*)+code.py/
      RewriteRule ^(.*)$ code.py/$1 [PT]
    </IfModule>

If the `code.py` is in the subfolder `myapp/`, adjust the RewriteBase to `RewriteBase /myapp/`. If you have static files like CSS files and images to pass through, duplicate the line with the icons for each path you want to allow.