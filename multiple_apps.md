---
layout: default
title: Django style multiple apps with web.py
---

# Django style multiple apps with web.py

Here is a hack to support decoupling urls for multiple applications using web.py


suppose we have two applications `blog` and `wiki` and we want to put them in same project.

This is the main driver.

    """run.py"""    import blog
    import wiki
    import delegate

    mapping = (
        ("/blog", blog.urls, blog),
        ("/wiki", wiki.urls, wiki)
    )

    if __name__ == "__main__":
        delegate.run(mapping)


The wiki application:

    """wiki.py"""
    urls = (
        "/", "welcome",
        "/hello", "hello"    )

    class welcome:
        def GET(self):
            print "welcome wiki"
    class hello:
        def GET(self):
            print "hello wiki"
The blog application:

    """blog.py"""
    urls = (
        "/", "welcome",
        "/hello", "hello"    )

    class welcome:
        def GET(self):
            print "welcome blog"
    class hello:
        def GET(self):
            print "hello blog"        

And this is the hack for supporting multiple application abstration.


    """delegate.py"""    import web
    import types

    def delegate_apps(mapping):
        """Delegates appropriate app based on prefix.
        `mapping` should be tuple of (prefix, urls, fvars).
        """        def f():
            for prefix, urls, fvars in mapping:
                if type(fvars) == types.ModuleType:
                    fvars = fvars.__dict__

                if web.ctx.path.startswith(prefix):
                    path = web.ctx.path[len(prefix):]

                    # it will be better if web.request.handle takes path also as argument.
                    # return web.request.handle(mapping, fvars, path)
                    
                    web.ctx.path = path
                    return web.request.handle(urls, fvars)
            else:
                return web.notfound()

        return f

    def run(mapping):
        """Starts web.py server with the specified mapping.
        `mapping` should be tuple of (prefix, urls, fvars).
        """        handler = delegate_apps(mapping)
        web.run(handler, {})
