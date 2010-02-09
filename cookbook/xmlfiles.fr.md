---
layout: default
title: Servir du XML
---

# Servir du XML

Autres langages [english](/../xmlfiles) | ...

### Probleme

Comment servir des fichiers XML correctement?


Cela est nécessaire lorsque vous avez une application tierce postant des données au service et attendant une réponse XML.

### Solution

Créez votre gabarit XML avec le fichier XML que vous souhaitez servir (par exemple : response.xml). Si le XML a des variables, utilisez le code gabarit  correspondant de web.py comme dans cet exemple:


    $def with (code)
    <?xml version="1.0"?>
    <RequestNotification-Response>
    <Status>$code</Status>
    </RequestNotification-Response>


Pour servir ce fichier, créez un programme standard web.py ( par exemple: response.py) et utilisez le code suivant. Soyez conscient que vous devez utiliser <code>web.header('Content-Type', 'text/xml')</code> pour dire au client que vous envoyez un fichier XML. (Vous n'avez pas besoin de définir explicitement l'en-tête des fichiers XML si votre fichier gabarit a l'extension '.xml' )

    import web

    render = web.template.render('templates/', cache=False)

    urls = (
        '/(.*)', 'index'
    )

    app = web.application(urls, globals())

    class index:
        def GET(self, code):
            web.header('Content-Type', 'text/xml')
            return render.index(code)

    web.webapi.internalerror = web.debugerror
    if __name__ == '__main__': app.run()