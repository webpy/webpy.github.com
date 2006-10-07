---
layout: default
title: Upgrade to web.py 0.2
---

# Upgrade to web.py 0.2

If you are migrating from the "one big file" version of web.py to the .2 version, you have to make some changes to your code.  


### Downloading web.py 0.2

From the command line, cd to the directory you wish to install web.py and run the following command:

    svn export http://webpy.org/svn/trunk/web/ 

Remove web.py and web.pyc from the loadpath.

### web.run()

Most importantly, upvars() was removed.  We have to change the run line from:

    if __name__ == '__main__': web.run(urls)

to:

    if __name__ == "__main__": web.run(urls, globals())


### web.config

If you use a db, change `web.db_parameters` and `web.db_printing` to `web.config.db_paramters` and `web.config.db_printing` respectively.


### debugging

web.py 0.1:

    web.internalerror = web.debugerror
    if __name__ == '__main__': web.run(urls, web.reloader)

web.py 0.2

    web.webapi.internalerror = web.debugerror
    if __name__ == "__main__": web.run(urls, globals(), web.reloader)

### fastcgi with apache

web.py 0.1:

    web.runwsgi = web.runfcgi

web.py 0.2:

    def runfcgi_apache(func):
      web.wsgi.runfcgi(func, None)

    web.wsgi.runwsgi = runfcgi_apache