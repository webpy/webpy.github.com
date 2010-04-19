---
layout: default
title: About web.py
---

# About web.py

Other languages : [français](/fr) | ...

**web.py** is a web framework for python that is as simple as it is powerful. web.py is in the public domain; you can use it for whatever purpose with absolutely no restrictions.

##A complete web.py application

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


## Get Started

web.py 0.34 was released on 2010-03-20: [web.py-0.34.tar.gz][16]

   [16]: /static/web.py-0.34.tar.gz

To always have the latest version of web.py, run:
    
    git clone git://github.com/webpy/webpy.git
    ln -s `pwd`/webpy/web .

Or download the latest version as [zip](http://github.com/webpy/webpy/zipball/master) or [tarball](http://github.com/webpy/webpy/tarball/master).

Upgrading from an older version? Be sure to [read the upgrade guide][17].

   [17]: http://webpy.org/docs/0.3/upgrade

## Who uses web.py?

web.py was originally published while Aaron Swartz worked at [reddit.com][20], where the site used it as it grew to become one of the top 1000 sites according to Alexa and served millions of daily page views. "It's the anti-framework framework. web.py doesn't get in your way," explained founder Steve Huffman. (The site was rewritten using other tools after being acquired by Condé Nast.)

   [20]: http://reddit.com/

[Frinki](http://frinki.com), a Facebook-like social network in spanish.

[Make History](http://makehistory.national911memorial.org), a project of the 9/11 Memorial Museum, is powered by web.py on top of Google App Engine. On September 11, 2009, it received nearly 200,000 visitors. "It's my first time working with web.py and basically with Python," noted its developer. "web.py was awesome."

[Oyster Hotel Reviews](http://www.oyster.com/), a website that reviews hotels and lets you book them, uses web.py for its booking pages and dynamic content. They note that "web.py gives us the control we need for a large-scale website".

[local.ch](http://www.local.ch), the official online Telephone Directory for Switzerland - using web.py in a backend service for tracking expired content - code open-sourced as [urldammit](http://github.com/harryf/urldammit/tree/master)

[sitecanary.com](https://sitecanary.com/) a site for being alerted if your website is down.

[watchdog.net](http://watchdog.net/), a political watchdog site, is built in web.py.

[archivd.com](http://www.archivd.com), a web application for collaborative research and archiving, is built on web.py

[colr.org](http://www.colr.org), a color scheme picking site, is built in web.py.


[Chiefmall](http://www.chiefmall.com/), a contractor search tool, was built with web.py.

[grouplite.com](http://www.grouplite.com) uses web.py.

[Yandex][21], a Russian traffic provider whose homepage alone receives 70 million daily page views, uses web.py for certain projects.

   [21]: http://yandex.ru

[LShift][22] has used web.py to build websites for [Expro][23] and [publisher Dorling Kindersley][24]. "web.py allows us to do what we do best," they report. "It does the webapp thing brilliantly, and without requiring us to compromise on flexibility and originality."

   [22]: http://www.lshift.net/
   [23]: http://exproretail.com/
   [24]: http://travel.dk.com/

[micropledge][m], a web app that collects funding for software ideas, is built in web.py. "We've enjoyed fitting in with its minimalist approach," says developer Ben Hoyt.

   [m]: http://micropledge.com/

The [bivalidator](http://xhtml-css.com/) checks your HTML and CSS validation.

[jottit.com](http://jottit.com) is built with web.py.  Jottit makes getting a website as easy as filling out a textbox. 

[Tasko][t] is built with web.py. Tasko is an online task management tool which  uses a plain text file format to store all the information.

   [t]: http://taskodone.com/

[Damiga][d] is built with web.py. Damiga is a place where you can anonymously and freely tell the world how you feel about other people: friends, celebrities, even fictional characters. It's also a place where you can see how the world feels about you.  

   [d]: http://damiga.com/

[Fotosaur.us][f], an unbelievably rad image bookmarking app, was written with web.py.

   [f]: http://fotosaur.us


[URIs.us][u] is service for creating short urls. Deploying on Google App Engine

   [u]: http://uris.us 


[xykra] [x] is a minimalist (160 Python lines) wiki using [Markdown](http://daringfireball.net/projects/markdown/).

   [x]: http://xykra.org

[Edgarest] [y] is built with web.py.Edgarest provides fast, intuitive search of SEC Filings.

   [y]: http://edgarest.com


[Wklej.to] [z] is a nopaste/Pastebin app with Free and Open api, and of course with desktop plugins and clients.

   [z]: http://wklej.to

[Sysinternals CD] [zz] integrates webpy and postgresql to render an automated website

   [zz]: http://sysinternals.xykra.org

[Biomed Search] [zzz] searches over a million biomedical images images in nicely viewable sizes.

   [zzz]: http://www.biomed-search.com

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

   [28]: http://github.com/antoine/ibrouteur/
   [34]: http://metagenda.org

"Guido [van Rossum, creator of Python], you'll probably find that web.py best suits your style. ... If you don't like it, I can't imagine which of the other dozens of frameworks out there you *would* like."   
- Phillip J. Eby, creator of the Python Web Server Gateway Interface (WSGI) [#][30]

   [30]: http://shortb.net/~f561f2

"... the [Cheetah] example I saw on web.py looks "right". (web.py itself OTOH gets an "F", for undocumented code with too much magic behavior. upvars(), bah.)"   
- Guido van Rossum, creator of Python [#][31]

   [31]: http://shortb.net/+f561f3

"suffice to say I think Aaron is headed in the right direction."   
- Harry Fuecks: [a simple wiki with web.py][32]

   [32]: http://www.sitepoint.com/blogs/2006/01/06/a-simple-wiki-with-webpy/

"a very fascinating moment for me. The feelings just like the first time I wrote my php script ... it sure have let me learn python in the fun way. Good work aaron !"   
- Kamal [simple blog in webpy, learning python the fun way][33]

   [33]: http://www.k4ml.com/node/165

### web.py documentation:

* [installation](/install)
    * [english](/install)
    * [mac os x](/install_macosx)
    * [español](/install/es)
    * [日本語](/install/ja)
    * [简体中文](/install/zh-cn)
    * [Italiano](/install/it)
    * [français](/install/fr)


* [tutorials for version 0.3 (latest)](/tutorial3)
    * [english](/tutorial3.en)
    * [简体中文](/tutorial3.zh-cn)
    * [p?????? 0.2](http://webpy.infogami.com/tutorial2.ru)
    * [????](http://www.dup2.org/files/web.py%200.2%20tutorial.html)
    * [template.py tutorial](/templetor)
    * [form.py (short) tutorial](/form)
    * [日本語](/tutorial2.ja)
    * [e???????](http://webpy.org/tutorial2.el)
    * [français](/tutorial3.fr)

* [tutorials (old version)](/tutorial):
    * [english](http://webpy.org/tutorial)
    * [español](/tutorial/es)
    * português: [1](http://www.writely.com/View.aspx?docid=bbcm927cd2fmj) [2](http://www.writely.com/View.aspx?docid=bbcnjdbhbfh6n) [3](http://www.writely.com/View.aspx?docid=bccxp4cgw36p3)
    * [français](http://sunfox.org/tutoriel-web-py-fr/)
    * [p??????](http://bobuk.infogami.com/webpytrans)
    * [日本語](http://kinneko.googlepages.com/webpy_tutorial_ja)


* [code documentation](/docs)


* FAQ:
    * [english](http://webpy.org/faq)
    * [español](/faq/es)
    * [???????](/faq/ru)
    * [???](http://kinneko.googlepages.com/webpy_faq)
    * [日本語](/faq/ja)
    * [简体中文](/faq/zh-cn)
    * [français](/faq/fr)

* cookbook:
      * [日本語](/cookbook/ja)
      * [english](/cookbook)
      * [简体中文](/cookbook/zh-cn)

* [code samples](/src)

* [friendly hosts](/hosts)

* [related projects](/related)

* [tricks](/tricks)



### web.py community

* [**mail list**](http://groups.google.com/group/webpy/ "web.py google group"): home of the web.py discussion

* [**irc channel**](irc://irc.freenode.net/webpy "#webpy on irc.freenode.net"): home of the web.py talk

* [powered by web.py buttons](http://luke.jottit.com/webpy_logo)

### web.py development

* [git repository](http://github.com/webpy/webpy)

* [launchpad site](http://launchpad.net/webpy)