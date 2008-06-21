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
* loadhooks/unloadhooks (requested)
* [How to use web.background](/cookbook/background)

##Sessions and user state:
* [Working with Session](/cookbook/sessions)
* [Working with Cookies](/cookbook/cookies)
* User authentication (requested)

##Utils:
* [Sending Mail](/cookbook/sendmail)
* [Sending Mail Using Gmail](/cookbook/sendmail_using_gmail)

##Templates:
* [Using Site Layout Templates](/cookbook/layout_template)
* [Alternating Style](/cookbook/alternating_style)
* [Use Mako template engine in webpy](/cookbook/template_mako)
* [Use Cheetah template engine in webpy](/cookbook/template_cheetah)

##User Input:
* [File Upload](/cookbook/fileupload)
* [Accessing user input through web.input](/cookbook/input)
* Using basic forms (requested)

##Database:
* [Mutliple databases](/cookbook/multidbs)
* [Select: Retrieving entries from a database](/cookbook/select)
* [Update: Updating entries in a database](/cookbook/update)
* Delete (requested)
* [Insert: Adding entries to a database](/Insert) 
* [Query: Advanced database queries](/cookbook/query)
* [How to use database transactions](/cookbook/transactions)

##Deployment:
* [Fastcgi deployment through lighttpd](/cookbook/fastcgi-lighttpd)
* Fastcgi deployment through Apache (requested)
* [CGI deployment through Apache](/cookbook/cgi-apache)
* mod_python deployment through Apache (requested)
* [mod_wsgi deployment through Apache](/cookbook/mod_wsgi-apache )
* nginx deployment (requested)

##Subdomains:
* Subdomains and how to access the username (requested)


