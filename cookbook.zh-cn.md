---
layout: default
title: Web.py Cookbook 简体中文版
---

# Web.py Cookbook 简体中文版

欢迎来到web.py 0.3的Cookbook。提醒您注意：某些特性在之前的版本中并不可用。当前开发版本是0.3。

#格式

1. 在编排内容时，请尽量使用cookbook格式...如：
    
    ###问题：如何访问数据库中的数据？
     
    ###解法：使用如下代码...

1. 请注意，网址中不必含有"web"。如"/cookbook/select"，而非"/cookbook/web.select"。

1. 该手册适用于0.3版本，所以您在添加代码时，请确认代码能在新版本中工作。

1. 一些建议：不妨结合 *http://kanrs.com/* 学习web.py cookbook和tutorial，我(初译者wrongway)个人感觉很有帮助。


-------------------------------------------------

##基本应用:
* [Hello World](/helloworld/zh-cn)
* [提供静态文件访问](/staticfiles/zh-cn)
* [Understanding URL handling (未译)](/url_handling/zh-cn)
* [跳转与重定向](/redirect+seeother/zh-cn)
* [使用子应用](/subapp/zh-cn)
* [提供XML访问](/xmlfiles/zh-cn)
* [从post读取原始数据](/postbasic/zh-cn)

##高级应用
* [用web.ctx获得客户端信息](/ctx/zh-cn)
* [应用处理器，添加钩子和卸载钩子](/application_processors/zh-cn)
* [如何使用web.background](/background/zh-cn)
* [自定义NotFound信息](/custom_notfound/zh-cn)
* [如何流传输大文件](/streaming_large_files/zh-cn)
* [对自带的webserver日志进行操作](/logging/zh-cn)
* [用cherrypy提供SSL支持](/ssl/zh-cn)
* [实时语言切换](/runtime-language-switch/zh-cn)

##Sessions and user state:
* [如何使用Session](/sessions/zh-cn)
* [如何在调试模式下使用Session](/session_with_reloader/zh-cn)
* [在template中使用session](/session_in_template/zh-cn)
* [如何操作Cookie](/cookies/zh-cn)
* [用户认证](/userauth/zh-cn)
* [一个在postgreSQL数据库环境下的用户认证的例子](/userauthpgsql/zh-cn)
* [如何在子应用中操作Session](/sessions_with_subapp/zh-cn)


##Utils:
* [如何发送邮件](/sendmail/zh-cn)
* [如何利用Gmail发送邮件](/sendmail_using_gmail/zh-cn)
* [使用soaplib实现webservice](/webservice/zh-cn)

##Templates:
* [Templetor: web.py 模板系统](http://webpy.org/docs/0.3/templetor/zh-cn)
* [Using Site Layout Templates (未译)](/layout_template/zh-cn)
* [Alternating Style (未译)](/alternating_style/zh-cn)
* [Import functions into templates (未译)](/template_import/zh-cn)
* [i18n support in template file (未译)](/i18n_support_in_template_file/zh-cn)
* [Use Mako template engine in webpy ](/template_mako/zh-cn)
* [Use Cheetah template engine in webpy (未译)](/template_cheetah/zh-cn)
* [Use Jinja2 template engine in webpy (未译)](/template_jinja/zh-cn)
* [How to use templates on Google App Engine (未译)](/templates_on_gae/zh-cn)

##Testing:
* [Testing with Paste and Nose (未译)](/testing_with_paste_and_nose/zh-cn)
* [RESTful doctesting using an application's request method (未译)](/restful_doctesting_using_request/zh-cn)

##User Input:
* [File Upload (未译)](/fileupload/zh-cn)
* [Store an uploaded file (未译)](/storeupload/zh-cn)
* [How to put a limit of size of uploaded files (未译)](/limiting_upload_size/zh-cn)
* [通过 web.input 接受用户输入](/input/zh-cn)
* [How to use forms (未译)](/forms/zh-cn)
* [Render individual form fields (未译)](/form_fields/zh-cn)

##Database:
* [多数据库操作](/multidbs/zh-cn)
* [Select: Retrieving entries from a database (未译)](/select/zh-cn)
* [Update: Updating entries in a database (未译)](/update/zh-cn)
* [Delete: Remove entries in a database (未译)](/delete/zh-cn)
* [Insert: Adding entries to a database (未译)](/Insert/zh-cn) 
* [Query: Advanced database queries (未译)](/query/zh-cn)
* [How to use database transactions (未译)](/transactions/zh-cn)
* [Using sqlalchemy (未译)](/sqlalchemy/zh-cn)
* [Integrating SQLite UDF (user-defined-functions) with webpy database layer (未译)](/sqlite-udf/zh-cn)
* [Using a dictionary as where clause (未译)](/where_dict/zh-cn)

##Deployment:
* [Fastcgi deployment through lighttpd (未译)](/fastcgi-lighttpd/zh-cn)
* [Fastcgi deployment through Apache (未译)](/fastcgi-apache/zh-cn) 
* [CGI deployment through Apache (未译)](/cgi-apache/zh-cn)
* mod_python deployment through Apache (requested)
* [mod_wsgi deployment through Apache (未译)](/mod_wsgi-apache/zh-cn)
* [mod_wsgi deployment through Nginx (未译)](/mod_wsgi-nginx/zh-cn)
* [Fastcgi deployment through Nginx (未译)](/fastcgi-nginx/zh-cn)

##Subdomains:
* Subdomains and how to access the username (requested)