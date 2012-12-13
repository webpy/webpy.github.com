---
layout: default
title: Installation
---

# Installation

Autre langages : [español](/install/es) | [Japan](/install/ja) | [chinese](/install/zh-cn) | [italiano](/install/it) | [english](/install) 

## Sommaire

* <a href="#installation">Installation</a>
	* <a href="#macosx">.. sur MacOS X</a>
* <a href="#dev">Développement</a>
* <a href="#prod">Production</a>
	* <a href="#lighttpd">LightTPD</a>
		* <a href="#lighttpdfastcgi">...avec FastCGI</a>
	* <a href="#apache">Apache</a>
		* <a href="#apachecgi">...avec CGI</a>
		* <a href="#apachecgihtaccess">.. avec CGI en utilisant .htaccess</a>
		* <a href="#apachefastcgi">.. avec FastCGI</a>
		* <a href="#apachescgi">.. avec SCGI</a>
		* <a href="#apachemodpython">.. avec mod_python</a>
		* <a href="#apachemodwsgi">.. avec mod_wsgi</a>
		* <a href="#apachemodrewrite">.. avec mod_rewrite</a>


<a name="installation"></a>
## Installation
Pour installer web.py, commencez par télécharger l'archive:
    
[web.py-0.33.tar.gz] (/static/web.py-0.33.tar.gz)

Décompressez l'archive et copier le dossier _web_ dans le dossier de votre application. Ou, pour rendre web.py accessible par toutes les applications, exécutez:
    
    python setup.py install

Note: sur certains systèmes Unix (ou Linux), il vous faudra vous connecter en tant que root (commande su) ou exécuter:

    sudo python setup.py install

Une autre option est d'utiliser [Easy Install](http://peak.telecommunity.com/DevCenter/EasyInstall). Une fois Easy Install correctement paramétré, exécutez:


    easy_install web.py

<a name="macosx"></a>
### ... Sur MacOS X

La procédure d'installation sur MacOS X n'a pas encore été traduite. Vous pouvez cependant visionner la version anglaise pour la version 0.1 : [Install MacOS X](/install_macosx) 


<a name="dev"></a>
## Développement:

webpy intègre son propre serveur web.  Apprenez comment écrire une application en suivant le [tutoriel](/tutorial3.fr).  Quand votre application est écrite, insérez votre code dans `code.py` et démarrez le serveur avec la commande:

     python code.py

Ouvrez votre navigateur et allez à l'adresse [http://localhost:8080/](http://localhost:8080/) pour visualiser la page. Pour spécifier un port différent, utilisez simplement `python code.py 1234`.

<a name="prod"></a>
## Production

Le serveur web intégré à web.py est bien pratique en phase de développement, mais pour un site en production, il vaut mieux prévoir quelque chose de plus sérieux. web.py fonctionne avec n'importe quel serveur http compatible avec  [WSGI](http://www.python.org/dev/peps/pep-0333/). 

WSGI est une API permettant la communication entre serveur web et applications, similaire à Java's Servlet Interface. Pour faire fonctionner web.py avec CGI, FastCGI ou SCGI, il vous faudra installer [flup](http://trac.saddi.com/flup) ([téléchargez ici](http://www.saddi.com/software/flup/dist/)), qui permet d'interfacer WSGI avec ces différentes API.

Pour utiliser une de ces variantes de CGI, ajoutez au début de votre `code.py` la ligne suivante :

    #!/usr/bin/env python

N'oubliez pas de le rendre exécutable: `chmod +x code.py`.

<a name="lighttpd"></a>
### LightTPD

<a name="lighttpdfastcgi"></a>
#### .. avec FastCGI

FastCGI associé à lighttpd est la manière recommandée d'utiliser web.py en production. [reddit.com][3] gère des millions de visites de cette façon.

   [3]: http://reddit.com/

Votre configuration lighttpd doit ressemble à ceci:
    
     server.modules = ("mod_fastcgi", "mod_rewrite")
     server.document-root = "/path/to/root/"     
     fastcgi.server = ( "/code.py" =>     
     (( "socket" => "/tmp/fastcgi.socket",
        "bin-path" => "/path/to/root/code.py",
        "max-procs" => 1
     ))
     )
    
     url.rewrite-once = (
       "^/favicon.ico$" => "/static/favicon.ico",
       "^/static/(.*)$" => "/static/$1",
       "^/(.*)$" => "/code.py/$1"
     )
    
