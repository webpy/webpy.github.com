---
layout: default
title: Custom NotFound message
---

# Custom NotFound message

## Problem

How to customize notfound and other messages?

## Solution

    import web

    urls = (...)
    app =  web.application(urls, globals())

    def notfound():
        return web.notfound("Sorry, the page you were looking for was not found.")

    app.notfound = notfound


And to return the custom 404 from your code, just do:

    class example:
        def GET(self):
            raise web.notfound()

In the same way InternalError message can also be customized.

    def internalerror():
        return web.internalerror("Bad, bad server. No donut for you.")

    app.internalerror = internalerror



