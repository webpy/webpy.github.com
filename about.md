---
layout: default
title: About
---

# About

web.py is a web framework for Python that is as simple as it is powerful.

<h2 id=changes>Current Status</h2>

<div class=hentry>
<p><span class=entry-title>Version 0.33 released</span> on <abbr class="published updated" title=2009-10-28>October 28, 2009</abbr> [ <a href=/static/web.py-0.33.tar.gz rel=bookmark>tar.gz</a> ].</p>
<ul>
  <li>form.Button takes optional argument `html`</li>
  <li>remove obsolete write function in http.py (tx Justin) (Bug#315337)</li>
  <li>refactor httpserver.runsimple code</li>
  <li>improve form.py for customizability</li>
  <li>new: add background updating to memoize</li>
  <li>fix: use sendmail from web.config.sendmail_path (tx Daniel Schwartz)</li>
  <li>fix: make web.profiler work on Windows (tx asmo) (Bug#325139)</li>
  <li>fix changequery to make it work correctly even when the input has multi-valued fields (Bug#118229)</li>
  <li>fix: make sure sequence exists before queying for currval(seqname) when executing postgres insert query (Bug#268705)</li>
  <li>fix: raise web.notfound() instead of return in autodelegate (tx SeC)</li>
  <li>fix: raise NotSupportedError when len or bool is used on sqlite result (Bug#179644)</li>
  <li>fix: make db paramater optional for creating postgres DB to allow taking it from environ. (Bug#153491)</li>
  <li>fix unicode errors in db module</li>
  <li>fix: convert unicode strings to UTF8 before printing SQL queries</li>
  <li>fix unicode error in debugerror</li>
  <li>fix: don't convert file upload data to unicode even when file={} is not passed to web.input</li>
  <li>fix checkbox value/checked confusion (Bug#128233)</li>
  <li>fix: consider empty lines as part of the indented block in templetor</li>
  <li>fix: fix a bug in web.group</li>
</ul>
</div>

1.  [Hello World](#hello)
1.  [Sites Built with web.py](#sites)
1.  [People Talking about web.py](#people)

<h2 id=hello>Hello World</h2>

<pre class=prettyprint><code>import web

resources = (
  r'/(.*)', 'Hello'
)
webapp = web.application(resources, globals())

class Hello:  
  def GET(self, name):
    if not name: 
        name = 'World'
    return 'Hello ' + name + '!'

if __name__ == '__main__':
  webapp.run()</code></pre>

[ [download](/usage/hello.py?format=raw) ]

<h2 id=sites>Sites Built with web.py</h2>

* <p class=vcard>web.py was originally published while Aaron Swartz worked at <a class="fn org url uid" href=http://reddit.com/>Reddit</a>, where the site used it as it grew to become one of the top 1000 sites according to Alexa and served millions of daily page views. "It's the anti-framework framework. web.py doesn't get in your way," explained founder Steve Huffman. <em>The site was rewritten using other tools after being acquired by Condé Nast.</em></p>

* <p class=vcard><a class="fn org url uid" href=http://frinki.com/>Frinki</a>, a Facebook-like social network in Spanish.

* <p class=vcard><a class="fn org url uid" href=http://makehistory.national911memorial.org/>Make History</a>, a project of the 9/11 Memorial Museum, is powered by web.py on top of Google App Engine. On September 11, 2009, it received nearly 200,000 visitors. "It's my first time working with web.py and basically with Python," noted its developer. "web.py was awesome."</p>

* <p class=vcard><a class="fn org url uid" href=http://local.ch/>local.ch</a>, the official online Telephone Directory for Switzerland - using web.py in a backend service for tracking expired content - code open-sourced as <a href=http://github.com/harryf/urldammit/tree/master>urldammit</a>.</p>

* <p class=vcard><a class="fn org url uid" href=http://sitecanary.com/>SiteCanary</a> a site for being alerted if your website is down.</p>

* <p class=vcard><a class="fn org url uid" href=http://watchdog.net/>watchdog.net</a>, a political watchdog site, is built in web.py.</p>

* <p class=vcard><a class="fn org url uid" href=http://archivd.com/>Archivd</a>, a web application for collaborative research and archiving, is built on web.py.</p>

* <p class=vcard><a class="fn org url uid" href=http://colr.org/>colr.org</a>, a color scheme picking site, is built in web.py.</p>

* <p class=vcard><a class="fn org url uid" href=http://chiefmall.com/>Chiefmall</a>, a contractor search tool, was built with web.py.</p>

* <p class=vcard><a class="fn org url uid" href=http://grouplite.com/>Grouplite</a> uses web.py.</p>

* <p class=vcard><a class="fn org url uid" href=http://yandex.ru/>Yandex</a>, a Russian traffic provider whose homepage alone receives 70 million daily page views, uses web.py for certain projects.</p>

* <p class=vcard><a class="fn org url uid" href=http://lshift.net/>LShift</a> has used web.py to build websites for <a href=http://exproretail.com/>Expro</a> and publisher <a href=http://travel.dk.com/>Dorling Kindersley</a>. "web.py allows us to do what we do best," they report. "It does the webapp thing brilliantly, and without requiring us to compromise on flexibility and originality."</p>

* <p class=vcard><a class="fn org url uid" href=http://micropledge.com/>microPledge</a>, a web app that collects funding for software ideas, is built in web.py. "We've enjoyed fitting in with its minimalist approach," says developer Ben Hoyt.</p>

* <p class=vcard><a class="fn org url uid" href=http://xhtml-css.com/>XHTML-CSS Validator</a> checks your HTML and CSS validation.</p>

* <p class=vcard><a class="fn org url uid" href=http://jottit.com/>Jottit</a> is built with web.py. Jottit makes getting a website as easy as filling out a textbox.</p>

* <p class=vcard><a class="fn org url uid" href=http://taskodone.com/>Tasko</a> is built with web.py. Tasko is an online task management tool which uses a plain text file format to store all the information.</p>

* <p class=vcard><a class="fn org url uid" href=http://damiga.com/>Damiga</a> is built with web.py. Damiga is a place where you can anonymously and freely tell the world how you feel about other people: friends, celebrities, even fictional characters. It's also a place where you can see how the world feels about you.</p>

* <p class=vcard><a class="fn org url uid" href=http://fotosaur.us/>Fotosaur.us</a>, an unbelievably rad image bookmarking app, was written with web.py.</p>

* <p class=vcard><a class="fn org url uid" href=http://uris.us/>URIs.us</a> is a service for creating short urls. Deployed on Google App Engine.</p>

* <p class=vcard><a class="fn org url uid" href=http://xykra.org/>xykra</a> is a minimalist (160 Python lines) wiki using <a href=http://daringfireball.net/projects/markdown/>Markdown</a>.</p>

* <p class=vcard><a class="fn org url uid" href=http://edgarest.com/>Edgarest</a> is built with web.py. Edgarest provides fast, intuitive search of SEC Filings.</p>

* <p class=vcard><a class="fn org url uid" href=http://wklej.to/>Wklej.to</a> is a nopaste/Pastebin app with a Free and Open API and of course with desktop plugins and clients.</p>

* <p class=vcard><a class="fn org url uid" href=http://sysinternals.xykra.org/>Sysinternals CD</a> integrates web.py and postgresql to render an automated website.</p>

* <p class=vcard><a class="fn org url uid" href=http://biomed-search.com/>Biomed Search</a> searches over a million biomedical images images in nicely viewable sizes.</p>

<h2 id=people>People Talking about web.py</h2>

>   [My] blog runs on the code I wrote this evening. ... I used a web framework we use at FriendFeed. It looks a lot like the webapp framework that ships with App Engine and web.py (which inspired both of them). [#](http://bret.appspot.com/entry/experimenting-google-app-engine)

<p class=vcard>—&thinsp;<a class="fn url uid" href=http://bret.appspot.com/>Brett Taylor</a><br><small>co-founder of FriendFeed and original tech lead on Google App Engine</small></p>

>   It's minimal. In the ecosystem of web frameworks, something needs to occupy the "small, light and fast" niche. web.py is it. [#](http://www.colr.org/rewrite.html)

<p class=vcard>—&thinsp;<a class="fn url uid" href=http://twitter.com/daltonlp>Lloyd Dalton</a><br><small>creator of colr.org</small></p>

>   We completed our server rewrite a few days ago with web.py and it was everything we could have wished for.

<p class=vcard>—&thinsp;<span class=fn>Sam Hsiung</span><br><small>creator of YouOS (out of service)</small></p>

>   Django lets you write web apps in Django. TurboGears lets you write web apps in TurboGears. web.py lets you write web apps in Python.

<p class=vcard>—&thinsp;<span class=fn>Adam Atlas</span></p>

>   If I were to start a personal project today I would probably pick [web.py]. It's very nicely written and concise (not to mention it's written by Aaron Swartz, whose coding skills are very trustable [sic]), and doesn't get in my way. [#](http://www.artima.com/forums/flat.jsp?forum=106&thread=146149#189284)

<p class=vcard>—&thinsp;<span class=fn>Jonas Galvez</span><br><small>Aupeo</small></p>

>   the first framework ... where I could just scribble code and see something working without even having to try to understand the logic of it. A pleasure to integrate."

<p class=vcard>—&thinsp;<span class=fn>Delaunay Antoine</span><br><small>creator of a <a href=http://github.com/antoine/ibrouteur/>photo gallery</a> and an <a href=http://metagenda.org/>agenda</a></small></p>

>   Guido [van Rossum, creator of Python], you'll probably find that web.py best suits your style. ... If you don't like it, I can't imagine which of the other dozens of frameworks out there you *would* like. [#](http://shortb.net/~f561f2)

<p class=vcard>—&thinsp;<span class=fn>Phillip J. Eby</span><br><small>creator of Python's <abbr title="Web Server Gateway Interface">WSGI</abbr></small></p>

>   ... the [Cheetah] example I saw on web.py looks "right". (web.py itself OTOH gets an "F", for undocumented code with too much magic behavior. upvars(), bah.) [#](http://shortb.net/~f561f3)

<p class=vcard>—&thinsp;<a class="fn url uid" href=http://www.python.org/~guido/>Guido van Rossum</a><br><small>creator of Python</small></p>

>   suffice to say I think Aaron is headed in the right direction.

<p class=vcard>—&thinsp;<span class=fn>Harry Fuecks</span><br><small><a href=http://www.sitepoint.com/blogs/2006/01/06/a-simple-wiki-with-webpy/>a simple wiki with web.py</a></small></p>

>   a very fascinating moment for me. The feelings just like the first time I wrote my php script ... it sure have let me learn python in the fun way. Good work aaron !

<p class=vcard>—&thinsp;<span class=fn>Kamal</span><br><small><a href=http://www.k4ml.com/node/165>simple blog in webpy, learning python the fun way</a></small></p>