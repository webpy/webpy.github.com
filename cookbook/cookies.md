---
layout: default
title: cookies
---

# cookies

##Problem
You want to set and retrieve cookies for a user browsing the site.

##Solution

web.setcookie can be used to set the cookie for a user, like this:


    class CookieSet:
        def GET(self):
            i = web.input(name='Bob')
            web.setcookie('name', i.name)
            return "Name set in your cookie"

Going to the above function will set a cookie with cookie name equal to "name" and cookie value default equal to "Bob", or whatever the user gives as input.  You could set a custom name by going to /cookieset?name=Guido.


web.getcookie can be used to access an already set cookie.  If a cookie is set using the above code, it can be retrieved like this:

    class CookieGet:
        def GET(self):
            c = web.cookies(name="Bob")
            return "Your name is: " + c.name

web.setcookie takes a third argument, "expires", so you can decide when you want your cookie to expire.  Any negative number will expire the cookie immediately.  Any positive number is the number of seconds that the cookie will last (3600 would result in an hour long cookie).  