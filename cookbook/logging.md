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

You need to subclass wsgilog.WsgiLog to pass keyword arguments to the base e.g. [this example](http://github.com/harryf/urldammit/blob/234bcaae6deb65240e64ee3199213712ed62883a/dammit/log.py)

    import sys, logging
    from wsgilog import WsgiLog, LogIO
    import config

    class Log(WsgiLog):
        def __init__(self, application):
            WsgiLog.__init__(
                self,
                application,
                logformat = '%(message)s',
                tofile = True,
                file = config.log_file,
                interval = config.log_interval,
                backups = config.log_backups
                )
            sys.stdout = LogIO(self.logger, logging.INFO)
            sys.stderr = LogIO(self.logger, logging.ERROR)

Then when you run your app, you pass a reference to to the class e.g. (if the above was part of the module 'mylog')

    from mylog import Log
    application = web.application(urls, globals())
    application.run(Log)