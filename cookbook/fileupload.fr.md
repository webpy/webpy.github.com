---
layout: default
title: Uploader un fichier
---

# Uploader un fichier

Autre langages: [english](/../fileupload) | ...

## Problème:

L'upload de fichiers peut être un peu difficile si vous n'êtes pas familier avec les formulaires
uploads, ou le CGI en général.

## Solution:

    import web
    
    urls = ('/upload', 'Upload')
    
    class Upload:
        def GET(self):
            return """<html><head></head><body>
    <form method="POST" enctype="multipart/form-data" action="">
    <input type="file" name="myfile" />
    <br/>
    <input type="submit" />
    </form>
    </body></html>"""
    
        def POST(self):
            x = web.input(myfile={})
            web.debug(x['myfile'].filename) # Ceci est le nom du fichier
            web.debug(x['myfile'].value) # Ceci est le contenu du fichier
            web.debug(x['myfile'].file.read()) # Ou utilisez un objet de type fichier
            raise web.seeother('/upload')


    if __name__ == "__main__":
       app = web.application(urls, globals()) 
       app.run()

## A savoir

Deux petites choses à surveiller:

* Le formulaire a besoin d'un attribut enctype="multipart/form-data", ou cela ne fonctionnera pas correctement.
* Dans le code de webpy, une valeur par défaut est néssessaire (*the myfile={}*) si vous voulez qu'il soit importé comme un objet FieldStorage CGI. Si vous ne spécifiez pas une valeur par défaut, le fichier sera transmis sous forme de chaîne -- cela fonctionne, mais vous perdez l'attribut nom de fichier.