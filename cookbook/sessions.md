---
layout: default
title: Sessions
---

# Sessions

### Problem

How to use sessions in web.py.

### Solution - FOR 0.3!!

The `web.session` module provides session support. Here is a simple application to count using sessions.

    import web
    urls = (
        "/count", "count",
        "/reset", "reset"
    )
    app = web.application(urls, locals())
    session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'count': 0})

    class count:
        def GET(self):
            session.count += 1
            return str(session.count)
            
    class reset:
        def GET(self):
            session.kill()
            return ""

    if __name__ == "__main__":
        app.run()

The session object is loaded with the session data before handling the request and saves the session data after handling the request, if modified.

The optional `initializer` argument to Session specifies the initial session.


