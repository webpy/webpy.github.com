---
layout: default
title: Site Layout Template
---

# Site Layout Template

### Problem

How do I use a site-wide base template that displays across every page? (In other frameworks, this is called template inheritance.)

### Solution

This can be done using the base attribute:
    
    render = web.template.render('templates/', base='layout')
    
Now if you do something like `render.foo()` it will render the `templates/foo.html` template and then wrap it in the `templates/layout.html` template.

The format for "layout.html" should be a simple template that takes one variable.  For example:

    $def with (content)
    <html>
    <head>
    <title>Foo</title>
    </head>
    <body>
    $:content
    </body>
    </html>

If you don't want to use the base template for something, just create a second render object without the base attribute, like:

    render_plain = web.template.render('templates/')
    
