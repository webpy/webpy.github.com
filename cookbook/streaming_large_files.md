---
layout: default
title: How to Stream Large Files
---

# How to Stream Large Files

This is an example of how you can use web.py to stream large files.  You'll find it DOES work as advertised, but there are some protocol changes you may have to make to stream files of certain types to certain clients.  

You need the content type and chunked header to make things show up correctly on a typical web browser.  

Simple Example

    # Simple streaming server demonstration
    import web
    import time
     
    urls = (
        "/",    "count_holder",
        "/(.*)",  "count_down",
        )
    app = web.application(urls, globals())
     

    class count_down:
        def GET(self,count):
            web.header('Content-type','text/html')
            web.header('Transfer-Encoding','chunked')        
            yield '<h2>Prepare for Launch!</h2>'
            j = '<li>Liftoff in %s...</li>'
            yield '<ul>'
            count = int(count)
            for i in range(count,0,-1):
                out = j % i
                time.sleep(1)
                yield out
            yield '</ul>'
            time.sleep(1)
            yield '<h1>Lift off</h1>'
            
    class count_holder:
        def GET(self):
            web.header('Content-type','text/html')
            web.header('Transfer-Encoding','chunked')        
            boxes = 4
            delay = 3
            countdown = 10
            for i in range(boxes):
                output = '<iframe src="/%d" width="200" height="500"></iframe>' % (countdown - i)
                yield output
                time.sleep(delay)
            
    if __name__ == "__main__":
        app.run()