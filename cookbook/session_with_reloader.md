---
layout: default
title: Using session with reloader
---

# Using session with reloader

Other languages: [français](/../cookbook/session_with_reloader/fr) | ...

# Problem

There are some issues in using sessions when running the application in debug mode. Is there any work-around?

# Solution

web.py runs the program in debug mode when run using the builtin webserver.
Simplest fix for this is to disable debug mode, which can be done by setting `web.config.debug = False`.

    import web
    web.config.debug = False

    # rest of your code


If you want to use sessions in debug mode then here is a work-around.

Since debug mode enables module reloading, the reloader loads the main module twice (once as __main__ and once with its name), 2 session objects will be created. This can be avoided by storing the session in some global place to avoid creating the second one. 

Here is a sample code which saves session in `web.config`.

    import web
    urls = ("/", "hello")

    app = web.application(urls, globals())

    if web.config.get('_session') is None:
        session = web.session.Session(app, web.session.DiskStore('sessions'), {'count': 0})
        web.config._session = session
    else:
        session = web.config._session

    class hello:
       def GET(self):
           print 'session', session
           session.count += 1
           return 'Hello, %s!' % session.count

    if __name__ == "__main__":
       app.run()