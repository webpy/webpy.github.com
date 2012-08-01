---
layout: default
title: quick vhosting hack
---

# quick vhosting hack

Here is a 10 minute hack with lots of room for improvement but I think its
pretty useful. I made this to allow the serving of multiple
sites from a single webpy app.

I created this because I would like to run a few small sites but my cheap
account at my hosting provider:

 * Only allows 40MB to be used by persistent processes. 
 * Only allows *one* persistent process.
 * Multiple instances of webpy would require multiple ports to be proxied with apache's mod_proxy
   and this configuration can only be done by the server admin.

So, I just made a quick decorator for `web.handler`.

###Stuff to Note:

This expects to be working behind a proxy but that can easily be corrected.

More work could be done on `web.render` and the page class names so
the code you create for sites in this setup can be more easily made into
standalone sites later on.

The /static directory is currently still shared between all sites.


###The Code

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

     #vhost mapping: {domain:url_mapping}

     vhosts={'test.org':urls_1,
             'www.test.org':urls_2,
             'another-url.org':urls_3
             }

     #
     ## VHOSTING DECORATOR
     #
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
                     print 'Direct access not allowed. Use proxy.'
                     return
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
     class index_2:
         def GET(self):
             web.render('../templates_2/main.html')
     
     ########################################################################
     # Site 3:
     ########################################################################
     class index_3:
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
         web.run(vhostrr()(web.handle), web.reloader)