Avec certaines versions de lighttpd, il est important de s'assurer que la propriété "check-local" du paramètre fastcgi.server est bien positionné à "false", surtout si votre `code.py` est situé en dehors de la racine.

Si vous recevez un message d'erreur indiquant qu'il n'est pas possible d'importer _flup_, installez-le en ligne de commande en utilisant la commande "easy_install flup".

Depuis la revision 145, il est nécessaire de définir une variable  "bin-environment" dans la configuration de fastcgi si votre code utilise des redirections.  Par exemple, si votre code redirige vers  http://domain.com/ et que vous voyez l'URL http://domain.com/code.py/ dans la barre de navigation, vous devrez modifier la configuration de fastcgi.server de la manière suivante:
     
    fastcgi.server = ( "/code.py" =>
    ((
       "socket" => "/tmp/fastcgi.socket",
       "bin-path" => "/path/to/root/code.py",
       "max-procs" => 1,
       "bin-environment" => (
         "REAL_SCRIPT_NAME" => ""
       ),
       "check-local" => "disable"
    ))
    )
    
<a name="apache"></a>
### Apache

<a name="apachecgi"></a>
#### .. avec CGI


Ajoutez les lignes suivante à `httpd.conf` ou `apache2.conf`.

    Alias /foo/static/ /path/to/static
    ScriptAlias /foo/ /path/to/code.py

<a name="apachecgihtaccess"></a>
#### .. avec CGI en utilisant .htaccess

CGI est facile à configurer mais ce n'est pas la meilleure des solutions pour les sites à très fort trafic.

Ajoutez les lignes suivantes à votre fichier `.htaccess`:

    Options +ExecCGI
    AddHandler cgi-script .py

Ouvrez votre navigateur et aller à l'URL `http://example.com/code.py/`. N'oubliez pas le slash final, sinon vous aurez droit à une 'page non trouvée'. Pour que ça fonctionne sans avoir à indiquer `code.py` dans l'URL, il faut activer le 'mod_rewrite' dans votre fichier '.htaccess' (voir en fin de document).

Note: la manière dont `web.py` est implémenté provoque une erreur du module `cgitb` à cause de la capture du `stdout`. Voici une façon de contourner le problème:
    
    import cgitb; cgitb.enable()
    import sys
    
    # ... import web etc here...
    
    def cgidebugerror():
        """                                                                         
        """        _wrappedstdout = sys.stdout
    
        sys.stdout = web._oldstdout
        cgitb.handler()
    
        sys.stdout = _wrappedstdout
    
    web.internalerror = cgidebugerror

<a name="apachefastcgi"></a>
#### .. avec FastCGI

FastCGI est facile à configurer et est aussi performant que 'mod_python'.

Ajoutez les lignes suivantes à votre fichier `.htaccess`:
    
    <Files code.py>      SetHandler fastcgi-script
    </Files>

Malheureusement, et contrairement à lighttpd, Apache ne donne aucune indication demandant à votre script web.py de fonctionner comme un serveur FastCGI, il faut donc l'indiquer à web.py de façon explicite, en ajoutant le code suivant dans votre script `code.py`, juste avant la ligne 
`if __name__ == "__main__":` :
    
    web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    
<a name="apachescgi"></a>
#### .. avec SCGI

