---
layout: default
title: cookies
---

# cookies

Other languages: [français](/../cookbook/cookies/fr) | ...

##Problem
You want to set and retrieve cookies for a user browsing the site.

##Solution
Web.py *comes* with an easy to use method for setting/getting cookies.

###Setting Cookies
####Overview
    setcookie(name, value, expires="", domain=None, secure=False): 
       
* *name* `(string)` - The actual name of the cookie, as stored by the browser, and returned to the server.
* *value* `(string)` - The value you want stored under that name.
* *expires* `(int)` - Optionally, is the time in seconds until the browser should expire the cookie.  Note: this must be an integer, not a string.
* *domain* `(string)` - The domain the cookie is valid for. By default, set to the host accessed, this allows you to set the domain, rather than just a host (such as `.webpy.org`).
* *secure* `(bool)`- If True, require that the cookie only be sent over HTTP/S.

####Example
`web.setcookie()` can be used to set the cookie for a user, like this:

    class CookieSet:
        def GET(self):
            i = web.input(age='25')
            web.setcookie('age', i.age, 3600)
            return "Age set in your cookie"


Calling the above class with GET will set a cookie named "age" with a default value equal to "25" (this default value actually comes from the web.input processing, NOT the setcookie function), which expires in 1 hour (3600 seconds).

The third (and optional) argument to `web.setcookie()`, "expires", allows you to set when you want your cookie to expire.  Any negative number will expire the cookie immediately.  Any positive number is the number of seconds that the cookie will last (3600 would result in an hour long cookie).  Leaving this argument empty results in a session cookie, which expires when your browser shuts down.  To make the cookie "permanent", simply update cookie expiration time at regular interval (e.g. when user logged in).

###Retrieving Cookies
####Overview
There are many methods to retrieve cookies, depending on the desired reaction to a missing cookie.
#####Way 1 (return None if cookie is not found):
    web.cookies().get(cookieName)  
        #cookieName is the name of the cookie submitted by the browser
#####Way 2 (raises exception AttributeError if cookie is not found):
    foo = web.cookies()
    foo.cookieName
#####Way 3 (avoids exception by setting default value for cookie if not found):
    foo = web.cookies(cookieName=defaultValue)
    foo.cookieName   # return the value (which could be default)
        #cookieName is the name of the cookie submitted by the browser

####Example
`web.cookies()` can be used to access an already set cookie.  If a cookie is set using the `web.setcookie()` code from above, it can be retrieved like this:

    class CookieGet:
        def GET(self):
            c = web.cookies(age="25")
            return "Your age is: " + c.age

The example sets a default value for the cookie if it does not exist.  The reason for setting a default value is that if the cookie is attempted to be accessed, but does not exist, `web.cookies()` raises an exception.  

Sometimes, you want to know specifically if something doesn't exist, in which case you can use something like the following:

    class CookieGet:
        def GET(self):
            try: 
                 return "Your age is: " + web.cookies().age
            except:
                 # Do whatever handling you need to, etc. here.
                 return "Cookie does not exist."

This code attempts to use the cookie submitted by the browser, but does not give it a default value.  If the cookie doesn't exist, an exception is raised, and the `except` clause is executed, giving the server an opportunity to handle the lack of cookie.

or

    class CookieGet:
        def GET(self):
            age=web.cookies().get('age')
            if age:
                return "Your age is: %s" % age
            else:
                return "Cookie does not exist."