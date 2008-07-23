---
layout: default
title: Testing webpy applications
---

# Testing webpy applications

Python Paste has a wsgi wrapper that intercepts requests to your application
and enables you to test for the correct responses/status codes etc.  Here's
a simple example (making sure the helloworld app works correctly).

    import web

    urls = (
        '/(.*)', 'hello'    )

    class hello:
        def GET(self, name):
            i = web.input(times=1)
            if not name: name = 'world'
            for c in xrange(int(i.times)): 
                web.output('Hello,' + name+'!') # you must use web.output
                                                # instead of print

    #if __name__ == "__main__": web.run(urls)  # don't run as usual


    from paste.fixture import TestApp, TestResponse
    from web import webpyfunc, wsgifunc

    middleware = []
    app = wsgifunc(webpyfunc(urls, globals()), *middleware)
    app = TestApp(app)

    r = app.get("/")
    assert "Hello" in r


You can get the paste modules from http://pythonpaste.org/index.html

