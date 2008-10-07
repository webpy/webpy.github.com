---
layout: default
title: Use Cheetah template engine in webpy
---

# Use Cheetah template engine in webpy

### Problem
How to use Cheetah template engine in webpy?

### Solution

You need to install both Cheetah and webpy(0.3) first: [http://www.cheetahtemplate.org/](http://www.cheetahtemplate.org/). And then try out the following code snippet:

    # encoding: utf-8
    # File: code.py

    import web
    from web.contrib.template import render_cheetah

    render = render_cheetah('templates/')

    urls = (
        '/(first)', 'first',
        '/(second)', 'second'
        )

    app = web.application(urls, globals(), web.reloader)

    class first:
        def GET(self, name):
            # cheetah template takes only keyword arguments,
            # you should call it as:
            #   return render.hello(name=name)
            # Below is incorrect:
            #   return render.hello(name)
            return render.first(name=name)

    class second:
        def GET(self, name):
            return render.first(**locals())

    if __name__ == "__main__":
        app.run()

Template file:

    ## File: templates/first.html

    hello, $name.