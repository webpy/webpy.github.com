---
layout: default
title: Logging
---

# Logging

Other languages: [français](/../cookbook/logging/fr) | ...

## Problem:

You want to control logging for default HTTPServer.

## Solution:

With the built-in webserver you can control http logging by passing a logging class to your app as [middleware](http://en.wikipedia.org/wiki/Middleware).

This code works for web.py version 0.37:

	import web.httpserver
	import logging, logging.handlers
	import config

	class syslogger(web.httpserver.LogMiddleware):
		def __init__(self, app):
			web.httpserver.LogMiddleware.__init__(self, app)
			self.format = 'webpy: %s - - [%s] "%s %s %s" - %s'

			self.logger = logging.getLogger('webpy')
			self.logger.addHandler(logging.handlers.SysLogHandler((config.log_server, 514)))
			self.logger.setLevel(logging.DEBUG)

		def log(self, status, environ):
			req = environ.get('PATH_INFO', '_')
			protocol = environ.get('ACTUAL_SERVER_PROTOCOL', '-')
			method = environ.get('REQUEST_METHOD', '-')
			host = "%s:%s" % (environ.get('REMOTE_ADDR','-'),
							  environ.get('REMOTE_PORT','-'))

			time = self.log_date_time_string()

			msg = self.format % (host, time, protocol, method, req, status)

			self.logger.debug(msg)			


  
Then when you run your app, you pass a reference to to the class e.g. (if the above was part of the module 'mylog')

    from mylog import syslogger
    application = web.application(urls, globals())
    application.run(syslogger)