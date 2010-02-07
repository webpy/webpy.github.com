---
layout: default
title: Hello World!
---

# Hello World!

Autre langages : [english](/../helloworld) | ...

## Probleme

Comment écrire un "Hello World" avec web.py


## Solution

    import web

    urls = ("/.*", "hello")
    app = web.application(urls, globals())

    class hello:
        def GET(self):
            return 'Hello, world!'

    if __name__ == "__main__":
        app.run()

###Tip: Ecrire une url avec ou sans "/", pointe sur la même classe.

Ajoutez ce qui suit au début des urls.

    '/(.*)/', 'redirect', 


et vous utiliserez la classe suivante pour traiter ces urls.

    class redirect:
        def GET(self, path):
            web.seeother('/' + path)