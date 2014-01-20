---
layout: default
title: Web.py Cookbook
---

# Web.py Cookbook

_Other languages:_ [简体中文](/cookbook/index.zh-cn) | [日本語](/cookbook/index.ja) |  [Français](/cookbook/index.fr)

## Basics
* [Hello World](/cookbook/helloworld)
* [Serving Static Files](/cookbook/staticfiles)
* [Understanding URL handling](/cookbook/url_handling)
* [Seeother and Redirect](/cookbook/redirect%2Bseeother)
* [using subapplications](/cookbook/subapp)
* [Serving XML](/cookbook/xmlfiles)
* [Reading raw data from post](/cookbook/postbasic)

## Advanced
* [Contextual and Environment variables - web.ctx](/cookbook/ctx)
* [Application processors, loadhooks and unloadhooks](/cookbook/application_processors)
* [How to use web.background](/cookbook/background)
* [Custom NotFound message](/cookbook/custom_notfound)
* [How to Stream Large Files](/cookbook/streaming_large_files)
* [Control over logging for default HTTPServer](/cookbook/logging)
* [SSL support in built-in cherrypy server](/cookbook/ssl)
* [Run-time language switch](/cookbook/runtime-language-switch)

## Sessions and user state
* [Working with Session](/cookbook/sessions)
* [Using session with reloader](/cookbook/session_with_reloader)
* [Using session in template](/cookbook/session_in_template)
* [Working with Cookies](/cookbook/cookies)
* [User authentication](/cookbook/userauth)
* [User authentication with http basic auth (RFC2617)](/cookbook/userauthbasic)
* [User authentication with Postgresql database](/cookbook/userauthpgsql)
* [Sessions with sub-apps](/cookbook/sessions_with_subapp)
* [Unpack session stored in postgresql](/cookbook/unpack_postgres_session)

## Utils
* [Sending Mail](/cookbook/sendmail)
* [Sending Mail Using Gmail](/cookbook/sendmail_using_gmail)
* [Webservice using soaplib + WSDL](/cookbook/webservice)

## Templates
* [Templetor: The web.py templating system](/docs/0.3/templetor )
* [Using Site Layout Templates](/cookbook/layout_template)
* [Alternating Style](/cookbook/alternating_style)
* [Import functions into templates](/cookbook/template_import)
* [i18n support in template file](/cookbook/i18n_support_in_template_file )
* [Use Mako template engine in webpy](/cookbook/template_mako)
* [Use Cheetah template engine in webpy](/cookbook/template_cheetah)
* [Use Jinja2 template engine in webpy](/cookbook/template_jinja)
* [How to use templates on Google App Engine](/cookbook/templates_on_gae)
* [Concatenate two rendered templates](/cookbook/concatenate_two_rendered_templates)

## Testing
* [Testing with Paste and Nose](/cookbook/testing_with_paste_and_nose)
* [RESTful doctesting using an application's request method](/cookbook/restful_doctesting_using_request)

## User input
* [File Upload](/cookbook/fileupload)
* [Store an uploaded file](/cookbook/storeupload)
* [How to put a limit of size of uploaded files](/cookbook/limiting_upload_size)
* [Accessing user input through web.input](/cookbook/input)
* [How to use forms](/cookbook/forms) 
* [Render individual form fields](/cookbook/form_fields)
* [How to protect forms from CSRF attacks](/cookbook/csrf) 

## Databases
* [Multiple databases](/cookbook/multidbs)
* [Select: Retrieving entries from a database](/cookbook/select)
* [Update: Updating entries in a database](/cookbook/update)
* [Delete: Remove entries in a database](/cookbook/delete)
* [Insert: Adding entries to a database](/cookbook/insert) 
* [Query: Advanced database queries](/cookbook/query)
* [How to use database transactions](/cookbook/transactions)
* [Using sqlalchemy](/cookbook/sqlalchemy) 
* [Integrating SQLite UDF (user-defined-functions) with webpy database layer](/cookbook/sqlite-udf)
* [Using a dictionary as where clause](/cookbook/where_dict)


## Deployment
* [Fastcgi deployment through lighttpd](/cookbook/fastcgi-lighttpd)
* [Fastcgi deployment through Apache](/cookbook/fastcgi-apache) 
* [CGI deployment through Apache](/cookbook/cgi-apache)
* mod_python deployment through Apache (requested)
* [mod_wsgi deployment through Apache on Red Hat](/cookbook/mod_wsgi-apache)
* [mod_wsgi deployment through Apache on Ubuntu](/cookbook/mod_wsgi-apache-ubuntu)
* [mod_wsgi deployment through Nginx](/cookbook/mod_wsgi-nginx )
* [Fastcgi deployment through Nginx](/cookbook/fastcgi-nginx)
* [PyISAPIe deployment through IIS7/IIS6](/cookbook/iis7_iis6_windows_pyisapie)
* [Deploying as a google app engine application](/cookbook/google_app_engine)

## Subdomains
* Subdomains and how to access the username (requested)
