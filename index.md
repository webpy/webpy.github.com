---
layout: default
title: Welcome to web.py!
---

**web.py** is a web framework for python that is as simple as it is powerful. web.py is in the public domain; you can use it for whatever purpose with absolutely no restrictions.

<div style="float: right">
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

web.py 0.34 is the latest released version of web.py. You can install it by running:

    sudo easy_install web.py

Or to get the latest development version from git:
    
    git clone git://github.com/webpy/webpy.git
    ln -s `pwd`/webpy/web .

## Who uses web.py?

web.py was originally published while Aaron Swartz worked at [reddit.com][20], where the site used it as it grew to become one of the top 1000 sites according to Alexa and served millions of daily page views. "It's the anti-framework framework. web.py doesn't get in your way," explained founder Steve Huffman. (The site was rewritten using other tools after being acquired by Condé Nast.)

   [20]: http://reddit.com/

[Frinki](http://frinki.com), a new social network in Spanish.

[Yandex][21], the leading Russian search engine (their homepage alone receives 70 million daily page views).

   [21]: http://yandex.ru

[Make History](http://makehistory.national911memorial.org), a project of the 9/11 Memorial Museum, is powered by web.py on top of Google App Engine. On September 11, 2009, it received nearly 200,000 visitors. "It's my first time working with web.py and basically with Python," noted its developer. "web.py was awesome."

[Oyster Hotel Reviews](http://www.oyster.com/), a website that reviews hotels and lets you book them, uses web.py for its booking pages and dynamic content. They note that "web.py gives us the control we need for a large-scale website".

[local.ch](http://www.local.ch), the official online Telephone Directory for Switzerland - using web.py in a backend service for tracking expired content - code open-sourced as [urldammit](http://github.com/harryf/urldammit/tree/master).

[archivd.com](http://www.archivd.com), a web application for collaborative research and archiving, is built on web.py.

[Chiefmall](http://www.chiefmall.com/), a contractor search tool, was built with web.py.

"[web.py inspired the] web framework we use at FriendFeed [and] the webapp framework that ships with App Engine..."  
 - [Brett Taylor](http://bret.appspot.com/entry/experimenting-google-app-engine), co-founder of FriendFeed and original tech lead on Google App Engine

"In the ecosystem of web frameworks, something needs to occupy the 'small, light and fast' niche. web.py is it."  
- Lloyd Dalton, [colr.org](http://colr.org)

"We completed our server rewrite a few days ago with web.py and it was everything we could have wished for."  
- Sam Hsiung, [YouOS][25]

   [25]: http://www.youos.com/

"Django lets you write web apps in Django. TurboGears lets you write web apps in TurboGears. Web.py lets you write web apps in Python."  
- Adam Atlas

"very nicely written and concise (not to mention it's written by Aaron Swartz, whose coding skills are very trustable), and doesn't get in my way"   
- Jonas Galvez, Aupeo [#][26]

   [26]: http://shortb.net/~f561f1

"the first framework ... where I could just scribble code and see something working without even having to try to understand the logic of it. A pleasure to integrate."   
- Delaunay Antoine built [a photo gallery][28] and [an agenda][34] with it

   [28]: http://www.tendances-de-mode.com/
   [34]: http://metagenda.org

"Guido [van Rossum, creator of Python], you'll probably find that web.py best suits your style. ... If you don't like it, I can't imagine which of the other dozens of frameworks out there you *would* like."   
- Phillip J. Eby, creator of the Python Web Server Gateway Interface (WSGI) [#][30]

   [30]: http://shortb.net/~f561f2

"... the [Cheetah] example I saw on web.py looks "right". (web.py itself OTOH gets an "F", for undocumented code with too much magic behavior. upvars(), bah.)"   
- Guido van Rossum, creator of Python [#][31] (the magic, like upvars, has since been removed)

   [31]: http://shortb.net/+f561f3

"suffice to say I think Aaron is headed in the right direction."   
- Harry Fuecks: [a simple wiki with web.py][32]

   [32]: http://www.sitepoint.com/blogs/2006/01/06/a-simple-wiki-with-webpy/

"a very fascinating moment for me. The feelings just like the first time I wrote my php script ... it sure have let me learn python in the fun way. Good work aaron !"   
- Kamal [simple blog in webpy, learning python the fun way][33]

   [33]: http://www.k4ml.com/node/165
