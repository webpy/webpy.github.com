---
layout: default
title: Hello World!
---

# Hello World!

## 問題点

web.py を使用して'Hello, world!'を表示させたいのですが？

## 解決手段

    import web

    urls = ("/.*", "hello")
    app = web.application(urls, globals())

    class hello:
        def GET(self):
            return 'Hello, world!'

    if __name__ == "__main__":
        app.run()