---
layout: default
title: 通过Gunicorn在Apache和Nginx下部署
---

# 通过Gunicorn在Apache和Nginx下部署

下面的代码基于Gunicorn 0.14.6在Debian 6.0.6和FreeBSD 9.0系统下测试。
目前最新版本的Gunicorn在使用方法上没有区别。
其它Linux发行版、各种BSD、Mac OS X等系统应该也没问题。
但不推荐Windows系统，虽然我没用过，但目测会多很多不必要的困难。

##Note:  
* 你可以重命名 <code>code.py</code>为任何你自己愿意的名字，该例子还是以code.py为例。
* <code>/path-to/webpy-app</code> 为包含你的 <code>code.py</code>代码的路径。
* <code>/path-to/webpy-app/code.py</code> 应该是你的**python file**的完整路径。

可以在命令行运行 gunicorn --version 查看当前gunicorn的版本。

###安装Gunicorn

参见Gunicorn官网：

http://gunicorn.org/#quickstart

官网的建议是用virtualenv方式安装，这是个好方法。这里不再介绍virtualenv（个人推荐用virtualenvwrapper），
以下以已安装好的virtualenv环境为例介绍，当然你也可以跳过virtualenv，直接全局安装（需要加上sudo）。

<pre>
pip install gunicorn
</pre>

##用Gunicorn部署web.py应用

当然不止是web.py应用，Gunicorn是用于部署wsgi应用的，任何支持wsgi的应用都可以。

整个部署过程分为两个部分：

* 用Gunicorn运行web.py/wsgi应用
* 配置web server前端的反向代理

###用Gunicorn运行web.py应用

前面已经说过，Gunicorn是用来部署wsgi应用的，所以首先要修改code.py，使之成为一个wsgi应用。

<pre>
#  ...
app = web.application(urls, globals())
#  在这里加入下面这句，即可
application = app.wsgifunc()
</pre>

最简单的运行方式就是：

<code>gunicorn code:application</code>

其中code就是指code.py，application就是那个wsgifunc的名字。

这样运行的话，gunicorn默认作为了个监听 127.0.0.1:8000 的web server，可以在本机通过： 
<code>http://127.0.0.1:8000</code> 访问。

如果要通过网络访问，则需要绑定不同的地址（需要改变端口也可以）：

<code>gunicorn -b 192.168.0.123:8080 code:application</code>

在多核服务器上，为了支持更多的并发访问并充分利用资源，可以使用更多的 gunicorn 进程：

<code>gunicorn -w 8 code:application</code>

这样就可以启动8个进程同时处理HTTP请求，提高系统响应性能。

另外， gunicorn 默认使用同步阻塞的网络模型(-k sync)，对于大并发的访问可能表现不够好，
它还支持其它更好的模式，比如：gevent或meinheld。

<pre>
#  gevent
gunicorn -k gevent code:application
#  meinheld
gunicorn -k egg:meinheld#gunicorn_worker code:application
</pre>

当然，要使用这两个东西需要另外安装，具体请参考各自的文档。

###配置Apapache的反向代理

简单的反向代理配置如下（以在VirtualHost里为例）：

<pre>
    ProxyPass / http://127.0.0.1:8000/
    ProxyPassReverse / http://127.0.0.1:8000/
    ProxyPreserveHost On
    ProxyErrorOverride Off
</pre>

将对根路径的所有访问请求全部代理到 <code>http://127.0.0.1:8000</code> 的 gunicorn 服务上。

###配置Nginx的反向代理

简单的反向代理配置如下（同样是以virtual host为例）：

<pre>
    location / {
        try_files $uri @test;
    }

    location @test {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $http_host;
        proxy_pass http://127.0.0.1:8000;
    } 
</pre>

将对根路径的所有访问请求全部代理到 <code>http://127.0.0.1:8000</code> 的 gunicorn 服务上。

实际应用中可能需要设置更多的 proxy_set_header 变量，视应用需求而定。
