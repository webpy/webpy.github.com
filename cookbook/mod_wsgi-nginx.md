---
layout: default
title: deploying web.py with nginx and mod_wsgi
---

# deploying web.py with nginx and mod_wsgi

It is possible to deploy web.py with nginx using a mod_wsgi similar to the module for Apache.

After compiling and installing nginx with mod_wsgi, you can easily get a web.py app up and running with the following config:


    wsgi_python_executable  /usr/bin/python;
    server {
        listen 0.0.0.0;
        server_name domain_name.com www.domain_name.com;

        include /etc/nginx/wsgi_vars;
        location / {
            wsgi_pass /path/to/your/webpy/app     
         }
    }


Helpful links:
http://nginx.net/
http://wiki.codemongers.com/NginxNgxWSGIModule
