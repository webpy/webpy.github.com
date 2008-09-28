---
layout: default
title: Hello World!
---

# Hello World!

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

