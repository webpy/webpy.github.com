---
layout: default
title: Upgrade to web.py 0.2
---

# Upgrade to web.py 0.2

If you are migrating form the "one big file" version of web.py to the .2 version, you have to make some changed to your code.  

### web.run()

Most importantly,upvars() was removed.  We have to change the run line from:

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
