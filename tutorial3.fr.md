---
layout: default
title: web.py 0.3 tutorial
---

# web.py 0.3 tutorial

## Intoduction

Vous connaissez Python et vous désirez construire un site web. Webpy vous permettra de le faire facilement.

Si vous décidez de suivre l'ensemble de ce tutorial, vous aurez besoin d'installer Python, web.py, flup, psycopg2 et Postgres (ou une base de donnée equivalente et les pilotes python). Pour plus de détails, veuillez consulter [webpy.org](http://webpy.org/)

Si vous possédez déjà un projet web.py existant, jetez un oeil à la page de [mise à jour] (http://webpy.infogami.com/upgrade_to_point3) pour plus d'informations sur la migration.

## Commençons

## Manipuler les URLs

La partie la plus importante de n'importe quel site web est la structure des URLs. Les URLs ne sont pas que des liens que vos visiteurs voient et envoient par mails à leurs amis, elles fournissent aussi un modèle mental sur la façon avec laquel un site web fonctionne. Sur des sites populaires tels que del.icio.us, les URLs font partie même de l'interface utilisateur. Web.py rend la création d'URLs facile.

Pour commencer avec votre application web.py, ouvrez un nouveau fichier texte (que nous appelerons "code.py") et tapez:

     import web

Cela importera le module web.py.

Maintenant, Nous devons donner à web.py notre structure URL. Commençons avec quelque chose de simple:

     urls = (
            '/', 'index'
            )

La première partie est une expression régulière que l'on applique à une chaîne de caractère (l'URL), telle que /, /help/faq, /item/(\d+), etc.. (Note: \d+ n'admettra qu'une séquence de chiffre). Les parenthèses signifient qu'il faut capturer la séquence pour s'en servir plus tard. La seconde partie est le nom d'une Classe vers laquelle la requête sera envoyée, comme 'index', 'view', 'welcome.hello' (qui recherchera la Classe hello du module welcome.), ou get_\1.
/1 est remplacé par la première capture de l'expression régulière; toutes les captures restantes seront passées à votre fonction. [Note traducteur : A préciser]

Cette ligne signifie que nous souhaitons l'URL / (Note: la page d'accueil) qui doit être traitée par la classe nommée 'index'.

Maintenant, nous avons besoin de créer une application spécifiant les URLs.

     app = web.application(urls, globals())

Cela explique à web.py qu'il faut créer une application avec les URLs qui sont listées ci-dessus, en appelant les Classes dans l'espace de noms global de ce fichier.

Maintenant, il est nécessaire d'écrire la Classe 'index'. Alors que la plupart des gens ne le remarquent pas en naviguant simplement, votre navigateur utilise un protocole connu appelé HTTP pour communiquer avec le World Wide Web. Les détails ne sont pas importants, mais l'idée de base est que les visiteurs de sites web demandent aux serveurs de sites web de remplir certaines fonctions (telles que GET ou POST) sur les URLs (comme / ou /foo?f=1).

GET est celle que nous connaissons tous, celle qui sert à demander le texte d'une page web. Lorsque vous tapez 'harvard.edu' dans votre navigateur, cela demande littéralement au serveur web de Harvard de fournir /. La seconde fonction très célèbre, POST, est souvent utilisée lorsque vous utilisez certains types de formulaires, comme une demande d'achat d'un produit. Vous utilisez POST chaque fois que vous soumettez une demande (comme le débit de votre carte de crédit et le traitement d'une commande). Cela est essentiel, parce que GET URLs peut être transmis et indexé par les moteurs de recherche, que vous voulez certainement pour la plupart de vos pages, mais ne désirez certainement pas pour des choses comme le traitement des ordres (imaginez si Google essaye de tout acheter sur votre site!)

Dans notre code web.py, nous faisons la distinction entre les deux clairement:

     class index:
        def GET(self):
           return "Hello, world!"

Cette fonction GET sera maintenant appelée par web.py chaque fois qu'il y aura une requête GET pour /.

Très bien, maintenant nous avons juste besoin d'en finir avec une ligne finale disant à web.py de commencer à fournir des pages web:

     if __name__ == "__main__": app.run()

Cela explique à web.py qu'il faut lancer l'application que nous avons créé ci-dessus.

Maintenant notez que, bien que j'ai beaucoup parlé ici, nous avons seulement cinq ou six lignes de code tout au plus. C'est tout ce dont nous avons besoin pour créer une application web.py complète. Si vous allez dans votre terminal et que vous tapez les lignes de commande suivantes :

     $ python code.py

Vous verrez s'afficher : http://0.0.0.0:8080/

Vous avez maintenant votre application web.py qui tourne comme un vrai serveur web sur votre ordinateur!

En visitant cette URL, vous devriez voir "Hello, world!" dans votre navigateur. (Vous pouvez ajouter une adresse IP/Port après la partie "code.py" pour contrôler où web.py lancera le serveur. Vous pouvez aussi lui dire de faire fonctionner un serveur fastcgi ou scgi.)
[Note traducteur : A PRECISER]

Note: Vous pouvez spécifier le numéro de port à utiliser dans la ligne de commande, si vous ne souhaitez pas utiliser le port par défaut :

     $ python code.py 1234

## Modèles, gabarits

Ecrire du HTML à l'intérieur de python peut être lourd et pesant. C'est bien plus amusant d'écrire du Python à l'intérieur du HTML. Par bonheur, web.py le fait très facilement.

Note: Les anciennes versions de web.py utilisent le système de gabarit de [Cheetah] (http://www.cheetahtemplate.org/). Vous êtes, evidemment, libres d'utiliser celui-ci ou n'importe quel autre logiciel de template avec web.py, mais il n'est plus officiellement supporté.

Créons un nouveau répertoire pour nos gabarits (nous l'appellerons templates). A l'intérieur, créons un nouveau fichier dont l'extension sera HTML (appelons-le index.html). Dans ce fichier, vous pouvez juste écrire du HTML classique:

     <em>Hello</em>, world!

Ou utiliser le langage de template de web.py (Templator) pour ajouter du code dans votre HTML:

     $def with (name)

        $if name:
           I just wanted to say <em>hello</em> to $name.
        $else:
           <em>Hello</em>, world!