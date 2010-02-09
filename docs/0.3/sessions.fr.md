---
layout: default
title: Les sessions web.py
---

# Les sessions web.py

Autres langages : [english](/../sessions) | ...


Les sessions sont un moyen de stocker des informations entre les requêtes, faisant ainsi du http un protocole avec état. Elles fonctionnent en envoyant à l'utilisateur un cookie, qui mappe vers un objet de stockage de session sur le serveur. Lorsque l'utilisateur fait une requête vers une page, le client renvoie le cookie avec la requête, web.py charge la session basée sur sa clef, et le code peut demander et stocker des informations dedans.

Les sessions sont pratiques car elles permettent à un programmeur de stocker l'état des utilisateurs dans des objets natifs Python.

## Types de stockage

Les sessions de web.py permettent différents procédés de stockage des données sessions. Ces méthodes comprennent:

* DiskStore: Les données sessions sont sérialisées dans un repertoire désigné. Lors de l'instanciation, le premier et le seul argument est le dossier dans lequel les informations de session doivent être stockées sur le disque.

* DBStore: Les données sessions sont sérialisées et sotckées dans une base de donnée. Cela peut être très utile si vous souhaitez stocker les données sessions sur un système séparé. Pendant la création, DBStore prend deux arguments: une instance web.py de base de donnée, et le nom de la table (string). La table qui stocke la session doit avoir la structure suivante:


        session_id CHAR(128) UNIQUE NOT NULL,
        atime DATETIME NOT NULL default current_timestamp,
        data TEXT

* ShelfStore: Les données sont stockées en utilisant le module [shelve](http://docs.python.org/library/shelve.html) de python.


Les méthodes de stockage ont des performances variées et des ajustement d'installation, donc les options vous permettent de choisir ce qui convient le mieux pour votre appplication.

## Exemple
Le code suivant montre comment utiliser une session de base DiskStore.

    import web
    
    
    urls = (
        '/', 'Index',
        '/login', 'Login',
        '/logout', 'Logout',
    )
    
    web.config.debug = False
    app = web.application(urls, locals())
    session = web.session.Session(app, web.session.DiskStore('sessions'))      
    
    class Index:
        def GET(self):
            if session.get('logged_in', False):
                return '<h1>You are logged in</h1><a href="/logout">Logout</a>'
            return '<h1>You are not logged in.</h1><a href="/login">Login now</a>'
    
    class Login:
        def GET(self):
            session.logged_in = True
            raise web.seeother('/')
    
    class Logout:
        def GET(self):
            session.logged_in = False
            raise web.seeother('/')
    
    
    if __name__ == '__main__':
        app.run()