---
layout: default
title: Very simple session example
---

# Very simple session example

This example is a simple counter using [DBHandler](/sessions/DBHandler); put this in code.py and run _python code.py_

    import time
    
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

                try:
                        s.click += 1
                except AttributeError:
                        s.click = 1
    
                print 'click: ', s.click


    if __name__ == '__main__':
        web.run(urls, globals(), web.reloader)