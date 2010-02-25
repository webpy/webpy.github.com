---
layout: default
title: Site Layout Template
---

# Site Layout Template

Other languages : [français](/layout_template/fr) | ...

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
    
###Tip: Page title is set in other template files which are then used by the layout (layout.html). Example:

#####templates/index.html
    $var title: This is title.

    <h3>Hello, world</h3>

#####templates/layout.html
    $def with (content)
    <html>
    <head>
        <title>$content.title</title>
    </head>
    <body>
    $:content
    </body>
    </html>

###Tip: Add css files in other template files. Example:
####templates/login.html

    $var cssfiles: static/login.css static/login2.css

    hello, world.

####templates/layout.html

    $def with (content)
    <html>
    <head>
        <title>$content.title</title>

        $if content.cssfiles:
            $for f in content.cssfiles.split():
                <link rel="stylesheet" href="$f" type="text/css" media="screen" charset="utf-8"/>

    </head>
    <body>
    $:content
    </body>
    </html>

The HTML output code looks like below:

    <link rel="stylesheet" href="static/login.css" type="text/css" media="screen" charset="utf-8"/>
    <link rel="stylesheet" href="static/login2.css" type="text/css" media="screen" charset="utf-8"/>