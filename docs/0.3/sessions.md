---
layout: default
title: web.py Sessions
---

# web.py Sessions

Other languages : [français](/sessions/fr) | ...

Sessions are a way to store information between requests, thereby making http stateful.  They work by sending the user a cookie, which maps to a session storage object on the server.  When the user requests a page, the client sends the cookie back with the request, web.py loads the session based on the key, and code can request and store information in it.

Sessions are convenient because they allow a programmer to store user state in native Python objects.

## Storage types
web.py sessions allow for multiple ways to store the session data.  These methods include:

* DiskStore. Session data is pickled in a designated directory. When instantiating, the first and only argument is the folder where the session information should be stored on disk.
* DBStore. Session data is pickled and stored in a database.  This can be useful if you want to store session data on a separate system. When creating, the DBStore takes 2 arguments: a web.py database instance, and the table name (string). The table which stores the session must have the following schema:

        session_id CHAR(128) UNIQUE NOT NULL,
        atime DATETIME NOT NULL default current_timestamp,
        data TEXT

* ShelfStore. Data is stored using the python shelve module. When creating, the ShelfStore takes the filename that should be used to store the data.

The storage methods have various performance and setup tradeoffs, so the options allow you to choose what's best for your application.


## Example
The following code shows how to use a basic DiskStore session.

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


## Sessions and Reloading/Debug Mode
Is your session data disappearing for seemingly no reason? This can happen when using the web.py app reloader (local debug mode), which will not persist the session object between reloads. Here's a nifty hack to get around this.

    # Hack to make session play nice with the reloader (in debug mode)
    if web.config.get('_session') is None:
        session = web.session.Session(app, db.SessionDBStore())
        web.config._session = session
    else:
        session = web.config._session
