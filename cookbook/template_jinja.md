---
layout: default
title: Use Jinja2 template engine in webpy
---

# Use Jinja2 template engine in webpy

### Problem
How to use Jinja2 (http://jinja.pocoo.org/2/) template engine in webpy?

### Solution

You need to install both Jinja2 and webpy(0.3) first, and then try out the following code snippet:

    import web
    from web.contrib.template import render_jinja

    urls = (
            '/(.*)', 'hello'
            )
    
    app = web.application(urls, globals())
    
    render = render_jinja(
            'templates',   # Set template directory.
            encoding = 'utf-8',                         # Encoding.
        )

    # Add/override some global functions.
    #render._lookup.globals.update(
    #       var=newvar,
    #       var2=newvar2,
    #)

    class hello:
        def GET(self, name):
            return render.hello(name=name)
    
    if __name__ == "__main__":
        app.run()

### Template file: templates/hello.html

    Hello, {{ name }}.