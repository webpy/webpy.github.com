---
layout: default
title: About
---

# About

web.py is a web framework for Python that is as simple as it is powerful. It is released to the public domain via a <a href=http://creativecommons.org/publicdomain/zero/1.0/ rel=license>Creative Commons Zero 1.0 License</a> &mdash; you can use it for whatever purpose with absolutely no restrictions.

<h2 id=status>Status</h2>

web.py 0.33 was released on 2009-10-28 [ [tar.gz](/static/web.py-0.33.tar.gz) ]

<h2 id=hello>Hello World</h2>

<pre class=prettyprint><code>"""
hello world

"""

import web

resources = (
  r'/(.*)', 'Hello'
)
webapp = web.application(resources, globals())

class Hello:
  """
  say Hello
  
  """
  
  def GET(self, name):
    if not name: 
        name = 'World'
    return 'Hello ' + name + '!'

if __name__ == '__main__':
  webapp.run()</code></pre>

[ [download](/usage/hello.py?format=raw) ]

<h2 id=who-uses>Who Uses web.py?</h2>

<p class=vcard>web.py was originally published while Aaron Swartz worked at <a class="fn org url uid" href=http://reddit.com/>Reddit</a>, where the site used it as it grew to become one of the top 1000 sites according to Alexa and served millions of daily page views. "It's the anti-framework framework. web.py doesn't get in your way," explained founder Steve Huffman. <em>The site was rewritten using other tools after being acquired by Condé Nast.</em></p>

<p class=vcard><a class="fn org url uid" href=http://frinki.com/>Frinki</a>, a Facebook-like social network in Spanish.

<p class=vcard><a class="fn org url uid" href=http://makehistory.national911memorial.org/>Make History</a>, a project of the 9/11 Memorial Museum, is powered by web.py on top of Google App Engine. On September 11, 2009, it received nearly 200,000 visitors. "It's my first time working with web.py and basically with Python," noted its developer. "web.py was awesome."</p>

<p class=vcard><a class="fn org url uid" href=http://local.ch/>local.ch</a>, the official online Telephone Directory for Switzerland - using web.py in a backend service for tracking expired content - code open-sourced as <a href=http://github.com/harryf/urldammit/tree/master>urldammit</a>.</p>

<p class=vcard><a class="fn org url uid" href=http://sitecanary.com/>SiteCanary</a> a site for being alerted if your website is down.</p>

<p class=vcard><a class="fn org url uid" href=http://watchdog.net/>watchdog.net</a>, a political watchdog site, is built in web.py.</p>

<p class=vcard><a class="fn org url uid" href=http://archivd.com/>Archivd</a>, a web application for collaborative research and archiving, is built on web.py.</p>

<p class=vcard><a class="fn org url uid" href=http://colr.org/>colr.org</a>, a color scheme picking site, is built in web.py.</p>

<p class=vcard><a class="fn org url uid" href=http://chiefmall.com/>Chiefmall</a>, a contractor search tool, was built with web.py.</p>

<p class=vcard><a class="fn org url uid" href=http://grouplite.com/>Grouplite</a> uses web.py.</p>

<p class=vcard><a class="fn org url uid" href=http://yandex.ru/>Yandex</a>, a Russian traffic provider whose homepage alone receives 70 million daily page views, uses web.py for certain projects.</p>

<p class=vcard><a class="fn org url uid" href=http://lshift.net/>LShift</a> has used web.py to build websites for <a href=http://exproretail.com/>Expro</a> and publisher <a href=http://travel.dk.com/>Dorling Kindersley</a>. "web.py allows us to do what we do best," they report. "It does the webapp thing brilliantly, and without requiring us to compromise on flexibility and originality."</p>

<p class=vcard><a class="fn org url uid" href=http://micropledge.com/>microPledge</a>, a web app that collects funding for software ideas, is built in web.py. "We've enjoyed fitting in with its minimalist approach," says developer Ben Hoyt.</p>

<p class=vcard><a class="fn org url uid" href=http://xhtml-css.com/>XHTML-CSS Validator</a> checks your HTML and CSS validation.</p>

<p class=vcard><a class="fn org url uid" href=http://jottit.com/>Jottit</a> is built with web.py. Jottit makes getting a website as easy as filling out a textbox.</p>

<p class=vcard><a class="fn org url uid" href=http://taskodone.com/>Tasko</a> is built with web.py. Tasko is an online task management tool which uses a plain text file format to store all the information.</p>

<p class=vcard><a class="fn org url uid" href=http://damiga.com/>Damiga</a> is built with web.py. Damiga is a place where you can anonymously and freely tell the world how you feel about other people: friends, celebrities, even fictional characters. It's also a place where you can see how the world feels about you.</p>

<p class=vcard><a class="fn org url uid" href=http://fotosaur.us/>Fotosaur.us</a>, an unbelievably rad image bookmarking app, was written with web.py.</p>

<p class=vcard><a class="fn org url uid" href=http://uris.us/>URIs.us</a> is a service for creating short urls. Deployed on Google App Engine.</p>

<p class=vcard><a class="fn org url uid" href=http://xykra.org/>xykra</a> is a minimalist (160 Python lines) wiki using <a href=http://daringfireball.net/projects/markdown/>Markdown</a>.</p>

<p class=vcard><a class="fn org url uid" href=http://edgarest.com/>Edgarest</a> is built with web.py. Edgarest provides fast, intuitive search of SEC Filings.</p>

<p class=vcard><a class="fn org url uid" href=http://wklej.to/>Wklej.to</a> is a nopaste/Pastebin app with a Free and Open API and of course with desktop plugins and clients.</p>

<p class=vcard><a class="fn org url uid" href=http://sysinternals.xykra.org/>Sysinternals CD</a> integrates web.py and postgresql to render an automated website.</p>

<p class=vcard><a class="fn org url uid" href=http://biomed-search.com/>Biomed Search</a> searches over a million biomedical images images in nicely viewable sizes.</p>

<h2 id=what-saying>What People are Saying about web.py</h2>

>   [web.py inspired the] web framework we use at FriendFeed [and] the webapp framework that ships with App Engine...

<p class=vcard>—<a href=http://bret.appspot.com/entry/experimenting-google-app-engine>Brett Taylor</a>, co-founder of FriendFeed and original tech lead on Google App Engine.</p>

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

   [31]: http://shortb.net/~f561f3

"suffice to say I think Aaron is headed in the right direction."   
- Harry Fuecks: [a simple wiki with web.py][32]

   [32]: http://www.sitepoint.com/blogs/2006/01/06/a-simple-wiki-with-webpy/

"a very fascinating moment for me. The feelings just like the first time I wrote my php script ... it sure have let me learn python in the fun way. Good work aaron !"   
- Kamal [simple blog in webpy, learning python the fun way][33]

   [33]: http://www.k4ml.com/node/165

<script src=http://angelo.gladding.name/assets/jquery.js></script>
<script src=http://angelo.gladding.name/assets/webpy/js-prettify/prettify.js></script>
<script src=http://angelo.gladding.name/assets/webpy/enliven.js></script>

<style>
@import url(http://angelo.gladding.name/assets/webpy/js-prettify/prettify.css);
@import url(http://angelo.gladding.name/assets/webpy/changes.css);
</style>