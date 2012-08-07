---
layout: default
title: web.py 0.3 tutorial
---

# web.py 0.3 tutorial

Autre langages : [english](/tutorial3.en) | [chinese](/tutorial3.zh-cn) | [japan](/tutorial2.ja) | ...

# Sommaire


* <a href="#introduction">Prérequis</a>
* <a href="#manipurl">Manipuler les URLs</a>
* <a href="#gereurl">Gérer les URLs</a>
* <a href="#getpost">GET et POST : la différence</a>
* <a href="#index">Page index - ma première classe</a>
* <a href="#lance">Lancer le serveur</a>
* <a href="#template">Modèles, gabarits</a>
* <a href="#formulaires">Formulaires</a>
* <a href="#bd">Base de données</a>
* <a href="#affbd">Afficher le contenu d'une base de données</a>
* <a href="#ecrbd">Ecrire dans une base de données</a>
* <a href="#debug">Debugger</a>
* <a href="#apres">Et Après ?</a>

<a name="introduction"></a>
# Prérequis



Vous connaissez Python et vous désirez construire un site web. Webpy vous permettra de le faire facilement.

Si vous décidez de suivre l'ensemble de ce tutorial, vous aurez besoin d'installer Python, [web.py] (/install/fr) , flup, psycopg2 et Postgres (ou une base de donnée equivalente et les pilotes python). Pour plus de détails, veuillez consulter [webpy.org](http://webpy.org/)

Si vous possédez déjà un projet web.py existant, jetez un oeil à la page de [mise à jour](http://webpy.org/docs/0.3/upgrade) pour plus d'informations sur la migration.


# Commençons


<a name="manipurl"></a>
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

<a name="gereurl"></a>
## Gérer les URLs

Maintenant, nous avons besoin de créer une application spécifiant les URLs.

     app = web.application(urls, globals())

Cela explique à web.py qu'il faut créer une application avec les URLs qui sont listées ci-dessus, en appelant les Classes dans l'espace de noms global de ce fichier.

<a name="getpost"></a>
## GET et POST: la différence

Alors que la plupart des gens ne le remarquent pas en naviguant simplement, votre navigateur utilise un protocole connu appelé HTTP pour communiquer avec le World Wide Web. Les détails ne sont pas importants, mais l'idée de base est que les visiteurs de sites web demandent aux serveurs de sites web de remplir certaines fonctions (telles que GET ou POST) sur les URLs (comme / ou /foo?f=1).

GET est celle que nous connaissons tous, celle qui sert à demander le texte d'une page web. Lorsque vous tapez 'harvard.edu' dans votre navigateur, cela demande littéralement au serveur web de Harvard de fournir /. La seconde fonction très célèbre, POST, est souvent utilisée lorsque vous utilisez certains types de formulaires, comme une demande d'achat d'un produit. Vous utilisez POST chaque fois que vous soumettez une demande (comme le débit de votre carte de crédit et le traitement d'une commande). Cela est essentiel, parce que GET URLs peut être transmis et indexé par les moteurs de recherche, que vous voulez certainement pour la plupart de vos pages, mais ne désirez certainement pas pour des choses comme le traitement des ordres (imaginez si Google essaye de tout acheter sur votre site!)


<a name="index"></a>
## Page index - ma première classe

Dans notre code web.py, nous faisons la distinction entre les deux clairement. Maintenant, il est nécessaire d'écrire la Classe 'index'.

     class index:
        def GET(self):
           return "Hello, world!"

Cette fonction GET sera maintenant appelée par web.py chaque fois qu'il y aura une requête GET pour /.

Très bien, maintenant nous avons juste besoin d'en finir avec une ligne finale disant à web.py de commencer à fournir des pages web:

     if __name__ == "__main__": app.run()

Cela explique à web.py qu'il faut lancer l'application que nous avons créé ci-dessus.

Maintenant notez que, bien que j'ai beaucoup parlé ici, nous avons seulement cinq ou six lignes de code tout au plus. C'est tout ce dont nous avons besoin pour créer une application web.py complète. 

<a name="lance"></a>
## Lancer le serveur

Si vous allez dans votre terminal et que vous tapez les lignes de commande suivantes :

     $ python code.py

Vous verrez s'afficher : http://0.0.0.0:8080/

Vous avez maintenant votre application web.py qui tourne comme un vrai serveur web sur votre ordinateur!

En visitant cette URL, vous devriez voir "Hello, world!" dans votre navigateur. (Vous pouvez ajouter une adresse IP/Port après la partie "code.py" pour contrôler où web.py lancera le serveur. Vous pouvez aussi lui dire de faire fonctionner un serveur fastcgi ou scgi.)

[Note traducteur : A PRECISER]

Note: Vous pouvez spécifier le numéro de port à utiliser dans la ligne de commande, si vous ne souhaitez pas utiliser le port par défaut :

     $ python code.py 1234



<a name="template"></a>
# Modèles, gabarits

Ecrire du HTML à l'intérieur de python peut être lourd et pesant. C'est bien plus amusant d'écrire du Python à l'intérieur du HTML. Par bonheur, web.py le fait très facilement.

Note: Les anciennes versions de web.py utilisent le système de gabarit de [Cheetah] (http://www.cheetahtemplate.org/). Vous êtes, evidemment, libres d'utiliser celui-ci ou n'importe quel autre logiciel de template avec web.py, mais il n'est plus officiellement supporté.

Créons un nouveau répertoire pour nos gabarits (nous l'appellerons templates). A l'intérieur, créons un nouveau fichier dont l'extension sera HTML (appelons-le index.html). Dans ce fichier, vous pouvez juste écrire du HTML classique:

     <em>Hello</em>, world!

Ou utiliser le langage de template de web.py ( [Templator](http://webpy.org/docs/0.3/templetor.fr) ) pour ajouter du code dans votre HTML:

     $def with (name)

        $if name:
           I just wanted to say <em>hello</em> to $name.
        $else:
           <em>Hello</em>, world!

Comme vous pouvez le voir, les gabarits ressemblent beaucoup à des fichiers Python, excepté la déclaration 'def' tout en haut (qui explique avec quoi le modèle est appelé) ainsi que les $s placés devant chaque code. 
Actuellement, template.py exige que la déclaration $def soit la première ligne du gabarit. Notez également que web.py encode automatiquement les variables utilisées ici, de sorte que si, pour une raison un nom est défini dans une valeur contenant du HTML, il sera proprement encodé et apparaitra comme un texte plein. 
Si vous souhaitez désactiver cette fonction, écrivez $:name à la place de $name.

Maintenant, retournons à notre "code.py". Sous la première ligne ajoutez:

     render = web.template.render('templates/')

Cela indique à web.py qu'il faut rechercher le gabarit dans le repertoire 'templates'. Maintenant modifiez le contenu de la fonction GET dans index en:

     name = 'Bob'    
     return render.index(name)

(Ici, 'index' est le nom du gabarit et 'name' est un argument qui lui est transmis)

Visitez votre site, il devrait vous afficher "I just wanted to say hello to Bob."

Mais imaginons que nous souhaitions que les gens entrent leur propre nom. Dans ce cas, remplacez les deux lignes que nous avons ajouté par:

     i = web.input(name=None)
     return render.index(i.name)

En visitant / il devrait vous afficher "Hello, world!". Mais en visitant /?name=Joe il vous affichera "I just wanted to say hello to Joe."
Naturellement, en voyant ceci, on constate que l'URL n'est pas très claire. Pour l'améliorer, modifiez votre ligne URL en haut en:

     '/(.*)', 'index'

Et modifiez la définition de la fonction GET de la classe index en:

     def GET(self, name):
        return render.index(name)

puis effaçez la ligne qui définit le nom. Maintenant, visitez /joe et il devrait vous afficher hello to Joe.

Si vous désirez en apprendre davantage sur les gabarits de web.py, visitez la page [Templetor](http://webpy.org/templetor)

<a name="formulaires"></a>
# Formulaires

Le module de formulaire de web.py permet de générer des formulaires HTML, de récuperer les entrées des utilisateurs, et les valider avant de les traiter ou les ajouter à une base de donnée.
Si vous souhaitez en apprendre plus sur l'utilisation du module de formulaires de web.py, consultez la [Documentation](http://webpy.org/docs/0.3.fr) ou la traduction française du module [Formulaires](http://webpy.org/docs/0.3/form.fr)

<a name="bd"></a>
# Base de données

Note: Avant de pouvoir utiliser une base de données, soyez certains d'avoir la librairie de la base de données appropriée déjà installée. Pour la base de donnée MySQL, utilisez MySQLdb et pour Postgres, utilisez psycopg2.

Premièrement, vous devez créer un objet database.

     db = web.database(dbn='postgres', user='username', pw='password', db='dbname')

(Adaptez ici -- particulièrement pour `username`, `password`, and `dbname` -- vos paramètres de connexion. les utilisateurs de MySQL devront modifier la définition `dbn` en `mysql`.)

C'est tout ce dont vous avez besoin -- web.py gèrera automatiquement la connexion et la déconnexion à la base de données.

<a name="affbd"></a>
## Afficher le contenu d'une base de données

Utilisez votre interface d'administration de la base de données, et créez une simple table dans la base de données:

     CREATE TABLE todo (
        id serial primary key,
        title text,
        created timestamp default now(),
        done boolean default 'f'    
        );

Ainsi qu'une ligne initiale:

     INSERT INTO todo (title) VALUES ('Learn web.py');

Revenez à "code.py" et modifiez la fonction 'GET' de la Classe 'index' de la façon suivante en remplaçant la fonction entièrement:

     def GET(self):
        todos = db.select('todo')
        return render.index(todos)

puis remodifiez le gestionnaire d'URLs pour qu'il ne prenne en compte que /:

     '/', 'index'

Editez et remplaçez le contenu entier du gabarit `index.html` de cette façon:

     $def with (todos)
        <ul>
           $for todo in todos:
              <li id="t$todo.id">$todo.title</li>
        </ul>

En visitant à nouveau votre site, vous devriez voir: "Learn web.py". 

Félicitations ! Vous venez de créer une application complète qui lit une base de données. 

<a name="ecrbd"></a>
## Ecrire dans une base données

Maintenant, nous allons écrire dans la base de données.

A la fin du gabarit `index.html`, ajoutez:

     <form method="post" action="add">
        <p><input type="text" name="title" /> <input type="submit" value="Add" /></p>
     </form>

puis modifiez la liste de vos URLs pour qu'elle ressemble à:

     '/', 'index',
     '/add', 'add'

(Vous devez être très prudents avec les virgules. Si vous en oubliez, Python joint les chaînes ensembles, et verra `/index/addadd` à la place de votre liste d'URLs!)

Maintenant, ajoutons une nouvelle Classe:

     class add:
        def POST(self):
           i = web.input()
           n = db.insert('todo', title = i.title)
           raise web.seeother('/')

(Avez-vous noté que nous utilisons la fonction `POST` pour celle-ci?)

`web.input` vous donne accès à toutes les variables de l'utilisateur soumises via un formulaire.

Note: Afin d'accéder aux données à partir de plusieurs éléments identiquement nommé, dans un format de liste (Une série de cases à cocher qui ont toutes l'attribut name="name"), utilisez:

     post_data=web.input(name=[])

`db.insert` insère les valeurs dans la table `todo` de la base de données et renvoie l'ID de la ligne créée.  
`seeother` redirige les utilisateurs vers cette URL.

Quelques notes additionnelles: 

`db.update` fonctionne comme `db.insert` excepté qu'au lieu de renvoyer l'ID, il doit recevoir en argument, après le nom de la table, soit l'ID soit une clause `WHERE` permettant d'identifier la ligne à modifier.

    
    db.update('todo', where="id = 10", title = "web.py pour les nuls")


`web.input`, `db.query`, et d'autres fonctions dans web.py renvoient des Objets de Stockage (Storage objects), qui sont comme des dictionnaires mis à part que vous pouvez écrire `d.foo` en plus de `d['foo']`. Cela rend le code plus clair.

<a name="debug"></a>
# Debugger

web.py possède aussi des outils de debugging pour nous aider. Quand nous le faisons tourner avec le server web intégré, il commence l'application en mode debuggage. Dans ce mode, toutes les modifications du code et des gabarits sont automatiquement rechargées et les messages d'erreur contiennent de précieuses informations.

Le debuggage n'est pas actif lorsque l'application tourne comme un vrai serveur. Si vous souhaitez désactiver ce mode, vous pouvez le faire en ajoutant la ligne suivante avant de créer votre application/gabarit:

     web.config.debug = False

C'est la fin du tutorial maintenant. Jetez un oeil à la [Documentation](http://webpy.org/docs/0.3.fr) pour voir ce que vous pouvez utiliser avec web.py.

Vous pourrez trouver pleins de détails de tout ceci ainsi que de toutes les fonctions web.py dans la [Documentation](http://webpy.org/docs/0.3.fr).

<a name="apres"></a>
## Et après ?

* [Plus de documentation](/docs/0.3.fr) 
* [Formulaires](/docs/0.3/form.fr) 
* [Templator: le modèle de gabarit de web.py](/docs/0.3/templetor.fr)
* [Cookbook](/cookbook/fr)
* [Exemples de codes](/src)