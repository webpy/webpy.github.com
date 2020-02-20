---
layout: default
title: 使用 Nginx 加 mod_wsgi 模块部署 web.py
---

# 使用 Nginx 加 mod_wsgi 模块部署 web.py

与 Apache 加载模块部署 web.py 程序类似，通过 Nginx 加 mod_wsgi 模块也可以部署 web.py 程序。

在编译并安装好 Nginx 的 mod_wsgi 模块后，使用下面配置文件提供的形式(注意需要修改相应的配置和路径)，即可部署一个 web.py 应用程序。


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


*注意：本段配置是 mod_wsgi 方式部署Web应用程序的示例，不是 Nginx 配置的完整信息。

参考链接:<br />
[ Nginx Website](http://nginx.net/ )<br />
[ Wiki page on mod_wsgi](http://wiki.codemongers.com/NginxNgxWSGIModule )
