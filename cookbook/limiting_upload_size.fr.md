---
layout: default
title: Comment limiter la taille des fichiers uploadés
---

# Comment limiter la taille des fichiers uploadés

Autre langages: [english](/../limiting_upload_size) | ...

## Problème:

Comment limiter la taille des fichiers uploadés ?

## Solution:

web.py utilise le module `cgi` pour parser les entrées de l'utilisateur et le module `cgi` a une disposition visant à limiter la taille maximale des entrées.

Le code suivant limite la taille des données entrantes à 10 Mo.

    import cgi

    # Données entrantes maximum que nous acceptons lorsque REQUEST_METHOD est POST
    # 0 ==> Données entrantes illimitées
    cgi.maxlen = 10 * 1024 * 1024 # 10Mo


Noter que cela limite la taille des données POST, pas des fichiers uploadés. Cependant, ce sera presque pareil s'il n'y a pas d'autre entrée.

Le module `cgi` lève l'exception `ValueError` quand la taille des données entrées est supérieure à `cgi.maxlen`. Elle peut être interceptée pour afficher le message d'erreur requis.

    class upload:
        def POST(self):
            try:
                i = web.input(file={})
            except ValueError:
                return "File too large"