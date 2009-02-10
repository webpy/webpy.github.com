---
layout: default
title: ctx
---

# ctx

Problem
-------

You want to use contextual variables in your code such as the referring page or the client's browser.

Solution
--------

Using `web.ctx` makes this possible. First a little architecture: `web.ctx` is based on the class `threadeddict` a.k.a. `ThreadedDict`. This class creates a dictionary-like object that has attributes specific to the thread process id. This is nice because it lets us use a dictionary-like object when many users are accessing the system simultaneously, and the object will only have the data for the given HTTP request (no data is shared so the object is thread-safe).

`web.ctx` holds variables for each request that contain specific information to each request such as the client environment variable. Assuming you want to determine what the referring page was for a user accessing a page:

Example
-------

    class example:
        def GET(self):
            referer = web.ctx.env.get('HTTP_REFERER', 'http://google.com')
            raise web.seeother(referer)

This code uses `web.ctx.env` to access the `HTTP_REFERER` environment variable. If there isn't one, it defaults to google.com. Finally, it redirects the user to the page they came from.

`web.ctx` is also useful because it can be set by a `loadhook`. Session data, for example, is set each time a request is handled and the data is stored in `web.ctx`. Since `web.ctx` is thread-safe, you can use the session data as if it were a regular python object.

Data Found in `ctx`
-------------------

### Request ###
*   `environ` a.k.a. `env` &ndash; a dictionary containing the standard [WSGI environment variables](http://www.python.org/dev/peps/pep-0333/#environ-variables)
*   `home` &ndash; the base path for the application *http://example.org*
*   `homedomain` &ndash; ??? *http://example.org*
*   `homepath` &ndash; ???
*   `host` &ndash; the domain requested by the user *example.org*
*   `ip` &ndash; the IP address of the user *xxx.xxx.xxx.xxx*
*   `method` &ndash; the HTTP method used *GET*
*   `path` &ndash; the path requested by the user */articles/845*
*   `protocol` &ndash; the protocol used *https*
*   `query` &ndash; an empty string if there are no query arguments otherwise a `?` followed by the query string *?foo=amorphous&bar=blasphemous*
*   `fullpath` a.k.a. `path + query` &ndash; the full path requested **including** query arguments */articles/845?foo=amorphous&bar=blasphemous*

### Response ###
*   `status` &ndash; the HTTP status code (default '200 OK') *401 Unauthorized*
*   `headers` &ndash; a list of 2-tuples containing HTTP headers
*   `output` &ndash; a string containing the response entity