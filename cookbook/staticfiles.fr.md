---
layout: default
title: Servir des fichiers statiques (tels que .js, .css et des images)
---

# Servir des fichiers statiques (tels que .js, .css et des images)

Autre langages : [english](/../staticfiles) | ...

Probleme
-------
Comment servir des fichiers statiques ?

Solution
--------

### Serveur web.py

Créez un répertoire (ou dossier) que vous nommerez <code>static</code> au même endroit ou se situe le script qui fait tourner web.py (par defaut code.py). Puis plaçez les fichiers statiques que vous servirez dans le repertoire "static".

Par exemple, l'url <code>http://localhost/static/logo.png</code> enverra l'image <code>./static/logo.png</code> au client.

### Apache

Pour servir des fichiers statiques une directive [Alias](http://httpd.apache.org/docs/2.2/mod/mod_alias.html#alias) peut être utilisée pour mapper la requête d'url vers un répertoire choisi, avant qu'il soit traité par web.py.

Voici un exemple d'Hôte Virtuel configuré sur un système de type Unix avec une Directive Alias en vigueur:

    <VirtualHost *:80>
        ServerName example.com:80
        DocumentRoot /doc/root/
        # Monte votre application si mod_wsgi est utilisé
        WSGIScriptAlias / /script/root/code.py
        # La Directive Alias
        Alias /static /doc/root/static
        
        <Directory />
            Order Allow,Deny
            Allow From All
            Options -Indexes
        </Directory>
        
	# Parce que l'Alias peut être utilisé pour référencer les ressources en dehors de docroot,
	# vous devez référencer le repertoire avec un chemin absolu.
        <Directory /doc/root/static>
            # les directives ont pour effet le répertoire statique
            Options +Indexes
        </Directory>
    </VirtualHost>