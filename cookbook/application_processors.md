---
layout: default
title: Application processors, hooks
---

# Application processors, hooks

Other languages : [français](/../cookbook/application_processors/fr) | ...

##  Problem

How to use application processors, loadhooks and unload hooks?

## Solution

web.py application allows adding processors which can do some processing before and after executing the requests

    def my_processor(handler): 
        print 'before handling'
        result = handler() 
        print 'after handling'
        return result

    app.add_processor(my_processor)

Load hooks and unload hooks can be used to do actions at begining and end of requests.

    def my_loadhook():
        print "my load hook"

    def my_unloadhook():
        print "my unload hook"

    app.add_processor(web.loadhook(my_loadhook))
    app.add_processor(web.unloadhook(my_unloadhook))

you can write or use global variables in hook function, for example: web.header()

    def my_loadhook():
        web.header('Content-type', "text/html; charset=utf-8")

    app.add_processor(web.loadhook(my_loadhook))

###Tip: and also can use web.ctx or web.input() in hook.

    def my_loadhook():
        input = web.input()
        print input