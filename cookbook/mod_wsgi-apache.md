---
layout: default
title: Webpy + Apache with mod_wsgi
---

# Webpy + Apache with mod_wsgi

The following steps were tested on Apache-2.2.3 (Red Hat Enterprise Linux 5.2, x86_64), mod_wsgi-2.0.

Note:

* You may replace 'appname' with your own project name.
* You may replace code.py with your own file name.
* /var/www/webpy-app found below refers to the path to the directory contains your code.py
* /var/www/webpy-app/code.py is the full path to your python file

Steps:

* Download and install mod_wsgi from its website: [http://code.google.com/p/modwsgi/](http://code.google.com/p/modwsgi/). It will install a '.so' module in Apache module directory. e.g.

        /usr/lib64/httpd/modules/

* Configure Apache to load mod_wsgi module and your project in httpd.conf:

        LoadModule wsgi_module modules/mod_wsgi.so

        WSGIScriptAlias /appname /var/www/webpy-app/code.py/

        Alias /appname/static /var/www/webpy-app/static/
        AddType text/html .py

        <Directory /var/www/webpy-app/>
            Order deny,allow
            Allow from all
        </Directory>

* Sample file 'code.py':

        import web

        urls = (
            '/.*', 'hello',
            )

        class hello:
            def GET(self):
                return "Hello, world."

        application = web.application(urls, globals()).wsgifunc()

* Point your browser to 'http://your_server_name/appname' to verify whether it works for you.

#Note: mod_wsgi + sessions

If you use sessions with mod_wsgi, you should change you code like below:

    app = web.application(urls, globals())

    curdir = os.path.dirname(__file__)
    session = web.session.Session(app, web.session.DiskStore(os.path.join(curdir,'sessions')),)

    application = app.wsgifunc()

#mod_wsgi performance:
For mod_wsgi performance, please refer to mod_wsgi wiki page:

<http://code.google.com/p/modwsgi/wiki/PerformanceEstimates>