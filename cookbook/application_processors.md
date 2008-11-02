---
layout: default
title: Application processors
---

# Application processors

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

    app.add_procerssor(web.loadhook(my_loadhook))
    app.add_procerssor(web.unloadhook(my_unloadhook))



