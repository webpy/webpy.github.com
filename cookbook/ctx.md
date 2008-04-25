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
            return web.seeother(referer)

This code uses `web.ctx.env` to access the `HTTP_REFERER` environment variable. If there isn't one, it defaults to google.com. Finally, it redirects the user to the page they came from.

`web.ctx` is also useful because it can be set by a `loadhook`. Session data, for example, is set each time a request is handled and the data is stored in `web.ctx`. Since `web.ctx` is thread-safe, you can use the session data as if it were a regular python object.

Data Found in `ctx`
-------------------

### Request ###
*   `environ` a.k.a. `env` &mdash; a dictionary containing the standard [WSGI environment variables](http://www.python.org/dev/peps/pep-0333/#environ-variables)
*   `home` &mdash; the base path for the application *http://example.org*
*   `homedomain` &mdash; ??? *http://example.org*
*   `homepath` &mdash; ???
*   `host` &mdash; the domain requested by the user *example.org*
*   `ip` &mdash; the IP address of the user *xxx.xxx.xxx.xxx*
*   `method` &mdash; the HTTP method used *GET*
*   `path` &mdash; the path requested by the user */articles/845*
*   `protocol` &mdash; the protocol used *https*
*   `query` &mdash; an empty string if there are no query arguments otherwise a `?` followed by the query string *?foo=amorphous&bar=blasphemous*
*   `fullpath` a.k.a. `path + query` &mdash; the full path requested **including** query arguments */articles/845?foo=amorphous&bar=blasphemous*

### Response ###
*   `status` &mdash; the HTTP status code (default '200 OK') *401 Unauthorized*
*   `headers` &mdash; a list of 2-tuples containing HTTP headers
*   `output` &mdash; a string containing the response entity