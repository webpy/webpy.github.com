---
layout: default
title: Welcome to web.py!
---

Other langages : [French](/index.fr.html) | [Español](/index.es.html) | ...

## About web.py

**web.py** is a web framework for Python that is as simple as it is powerful. web.py is in the public domain; you can use it for whatever purpose with absolutely no restrictions.

<div style="float: right; margin: 1em">
<pre>
import web

urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello, ' + name + '!'

if __name__ == "__main__":
    app.run()
</pre>
<em>A complete web.py application.</em>
</div>

## Get Started

To install the latest web.py, please run:

    pip install web.py

The latest `0.51` release supports both Python 2.7 and Python >= 3.5.

Or to get the latest development version from git:
    
    git clone git://github.com/webpy/webpy.git
    ln -s `pwd`/webpy/web .

## Who uses web.py?

web.py was originally published while Aaron Swartz worked at [reddit.com][20], where the site used it as it grew to become one of the top 1000 sites according to Alexa and served millions of daily page views. "It's the anti-framework framework. web.py doesn't get in your way," explained founder Steve Huffman. (The site was rewritten using other tools after being acquired by Condé Nast.)

   [20]: http://reddit.com/

### Some user testimonials:

* "In the ecosystem of web frameworks, something must occupy the niche of 'small, light, and fast': web.py does this."*  
<span class="cite">&nbsp;&nbsp;&mdash;&nbsp; Lloyd Dalton, [colr.org](http://colr.org)</span>

* "We finished rewriting our server in only a fews days with web.py and it was everything we hoped for."*  
<span class="cite">&nbsp;&nbsp;&mdash;&nbsp; Sam Hsiung, [YouOS][25]</span>

   [25]: http://www.youos.com/

* "[Web.py inspired the] web framework we use at FriendFeed [and] the webapp framework that ships with App Engine..."*  
<span class="cite">&nbsp;&nbsp;&mdash;&nbsp; [Brett Taylor](http://backchannel.org/blog/google-app-engine), co-founder of FriendFeed and original tech lead on Google App Engine</span>

* "Django lets you write web apps in Django. TurboGears lets you write web apps in TurboGears. Web.py lets you write web apps in Python."*  
<span class="cite">&nbsp;&nbsp;&mdash;&nbsp; Alice Atlas</span>

* "Guido* [van Rossum, creator of Python]*, you'll probably find that web.py best suits your style. ... If you don't like it, I can't imagine which of the other dozens of frameworks out there you __would__ like."*   
<span class="cite">&nbsp;&nbsp;&mdash;&nbsp; Phillip J. Eby, creator of the Python Web Server Gateway Interface (WSGI) [#][30]</span>

   [30]: http://www.artima.com/forums/flat.jsp?forum=106&thread=146149&start=30&msRange=15
