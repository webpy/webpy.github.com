---
layout: default
title: Personnaliser le message NotFound
---

# Personnaliser le message NotFound

Autre langages: [english](/../custom_notfound) | ...

## Probleme

Comment personnaliser les messages notfound et autres?

## Solution

    import web

    urls = (...)
    app =  web.application(urls, globals())

    def notfound():
        return web.notfound("Désolé, la page que vous recherchez n'a pas été trouvée.")

	# Vous pouvez utiliser des résultats avec gabarits comme ci-dessous, l'un ou l'autre fonctionne: 
        #return web.notfound(render.notfound())
        #return web.notfound(str(render.notfound()))

    app.notfound = notfound


Puis, pour renvoyer la 404 personnalisée depuis votre code, faites juste:

    class example:
        def GET(self):
            raise web.notfound()

De la même manière, le message InternalError peut aussi être personnalisé:

    def internalerror():
        return web.internalerror("Vilain, vilain serveur. Pas de friandises.")

    app.internalerror = internalerror