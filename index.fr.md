---
layout: default
title: A propos de Web.py
---

# A propos de Web.py

Autre langages: [English](/) | [Español](/index.es.html) | ...

**web.py** est un framework pour python qui est aussi simple qu'il est puissant. Web.py est dans le domaine publique; vous pouvez l'utiliser à toutes fins sans aucunes restrictions.

## Une application complète web.py

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

## Pour commençer

web.py 0.51 a été réalisé le 2019-09-27: [web.py-0.51.tar.gz][16]

   [16]: https://github.com/webpy/webpy/archive/0.51.zip

Pour avoir toujours la dernière version de web.py, exécutez:
    
    git clone git://github.com/webpy/webpy.git
    ln -s `pwd`/webpy/web .

ou bien téléchargez la dernière version en [zip](http://github.com/webpy/webpy/zipball/master) ou [tarball](http://github.com/webpy/webpy/tarball/master).

Mise à jour depuis une version plus ancienne? Assurez-vous de [lire le guide de mise à jour][17].

   [17]: http://webpy.org/docs/0.3/upgrade

## Qui utilise web.py ?

web.py a été publié alors que Aaron Swartz travaillait sur [reddit.com][20], où le site l'utilisait pour grandir et devenir l'un des 1000 premiers sites selon Alexa et servait des millions de pages vues tous les jours. "C'est le framework anti-framework. web.py ne vous gagne en aucune manière," expliquait le fondateur Steve Huffman. (Le site a été réécrit en utilisant d'autres outils, après avoir été acquis par Condé Nast.)

   [20]: http://reddit.com/

* [Make History](http://makehistory.national911memorial.org), un projet du 9/11 Memorial Museum, qui est conçu avec Web.py en tête de Google App Engine. Le 11 septembre 2009, il reçevait près de 200.000 visiteurs. "C'est la première fois que je travaille avec web.py et essentiellement en Python," note son développeur. "web.py est génial."

* [local.ch](http://www.local.ch), Le répertoire téléphonique en ligne officiel de Suisse - utilise web.py en service d'arrière plan pour suivre les contenus expirés - code en open-source sur [urldammit](http://github.com/harryf/urldammit/tree/master)

* [colr.org](http://www.colr.org), un site de ponctions de couleurs, réalisé avec web.py.

* [Yandex][21], Un fournisseur d'acces internet Russe dont la page d'accueil seule reçoit 70 millions de visites par jour, utilise web.py pour certains projets.
   [21]: http://yandex.ru

* [LShift][22] a utilisé web.py pour construire des sites web pour [Expro][23] et [publisher Dorling Kindersley][24]. "web.py nous permet de faire ce que nous faisons de mieux," rapportent-ils. "il réalise les applications web avec brio, sans nous obliger à faire des compromis sur la flexibilité et l'originalité."

   [22]: http://www.lshift.net/
   [23]: http://www.lshift.net/blog/2006/11/15/web-development-with-dynamic-languages/
   [24]: http://travel.dk.com/

* [URIs.us][u] est un service pour créer des urls courtes. Déployé sur Google App Engine

   [u]: http://uris.us 

* [Biomed Search] [zzz] recherche plus de un million d'images biomédicales dans des tailles bien visibles.

   [zzz]: http://www.biomed-search.com

### Appréciations des

"Dans l'écosystème des frameworks web, quelque chose doit occuper le créneau du "petit, léger et rapide". web.py est celui-là."  
- Lloyd Dalton, [colr.org](http://colr.org)

"Nous avons terminé la réécriture de notre serveur il y a quelques jours avec web.py et c'était tout ce que nous souhaitions."  
- Sam Hsiung, [YouOS][25]

   [25]: http://www.youos.com/

"Django vous permet d'écrire des applications web en Django. TurboGears vous permet d'écrire des applications web en TurboGears. Web.py vous permet d'écrire des applications web en Python."  
- Alice Atlas

"Très élégant et concis (sans oublier que c'est écrit par Aaron Swartz, dont les compétences en codage sont impressionnantes), et ça ne m'a pas fait perdre de temps."   
- Jonas Galvez, Aupeo [#][26]

   [26]: http://www.artima.com/forums/flat.jsp?forum=106&thread=146149

"Le premier framework ... sur lequel je peux bidouiller du code et voir quelque chose fonctionner sans même être obligé de comprendre la logique de celui-ci. Un plaisir à intégrer."   
- Delaunay Antoine built [a photo gallery][28] and [an agenda][34] with it

   [28]: http://github.com/antoine/ibrouteur/
   [34]: http://metagenda.org

"Guido [van Rossum, Créateur de Python], vous constaterez probablement que web.py convient le mieux à votre style. ...Si vous ne l'aimez pas, je ne peux imaginer lequel des autres douzaines d'autres framework sortis vous *pourriez* aimer."   
- Phillip J. Eby, créateur du Python Web Server Gateway Interface (WSGI) [#lien][30]

   [30]: http://www.artima.com/forums/flat.jsp?forum=106&thread=146149&start=30&msRange=15

"... l'exemple [Cheetah] que j'ai vu sur web.py à l'air "bon". (web.py itself OTOH gets an "F", for undocumented code with too much magic behavior. upvars(), bah.)"  [ Note traducteur : A préciser]
- Guido van Rossum, Créateur de Python [#Lien][31]

   [31]: http://www.artima.com/weblogs/viewpost.jsp?thread=146503

"il suffit de dire je crois, que Aaron se dirige dans la bonne direction."   
- Harry Fuecks: [un simple wiki avec web.py][32]

   [32]: http://www.sitepoint.com/blogs/2006/01/06/a-simple-wiki-with-webpy/

"un moment très fascinant pour moi. Le même sentiment que j'ai eu lorsque j'ai écrit pour la première fois un script PHP. il est certain que ça me permettra d'apprendre python de façon amusante. Bon travail Aaron !"   
- Kamal [Un simple blog en webpy, apprendre python de façon amusante][33]

   [33]: http://www.k4ml.com/node/165
