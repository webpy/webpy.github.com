---
layout: default
title: using subapplications
---

# using subapplications

Other languages [français](/../cookbook/subapp/fr) | ...

## Problem

How do you include an application defined in another file in your application?

## Solution

In `blog.py`:

    import web
    urls = (
      "", "reblog",
      "/(.*)", "blog"
    )

    class reblog:
        def GET(self): raise web.seeother('/')

    class blog:
        def GET(self, path):
            return "blog " + path

    app_blog = web.application(urls, locals())

In your main `code.py`:

    import web
    import blog
    urls = (
      "/blog", blog.app_blog,
      "/(.*)", "index"
    )
    
    class index:
        def GET(self, path):
            return "hello " + path
    
    app = web.application(urls, locals())

    if __name__ == "__main__":
        app.run()