Téléchargez et installez le [module mod_scgi](http://www.mems-exchange.org/software/files/mod_scgi/)

modifier le fichier 'httpd.conf':

    LoadModule scgi_module Modules/mod_scgi.so
    SCGIMount / 127.0.0.1:8080

redémarrez le serveur Apache et lancer votre 'code.py' avec la commande suivante:

    python code.py 127.0.0.1:8080 scgi

lancez votre navigateur et visitez l'adresse suivante 127.0.0.1
C'est aussi simple que ça...enfin, si ça marche du premier coup ;-) 

<a name="apachemodpython"></a>
#### .. avec mod_python

mod_python est aussi performant que FastCGI, mais il n'est pas aussi évident à configurer. Suivez le guide:

Pour Python 2.5, procédez comme suit:

    cd /usr/lib/python2.5/wsgiref
    # or in windows: cd /python2.5/lib/wsgiref
    wget -O modpython_gateway.py http://projects.amor.org/misc/browser/modpython_gateway.py?format=raw
    # or fetch the file from that address using your browser

Pour Python <2.5, procéder plutôt ceci:

    cd /usr/lib/python2.4/site-packages
    # or in windows: cd /python2.4/lib/site-packages
    svn co svn://svn.eby-sarna.com/svnroot/wsgiref/wsgiref
    cd wsgiref
    wget -O modpython_gateway.py http://projects.amor.org/misc/browser/modpython_gateway.py?format=raw
    # or fetch the file from that address using your browser  


renommez votre script `code.py` en quelque chose comme `codep.py` et ajoutez le code suivant:
    
    main = web.wsgifunc(web.webpyfunc(urls, globals()))

Dans votre fichier `.htaccess`, ajoutez:
    
    
    AddHandler python-program .py
    PythonHandler wsgiref.modpython_gateway::handler
    PythonOption wsgi.application codep::main
    

Vous aurez surement aussi besoin d'ajouter une `RewriteRule` pour rediriger  `/` vers `/codep.py/`

<a name="apachemodwsgi"></a>
#### .. avec mod_wsgi

mod\_wsgi est un nouveau module Apache  [plus performant que mod_python](http://code.google.com/p/modwsgi/wiki/PerformanceEstimates) pour l'hébergement d'applications WSGI, et très facile à mettre en place.

A la fin de votre script `code.py`, ajoutez la ligne suivante:

    application = web.wsgifunc(web.webpyfunc(urls, globals()))

mod\_wsgi offre [plusieurs façons différentes](http://code.google.com/p/modwsgi/wiki/ConfigurationDirectives) de spécifier l'URL pointant vers une application WSGI, mais une manière simple peut être d'ajouter le code suivant dans votre fichier '.htaccess':

    <Files code.py>
        SetHandler wsgi-script
        Options ExecCGI FollowSymLinks
    </Files>

Si vous recevez un message d'erreur du style "ImportError: No module named web" dans le fichier error.log d'Apache, vous pouvez essayer de spécifier un chemin absolu dans votre script 'code.py' avant l'instruction 'import web':

    import sys, os
    abspath = os.path.dirname(__file__)
    sys.path.append(abspath)
    os.chdir(abspath)
    import web

Plus d'information dans la section "Application Working Directory"  sur [Common problems with WSGI application](http://code.google.com/p/modwsgi/wiki/ApplicationIssues).

Encore une fois, votre application devrait-être accessible à l'URL suivante: `http://example.com/code.py/` (sans oublier le slash final!!!).

<a name="apachemodrewrite"></a>
#### mod_rewrite pour Apache

Si vous voulez que webpy soit accessible par l'URL 'http://example.com' au lieu de  'http://example.com/code.py/' ajoutez les directives suivantes dans votre fichier `.htaccess`:

    <IfModule mod_rewrite.c>      
      RewriteEngine on
      RewriteBase /
      RewriteCond %{REQUEST_URI} !^/icons
      RewriteCond %{REQUEST_URI} !^/favicon.ico$
      RewriteCond %{REQUEST_URI} !^(/.*)+code.py/
      RewriteRule ^(.*)$ code.py/$1 [PT]
    </IfModule>

Si le script `code.py` est situé dans le sous-répertoire `myapp/`, changez la directive  `RewriteBase /` en `RewriteBase /myapp/`. 

Si vous avez d'autres fichiers statiques à exclure de la règle de réécriture  (fichiers CSS ou des images), indiquez-les également ici, en dupliquant et adaptant la ligne `RewriteCond %{REQUEST_URI} !^/icons.` ,par exemple, autant de fois que nécessaire.

Pour plus d'information sur le module mod_rewrite et l'utilisation du fichier `.htaccess`, je vous conseille l'excellent article [URL Rewriting pour les nuls] (http://seo.feuxi.com/URL-Rewriting-pour-les-nuls.html).
