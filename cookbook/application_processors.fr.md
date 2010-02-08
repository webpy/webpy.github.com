---
layout: default
title: Application processors, hooks
---

# Application processors, hooks

Autre langages [english](/../application_processors) | ...

##  Probleme

Comment utiliser les application processors, charger les hooks et les décharger ? [Note traducteur: est-il possible de traduire "hook" par personnalisation du fonctionnement?]

## Solution

L'application web.py permet d'ajouter des processors qui peuvent effectuer quelques traitements avant et après l'execution des requêtes.

    def my_processor(handler): 
        print 'avant le traitement de la requête'
        result = handler() 
        print 'après le traitement de la requête'
        return result

    app.add_processor(my_processor)

Le chargement et déchargement des hooks peuvent être utilisés pour faire des actions au début et à la fin des requêtes.

    def my_loadhook():
        print "mon chargement de hook"

    def my_unloadhook():
        print "mon déchargement de hook"

    app.add_processor(web.loadhook(my_loadhook))
    app.add_processor(web.unloadhook(my_unloadhook))

Vous pouvez écrire ou utiliser les variables globales dans les fonctions hook, par exemple : web.header()

    def my_loadhook():
        web.header('Content-type', "text/html; charset=utf-8")

    app.add_processor(web.loadhook(my_loadhook))


###Tip: et vous pouvez également utiliser web.ctx ou web.input() dans un hook.

    def my_loadhook():
        input = web.input()
        print input