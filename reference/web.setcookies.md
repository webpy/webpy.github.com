---
layout: default
title: web.setcookies()
---

# web.setcookies()

Allows you to set a cookie. Useful for carrying around non-private data       

accepts the following arguments:
name, value, expiration time, domain

in the following example you can see that the name of the cookie is 'hc', the value is '1', the expiry is in seconds, so 3600 seconds == 1 hour, then domain is 'huntercross.com'


## example 

        web.setcookie('hc', '1', 3600, 'huntercross.com')
        
        print web.cookies()

