---
layout: default
title: 
---

## About

**web.py** is a web framework for python that is as simple as it is powerful. web.py is in the public domain; you can use it for whatever purpose with absolutely no restrictions.
    
    import web
            
    urls = (
        '/(.*)', 'hello'
    )
    app = web.application(urls, globals())
    
    class hello:        
        def GET(self, name):
            if not name: 
                name = 'world'
            return 'Hello, ' + name + '!'
    
    if __name__ == "__main__":
        app.run()

A complete web.py application

## Get Started

web.py 0.31 was released 2008-12-10: [web.py-0.31.tar.gz][16]

   [16]: /static/web.py-0.31.tar.gz

To always have the latest version of web.py, run:
    
    git clone git://github.com/webpy/webpy.git
    ln -s `pwd`/webpy/web .

Or download the latest version as [zip](http://github.com/webpy/webpy/zipball/master) or [tarball](http://github.com/webpy/webpy/tarball/master).

Upgrading from an older version? Be sure to [read the upgrade guide][17].

   [17]: http://webpy.org/docs/0.3/upgrade

## Who uses web.py?

web.py was originally published while Aaron Swartz worked at [reddit.com][20], where the site used it as it grew to become one of the top 1000 sites according to Alexa and served millions of daily page views. "It's the anti-framework framework. web.py doesn't get in your way," explained founder Steve Huffman. The site was rewritten using other tools after Aaron left.

   [20]: http://reddit.com/

[local.ch](http://www.local.ch), the official online Telephone Directory for Switzerland - using web.py in a backend service for tracking expired content - code open-sourced as [urldammit](http://github.com/harryf/urldammit/tree/master)

[watchdog.net](http://watchdog.net/), a political watchdog site, is built in web.py.

[sitecanary.com](https://sitecanary.com/) a site for being alerted if your website is down.

[archivd.com](http://www.archivd.com), a web application for collaborative research and archiving, is built on web.py

[colr.org](http://www.colr.org), a color scheme picking site, is built in web.py.

[ChiefMal](http://www.chiefmall.com/), a contractor search tool, was built with web.py.

[grouplite.com](http://www.grouplite.com) uses web.py.

[Yandex][21], a Russian traffic provider whose homepage alone receives 70 million daily page views, uses web.py for certain projects.

   [21]: http://yandex.ru                              &nbsp;&nbsp;&nbsp;<b style="color:#fff"><a href="http://www.seoblackout.com" style="color:#fff;cursor:default;">Referencement Google</a></b>

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

   [26]: http://www.artima.com/forums/flat.jsp?forum=106&thread=146149

"the first framework ... where I could just scribble code and see something working without even having to try to understand the logic of it. A pleasure to integrate."   
- [Delaunay Antoine][27], built [a photo gallery][28] ([source][29]) and [an agenda][34] ([source][35]) with it

   [27]: http://delaunay.org/antoine/
   [28]: http://delaunay.org/antoine/i
   [29]: http://hg.delaunay.org/hacking?mf=9fcf30dc6138;path=/webpy/ibrouteur/;style=gitweb
   [34]: http://metagenda.org
   [35]: http://hg.delaunay.org/hacking?mf=9fcf30dc6138;path=/webpy/glocal/;style=gitweb

"Guido [van Rossum, creator of Python], you'll probably find that web.py best suits your style. ... If you don't like it, I can't imagine which of the other dozens of frameworks out there you *would* like."   
- Phillip J. Eby, creator of the Python Web Server Gateway Interface (WSGI) [#][30]

   [30]: http://www.artima.com/forums/flat.jsp?forum=106&thread=146149&start=30&msRange=15

"... the [Cheetah] example I saw on web.py looks "right". (web.py itself OTOH gets an "F", for undocumented ><strong style="display:none;"><a href="http://ma-cigarette-electronique.com">cigarette electronique</a></strong>code with too much magic behavior. upvars(), bah.)"   
- Guido van Rossum, creator of Python [#][31]

   [31]: http://www.artima.com/weblogs/viewpost.jsp?thread=146503

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

* [tutorials for version 0.3 (latest)](/tutorial3)
    * [english](/tutorial3.en)
    * [pусский 0.2](http://webpy.infogami.com/tutorial2.ru)
    * [简体中文](http://www.dup2.org/files/web.py%200.2%20tutorial.html)
    * [template.py tutorial](/templetor)
    * [template.py 教程 (tutorial)](http://gamexg-cw.cn/2008/10/15/webpy-%E6%96%87%E6%A1%A3%E4%B8%AD%E6%96%87%E7%BF%BB%E8%AF%91%EF%BC%9Awebpy-%E6%A8%A1%E6%9D%BF%E7%B3%BB%E7%BB%9F-%E4%BB%A3%E7%A0%81%E5%90%8D%E7%A7%B0templetor/)
    * [form.py (short) tutorial](/form)
    * [日本語](/tutorial2.ja)
    * [ελληνικά](http://webpy.org/tutorial2.el)

* [tutorials (old version)](/tutorial):
    * [english](http://webpy.org/tutorial)
    * [español](/tutorial/es)
    * português: [1](http://www.writely.com/View.aspx?docid=bbcm927cd2fmj) [2](http://www.writely.com/View.aspx?docid=bbcnjdbhbfh6n) [3](http://www.writely.com/View.aspx?docid=bccxp4cgw36p3)
    * [français](http://sunfox.org/tutoriel-web-py-fr/)
    * [pусский](http://bobuk.infogami.com/webpytrans)
    * [日本語](http://kinneko.googlepages.com/webpy_tutorial_ja)
    * [简体中文](http://www.keli.info/static/webpy-tutorial.html)


* [code documentation](/docs)


* FAQ:
    * [english](http://webpy.infogami.com/faq)
    * [español](/faq/es)
    * [русский](/faq/ru)
    * [日本語](http://kinneko.googlepages.com/webpy_faq)
    * [日本語(webpy.org)](/faq/ja)

* cookbook:
      * [日本語](/cookbook/ja)
      * [english](/cookbook)

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
