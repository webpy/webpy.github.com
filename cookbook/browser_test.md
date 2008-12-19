---
layout: default
title: Browser Testing
---

# Browser Testing

### Problem

You want to test webpy applications.

### Solution

Use the 'browser' module. 
    
    urls = (
        '/', 'Index',
        '/login', 'Login',
    )

    class Index:
    
        def GET(self):
            return """
            <html><body>
            <a href="/login">Login</a>
            </body></html>"""

    class Login:
        
        def GET(self):
            return """
            <html><body>
            <form name="login" action="">
            Name: <input type="text" name="username"><br>
            PW: <input type="password" name="password"><br>
            </form>
            </body><html>
            """
    
        def POST(self):
            i = web.input()
            return "Welcome " + i.name
             
    
    app = web.application(urls, globals())
    
    b = app.browser()
    b.open('/')
    b.follow_link(text='Login')

    b.select_form(name='login')
    b['username'] = 'joe'
    b['password'] = 'secret'
    b.submit()

    assert b.path == '/login'
    assert 'Welcome joe' in b.get_text()

It is also possible to use the browser module for crawling or testing
existing websites.

    b = web.Browser()
    b.open('http://webpy.org')
    b.follow_link(url_regex='login')

    b.select_form(name='login')
    b['username'] = 'joe'
    b['password'] = 'secret'
    b.submit()

    assert b.path == '/'
    assert 'Log Out' in b.get_text() 