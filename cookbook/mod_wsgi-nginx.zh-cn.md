---
layout: default
title: 使用nginx加mod_wsgi模块部署web.py
---

# 使用nginx加mod_wsgi模块部署web.py

与Apache加载模块部署web.py程序类似，通过nginx加mod_wsgi模块也可以部署web.py程序。

在编译并安装好nginx的mod_wsgi模块后，使用下面配置文件提供的形式(注意需要修改相应的配置和路径)，即可部署一个web.py应用程序。


    wsgi_python_executable  /usr/bin/python;

    server {
        listen 80;
        server_name www.domain_name.com domain_name.com;
        root /path/to/your/webpy;

        include /etc/nginx/wsgi_vars;
        location / {
            wsgi_pass /path/to/your/webpy/app.py;
         }
    }


*注意：本段配置是mod_wsgi方式部署Web应用程序的示例，不是nginx配置的完整信息。

参考链接:<br />
[ nginx website](http://nginx.net/ )<br />
[ wiki page on mod_wsgi](http://wiki.codemongers.com/NginxNgxWSGIModule )
