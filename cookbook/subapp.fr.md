---
layout: default
title: Utiliser les sous-applications
---

# Utiliser les sous-applications

Autre langages: [english](/../subapp) | ...

## Probleme

Comment inclure une application définie dans un autre fichier dans votre application principale ?

## Solution

Dans `blog.py`:

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

Dans votre application principale `code.py`:

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