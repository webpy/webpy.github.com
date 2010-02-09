---
layout: default
title: Contrôler les évènements sur le serveur intégré par défaut
---

# Contrôler les évènements sur le serveur intégré par défaut

Autre langages: [english](/../logging) | ...

## Problème:

Vous souhaitez contrôler le [logging](http://www.jmdoudoux.fr/java/dej/chap026.htm#logging-1), les évenements,  avec le serveur intégré.

## Solution:

Avec le serveur intégré, vous pouvez contrôler les évènements en utilisant [wsgilog](http://pypi.python.org/pypi/wsgilog/) et en le passant à votre application comme un logiciel médiateur ([middleware](http://fr.wikipedia.org/wiki/Middleware))

Vous devez sous-classer wsgilog.WsgiLog pour passer des arguments mot-clé à la base par [exemple](http://github.com/harryf/urldammit/blob/234bcaae6deb65240e64ee3199213712ed62883a/dammit/log.py)

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

Ensuite, lorsque vous exécutez votre application, vous passez une référence à la classe. Par exemple (si ce qui précède est une partie du module 'mylog')

    from mylog import Log
    application = web.application(urls, globals())
    application.run(Log)