---
layout: default
title: Webpy + Apache with mod_wsgi on Ubuntu
---

# Webpy + Apache with mod_wsgi on Ubuntu

The following steps were tested on:

1. Ubuntu 10.04, with Apache 2.2.16 and mod_wsgi 3.2-2, and
2. Ubuntu 12.04, with Apache 2.2.22 and mod_wsgi 3.3-4.

The same steps should work in other versions of Ubuntu as well.

Note:

* You may replace `appname` with your own project name.
* You may replace `code.py` with your own file name.
* `/var/www/webpy-app` found below refers to the path to the directory contains your code.py.
* `/var/www/webpy-app/code.py` is the full path to your python file.

### Steps:

1. Install mod_wsgi:
        
        sudo apt-get install libapache2-mod-wsgi

 This will install a `.so` module in Apache's **module directory**:

        /usr/lib/apache2/modules/mod_wsgi.so

 It will also automatically configure Apache to load the `mod_wsgi` module upon restart. You can confirm the presence of the module in Apache's **available modules directory**…

        /etc/apache2/mods-available/wsgi.conf
        /etc/apache2/mods-available/wsgi.load
 …as well as in Apache's **enabled modules directory**:

        /etc/apache2/mods-enabled/wsgi.conf
        /etc/apache2/mods-enabled/wsgi.load
        
2. Configure a website on Apache to load the `mod_wsgi` module. This can either be your default website, or another Virtual Host, which you can create by copying `/etc/apache2/sites-available/default` to something like `/etc/apache2/sites-available/my-website`. Add the following lines, under the `DocumentRoot` directive:

        WSGIScriptAlias /appname /var/www/webpy-app/code.py/
        AddType text/html .py

 Typically, the above two lines are the only ones necessary to serve a website built with web.py. Most probably, you will additionally need to define a subdirectory in your application, from which static files will be served. In this case, add:

        Alias /appname/static /var/www/webpy-app/static/

 After you have finished editing your website definition, you need to enable it (in case it is not already enabled). Do:
 
        sudo a2ensite my-website
        
3. Finally, create a sample file `/var/www/webpy-app/code.py`:

        import web

        urls = (
            '/.*', 'hello',
            )

        class hello:
            def GET(self):
                return "Hello, world."

        application = web.application(urls, globals()).wsgifunc()

4. Point your browser to 'http://your_server_name/appname' to verify whether it works for you.

### Note: mod_wsgi + sessions

If you use sessions with `mod_wsgi`, you should change your code like below:

    app = web.application(urls, globals())

    curdir = os.path.dirname(__file__)
    session = web.session.Session(app, web.session.DiskStore(os.path.join(curdir,'sessions')),)

    application = app.wsgifunc()

### mod_wsgi performance:
For mod_wsgi performance, please refer to mod_wsgi wiki page:

<http://code.google.com/p/modwsgi/wiki/PerformanceEstimates>
