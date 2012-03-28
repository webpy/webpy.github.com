---
layout: default
title: A propos de Web.py
---

# A propos de Web.py

Autre langages : [english](/) | ...


**web.py** est un framework pour python qui est aussi simple qu'il est puissant. Web.py est dans le domaine publique; vous pouvez l'utiliser à toutes fins sans aucunes restrictions.

##Une application complète web.py

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

web.py 0.33 a été réalisé le 2009-10-28: [web.py-0.33.tar.gz][16]

   [16]: /static/web.py-0.33.tar.gz

Pour avoir toujours la dernière version de web.py, exécutez:
    
    git clone git://github.com/webpy/webpy.git
    ln -s `pwd`/webpy/web .

ou bien téléchargez la dernière version en [zip](http://github.com/webpy/webpy/zipball/master) ou [tarball](http://github.com/webpy/webpy/tarball/master).

Mise à jour depuis une version plus ancienne? Assurez-vous de [lire le guide de mise à jour][17].

   [17]: http://webpy.org/docs/0.3/upgrade

## Qui utilise web.py ?

web.py a été publié alors que Aaron Swartz travaillait sur [reddit.com][20], où le site l'utilisait pour grandir et devenir l'un des 1000 premiers sites selon Alexa et servait des millions de pages vues tous les jours. "C'est le framework anti-framework. web.py ne vous gagne en aucune manière," expliquait le fondateur Steve Huffman. (Le site a été réécrit en utilisant d'autres outils, après avoir été acquis par Condé Nast.)

   [20]: http://reddit.com/

[Frinki](http://frinki.com), Un réseau social de type Facebook en espagnol.

[Make History](http://makehistory.national911memorial.org), un projet du 9/11 Memorial Museum, qui est conçu avec Web.py en tête de Google App Engine. Le 11 septembre 2009, il reçevait près de 200.000 visiteurs. "C'est la première fois que je travaille avec web.py et essentiellement en Python," note son développeur. "web.py est génial."

[local.ch](http://www.local.ch), Le répertoire téléphonique en ligne officiel de Suisse - utilise web.py en service d'arrière plan pour suivre les contenus expirés - code en open-source sur [urldammit](http://github.com/harryf/urldammit/tree/master)

[sitecanary.com](https://sitecanary.com/) un site pour être alerté quand votre site web est hors-service.

[watchdog.net](http://watchdog.net/), un site de service politique, construit en web.py.

[archivd.com](http://www.archivd.com), une application web pour des recherches collaboratives et de l'archivage, réalisé avec web.py

[colr.org](http://www.colr.org), un site de ponctions de couleurs, réalisé avec web.py.


[Chiefmall](http://www.chiefmall.com/), un outil de recherche d'entrepeneurs, qui a été réalisé avec web.py.

[grouplite.com](http://www.grouplite.com) utilise web.py.

[Yandex][21], Un fournisseur d'acces internet Russe dont la page d'accueil seule reçoit 70 millions de visites par jour, utilise web.py pour certains projets.
   [21]: http://yandex.ru

[LShift][22] a utilisé web.py pour construire des sites web pour [Expro][23] et [publisher Dorling Kindersley][24]. "web.py nous permet de faire ce que nous faisons de mieux," rapportent-ils. "il réalise les applications web avec brio, sans nous obliger à faire des compromis sur la flexibilité et l'originalité."

   [22]: http://www.lshift.net/
   [23]: http://exproretail.com/
   [24]: http://travel.dk.com/

[micropledge][m], une application Web qui recueille des fonds pour des idées de logiciels, et qui est construite avec web.py. "Nous avons apprécié sont intégration avec son approche minimale," raconte le développeur Ben Hoyt.

   [m]: http://micropledge.com/

Le [bivalidateur](http://xhtml-css.com/) vérifie votre HTML et la validation CSS.

[jottit.com](http://jottit.com) est construit avec web.py.  Jottit permet d'obtenir un site web aussi facilement que le remplissage d'un champ de saisie. 

[Tasko][t] élaboré avec web.py. Tasko est un gestionnaire de tâches en ligne qui utilise un format de fichier de texte brut pour stocker toutes les informations.

   [t]: http://taskodone.com/

[Damiga][d] est bâtit avec web.py. Damiga est un endroit où vous pouvez anonymement et librement dire au monde ce que vous ressentez à propos d'autres personnes: amis, célébrités, même des personnages de fiction. C'est aussi un endroit où vous pouvez voir ce que le monde pense de vous. 

   [d]: http://damiga.com/

[Fotosaur.us][f], une incroyable application de marque-pages d'images, réalisée avec web.py.

   [f]: http://fotosaur.us


[URIs.us][u] est un service pour créer des urls courtes. Déployé sur Google App Engine

   [u]: http://uris.us 


[xykra] [x] est un wiki minimaliste (160 lignes de Python) qui utilise [Markdown](http://daringfireball.net/projects/markdown/).

   [x]: http://xykra.org

[Edgarest] [y] est réalisé avec Web.py. Edgarest fournit un accès rapide et une recherche intuitive de SEC Filings (publication de documents boursiers)

   [y]: http://edgarest.com


[Wklej.to] [z] est une application nopaste/Pastebin( application web qui permet aux utilisateurs de télécharger des morceaux de textes) avec une api ouverte et libre, et naturellement des modules Desktop et des clients.

   [z]: http://wklej.to

[Biomed Search] [zzz] recherche plus de un million d'images biomédicales dans des tailles bien visibles.

   [zzz]: http://www.biomed-search.com

"[web.py a inspiré le] framework web que nous utilisons tel que FriendFeed [et] l'application framework livrée avec App Engine..."  
 - [Brett Taylor](http://bret.appspot.com/entry/experimenting-google-app-engine), co-fondateur de FriendFeed et leader technique original de Google App Engine

"Dans l'écosystème des frameworks web, quelque chose doit occuper le créneau du "petit, léger et rapide". web.py est celui-là."  
- Lloyd Dalton, [colr.org](http://colr.org)

"Nous avons terminé la réécriture de notre serveur il y a quelques jours avec web.py et c'était tout ce que nous souhaitions."  
- Sam Hsiung, [YouOS][25]

   [25]: http://www.youos.com/

"Django vous permet d'écrire des applications web en Django. TurboGears vous permet d'écrire des applications web en TurboGears. Web.py vous permet d'écrire des applications web en Python."  
- Adam Atlas

"très élégant et concis (sans oublier que c'est écrit par Aaron Swartz, dont les compétences en codage sont impressionnantes), et ça ne m'a pas fait perdre de temps."   
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

### Documentation web.py :

* [installation](/install)
    * [english](/install)
    * [mac os x](/install_macosx)
    * [español](/install/es)
    * [日本語](/install/ja)
    * [简体中文](/install/zh-cn)
    * [Italiano](/install/it)
    * [français](/install/fr)


* [tutoriaux pour la version 0.3 (dernière en date)](/tutorial3)
    * [english](/tutorial3.en)
    * [简体中文](/tutorial3.zh-cn)
    * [p?????? 0.2](http://webpy.infogami.com/tutorial2.ru)
    * [????](http://www.dup2.org/files/web.py%200.2%20tutorial.html)
    * [template.py tutorial](/templetor)
    * [form.py (short) tutorial](/form)
    * [日本語](/tutorial2.ja)
    * [e???????](http://webpy.org/tutorial2.el)
    * [français](/tutorial3.fr)

* [tutoriaux (anciennes versions)](/tutorial):
    * [english](http://webpy.org/tutorial)
    * [español](/tutorial/es)
    * português: [1](http://www.writely.com/View.aspx?docid=bbcm927cd2fmj) [2](http://www.writely.com/View.aspx?docid=bbcnjdbhbfh6n) [3](http://www.writely.com/View.aspx?docid=bccxp4cgw36p3)
    * [français](http://sunfox.org/tutoriel-web-py-fr/)
    * [p??????](http://bobuk.infogami.com/webpytrans)
    * [日本語](http://kinneko.googlepages.com/webpy_tutorial_ja)


* [Documentation](/docs/0.3.fr)


* FAQ:
    * [english](http://webpy.org/faq)
    * [español](/faq/es)
    * [???????](/faq/ru)
    * [???](http://kinneko.googlepages.com/webpy_faq)
    * [日本語](/faq/ja)
    * [简体中文](/faq/zh-cn)
    * [français](/faq/fr)

* cookbook:
      * [日本語](/cookbook/ja)
      * [english](/cookbook)
      * [简体中文](/cookbook/zh-cn)
      * [français](/cookbook/fr)

* [exemples de code](/src)

* [friendly hosts](/hosts)

* [related projects](/related)

* [tricks](/tricks)


### Communauté web.py

* [**mail list**](http://groups.google.com/group/webpy/ "web.py google group"): home of the web.py discussion

* [**irc channel**](irc://irc.freenode.net/webpy "#webpy on irc.freenode.net"): home of the web.py talk

* [powered by web.py buttons](http://luke.jottit.com/webpy_logo)

### Developpement web.py 

* [git repository](http://github.com/webpy/webpy)

* [launchpad site](http://launchpad.net/webpy)