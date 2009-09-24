---
layout: default
title: SSL support in built-in cherrypy server
---

# SSL support in built-in cherrypy server

## Problem

How to set SSL support in built-in cherrypy server web.py

## Solution

    import web
    
    from web.wsgiserver import CherryPyWSGIServer

    CherryPyWSGIServer.ssl_certificate = "path/to/ssl_certificate"
    CherryPyWSGIServer.ssl_private_key = "path/to/ssl_private_key"

    urls = ("/.*", "hello")
    app = web.application(urls, globals())

    class hello:
        def GET(self):
            return 'Hello, world!'

    if __name__ == "__main__":
        app.run()