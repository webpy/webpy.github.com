---
layout: default
title: Very simple session example
---

# Very simple session example

put this in code.py and run python code.py

    import web

    web.config.db_parameters = {
                                'dbn' : 'postgres',
                                'host' : 'localhost',
                                'user' : 'web',
                                'pw' : 'web',
                                'db' : 'web'
                        }

    urls = (
        '/', 'index'
    )

    class index:
        def GET(self):
            s = web.ctx.session
            s.start()

            try:
                s.click += 1
            except AttributeError:
                s.click = 1

            print 'click: ', s.click
            s.save()

    if __name__ == '__main__':
        web.run(urls, globals(), web.reloader)
