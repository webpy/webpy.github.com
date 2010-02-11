---
layout: default
title: Accéder aux entrées utilisateurs par le biais de web.input
---

# Accéder aux entrées utilisateurs par le biais de web.input

Autre langages: [english](/../input) | ...


### Problème:

Comment obtenir les données utilisateur depuis un  formulaire, ou un paramètre encodé dans l'URL.

### Solution:

La méthode web.input() renvoi un objet web.storage (de type dictionnaire) qui contient les variables de l'url (dans GET) ou de l'en-tête HTTP (dans POST).
Par exemple, si vous allez sur la page http://example.com/test?id=10, vous voudrez extraire le id=10 en arrière plan. En utilisant web.input(), cela devient facile:

    class SomePage:
        def GET(self):
            user_data = web.input()
            return "<h1>" + user_data.id + "</h1>"

Parfois, vous aurez besoin de spécifier une variable par défaut, dans le cas ou aucune n'est donnée. Voici le même code avec une valeur par defaut:

    class SomePage:
        def GET(self):
            user_data = web.input(id="no data")
            return "<h1>" + user_data.id + "</h1>"


*Notez que les valeurs de web.input() sont des chaînes, même si ce sont des numéros qui lui sont passées*

Que faire si vous passez plusieurs noms de variable équivalents, comme ceci:

<select multiple size="3"><option>foo</option><option>bar</option><option>baz</option></select>


Vous aurez besoin de faire savoir à web.input qu'il doit s'attendre à des entrées multiples, sinon il les référencera tous, sauf un. Passez la valeur par défaut d'une liste à web.input et il fonctionnera correctement. Par exemple,  http://example.com?id=10&id=20:

    class SomePage:
        def GET(self):
            user_data = web.input(id=[])
            return "<h1>" + ",".join(user_data.id) + "</h1>"