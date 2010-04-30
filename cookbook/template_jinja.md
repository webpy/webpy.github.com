---
layout: default
title: Use Jinja2 template engine in webpy
---

# Use Jinja2 template engine in webpy

### Problem
How to use Jinja2 (http://jinja.pocoo.org/2/) template engine in webpy?

### Solution 1

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

### Solution 2

With this solution, you have to specify template name, it's useful if template files are organized in different directories.

    import os
    import web
    from jinja2 import Environment,FileSystemLoader
    
    urls = ("/.*", "hello")
    app = web.application(urls, globals())
    
    def render_template(template_name, **context):
        extensions = context.pop('extensions', [])
        globals = context.pop('globals', {})
    
        jinja_env = Environment(
                loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
                extensions=extensions,
                )
        jinja_env.globals.update(globals)
    
        #jinja_env.update_template_context(context)
        return jinja_env.get_template(template_name).render(context)
    
    class hello:
        def GET(self):
            # You can use a relative path as template name, for example, 'ldap/hello.html'.
            return render_template('hello.html', name='world',)
    
    if __name__ == "__main__":
        app.run()