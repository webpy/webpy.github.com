---
layout: default
title: Webpy + LightTTPD avec FastCGi
---

# Webpy + LightTTPD avec FastCGi

Autre langages: [English](/../fastcgi-lighttpd) | ...

## Problème:

Comment configurer [lighttpd](http://www.lighttpd.net/) sous Debian GNU/Linux ?

## Solution:

*Si vous avez des problèmes avec cette astuce, veuillez lire ce [fil](http://www.mail-archive.com/webpy@googlegroups.com/msg02800.html).
Ce qui suit s'applique à la version 1.4.18 de lighttpd.*

### Note:

* Vous devez remplacer `code.py` par le nom de votre propre fichier.
* `/path-to/webpy-app` que vous trouverez ci-dessous, concerne le chemin vers le répertoire contenant votre `code.py`
* `/path-to/webpy-app/code.py` est le chemin complet de votre **fichier python**

Si vous n'êtes pas certain de savoir quelle version de [lighttpd](http://www.lighttpd.net/) s'execute, tapez : `lighttpd -v` dans la console.

*Note: La version précédente de lighttpd organise les fichiers .conf différemment. Cependant, les mêmes principes s'appliquent aussi bien sur eux.*

## Configuration de lighttpd sous Debian GNU/Linux

```
Fichiers er répertoires de /etc/lighttpd:
---------------------------------------

lighttpd.conf:
         fichier de configuration principal

conf-available/

	Ce répertoire contient une série de fichiers .conf. Ces fichiers contiennent
	les directives de configuration nécesssaire pour charger et executer les modules
	du serveur web. Si vous voulez créer vos propres fichiers, leurs noms doivent être
	construits ainsi : nn-name.conf. "nn" est un nombre à deux chiffres (ce nombre est
	utilisé pour déterminer l'ordre de chargement des fichiers)	

conf-enabled/

	Afin d'activer effectivement un module pour lighttpd, il est nécessaire
	de créer dans ce répertoire un lien symbolique vers le fichier .conf concerné
	du répertoire conf-available/.

l'Activation et désactivation des modules peut se faire en lançant:
	/usr/sbin/lighty-enable-mod
 	/usr/sbin/lighty-disable-mod scripts.
```

**Pour web.py vous devrez activer mod_fastcgi et mod_rewrite en executant: `/usr/sbin/lighty-enable-mod` et en fournissant `fastcgi` (mod_rewrite sera activé dans le fichier `10-fastcgi.conf`, comme vous pourrez le voir dans un instant.)**

## Voici les instructions pour les fichiers suivants:

* `/etc/lighttpd/lighttpd.conf`
* `/etc/lighttpd/conf-available/10-fastcgi.conf`
* `code.py`

### `/etc/lighttpd/lighttpd.conf`

```
server.modules              = (
            "mod_access",
            "mod_alias",
            "mod_accesslog",
            "mod_compress",
)
server.document-root       = "/path-to/webpy-app"
```

*Dans mon cas, j'ai utilisé [postgreSQL](http://doc.ubuntu-fr.org/postgresql). Pour executer lighttpd avec postgres et afin d'accorder des autorisations à la base de donnée, j'ai ajouté la ligne:*

```
server.username = "postgres"
```

### `/etc/lighttpd/conf-available/10-fastcgi.conf`

```
server.modules   += ( "mod_fastcgi" )
server.modules   += ( "mod_rewrite" )

 fastcgi.server = ( "/code.py" =>
 (( "socket" => "/tmp/fastcgi.socket",
    "bin-path" => "/path-to/webpy-app/code.py",
    "max-procs" => 1,
   "bin-environment" => (
     "REAL_SCRIPT_NAME" => ""
   ),
   "check-local" => "disable"
 ))
 )

 url.rewrite-once = (
   "^/favicon.ico$" => "/static/favicon.ico",
   "^/static/(.*)$" => "/static/$1",
   "^/(.*)$" => "/code.py/$1",
 )
```

### `code.py`

En haut du fichier, ajoutez:

```
#!/usr/bin/env python
```

...et n'oubliez pas de le rendre executable (Autrement, vous aurez une erreur "permission denied"):

```
$ chmod 755 /path-to/webpy-app/code.py
```
