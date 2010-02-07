---
layout: default
title: Serving Static Files (such as js, css and images)
---

# Serving Static Files (such as js, css and images)

Other languages : [français](/staticfiles/fr) | ...

Problem
-------
How to serve static files?

Solution
--------

### web.py server

Create a directory (also known as a folder) called <code>static</code> in the location of the script that runs the web.py server. Then place the static files you wish to serve in the static folder.

For example, the URL <code>http://localhost/static/logo.png</code> will send the image <code>./static/logo.png</code> to the client.

### Apache

To serve static files with Apache an [Alias](http://httpd.apache.org/docs/2.2/mod/mod_alias.html#alias) directive can be used to map the request for a URL to a chosen directory, before it is handled by web.py.

Here is an example Virtual Host configured on a Unix like system with an Alias directive in effect:

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