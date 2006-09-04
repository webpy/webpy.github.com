---
layout: default
title: Upgrade to web.py 0.2
---

# Upgrade to web.py 0.2

If you are migrating form the "one big file" version of web.py to the .2 version, you have to make some changed to your code.  

### web.run()

Most importantly, thanks to Guido, change the run line from:

    if __name__ == '__main__': web.run(urls, web.reloader)

to:

    if __name__ == "__main__": web.run(urls, globals())


### web.config

If you use a db, change `web.db_parameters` and `web.db_printing` to `web.config.db_paramters` and `web.config.db_printing` respectively.
