---
layout: default
title: Install guide
---

# Install guide

Other languages : [español](/install.es) | [Japan 日本語 ](/install.ja) | [chinese 简体中文 ](/install.zh-cn) | [italiano](/install.it) | [français](/install.fr) | [Serbo-Croatian](http://science.webhostinggeeks.com/webpy-vodic-za-instalaciju)

## Summary

* <a href="#install">Install</a>
	* <a href="#macosx">.. on MacOS X</a>
* <a href="#dev">Development</a>
* <a href="#prod">Production</a>
	* <a href="#lighttpd">LightTPD</a>
		* <a href="#lighttpdfastcgi">.. with FastCGI</a>
	* <a href="#apache">Apache</a>
		* <a href="#apachecgi">.. with CGI</a>
		* <a href="#apachecgihtaccess"> .. with CGI using .htaccess</a>
		* <a href="#apachefastcgi">.. with FastCGI</a>
		* <a href="#apachescgi">.. with SCGI</a>
		* <a href="#apachemodpython">.. with mod_python</a>
		* <a href="#apachemodwsgi">.. with mod_wsgi</a>
		* <a href="#apachemodrewrite">.. with mod_rewrite</a>


<a name="install"></a>
## Install


To install web.py, download:
    
    http://webpy.org/static/web.py-0.37.tar.gz

or the get the latest dev version:

    https://github.com/webpy/webpy/tarball/master

extract it and copy the _web_ folder into a directory where your application is. Or, to make it accessible to all applications, run:
    
    python setup.py install

Note: on some unix like systems you may need to switch to root or run:

    sudo python setup.py install

see [recommended setup](/recommended_setup).

Another option is to use [Easy Install](http://peak.telecommunity.com/DevCenter/EasyInstall). Once Easy Install is properly setup:


    sudo easy_install web.py
    
Or [PIP](http://packages.python.org/distribute/)

    sudo pip install web.py

<a name="macosx"></a>
### MacOS X

To install web.py on  [mac os x](/install_macosx). Web.py 0.1 only...

<a name="dev"></a>
## Development

web.py comes with a built-in webserver.  Learn how to write an application by following the [tutorial](http://webpy.org/tutorial).  When you have an application written, put your code into `code.py` and start the server like this:

     python code.py

Open your browser and go to [http://localhost:8080/](http://localhost:8080/) to view the page. To specify another port, use `python code.py 1234`.

<a name="prod"></a>
## Production

The web server that gets started when you run a web.py program is nice, but for popular sites you're going to want something a little more serious. web.py implements [WSGI](http://www.python.org/dev/peps/pep-0333/) and runs with everything that is compatible to it. WSGI is a common API between web servers and applications, analogous to Java's Servlet Interface. To run web.py with CGI, FastCGI or SCGI you will need to install [flup](http://trac.saddi.com/flup) ([download here](http://www.saddi.com/software/flup/dist/)), which provides WSGI interfaces for those APIs. 

For all the CGI variants, add this to the top of your `code.py`:

    #!/usr/bin/env python

And run `chmod +x code.py` to make it executable.

<a name="lighttpd"></a>
### LightTPD

<a name="lighttpdfastcgi"></a>
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
    
<a name="apache"></a>
### Apache

<a name="apachecgi"></a>
#### .. with CGI


Add the following to `httpd.conf` or `apache2.conf`.

    Alias /foo/static/ /path/to/static
    ScriptAlias /foo/ /path/to/code.py

<a name="apachecgihtaccess"></a>
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
        """        
        _wrappedstdout = sys.stdout
    
        sys.stdout = web._oldstdout
        cgitb.handler()
    
        sys.stdout = _wrappedstdout
    
    web.internalerror = cgidebugerror


<a name="apachefastcgi"></a>
#### .. with FastCGI

FastCGI is easy to configure and performs as well as mod_python.

Add this to your `.htaccess`:
    
    <Files code.py>      
    SetHandler fastcgi-script
    </Files>

Unfortunately, unlike lighttpd, Apache gives no hint that it wants your web.py script to act as a FastCGI server so you have to tell web.py explicitly. Add this to `code.py` before your `if __name__ == "__main__":` line:
    
    web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    
and point your browser to `http://example.com/code.py/`. Don't forget the trailing slash, otherwise you'll see a `not found` message (because the `urls` list you defined do not match anything). To make things work without having to enter `code.py`, enable mod_rewrite rules (see below).

[Walter has some additional advice](http://lemurware.blogspot.com/2006/05/webpy-apache-configuration-and-you.html).


<a name="apachescgi"></a>
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


<a name="apachemodpython"></a>
#### .. with mod_python

mod_python performs as well as FastCGI, but is not as straight-forward to configure.

For Python 2.5 do this:

    cd /usr/lib/python2.5/wsgiref
    # or in windows: cd /python2.5/lib/wsgiref
    wget -O modpython_gateway.py http://svn.aminus.net/misc/modpython_gateway.py
    # or fetch the file from that address using your browser

For Python <2.5 do this:

    cd /usr/lib/python2.4/site-packages
    # or in windows: cd /python2.4/lib/site-packages
    svn co svn://svn.eby-sarna.com/svnroot/wsgiref/wsgiref
    cd wsgiref
    wget -O modpython_gateway.py http://svn.aminus.net/misc/modpython_gateway.py
    # or fetch the file from that address using your browser  


Rename your `code.py` to something like `codep.py` and add:
    
    app = web.application(urls, globals())
    main = app.wsgifunc()

In your `.htaccess`, add:
    
    
    AddHandler python-program .py
    PythonHandler wsgiref.modpython_gateway::handler
    PythonOption wsgi.application codep::main
    

You also probably want to add a `RewriteRule` pointing `/` to `/codep.py/`

Be sure to visit `/codep.py/` with the extra `/` on the end. Otherwise, you'll see an error message like `A server error occurred. Please contact the administrator.`

<a name="apachemodwsgi"></a>
#### .. with mod_wsgi

mod\_wsgi is a new Apache module which [typically outperforms mod_python](http://code.google.com/p/modwsgi/wiki/PerformanceEstimates) for hosting WSGI applications, and is very easy to set up. <div style="text-indent:-90000px;">[Watch Live Sports Online](http://www.sportspiks.com)[Watch tv episodes online](http://purehunting.blogspot.com)[Watch movies Online](http://www.overheadmovies.com)[Watch Resident Evil Afterlife (2010) Online](http://www.overheadmovies.com/action/resident-evil-afterlife-2010)</div>

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



<a name="apachemodrewrite"></a>
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
