---
layout: default
title: Sessions with Sub-apps
---

# Sessions with Sub-apps

Other languages: [français](/../cookbook/sessions_with_subapp/fr) | ...

###Note
*This solutions is taken from [this](http://www.mail-archive.com/webpy@googlegroups.com/msg02557.html) post on the web.py mailing list.*

##Problem
In its default behavior, session information can only be shared from within the main application, even if you 'import' the session from other modules. You need to be able to access session information from 'sub applications' but how?

##Solution

In your app.py (or main.py) initialize your session like this:

    session = web.session.Session(app, web.session.DiskStore('sessions'),
    initializer = {'test': 'woot', 'foo':''})

.. and create a processor via web.loadhook

    def session_hook():
        web.ctx.session = session

    app.add_processor(web.loadhook(session_hook))

.. and now in your 'sub-apps' (like sub-app.py) you can access the the session information like this:

    print web.ctx.session.test
    web.ctx.session.foo = 'bar'