---
layout: default
title: Web.py Cookbook
---

# Web.py Cookbook

Cookbook style documentation for web.py 0.3. Note that some of these features aren't available in previous versions.  Currently version 0.3 is the development branch.

#Formatting

1. In terms of formatting, please try to use a cookbook-like format...that is:
    
    ###Problem: You want to access data from database.
     
    ###Solution: Use this code...

1. Note that the urls don't need "web" in them -- just "/cookbook/select" , not "/cookbook/web.select".  

1. Finally, this documentation is for version 0.3, so please only add code that you know works with the new version.

-------------------------------------------------

##Basics:
* [Hello World](/cookbook/helloworld)
* [Serving Static Files](/cookbook/staticfiles)
* [Seeother and Redirect](/cookbook/redirect+seeother)
* [using subapplications](/cookbook/subapp)
* [Serving XML](/cookbok/xmlfiles)

##Advanced
* [web.ctx](/cookbook/ctx)
* [Application processors, loadhooks and unloadhooks](/cookbook/application_processors)
* [How to use web.background](/cookbook/background)
* [Custom NotFound message](/cookbook/custom_notfound)
* [How to Stream Large Files](/cookbook/streaming_large_files)
* [Control over logging for default HTTPServer](/cookbook/logging)

##Sessions and user state:
* [Working with Session](/cookbook/sessions)
* [Using session with reloader](/cookbook/session_with_reloader)
* [Working with Cookies](/cookbook/cookies)
* [User authentication](/cookbook/userauth)

##Utils:
* [Sending Mail](/cookbook/sendmail)
* [Sending Mail Using Gmail](/cookbook/sendmail_using_gmail)

##Templates:
* [Templetor: The web.py templating system](http://webpy.org/docs/0.3/templetor )
* [Using Site Layout Templates](/cookbook/layout_template)
* [Alternating Style](/cookbook/alternating_style)
* [i18n support in template file](/cookbook/i18n_support_in_template_file )
* [Use Mako template engine in webpy](/cookbook/template_mako)
* [Use Cheetah template engine in webpy](/cookbook/template_cheetah)
* [Use Jinja2 template engine in webpy](/cookbook/template_jinja)
* [How to use templates on Google App Engine](/cookbook/templates_on_gae)

##Testing:
* [Testing with Paste and Nose](/cookbook/testing_with_paste_and_nose)

##User Input:
* [File Upload](/cookbook/fileupload)
* [Store an uploaded file](/cookbook/storeupload)
* [How to put a limit of size of uploaded files](/cookbook/limiting_upload_size)
* [Accessing user input through web.input](/cookbook/input)
* [How to use forms](/cookbook/forms)
* [Render individual form fields](/cookbook/form_fields)

##Database:
* [Multiple databases](/cookbook/multidbs)
* [Select: Retrieving entries from a database](/cookbook/select)
* [Update: Updating entries in a database](/cookbook/update)
* [Delete: Remove entries in a database](/cookbook/delete)
* [Insert: Adding entries to a database](/Insert) 
* [Query: Advanced database queries](/cookbook/query)
* [How to use database transactions](/cookbook/transactions)
* [Using sqlalchemy](/cookbook/sqlalchemy)
* [Integrating SQLite UDF (user-defined-functions) with webpy database layer](/cookbook/sqlite-udf)


##Deployment:
* [Fastcgi deployment through lighttpd](/cookbook/fastcgi-lighttpd)
* [Fastcgi deployment through Apache](/cookbook/fastcgi-apache) 
* [CGI deployment through Apache](/cookbook/cgi-apache)
* mod_python deployment through Apache (requested)
* [mod_wsgi deployment through Apache](/cookbook/mod_wsgi-apache )
* [mod_wsgi deployment through Nginx](/cookbook/mod_wsgi-nginx )
* [Fastcgi deployment through Nginx](/cookbook/fastcgi-nginx)

##Subdomains:
* Subdomains and how to access the username (requested)