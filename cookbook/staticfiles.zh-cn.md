---
layout: default
title: 提供静态文件 (诸如js脚本, css样式表和图象文件)
---

# 提供静态文件 (诸如js脚本, css样式表和图象文件)

## 问题
如何在web.py自带的web server中提供静态文件访问？

## 解法

### web.py 服务器
在当前应用的目录下，创建一个名为static的目录，把要提供访问的静态文件放在里面即可。

例如, 网址 <code>http://localhost/static/logo.png</code> 将发送 <code>./static/logo.png</code> 给客户端。

### Apache
在 Apache 中可以使用 [Alias](http://httpd.apache.org/docs/2.2/mod/mod_alias.html#alias) 指令，在处理 web.py 之前将请求映射到指定的目录。

这是一个在 Unix like 系统上虚拟主机配置的例子：

    <VirtualHost *:80>
        ServerName example.com:80
        DocumentRoot /doc/root/
        # mounts your application if mod_wsgi is being used
        WSGIScriptAlias / /script/root/code.py
        # the Alias directive
        Alias /static /doc/root/static
        
        <Directory />
            Order Allow,Deny
            Allow From All
            Options -Indexes
        </Directory>
        
        # because Alias can be used to reference resources outside docroot, you
        # must reference the directory with an absolute path
        <Directory /doc/root/static>
            # directives to effect the static directory
            Options +Indexes
        </Directory>
    </VirtualHost>
