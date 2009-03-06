---
layout: default
title: How to use web.background
---

# How to use web.background

*WARNING* web.backgrounder was moved to experimental with web.py 3.x and it no longer part of the default distribution. You can get it from [here](http://github.com/webpy/webpy/blob/686aafab4c1c5d0e438b4b36fab3d14d121ef99f/experimental/background.py) and put it in the same directory as application.py i.e. the web directory for this to work.

Intro
-----

web.background (and web.backgrounder) are python function decorators which allow you to execute a function in a separate background thread to that thread which served the current HTTP request and later report back on the status of the background thread (the stdout of the background function is in effect returned to the "backgrounder" that initiated the thread.

This allows you to respond quickly to the client and move to to serving other http requests, while the background thread performs some long running function.

Example
-------

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    from web import run, background, backgrounder
    from datetime import datetime; now = datetime.now
    from time import sleep

    urls = (
        '/', 'index',
        )

    class index:
        @backgrounder
        def GET(self):
            print "Started at %s" % now()
            print "hit f5 to refresh!"
            longrunning()
            

    @background
    def longrunning():
        for i in range(10):
            sleep(1)
            print "%s: %s" % (i, now())

    if __name__ == '__main__':
        run(urls, globals())

On requesting http://localhost:8080/ you will be redirected automatically to a URL like http://localhost:8080/?_t=3080772748 ( depending on the background thread id) and (after you hit refresh a few times) you'll see something like;

    Started at 2008-06-14 15:50:26.764474
    hit f5 to refresh!
    0: 2008-06-14 15:50:27.763813
    1: 2008-06-14 15:50:28.763861
    2: 2008-06-14 15:50:29.763844
    3: 2008-06-14 15:50:30.763853
    4: 2008-06-14 15:50:31.764778
    5: 2008-06-14 15:50:32.763852
    6: 2008-06-14 15:50:33.764338
    7: 2008-06-14 15:50:34.763925
    8: 2008-06-14 15:50:35.763854
    9: 2008-06-14 15:50:36.763789

Notes
------------

web.py keeps track of threads in the background.threaddb dictionary. It's easy to examine the state of it like;

    class threaddbviewer:
        def GET(self):
            for k, v in background.threaddb.items():
                print "%s - %s" % ( k, v )

web.py doesn't attempt to clean up threaddb dictionary, which allows the output (like http://localhost:8080/?_t=3080772748 ) to continue to be served but is going to fill up memory over time.

Probably the backgrounder needs to clean up, as it's able to determine the thread id (from web.input() - '_t') although it's actually the background function which knows when it's finished, but doesn't know it's thread ID.

Note also [How not to do thread local storage with Python](http://blogs.gnome.org/jamesh/2008/06/11/tls-python/) - thread id's are going to get re-used at some point (there's probably bugs to report here).

In other words, _handle with care_.