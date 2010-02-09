---
layout: default
title: How to Stream Large Files
---

# How to Stream Large Files

Other languages: [français](/../cookbook/streaming_large_files/fr) | ...

## Problem:

You want to use web.py to stream large files.

##Solution:

This is an example of how you can use web.py to stream large files.  You'll find it DOES work as advertised, but you need to make sure you add the Transfer-Encoding chunked header for it to display properly.  Otherwise the browser will buffer all data before displaying it to you.

You can't mix basic string and Yield returns in the same method.  If you use Yield, you'll have to use yield for everything because your function becomes a generator.


##Simple Example:

    # Simple streaming server demonstration
    # Uses time.sleep to emulate a large file read
    import web
    import time
     
    urls = (
        "/",    "count_holder",
        "/(.*)",  "count_down",
        )
    app = web.application(urls, globals())
     

    class count_down:
        def GET(self,count):
            # These headers make it work in browsers
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