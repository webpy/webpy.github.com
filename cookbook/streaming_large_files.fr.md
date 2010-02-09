---
layout: default
title: Comment streamer de gros fichiers
---

# Comment streamer de gros fichiers

Autre langages: [english](/../streaming_large_files) | ...

## Problème:

Vous souhaitez utiliser web.py pour streamer de gros fichiers.

## Solution:

Voici un exemple qui vous permettra d'utiliser web.py pour streamer de larges fichiers. Vous verrez qu'il fonctionne comme annoncé, mais vous devez vous assurer que vous avez ajouté 'chunked' dans l'en-tête Transfer-Encoding pour qu'il s'affiche correctement. Sinon, le navigateur va mettre en cache toutes les données avant de vous les afficher.


Vous ne pouvez pas mélanger une chaîne de base et les retours [ Yield](http://fr.wikipedia.org/wiki/Yield_(instruction)) dans la même méthode. Si vous utilisez [ Yield](http://fr.wikipedia.org/wiki/Yield_(instruction)), vous devrez utiliser [ Yield](http://fr.wikipedia.org/wiki/Yield_(instruction)) pour tout, parce que votre fonction devient un générateur.

##Simple exemple

    # Simple démonstration d'un serveur de streaming 
    # Il utilise time.sleep la lecture d'un gros fichier
    import web
    import time
     
    urls = (
        "/",    "count_holder",
        "/(.*)",  "count_down",
        )
    app = web.application(urls, globals())
     

    class count_down:
        def GET(self,count):
            # Ces en-têtes le font fonctionner dans les navigateurs
            web.header('Content-type','text/html')
            web.header('Transfer-Encoding','chunked')        
            yield '<h2>Prepare for Launch!</h2>'
            j = '<li>Liftoff in %s...</li>'
            yield '<ul>'
            count = int(count)
            for i in range(count,0,-1):
                out = j % i
                time.sleep(1)
                yield out
            yield '</ul>'
            time.sleep(1)
            yield '<h1>Lift off</h1>'
            
    class count_holder:
        def GET(self):
            web.header('Content-type','text/html')
            web.header('Transfer-Encoding','chunked')        
            boxes = 4
            delay = 3
            countdown = 10
            for i in range(boxes):
                output = '<iframe src="/%d" width="200" height="500"></iframe>' % (countdown - i)
                yield output
                time.sleep(delay)
            
    if __name__ == "__main__":
        app.run()