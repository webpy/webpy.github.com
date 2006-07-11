---
layout: default
title: MetaClassAutoURLS
---

# MetaClassAutoURLS

web.py maps URLs regexes to classes via a list like so:

    class Default(object):
        ''' Action for / '''        def GET(self):
            pass

    class Login(object):
        ''' Action for /login '''        def GET(self):
            pass

        def POST(self):
            pass

    urls = ["/", "Default", "/login", "Login"]

One of the disadvantages of this approach is that for large applications, the urls list can get very long and tedious to maintain.  Things get worse during long refactorings/reorgnanizations because it's easy to typo a class or module name or just forget to update the urls list.  After spending a couple hours debugging just this problem and then smacking myself on the forehead for missing such a simple mistake, I thought to myself, _There's got to be a way to automate this!_  After some research, I found that metaclasses can do exactly what I want:

    urls = [ ]

    class ActionMetaClass(type):
        def __init__(klass, name, bases, attrs):
            urls.append(attrs["url"])
            urls.append("%s.%s" % (klass.__module__, name))

    class Default(object):
        __metaclass__ = ActionMetaClass
        url = "/"
        def GET(self):
            pass

    class Login(object):
        __metaclass__ = ActionMetaClass
        url = "/login"
        def GET(self):
            pass

        def POST(self):
            pass

Of course, this is a simple example that leaves a lot to be desired (handling attrs lacking a url key, for instance), but it should get you on your way.

* * *

**AaronSw writes:** That's a clever idea. One improvement might be to have the classes inherit from a class with the metaclass set, so you don't have that unsightly `__metaclass__` every time.