---
layout: default
title: web.py Sessions
---

# web.py Sessions

Sessions are a way to store information between requests, thereby making http stateful.  They work by sending the user a cookie, which maps to a session storage object on the server.  When the user requests a page, the client sends the cookie back with the request, web.py loads the session based on the key, and code can request and store information in it.

Sessions are convenient because they allow a programmer to store user state in native Python objects.

## Storage types
web.py sessions allow for multiple ways to store the session data.  These methods include:

* Disk store. Session data is pickled in a designated directory.
* DB Store. Session data is pickled and stored in a database.  This can be useful if you want to store session data on a separate system.
* Shelve store. Data is stored using the python shelve module.

The storage methods have various performance and setup tradeoffs, so the options allow you to choose what's best for your application.


###/sess.py

    import web
    
    
    urls = (
        '/', 'Index',
        '/login', 'Login',
        '/logout', 'Logout',
    )
    
    web.config.debug = False
    app = web.application(urls, locals())
    session = web.session.Session(app, web.session.DiskStore('sessions'))      
    
    class Index:
        def GET(self):
            if session.get('logged_in', False):
                return '<h1>You are logged in</h1><a href="/logout">Logout</a>'
            return '<h1>You are not logged in.</h1><a href="/login">Login now</a>'
    
    class Login:
        def GET(self):
            session.logged_in = True
            raise web.seeother('/')
    
    class Logout:
        def GET(self):
            session.logged_in = False
            raise web.seeother('/')
    
    
    if __name__ == '__main__':
        app.run()