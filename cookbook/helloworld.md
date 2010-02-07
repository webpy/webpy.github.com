---
layout: default
title: Hello World!
---

# Hello World!

Other languages : [français](/helloworld/fr) | ...

## Problem

How to write hello world with web.py

## Solution

    import web

    urls = ("/.*", "hello")
    app = web.application(urls, globals())

    class hello:
        def GET(self):
            return 'Hello, world!'

    if __name__ == "__main__":
        app.run()

###Tip: Make url ending with or without '/' going to the same class.

add the following to the beginning of urls.

    '/(.*)/', 'redirect', 

and have the following class to handle those urls.

    class redirect:
        def GET(self, path):
            web.seeother('/' + path)