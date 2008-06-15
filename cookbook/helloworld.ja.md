---
layout: default
title: Hello World!
---

# Hello World!

### 問題

web.py を使用して'Hello, world!'を書く方法

### 解答

    import web

    urls = ("/.*", "hello")
    app = web.application(urls, globals())

    class hello:
        def GET(self):
            return 'Hello, world!'

    if __name__ == "__main__":
        app.run()