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

**xunil writes:** Yeah, I went w/ this approach in the end since I found that I wanted each action class to inherit some common functionality anyway.  You can [view the source](http://www.theanykey.com/svn/) for [my incomplete site](http://dev.theanykey.com) which uses a metaclass and decorators.

* * *

May be it's better to do it with decorators?

**xunil writes:** I originally tried to use decorators to do this since I was already familiar w/ them, but unless I'm missing something, decorators don't work on classes eg.

    @action("/")
    class Default:
        def GET(self):
            pass

That won't work.  [The PEP for decorators](http://www.python.org/dev/peps/pep-0318/) describes it, but apparently it was never incorporated into the language (perhaps b/c metaclasses are available and do the same thing).

* * *

I couldn't figure out how to get this to work with URL classes in separate files, so I did something a little different, based on [this Python Cookbook recipe](http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/436873):

    import os, web
    
    urls = [ ]
    
    for aaa in os.listdir(os.getcwd()):
        module_name, ext = os.path.splitext(aaa)
        if module_name.startswith('cgi_') and ext == '.py':
            module = __import__(module_name)
            urls.append(module.url[0])
            urls.append(module_name + "." + module.url[1])
    
    if __name__ == "__main__":
        web.run(urls)

And then e.g. cgi_hello.py (in the same directory) would be:

    import web
    url = ('/(.*)', 'hello')
    
    class hello:
        def GET(self, name):
            i = web.input(times=1)
            if not name: name = 'world'            for c in xrange(int(i.times)): print 'Hello,', name+'!'
Is this a terrible way to do it?

* * *

**xunil writes:** This is not altogether a bad idea, but it again decouples the URL information from the class, making it a module-level tuple or list.  You could combine your importing logic w/ my metaclass idea, actually, and achieve the same thing as me eg.

    import os, web
    
    for aaa in os.listdir(os.getcwd()):
        module_name, ext = os.path.splitext(aaa)
        if module_name.startswith('cgi_') and ext == '.py':
            module = __import__(module_name)
    
    if __name__ == "__main__":
        import metaclass
        web.run(metaclass.urls)

metaclass.py:

    urls = [ ]

    class ActionMetaClass(type):
        def __init__(klass, name, bases, attrs):
            urls.append(attrs["url"])
            urls.append("%s.%s" % (klass.__module__, name))

cgi_hello.py:

    import web
    from metaclass import ActionMetaClass
    
    class hello:
        __metaclass__ = ActionMetaClass
        url = '/(.*)'
        def GET(self, name):
            i = web.input(times=1)
            if not name: name = 'world'            for c in xrange(int(i.times)): print 'Hello,', name+'!'
* * *