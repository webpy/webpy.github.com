---
layout: default
title: Привет мир!!!
---

# Привет мир!!!

## Проблема

Как создать первое приложение("Hello world") с помощью web.py

## Решение

    import web

    urls = ("/.*", "hello")
    app = web.application(urls, globals())

    class hello:
        def GET(self):
            return 'Hello, world!'

    if __name__ == "__main__":
        app.run()

###Tip: Make url ending with or without '/' going to the same class.

добавьте следующую строчкув начало списка urls.

    '/(.*)/', 'redirect', 

также добавьте следующий класс для обработки этого URL.

    class redirect:
        def GET(self, path):
            web.seeother('/' + path)