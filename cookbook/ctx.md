---
layout: default
title: web.ctx
---

# web.ctx

##web.ctx

### Problem
You want to use contextual variables in your code, such as the referring page or the clients browser.

### Solution

Using the web.ctx makes this possible. First a little architecture:  web.ctx is based on a class called threadeddict.  This class creates a dictionary-like object, that has attributes specific to that thread process id.  This is nice because it lets us use a dictionary-like object when many users are accessing the system simultaneously, and the object will only have the data for the given http request (no data is shared, so the object is threadsafe).

For this reason, web.ctx holds variables for each request that contain specific information to each request, such the client environment variable.  Assuming you want to determine what the referring page was for a user accessing a page:

    class SomePage:
        GET(self):
            user_came_from = web.ctx.env.get('HTTP_REFERER', 'http://google.com')
            web.seeother(user_came_from)

This code uses the environment variable, and gets the HTTP_REFERER variable; if there isn't one, it defaults to google.com.  Then, it redirects them to wherever they came from.

web.ctx is also useful because it can be set by a loadhook.  Session data, for example, is set each time a request is handled on the load, and the data is stored in web.ctx.  Since web.ctx is a threadsafe, you can use the session data as if it were a regular python object.
