---
layout: default
title: Auto Application
---

# Auto Application

Autre langages : [english](/docs/0.3/apps/auto) | ...

L'auto application agit comme la [basic application](/docs/0.3/apps/basic/fr), seulement il ne nécessite pas un mapping d'url pour être créé. Le mapping est dérivé des noms de classe (utilisant les métaclasses). Dans sa forme la plus basique :

## Exemple

     app = web.auto_application() 

     class hello(app.page): 
         def GET(self): 
             return "hello, world!"
     
     if __name__ == '__main__':
         app.run() # goto http://hostname:8080/hello



Vous pouvez également modifier le chemin par défaut (qui est le nom de la classe) en définissant une variable de classe "path". Voir ci-dessous:

## Exemple:

    app = web.auto_application() 
    
    class hello(app.page): 
        path = "/foobar"
        def GET(self): 
            return "hello, world!" 
    
    if __name__ == '__main__':
        app.run() # goto http://hostname:8080/foobar