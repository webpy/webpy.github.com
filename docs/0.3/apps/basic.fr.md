---
layout: default
title: Basic Application
---

# Basic Application

Autres langages : [français](/../basic) | ...


La basic application définit un appariement des urls à des mappings de classe. Dans l'exemple ci-dessous, les variables URL définissent un appariement d'une expression régulière à un nom de classe.

Quand un utilisateur a accès à une ressource,  la liste des expressions régulières d'url est parcourue. Si une URL correspondant à la regex, la classe est instanciée, et la méthode 'GET' ou 'POST' est appelée selon la méthode http. Les données retournées depuis GET ou POST sont affichées dans le navigateur.


Si l'URL demandée ne correspond à aucune des expressions régulières, une erreur 404 est renvoyée.

## Exemple

    import web
            
    urls = (
        '/(.*)', 'hello'
    )
    app = web.application(urls, globals())
    
    class hello:        
        def GET(self, name):
            if not name: 
                name = 'World'
            return 'Hello, ' + name + '!'
    
    if __name__ == "__main__":
        app.run()