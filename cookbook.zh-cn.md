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

1. 最后，该手册适用于0.3版本，所以您在添加代码时，请确认代码能在新版本中工作。
-------------------------------------------------

##基本应用:
* [Hello World](/cookbook/zh-cn/helloworld)
* [Serving Static Files 提供静态文件](/cookbook/zh-cn/staticfiles)
* [Seeother and Redirect(重定向)](/cookbook/zh-cn/redirect+seeother)
* [using subapplications 使用子应用](/cookbook/zh-cn/subapp)
* [Serving XML 提供XML](/cookbok/zh-cn/xmlfiles)

##高级应用
* [web.ctx](/cookbook/zh-cn/ctx)
* [Application processors, loadhooks and unloadhooks 应用处理器，添加钩子和卸载钩子](/cookbook/zh-cn/application_processors)
* [How to use web.background 如何使用web.background](/cookbook/zh-cn/background)
* [Custom NotFound message](/cookbook/zh-cn/custom_notfound)
* [How to Stream Large Files](/cookbook/zh-cn/streaming_large_files)
* [Control over logging for default HTTPServer](/cookbook/zh-cn/logging)
* [SSL support in built-in cherrypy server](/cookbook/zh-cn/ssl)

##Sessions and user state:
* [Working with Session (未译)](/cookbook/sessions)
* [Using session with reloader (未译)](/cookbook/session_with_reloader)
* [Working with Cookies (未译)](/cookbook/cookies)
* [User authentication (未译)](/cookbook/userauth)
* [User authentication with Postgresql database (未译)](/cookbook/userauthpgsql)
* [Sessions with sub-apps (未译)](/cookbook/sessions_with_subapp)


##Utils:
* [Sending Mail (未译)](/cookbook/sendmail)
* [Sending Mail Using Gmail (未译)](/cookbook/sendmail_using_gmail)
* [Webservice using soaplib + WSDL (未译)](/cookbook/webservice)

##Templates:
* [Templetor: The web.py templating system (未译)](http://webpy.org/docs/0.3/templetor )
* [Using Site Layout Templates (未译)](/cookbook/layout_template)
* [Alternating Style (未译)](/cookbook/alternating_style)
* [i18n support in template file (未译)](/cookbook/i18n_support_in_template_file )
* [Use Mako template engine in webpy (未译)](/cookbook/template_mako)
* [Use Cheetah template engine in webpy (未译)](/cookbook/template_cheetah)
* [[cookbook/template_jinja|Use Jinja2 template engine in webpy (未译)
* [How to use templates on Google App Engine (未译)](/cookbook/templates_on_gae)

##Testing:
* [Testing with Paste and Nose (未译)](/cookbook/testing_with_paste_and_nose)
* [RESTful doctesting using an application's request method (未译)](/cookbook/restful_doctesting_using_request)

##User Input:
* [File Upload (未译)](/cookbook/fileupload)
* [Store an uploaded file (未译)](/cookbook/storeupload)
* [How to put a limit of size of uploaded files (未译)](/cookbook/limiting_upload_size)
* [Accessing user input through web.input (未译)](/cookbook/input)
* [How to use forms (未译)](/cookbook/forms)
* [Render individual form fields (未译)](/cookbook/form_fields)

##Database:
* [Multiple databases (未译)](/cookbook/multidbs)
* [Select: Retrieving entries from a database (未译)](/cookbook/select)
* [Update: Updating entries in a database (未译)](/cookbook/update)
* [Delete: Remove entries in a database (未译)](/cookbook/delete)
* [Insert: Adding entries to a database (未译)](/Insert) 
* [Query: Advanced database queries (未译)](/cookbook/query)
* [How to use database transactions](/cookbook/transactions)
* [Using sqlalchemy](/cookbook/sqlalchemy)
* [Integrating SQLite UDF (user-defined-functions) with webpy database layer](/cookbook/sqlite-udf)


##Deployment:
* [Fastcgi deployment through lighttpd (未译)](/cookbook/fastcgi-lighttpd)
* [Fastcgi deployment through Apache (未译)](/cookbook/fastcgi-apache) 
* [CGI deployment through Apache (未译)](/cookbook/cgi-apache)
* mod_python deployment through Apache (requested)
* [mod_wsgi deployment through Apache (未译)](/cookbook/mod_wsgi-apache )
* [mod_wsgi deployment through Nginx (未译)](/cookbook/mod_wsgi-nginx )
* [Fastcgi deployment through Nginx (未译)](/cookbook/fastcgi-nginx)

##Subdomains:
* Subdomains and how to access the username (requested)