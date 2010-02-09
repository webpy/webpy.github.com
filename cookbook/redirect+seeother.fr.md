---
layout: default
title: web.redirect et web.seeother
---

# web.redirect et web.seeother

Autres langages [english](/../redirect+seeother/) | ...


### Probleme

Après le traitement des entrées utilisateurs (depuis un formulaire, par exemple), vous souhaitez les rediriger vers une autre page.

### Solution

    class SomePage:
        def POST(self):
            # Executez une application logique ici, puis:
            raise web.seeother('/someotherpage')


Quand un post est envoyé à cette fonction, à la fin il enverra au navigateur un code HTTP 303, et le nouvel emplacement. Le navigateur va alors effectuer un GET sur l'emplacement défini dans l'argument seeother.

Note: web.seeother et web.redirect génèrent des exceptions dans la version 0.3.

### A savoir

Il est peu probable que vous utilisiez la fonction web.redirect très souvent -- elle semble faire la même chose, mais elle envoie le code HTTP 301, qui est une redirection permanente. La plupart des navigateurs mettront en cache la nouvelle redirection, et vous enverront automatiquement à cet emplacement lorsque vous essaierez d'exécuter l'action à nouveau. Un bon cas d'utilisation des redirections est lorsque vous modifiez la structure d'URL de votre site, mais que vous désirez conserver les anciens liens à cause des marques-pages, signets, ou favoris.