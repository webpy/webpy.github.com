---
layout: default
title: Use Mako template engine in webpy
---

# Use Mako template engine in webpy

### Problem
How to use Mako template engine in webpy?

### Solution

You need to install both Mako and webpy(0.3) first: [http://www.makotemplates.org/](http://www.makotemplates.org) and then try out the following code snippet:

    # encoding: utf-8
    # File: code.py

    import web

    from web.contrib.template import render_mako

    urls = (
            '/(.*)', 'hello'
            )

    app = web.application(urls, globals(), autoreload=True)

    # input_encoding and output_encoding is important for unicode
    # template file. Reference:
    # http://www.makotemplates.org/docs/documentation.html#unicode
    render = render_mako(
            directories=['templates'],
            input_encoding='utf-8',
            output_encoding='utf-8',
            )

    class hello:
        def GET(self, name):
            return render.hello(name=name)
            # Another way:
            #return render.hello(**locals())

    if __name__ == "__main__":
        app.run()

Template file:

    ## File: templates/hello.html

    Hello, ${name}.

###Note:

if you use Apache + mod_wsgi to deploy webpy apps, you may get the similar error msg in your apache error log:

    [Sat Jun 21 21:56:22 2008] [error] [client 192.168.122.1] TopLevelLookupException: Cant locate template for uri 'index.html'

You have to specify location of templates as absolute path as no
guarantees as to what current working directory will be.

You can use relative paths in order to make it easier too. e.g.

    import os

    render = render_mako(
            directories=[os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),],
            input_encoding='utf-8',
            output_encoding='utf-8',
            )


#Reference:
* http://code.google.com/p/modwsgi/wiki/ApplicationIssues

#i18n support in Mako template file:
Please refer to cookbook 'i18n support in webpy template file' for i18n support in mako template file:

* Cookbook: [i18n support in webpy template file](i18n_support_in_template_file )

#Note:
Babel is only needed to generate the .mo files.