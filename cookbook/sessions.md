---
layout: default
title: Sessions
---

# Sessions

### Problem

How to use sessions in web.py.

### Solution - 0.3 Only!

*sessions doesn't work in debug mode because it interfere with reloading. see [session_with_reloader](/session_with_reloader) for more details.*

The `web.session` module provides session support. Here is a simple application to count using sessions.

    import web
    web.config.debug = False
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

The session object is loaded with the session data before handling the request and saves the session data after handling the request, if modified. Note in the current (11-22-2008) version of web.py, one must turn off debug to use the development server with sessions.

The optional `initializer` argument to Session specifies the initial session.

You can use `DBStore` instead of `DiskStore` if you prefer to store sessions in database instead of disk. For using DBStore you need to have a table with the following schema.

     create table sessions (
        session_id char(128) UNIQUE NOT NULL,
        atime timestamp NOT NULL default current_timestamp,
        data text
    );

And you need to pass `db` object and session table name to the constructor of `DBStore`.

    db = web.database(dbn='postgres', db='mydatabase', user='myname', pw='')
    store = web.session.DBStore(db, 'sessions')
    session = web.session.Session(app, store, initializer={'count': 0})
