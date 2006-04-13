---
layout: default
title: dreamhost
---

# dreamhost

There is currently a page on the Dreamhost wiki <a href="http://wiki.dreamhost.com/index.php/Web.py">for web.py</a>.   The instructions there will work, just give plenty of time for FastCGI to be enabled.  Dreamhost's panel application says 10 minutes but it may take much longer. 

If you want it all happily redirected with mod_rewrite on dreamhost:

Where index.fcgi is whatever your fcgi filename is.

    # BEGIN  
    <IfModule mod_rewrite.c>  
    RewriteEngine On  
    RewriteBase /  
    RewriteCond %{REQUEST_FILENAME} !-f  
    RewriteCond %{REQUEST_FILENAME} !-d  
    RewriteRule (.*) /index.fcgi/$1 [L]  
    </IfModule>  
    # END  
