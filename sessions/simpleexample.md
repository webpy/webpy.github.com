---
layout: default
title: Very simple session example
---

# Very simple session example

put this in code.py and run python code.py
Note : Tested with python2.7.  You should install virtualenv with wirtualenvwrapper to avoid interference with your own Python configuration.

import web
import shelve


urls = (
        '/add', 'counter',
        '/reset', 'reset'
       )

    shelf = shelve.open('session')
    shelfStore = web.session.ShelfStore(shelf)
app = web.application(urls, globals())

    class counter:        

        def GET(self):
            s = web.session.Session(app, shelfStore)
            try:
                s.store.shelf["count"] += 1
                except Exception:
                s.store.shelf["count"] = 1
                return s.store.shelf.get("count")


                class reset:
                    def GET(self): 
    s = web.session.Session(app, shelfStore)
    s.store.shelf.clear()

    if __name__ == "__main__":
app.run()


