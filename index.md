---
layout: default
title: Welcome to web.py!
---

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

web.py 0.37 is the latest released version of web.py. You can install it by running:

    sudo easy_install web.py

Or to get the latest development version from git:
    
    git clone git://github.com/webpy/webpy.git
    ln -s `pwd`/webpy/web .

## Who uses web.py?

web.py was originally published while Aaron Swartz worked at [reddit.com][20], where the site used it as it grew to become one of the top 1000 sites according to Alexa and served millions of daily page views. "It's the anti-framework framework. web.py doesn't get in your way," explained founder Steve Huffman. (The site was rewritten using other tools after being acquired by Condé Nast.)

   [20]: http://reddit.com/

* [Frinki](http://frinki.com), a new social network in Spanish.

* [Yandex][21], the leading Russian search engine (their homepage alone receives 70 million daily page views).

   [21]: http://yandex.ru

* [Make History](http://makehistory.national911memorial.org), a project of the 9/11 Memorial Museum, is powered by web.py on top of Google App Engine. On September 11, 2009, it received nearly 200,000 visitors. "It's my first time working with web.py and basically with Python," noted its developer. "web.py was awesome."

* [Oyster.com](http://www.oyster.com/), a website that reviews and photographs hotels, uses web.py for the entire site. They note that "web.py gives us the control we need for a large-scale website". As of Jan 2013, Oyster.com renders about 230,000 pages per day.

* [local.ch](http://www.local.ch), the official online Telephone Directory for Switzerland - using web.py in a backend service for tracking expired content - code open-sourced as [urldammit](http://github.com/harryf/urldammit/tree/master).

* [archivd.com](http://www.archivd.com), a web application for collaborative research and archiving, is built on web.py.

* [Chiefmall](http://www.chiefmall.com/), a contractor search tool, was built with web.py.

* [pudung.com](http://pudung.com), Online Store based in Jakarta, Indonesia, is using [onlinestore-multi](https://github.com/nopri/onlinestore-multi) (Simple Online Store application built using Python, web.py, jQuery and MySQL).

"[web.py inspired the] web framework we use at FriendFeed [and] the webapp framework that ships with App Engine..."  
<span class="cite">&nbsp;&nbsp;&mdash;&nbsp; [Brett Taylor](http://bret.appspot.com/entry/experimenting-google-app-engine), co-founder of FriendFeed and original tech lead on Google App Engine</span>

"Django lets you write web apps in Django. TurboGears lets you write web apps in TurboGears. Web.py lets you write web apps in Python."  
<span class="cite">&nbsp;&nbsp;&mdash;&nbsp; Adam Atlas</span>

"Guido [van Rossum, creator of Python], you'll probably find that web.py best suits your style. ... If you don't like it, I can't imagine which of the other dozens of frameworks out there you *would* like."   
<span class="cite">&nbsp;&nbsp;&mdash;&nbsp; Phillip J. Eby, creator of the Python Web Server Gateway Interface (WSGI) [#][30]</span>

   [30]: http://www.artima.com/forums/flat.jsp?forum=106&thread=146149&start=30&msRange=15
