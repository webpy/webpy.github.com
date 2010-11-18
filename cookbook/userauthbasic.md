---
layout: default
title: Basic authentication
---

# Basic authentication

##Problem
This is a proof of concept implementation of doing basic authentication
with web.py.
You may want to read [RFC 2617](http://www.ietf.org/rfc/rfc2617.txt) or
[http://en.wikipedia.org/wiki/Basic_access_authentication](http://en.wikipedia.org/wiki/Basic_access_authentication) for reference.

##Solution
Create a python file containing the code below and start the script.
When you enter the url [http://localhost:8080/](http://localhost:8080/) you will be redirected
to the url [http://localhost:8080/login](http://localhost:8080/login).
When you are successfully authenticated, you will be redirected to the
index page.

##
    import web
    import re
    import base64
    
    urls = (
        '/','Index',
        '/login','Login'
    )
    
    app = web.application(urls,globals())
    
    allowed = (
        ('jon','pass1'),
        ('tom','pass2')
    )
    
    
    class Index:
        def GET(self):
            if web.ctx.env.get('HTTP_AUTHORIZATION') is not None:
                return 'This is the index page'
            else:
                raise web.seeother('/login')
    
    class Login:
        def GET(self):
            auth = web.ctx.env.get('HTTP_AUTHORIZATION')
            authreq = False
            if auth is None:
                authreq = True
            else:
                auth = re.sub('^Basic ','',auth)
                username,password = base64.decodestring(auth).split(':')
                if (username,password) in allowed:
                    raise web.seeother('/')
                else:
                    authreq = True
            if authreq:
                web.header('WWW-Authenticate','Basic realm="Auth example"')
                web.ctx.status = '401 Unauthorized'
                return
    
    if __name__=='__main__':
        app.run()
  
##Notes
Do not use this code on real site - this is only for illustration.