---
layout: default
title: Roadmap
---

# Roadmap

[[discussion](http://groups.google.com/group/webpy/browse_thread/thread/b8505370cef1c37c/9e65f5d621c47913)]

Next release of web.py will be version 0.3. As the number suggests it   
will be major release. There will be some changes to API, which   
breaks the backward compatability. But I promise, it is not going to   
change very much. 

Major changes will be 

     * return instead of print 
     * moving away from globals 
     * better db api 

Apart from these, the existing subversion repository is be migrated   
to bazaar. 
 From now on, the official repository will be 

     http://webpy.org/bzr/webpy.dev 

Please let me know if you have any suggestions, objections or feature   
requests. 
Some of these changes(application stuff and return instead of print)   
are already checked in, I request you to play with it and let me know   
if there are any bugs. 

Here is how the new API is going to look like. 

## Hello world 

`print` will be replaced with `return`. 

     import web 

     urls = ( 
         '/(.*)', 'hello' 
     ) 

     # more about this later 
     app = web.application(urls, globals()) 

     class hello: 
         def GET(self, name): 
             if not name: name = 'world' 
             return 'Hello,' + name + '!' 

     if __name__ == "__main__": 
         app.run() 

## database 

db configuration will not be global any more. Multiple databases can   
be used at the same time and no `web.load()` magic required to make   
database work. 

     import web 

     db = web.database(dbn='postgres', db='todo', user='you', pw='') 

     db.select('todo') 
     db.select('todo', where='id=$id', vars={'id': 2}) 
     db.query('SELECT * FROM todo') 

## application 
Application is a new way of mapping urls to classes, coming in 0.3. 
There will be many different kinds of supported applications. 

### web.application 
Application to delegate requests based on path. 

     urls = ( 
         "/hello", "hello", 
         "/magic/.*", "magic") 

     app = web.application(urls, globals()) 

### web.auto_application 
Application similar to web.application but urls are constructed   
automatiacally using metaclasses. 

     app = web.auto_application() 

     class hello(app.page): 
         def GET(self): 
             return "hello, world!" 

### web.subdir_application 
Application to delegate requests based on subdir. 
This allows reuse of code easily by taking some existing app and   
mounting it at a directory. 

     import wiki 
     import blog 
     import auth 

     mapping = ( 
         "/wiki", wiki.app, 
         "/blog", blog.app, 
         "/auth", auth.app) 

     app = web.subdir_application(mapping) 

### web.subdomain_application 
Application to delegate requests based on host. 
This makes virtual hosting very easy. 

     import mainsite 
     import usersite 

     mapping = ( 
         "(www\.)?example.com", mainsite.app, 
         ".*\.example.com", usersite.app 
     ) 

     app = web.subdomain_application(mapping) 

## testing 

Testing becomes very easy with applications. Both doctest and   
unittest can be used to test web applications. 

doctest: 

     urls = ("/hello", "hello") 
     app = web.application(urls, globals()) 

     class hello: 
         """Hello world example. 

             >>> response = app.request("/hello") 
             >>> response.data 
             'hello, world!' 
             >>> response.status 
             '200 OK' 
             >>> response.headers['Content-Type'] 
             'text/plain' 
         """ 
         def GET(self): 
             web.header('Content-Type', 'text/plain') 
             return "hello, world!" 

unittest: 

     import unittest 
     from helloworld import app 

     class HelloWorldTest(unittest.TestCase): 
         def testHelloWorld(self): 
             response = app.request('GET', '/')
             self.assertEquals(response.data, 'hello, world!')
             self.assertEquals(response.headers['Content-Type'], 'text/plain')
             self.assertEquals(response.status, '200 OK')

     if __name__ == "__main__": 
         unittest.main() 

## templates 

* no whitespace magic 
* better error reporting 
* should allow template reuse 
* Probably use Adam Atlas's implementation 

## Contrib 

* New module, `web.contrib` with contributed utilities, which are not   
part of the web.py core. For example, good auth module (port from   
django?) and OpenID support.