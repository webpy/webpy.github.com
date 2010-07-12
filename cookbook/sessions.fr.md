---
layout: default
title: Travailler avec les sessions
---

# Travailler avec les sessions

Autre langages: [english](/../sessions) | ...

### Problème

Comment utiliser les sessions dans web.py.

### Solution

*Les sessions ne fonctionnent pas en mode [debug](/tutorial3.fr#debug) parce qu'elles interfèrent avec reloading. Veuillez lire [session_with_reloader](/session_with_reloader) pour plus de détail.*

Le module `web.session` fournit un support session. Voici une application simple de compteur utilisant les sessions.

    import web
    web.config.debug = False
    urls = (
        "/count", "count",
        "/reset", "reset"
    )
    app = web.application(urls, locals())
    session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'count': 0})

    class count:
        def GET(self):
            session.count += 1
            return str(session.count)
            
    class reset:
        def GET(self):
            session.kill()
            return ""

    if __name__ == "__main__":
        app.run()

L'objet session est chargé avec des données session avant le traitement de la requête et sauve des données session après avoir traité la requête, si il est modifié. Notez que dans la version du 22-11-2008 de web.py, il faut désactiver le [débogage](/tutorial3.fr#debug) pour utiliser le serveur de développement avec les sessions.

L'argument optionnel `initializer` de Session spécifie la session initiale.


Vous pouvez utiliser `DBStore` à la place de `DiskStore` si vous préférez stocker les sessions dans une base de donnée au lieu du disque. Pour utiliser DBStore, vous avez besoin d'une table avec la structure suivante:

     create table sessions (
        session_id char(128) UNIQUE NOT NULL,
        atime timestamp NOT NULL default current_timestamp,
        data text
    );

Puis vous devez passer l'objet `db` et le nom de la table de session au constucteur de `DBStore`.

    db = web.database(dbn='postgres', db='mydatabase', user='myname', pw='')
    store = web.session.DBStore(db, 'sessions')
    session = web.session.Session(app, store, initializer={'count': 0})


Des options relatives aux sessions peuvent être modifiées en utilisant le dictionnaire `sessions_parameters` dans `web.config`. Les valeurs par défaut sont montrées ci-dessous:

    web.config.session_parameters['cookie_name'] = 'webpy_session_id'
    web.config.session_parameters['cookie_domain'] = None
    web.config.session_parameters['timeout'] = 86400, #24 * 60 * 60, # 24 heures en secondes
    web.config.session_parameters['ignore_expiry'] = True
    web.config.session_parameters['ignore_change_ip'] = True
    web.config.session_parameters['secret_key'] = 'fLjUfxqXtfNoIldA0A0J'
    web.config.session_parameters['expired_message'] = 'La session expire.'

 * `cookie_name` - nom du cookie utilisé pour stocker la session id
 * `cookie_domain` - domaine du cookie utilisé pour stocker l'ID de session
 * `timeout` - nombre de secondes d'inactivité autorisées avant que la session expire
 * `ignore_expiry` - si `True`, l'expiration de la session est ignoré
 * `ignore_change_ip` - si `False`, la session est valide uniquement quand elle est accessible à partir de la même adresse IP qui l'a créé
 * `secret_key`       - clef utilisée dans la génération du hachage session id (demande d'explications plus détaillées))
 * `expired_message`  - message affiché lorsque la session a expiré