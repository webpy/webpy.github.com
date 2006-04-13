---
layout: default
title: quick vhosting hack
---

# quick vhosting hack

Here is a 10 minute hack with lots of room for improvement but I think its
pretty useful. I made this to allow serving of multiple
sites from a single webpy app.

I created this because I would like to run a few small sites but my cheep
account at my hosting provider:

 * only allows 40MB to be used by persistant processes. 
 * I need a special apache's mod_proxy setup by the admin for each webpy
   instance I run.


So, I just made a quick decorator for `web.handler`. Note that this
expects to be working behind a proxy but that can easily be corrected.


     
     #
     ## URL MAPPING
     #
     urls_1 = (
         '/','index_1',
     )
     
     urls_2 =(
         '/','index_2',
     )
     
     urls_3=(
         '/','index_3',
     )



     vhosts={'test.org':urls_1,
             'www.test.org':urls_2,
             'another-url.org':urls_3
             }
     
     def vhostrr(vhosts=vhosts):
         def decorator(func): 
             def proxyfunc(*args, **kw):
                 if 'HTTP_X_FORWARDED_HOST' in web.ctx.environ:
                     rd=web.ctx.environ['HTTP_X_FORWARDED_HOST']
                     mapping=None
                     for d in vhosts.keys():
                         if d==rd:
                             mapping=vhosts[d]
                     if mapping==None:
                         print 'Error, Not configured for vhost: '+rd
                         return
                 else:
                     print 'Direct access not allowed. Use proxy.'                     return
                 return func(mapping=mapping, *args, **kw)
             return proxyfunc
         return decorator
     
     
     ########################################################################
     # Site 1:
     ########################################################################
     class index_1:
         def GET(self):
             web.render('../templates_1/main.html')
     
     ########################################################################
     # Site 2:
     ########################################################################
     class index_1:
         def GET(self):
             web.render('../templates_2/main.html')
     
     ########################################################################
     # Site 3:
     ########################################################################
     class index_1:
         def GET(self):
             web.render('../templates_3/main.html')

     
     
     #
     ## RUN APPLICATION
     #
     
     if __name__ == "__main__":
     
         import sys
         sys.argv.append('2345') #Set the port I want. A better way to do this?
         
         #instead of:
         #web.run(urls, web.reloader, session_mw)
         
         #apply the vhostrr "decorator" remotely
         web.run(vhostrr()(web.handle), web.reloader, session_mw)
