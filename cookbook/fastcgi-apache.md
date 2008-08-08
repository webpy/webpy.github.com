---
layout: default
title: Web.py using FastCGI and Apache 2
---

# Web.py using FastCGI and Apache 2

#Requirements
* Apache 2.x
* [mod_fcgid](http://fastcgi.coremail.cn/)
* [mod_rewrite](http://httpd.apache.org/docs/2.0/rewrite/)
* [Flup](http://trac.saddi.com/flup)

#Apache Configuration
    LoadModule rewrite_module modules/mod_rewrite.so
    LoadModule fcgid_module modules/mod_fcgid.so

    SocketPath /tmp/fcgidsock
    SharememPath /tmp/fcgid_shm

    Alias / "/var/www/myapp/code.py/"
    <Directory "/var/www/myapp/">
        allow from all
        SetHandler fcgid-script    
        Options ExecCGI
        AllowOverride None
    </Directory>

    <IfModule mod_rewrite.c>      
        RewriteEngine on
        RewriteBase /
        RewriteCond %{REQUEST_URI} !^/icons
        RewriteCond %{REQUEST_URI} !^/favicon.ico$
        RewriteCond %{REQUEST_URI} !^(/.*)+code.py/
        RewriteRule ^(.*)$ code.py/$1 [PT]
    </IfModule>


#Hello World
Note the following line is required:
web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)

    #!/usr/bin/python

    import web

    urls = ("/.*", "hello")
    app = web.application(urls, globals())

    class hello: 
        def GET(self):
        return 'Hello, world!'

    web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    if __name__ == "__main__":
        app.run()


#Run
1. Start your server. 
1. Open your application with your browser
1. To confirm your application is running try:

<code>
 ps aux | grep code.py
</code>


#Misc

After updating your application you may need to restart your web server to see the changes.


