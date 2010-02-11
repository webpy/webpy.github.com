---
layout: default
title: Stocker un fichier uploadé
---

# Stocker un fichier uploadé

Autre langages: [english](/../storeupload) | ...

## Problème

Vous voulez uploader un fichier et le stocker dans un dossier prédéfini.

## Solution

    import web
    
    urls = ('/upload', 'Upload')
    
    class Upload:
        def GET(self):
            web.header("Content-Type","text/html; charset=utf-8")
            return """<html><head></head><body>
    <form method="POST" enctype="multipart/form-data" action="">
    <input type="file" name="myfile" />
    <br/>
    <input type="submit" />
    </form>
    </body></html>"""
    
        def POST(self):
            x = web.input(myfile={})
            filedir = '/path/where/you/want/to/save' # modifiez ceci pour le répertoire dans lequel vous voulez stocker le fichier.
            if 'myfile' in x: # pour vérifier si le l'objet fichier est créé.
                filepath=x.myfile.filename.replace('\\','/') # Remplace les "slashs" de type windows par ceux de linux.
                filename=filepath.split('/')[-1] # scinde et choisit la dernière partie (le nom du fichier avec l'extension)
                fout = open(filedir +'/'+ filename,'w') # crée le fichier où le fichier téléchargé doit être stocké
                fout.write(x.myfile.file.read()) # écrit le fichier téléchargé vers le fichier nouvellement créé.
                fout.close() # clôt le fichier, upload terminé.
            raise web.seeother('/upload')


    if __name__ == "__main__":
       app = web.application(urls, globals()) 
       app.run()

## A savoir

Deux petites choses à surveiller:

* Voir [Uploader un fichier](/../fileupload/fr).
* Ne pas mettre le fichier dans un dossier qui est exécutable sans vérification de l'extension et du type de fichier.
* En fait, nous avons besoin d'ouvrir l'objet fichier 'fout' en mode "wb" (sous Windows) *mode d'écriture binaire, sinon l'image uploadée est cassée.*