---
layout: default
title: SSL support in built-in cherrypy server
---

# SSL support in built-in cherrypy server

Other languages: [français](/../cookbook/ssl/fr) | ...

## Problem

How to set SSL support in built-in cherrypy server web.py

## Solution (Requires latest web.py version [0.37 installed from source as of this writing])
    import web
    from web.wsgiserver import CherryPyWSGIServer
    
    CherryPyWSGIServer.ssl_certificate = "/path/to/ssl_certificate"
    CherryPyWSGIServer.ssl_private_key = "/path/to/ssl_private_key"
       
    urls = ("/.*", "hello")
    app = web.application(urls, globals())

    class hello:
        def GET(self):
            return 'Hello, world!'

    if __name__ == "__main__":
        app.run()

## For version 0.36 and earlier (somewhat broken implementation, will crash on SSLException)

    import web
    from web.wsgiserver import CherryPyWSGIServer
    from web.wsgiserver.ssl_builtin import BuiltinSSLAdapter
    
    ssl_cert = "path/to/ssl_certificate"
    ssl_key = "path/to/ssl_private_key"
    
    CherryPyWSGIServer.ssl_adapter = BuiltinSSLAdapter(ssl_cert,ssl_key,None)


    urls = ("/.*", "hello")
    app = web.application(urls, globals())

    class hello:
        def GET(self):
            return 'Hello, world!'

    if __name__ == "__main__":
        app.run()