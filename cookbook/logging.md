---
layout: default
title: Logging
---

# Logging

Other languages: [français](/../cookbook/logging/fr) | ...

## Problem:

You want to control logging for default HTTPServer.

## Solution:

With the built-in webserver you can control logging by using [wsgilog](http://pypi.python.org/pypi/wsgilog/) and passing it to your app as [middleware](http://en.wikipedia.org/wiki/Middleware).

This code works for wsgilog version 0.2

    import sys, logging
    from wsgilog import WsgiLog
    import config

    class Log(WsgiLog):
        def __init__(self, application):
            WsgiLog.__init__(
                self,
                application,
                logformat = '%(message)s',
                tofile = True,
                toprint = True,
                file = config.log_file,
                interval = config.log_interval,
                backups = config.log_backups
                )


Then when you run your app, you pass a reference to to the class e.g. (if the above was part of the module 'mylog')

    from mylog import Log
    application = web.application(urls, globals())
    application.run(Log)