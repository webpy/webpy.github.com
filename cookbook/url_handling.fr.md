---
layout: default
title: Comprendre la gestion des urls
---

# Comprendre la gestion des urls

Autres langages [english](/../url_handling) | ...

##Probleme: Comment conçevoir un gestionnaire d'url / distribuer un schéma pour l'ensemble du site


##Solution:

Le schéma de traitement des urls de web.py est simple, mais puissant et flexible. Au sommet de chaque application, vous trouverez habituellement le schéma complet de distribution des urls défini comme un tuple:


    urls = (
        "/tasks/?", "signin",
        "/tasks/list", "listing",
        "/tasks/post", "post",
        "/tasks/chgpass", "chgpass",
        "/tasks/act", "actions",
        "/tasks/logout", "logout",
        "/tasks/signup", "signup"
    )


Le format de ce tuple est: _motif du chemin url_, _gestionnaire de classe_ ce modèle se répètera tant que des motifs de chemins urls sont définis. Si vous ne comprenez pas la relation entre les motifs des chemins urls et les gestionnaire de classe, veuillez lire l'exemple [Hello World](/../helloworld/fr) ou le [rapide tutorial](/tutorial3.fr) avant de lire d'autres astuces cookbook.

## Correspondance des chemins


Vous pouvez utiliser la puissance des expressions régulières pour conçevoir des modèles urls plus flexibles. Par exemple,
/(test1|test2) capturera soit /test1, soit /test2. Le point clef à comprendre est que ce filtrage se déroule sur le 'chemin' même de l'url. Par exemple, pour l'url suivante:

    http://localhost/myapp/greetings/hello?name=Joe


Le chemin de cette URL est _/myapp/greetings/hello_. web.py ajoutera en interne ^ et $ à la structure de l'url, ce qui fait que le motif _/task/_ ne filtrera pas _/tasks/addnew_. Tandis qu'il filtre le chemin, vous ne pouvez pas utiliser un motif de type: _/tasks/delete?name=(.+)_ alors que la partie après ? appelée 'requête' n'est pas filtrée. Pour une description détaillée des éléments d'URL, veuillez lire [web.ctx](/cookbook/ctx).


##Capture de paramètres

Dans un motif url vous pouvez capturer des paramètres qui peuvent être utilisés dans votre gestionnaire de classe:

    /users/list/(.+), "list_users"

Les blocs après _list/_  sont capturés et peuvent être utilisés comme paramètres dans GET et POST:

    class list_users:
        def GET(self, name):
            return "Liste des infos conçernant l'utilisateur: {0}".format(name)

Vous pouvez définir plusieurs paramètres si vous le souhaitez. Notez simplement, que les paramètres de requête URL (qui apparaissent après le ?) peuvent être obtenues à l'aide de [web.input()](/cookbook/input)

##Note sur les sous_applications

Afin de mieux traiter de grandes applications Web, web.py encourage l'utilisation des [sous-applications](/cookbook/subapp/fr). Tout en concevant des mécanismes d'URL avec des sous-applications, gardez à l'esprit que le chemin (web.ctx.path) trouvera un  chemin parent dépouillé. 
Par exemple, si dans l'application principale, vous transmettez un format d'url "/blog" à la sous-application 'blog', dans votre sous-application blog, tous les formats d'url commençeront avec "/", et non avec /blog. Lisez les astuces cookbook [web.ctx](/cookbook/ctx) pour plus de détails.