---
layout: default
title: web.py 0.2 tutorial
---

# web.py 0.2 tutorial

## Installation
Vous  connaissez Python et vous voulez construire un site web. Web.py fournit le code pour faire cela d'une manière simple.

Si vous voulez faire l’ensemble de ce tutoriel vous devrez installer Python, web.py, flup, psycopg2 et Postgres (ou une autre base de données avec son driver pour Python, par exemple : MySQL et mysqldb). Pour plus de détails voir le site de [webpy.org](http://webpy.org/).

Si vous avez un projet web.py existant, regardez la page de [upgrade](http://webpy.infogami.com/upgrade_to_point2) pour plus d’informations sur la migration vers la nouvelle version.



## Gestion des URLs
La partie la plus importante pour chaque site web  est la structure des URLs. Les URLs ne sont pas seulement ce que les visiteurs regarde et partage avec d’autres amis, mais ils sont aussi un modèle mental qui indique comment un Site Web fonctionne. (Dans les sites populaires comme [del.icio.us](http://del.icio.us/), les URLs font partie de l’interface de l’utilisateur). Pour cela Web.py facilite la création et la gestion des URL.

Pour commencer l’application  web.py , Créez un nouveau fichier et appelez le code.py par exemple et écrivez ceci dedans:

    import web

Ceci importera le module web.py.

Maintenant on implémente la structure de nos URLs, on commence par quelque chose de simple, ajoutez cela :

    urls = (
      '/', 'index'    )


La première partie est l’[expression régulière](http://osteele.com/tools/rework/)  qui représente un chemin. Par exemple : ‘/’, ‘/aide/faq’, ‘/article/(\d+)’, etc. Le \d+ représente une séquence de chiffres. Les parenthèses (..) servent à capturer les éléments retournés pour plus tard. La deuxième partie est le nom d’une classe à laquelle envoyer la requête, comme view, welcomes.hello (qui utilise la classe hello du module welcomes), ou bien get_\1. \1 est remplacé par la première capture de l’expression régulière. Toutes captures restantes seront passées à la fonction.

La ligne ('/', 'index') dis qu’on a besoin de l’URL ‘/’ (i.e la page d’accueil) qui sera prit en charge  par la classe nommé ‘index’.

Maintenant on écrit le code de la classe index:

    class index:
        def GET(self):
            print " Bonjour, monde !"

Comme vous avez pu le deviner, `GET` est appelé par web.py lorsque quelqu’un appelle la méthode HTTP GET sur votre URL ‘/’ (c’est-à-dire quand ils la visitent avec un navigateur web). La dernière ligne renvoie le texte brut “Bonjour, monde !” au visiteur.

Tous est bon maintenant, on aura besoin que de finir en ajoutant la ligne qui démarre l’application web

    if __name__ == "__main__": web.run(urls, globals())

Ceci dit à web.py de lancer votre application avec `urls` en regardant toutes les classes présentes dans le fichier.

Pour lancer le serveur web faisant tourner votre application tapez dans une invite de commande:

    $ python code.py
    Launching server: http://0.0.0.0:8080/

Maintenant si vous visitez http://0.0.0.0:8080/ avec un navigateur web, vous devriez voir apparaître “Bonjour, monde !”.

**Note:** vous pouvez spécifier le port en le passant comme paramètre

    $ python code.py 1234

Puis visiter la page : http://0.0.0.0:1234/

(La suite à accomplir...)