---
layout: default
title: Utiliser les sessions avec reloader
---

# Utiliser les sessions avec reloader

Autre langages: [english](/../session_with_reloader) | ...

# Probleme

Il ya quelques problèmes en utilisant les sessions lors de l'exécution de l'application en mode [débogage](/tutorial3.fr#debug). Existe-t-il une  méthode permettant de les contourner?

# Solution

web.py fait tourner le programme en mode débogage lorsqu'il fonctionne en utilisant le serveur intégré.

Un simple correctif pour ceci, est de désactiver le mode debug, ce qui peut être réalisé en déterminant `web.config.debug = False`.

    import web
    web.config.debug = False

    # Le reste de votre code


Si vous voulez utiliser les sessions en mode debug, voici une solution de fortune.

Depuis que le mode de débogage permet le module reloading, le reloader charge le module principal à deux reprises (une fois comme __main__ et une fois avec son nom), deux objets session sont créés. Cela peut être évité en stockant la session dans un emplacement global afin d'éviter la création de la seconde.

Voici un exemple de code qui sauve la session dans «web.config».

    import web
    urls = ("/", "hello")

    app = web.application(urls, globals())

    if web.config.get('_session') is None:
        session = web.session.Session(app, web.session.DiskStore('sessions'), {'count': 0})
        web.config._session = session
    else:
        session = web.config._session

    class hello:
       def GET(self):
           print 'session', session
           session.count += 1
           return 'Hello, %s!' % session.count

    if __name__ == "__main__":
       app.run()