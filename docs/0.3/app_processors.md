---
layout: default
title: Application processors
---

# Application processors

Other languages : [français](/app_processors/fr) | ...

Application processors allow the programmer to execute common code before each request is processed.  This is helpful for authentication schemes or for setting up user state on each request.  Multiple processors can be added per application, and they will be executed in the order which they are added.  The most basic processor looks like this:

    def proc(handle):
        # do whatever you need to here
        web.ctx.user = web.cookies(user=None).user
        # return the executed handle
        return handle()
    
    app = web.application(urls, globals()
    # Add the processor
    app.add_processor(proc)

The "handle" of the app processor refers to the code that will be dispatched by the matching URL (and any subsequent processors).  This allows us to use try and except, like this:

        def proc(handle):
            try:
                ret = handle()
            except:
                log_error('Uh oh')
            return ret


Here's a basic example of how an authentication scheme is created using app processors.  This is not secure for actual use; it is only meant to demonstrate how app processors can check something before each url is processed.

## Example
    """ Application processors in web.py """
    import web
    
    urls = (
        '/', 'Index',
        '/login', 'Login',
        '/logout', 'Logout',
    )
    
    class Index:
    
        def GET(self):
            return '<html>Hello %s <a href="/logout">Logout</a></html>' \
                % web.ctx.username
    
    
    class Login:
        
        def GET(self):
            return """
            <html>
            <form action="" method="post">
                <input type="text" name="username">
                <input type="submit" value="Login">
            </form>
            </html>
            """
    
        def POST(self):
            # only set cookie if user login succeeds
            name = web.input(username=None).username
            if name:
                web.setcookie('username', name)
            raise web.seeother('/')
    
    
    class Logout:
        
        def GET(self):
            web.setcookie('username', '', expires=-1)
            raise web.seeother('/login')
        
    
    
    app = web.application(urls, globals())
    
    # Auth Processor
    def auth_app_processor(handle):
        path = web.ctx.path
        web.ctx.username = name = web.cookies(username=None).username
        if not name and path != '/login':
            raise web.seeother('/login')
        return handle()
    
    app.add_processor(auth_app_processor)
    
    
    if __name__ == '__main__':
        app.run()