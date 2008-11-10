---
layout: default
title: Using session with reloader
---

# Using session with reloader


# Problem

There are some issues in using sessions when running the application with autoreload=True. Is there any work-around?

# Solution

Since the reloader loads the main module twice (once as __main__ and once with its name), 2 session objects will be created. This can be avoided by storing the session in some global place to avoid creating the second one. 

Here is a sample code which saves session in `web.config`.

    import web
    urls = ("/", "hello")

    app = web.application(urls, globals(), autoreload=True)

    if web.config.get('_session') is None:
        session = web.session.Session(app, web.session.DiskStore('sessions'), {'count': 0})
        web.config._session = session
    else:
        session = web.config._session

    print '** session', id(session), session
    web.config.debug = 'True'

    class hello:
       def GET(self):
           print 'session', session
           session.count += 1
           return 'Hello, %s!' % session.count

    if __name__ == "__main__":
       app.run()

