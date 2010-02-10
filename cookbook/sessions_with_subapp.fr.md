---
layout: default
title: Utiliser les sessions avec les sous-applications
---

# Utiliser les sessions avec les sous-applications

Autre langages: [english](/../sessions_with_subapp) | ...

###Note

*Cette solution est issue de ce [post](http://www.mail-archive.com/webpy@googlegroups.com/msg02557.html) de la mailing liste de web.py.*

##Problème:

Dans le comportement par défaut, les informations de session ne peuvent être partagées qu'au sein de l'application principale, même si vous «importez» la session depuis d'autres modules. Vous devez être en mesure d'accéder aux informations de session depuis une sous-application, mais comment?

##Solution:

Dans votre application principale (code.py par defaut), initialisez votre session de cette façon:

    session = web.session.Session(app, web.session.DiskStore('sessions'),
    initializer = {'test': 'woot', 'foo':''})

.. puis créez un processor via web.loadhook

    def session_hook():
        web.ctx.session = session

    app.add_processor(web.loadhook(session_hook))

.. et maintenant dans votre sous-application (par exemple sub-app.py) vous pouvez accèder aux informations de session de cette manière:

    print web.ctx.session.test
    web.ctx.session.foo = 'bar'