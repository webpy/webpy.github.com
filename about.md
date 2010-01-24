---
layout: default
title: About
---

# About

<p class=vevent>web.py is a web framework for Python that is as simple as it is powerful. <span class=summary>Version 0.33</span> was <span class=summary>released</span> on <abbr class=dtstart title=2009-10-28>October 28, 2009</abbr> [ <a href=/static/web.py-0.33.tar.gz>tar.gz</a> | <a href=/changes#0.33>changes</a> ].</p>

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

<h2 id=changes>Change Log</h2>

**2009-10-28: web.py 0.33**

* form.Button takes optional argument `html`
* remove obsolete write function in http.py (tx Justin) (Bug#315337)
* refactor httpserver.runsimple code
* improve form.py for customizability
* new: add background updating to memoize
* fix: use sendmail from web.config.sendmail_path (tx Daniel Schwartz)
* fix: make web.profiler work on Windows (tx asmo) (Bug#325139)
* fix changequery to make it work correctly even when the input has multi-valued fields (Bug#118229)
* fix: make sure sequence exists before queying for currval(seqname) when executing postgres insert query (Bug#268705)
* fix: raise web.notfound() instead of return in autodelegate (tx SeC) 
* fix: raise NotSupportedError when len or bool is used on sqlite result (Bug#179644)
* fix: make db paramater optional for creating postgres DB to allow taking it from environ. (Bug#153491)
* fix unicode errors in db module
* fix: convert unicode strings to UTF8 before printing SQL queries
* fix unicode error in debugerror
* fix: don't convert file upload data to unicode even when file={} is not passed to web.input
* fix checkbox value/checked confusion (Bug#128233)
* fix: consider empty lines as part of the indented block in templetor
* fix: fix a bug in web.group

**2009-06-04: web.py 0.32**

* optional from_address to web.emailerrors
* upgrade wsgiserver to CherryPy/3.1.2
* support for extensions in Jinja2 templates (tx Zhang Huangbin)
* support web.datestr for datetime.date objects also
* support for lists in db queries
* new: uniq and iterview
* fix: set debug=False when application is run with mod_wsgi (tx
Patrick Swieskowski)
[Bug#370904](https://bugs.launchpad.net/webpy/+bug/370904)
* fix: make web.commify work  with decimals
[Bug#317204](https://bugs.launchpad.net/webpy/+bug/317204)
* fix: unicode issues with sqlite database
[Bug#373219](https://bugs.launchpad.net/webpy/+bug/373219)
* fix: urlquote url when the server is lighttpd
[Bug#339858](https://bugs.launchpad.net/webpy/+bug/339858)
* fix: issue with using date.format in templates
* fix: use TOP instead of LIMIT in mssql database
[Bug#324049](https://bugs.launchpad.net/webpy/+bug/324049)
* fix: make sessions work well with expirations
* fix: accept both list and tuple as arg values in form.Dropdown
[Bug#314970](https://bugs.launchpad.net/webpy/+bug/314970)
* fix: match parenthesis when parsing `for` statement in templates
* fix: fix python 2.3 compatibility
* fix: ignore dot folders when compiling templates (tx Stuart Langridge)
* fix: don't consume KeyboardInterrupt and SystemExit errors
* fix: make application work well with iterators

** 2008-12-10: 0.31**

* new: browser module
* new: test utilities
* new: ShelfStore
* fix: web.cookies error when default is None
* fix: paramstyle for OracleDB (tx kromakey)
* fix: performance issue in SQLQuery.join
* fix: use wsgi.url_scheme to find ctx.protocol

**2008-12-06: 0.3**

* new: replace print with return (<i>backward-incompatible</i>)
* new: application framework (<i>backward-incompatible</i>)
* new: modular database system (<i>backward-incompatible</i>)
* new: templetor reimplementation
* new: better unicode support
* new: debug mode (web.config.debug)
* new: better db pooling
* new: sessions
* new: support for GAE
* new: etag support
* new: web.openid module
* new: web.nthstr
* fix: various form.py fixes
* fix: python 2.6 compatibility
* fix: file uploads are not loaded into memory
* fix: SQLLiteral issue (Bug#180027)
* change: web.background is moved to experimental (<i>backward-incompatible</i>) 
* improved API doc generation (tx Colin Rothwell)

**2008-01-19: 0.23**

* fix: for web.background gotcha ([133079](http://bugs.launchpad.net/webpy/+bug/133079))
* fix: for postgres unicode bug ([177265](http://bugs.launchpad.net/webpy/+bug/177265))
* fix: web.profile behavior in python 2.5 ([133080](http://bugs.launchpad.net/webpy/+bug/133080))
* fix: only uppercase HTTP methods are allowed. ([176415](http://bugs.launchpad.net/webpy/+bug/176415))
* fix: transaction error in with statement ([125118](http://bugs.launchpad.net/webpy/+bug/125118))
* fix: fix in web.reparam ([162085](http://bugs.launchpad.net/webpy/+bug/162085))
* fix: various unicode issues ([137042](http://bugs.launchpad.net/webpy/+bug/137042), [180510](http://bugs.launchpad.net/webpy/+bug/180510), [180549](http://bugs.launchpad.net/webpy/+bug/180549), [180653](http://bugs.launchpad.net/webpy/+bug/180653))
* new: support for https
* new: support for secure cookies
* new: sendmail
* new: htmlunquote


**2007-08-23: 0.22**

* compatibility with new DBUtils API ([122112](https://bugs.launchpad.net/webpy/+bug/122112))
* fix reloading ([118683](https://bugs.launchpad.net/webpy/+bug/118683))
* fix compatibility between `changequery` and `redirect` ([118234](https://bugs.launchpad.net/webpy/+bug/118234))
* fix relative URI in `web.redirect` ([118236](https://bugs.launchpad.net/webpy/+bug/118236))
* fix `ctx._write` support in built-in HTTP server ([121908](https://bugs.launchpad.net/webpy/+bug/121908))
* fix `numify` strips things after '.'s ([118644](https://bugs.launchpad.net/webpy/+bug/118644))
* fix various unicode isssues ([114703](https://bugs.launchpad.net/webpy/+bug/114703), [120644](https://bugs.launchpad.net/webpy/+bug/120644), [124280](https://bugs.launchpad.net/webpy/+bug/124280))

**2007-05-28: 0.21**

* <strong>security fix:</strong> prevent bad characters in headers
* support for cheetah template reloading                    
* support for form validation                               
* new `form.File`                                           
* new `web.url`                                             
* fix rendering issues with hidden and button inputs        
* fix 2.3 incompatability with `numify`                     
* fix multiple headers with same name                       
* fix web.redirect issues when homepath is not /            
* new CherryPy wsgi server                                  
* new nested transactions                                   
* new sqlliteral                                            

**2006-05-09: 0.138**

* New function: `intget`
* New function: `datestr`
* New function: `validaddr`
* New function: `sqlwhere`
* New function: `background`, `backgrounder`
* New function: `changequery`
* New function: `flush`
* New function: `load`, `unload`
* New variable: `loadhooks`, `unloadhooks`
* Better docs; generating [docs](documentation) from web.py now
* global variable `REAL_SCRIPT_NAME` can now be used to work around lighttpd madness
* fastcgi/scgi servers now can listen on sockets
* `output` now encodes Unicode
* `input` now takes optional `_method` argument
* <strong>Potentially-incompatible change:</strong> `input` now returns `badrequest` automatically when `requireds` aren't found
* `storify` now takes lists and dictionaries as requests (see docs)
* `redirect` now blanks any existing output
* Quote SQL better when `db_printing` is on
* Fix delay in `nomethod`
* Fix `urlquote` to encode better.
* Fix 2.3 incompatibility with `iters` (tx ??)
* Fix duplicate headers
* Improve `storify` docs
* Fix `IterBetter` to raise IndexError, not KeyError

**2006-03-27: 0.137**

* Add function `dictfindall` (tx Steve Huffman)
* Add support to `autodelegate` for arguments
* Add functions `httpdate` and `parsehttpdate`
* Add function `modified`
* Add support for FastCGI server mode
* Clarify `dictadd` documentation (tx Steve Huffman)
* Changed license to public domain
* Clean up to use `ctx` and `env` instead of `context` and `environ`
* Improved support for PUT, DELETE, etc. (tx list)
* Fix `ctx.fullpath` (tx Jesir Vargas)
* Fix sqlite support (tx Dubhead)
* Fix documentation bug in `lstrips` (tx Gregory Petrosyan)
* Fix support for IPs and ports (1/2 tx Jesir Vargas)
* Fix `ctx.fullpath` (tx Jesir Vargas)
* Fix sqlite support (tx Dubhead)
* Fix documentation bug in `lstrips` (tx Gregory Petrosyan)
* Fix `iters` bug with sets
* Fix some breakage introduced by Vargas's patch
* Fix `sqlors` bug
* Fix various small style things (tx Jesir Vargas)
* Fix bug with `input` ignoring GET input

**2006-02-22: 0.136 (svn)**

* Major code cleanup (tx to Jesir Vargas for the patch).
* 2006-02-15: 0.135
* Really fix that mysql regression (tx Sean Leach).
* 2006-02-15: 0.134
* The `StopIteration` exception is now caught. This can be used by functions that do things like check to see if a user is logged in. If the user isn't, they can output a message with a login box and raise StopIteration, preventing the caller from executing.
* Fix some documentation bugs.
* Fix mysql regression (tx mrstone).

**2006-02-12: 0.133**

* Docstrings! (tx numerous, esp. Jonathan Mark (for the patch) and Guido van Rossum (for the prod))
* Add `set` to web.iters.
* Make the `len` returned by `query` an int (tx ??).
* <strong>Backwards-incompatible change:</strong> `base` now called `prefixurl`.
* <strong>Backwards-incompatible change:</strong> `autoassign` now takes `self` and `locals()` as arguments.

**2006-02-07: 0.132**

* New variable `iters` is now a listing of possible list-like types (currently list, tuple, and, if it exists, Set).
* New function `dictreverse` turns `{1:2}` into `{2:1}`.
* `Storage` now a dictionary subclass.
* `tryall` now takes an optional prefix of functions to run.
* `sqlors` has various improvements.
* Fix a bunch of DB API bugs.
* Fix bug with `storify` when it received multiple inputs (tx Ben Woosley).
* Fix bug with returning a generator (tx Zbynek Winkler).
* Fix bug where len returned a long on query results (tx F.S).


**2006-01-31: 0.131 (not officially released)**

* New function `_interpolate` used internally for interpolating strings.
* Redone database API. `select`, `insert`, `update`, and `delete` all made consistent. Database queries can now do more complicated expressions like `$foo.bar` and `${a+b}`. You now have to explicitly pass the dictionary to look up variables in. Pass `vars=locals()` to get the old functionality of looking up variables .
* New functions `sqllist` and `sqlors` generate certain kinds of SQL.

**2006-01-30: 0.13**

* New functions `found`, `seeother`, and `tempredirect` now let you do other kinds of redirects. `redirect` now also takes an optional status parameter. (tx many)
* New functions `expires` and `lastmodified` make it easy to send those headers.
* New function `gone` returns a 410 Gone (tx David Terrell).
* New function `urlquote` applies url encoding to a string.
* New function `iterbetter` wraps an iterator and allows you to do __getitem__s on it.
* Have `query` return an `iterbetter` instead of an iterator.
* Have `debugerror` show tracebacks with the innermost frame first.
* Add `__hash__` function to `threadeddict` (and thus, `ctx`).
* Add `context.host` value for the requested host name.
* Add option `db_printing` that prints database queries and the time they take.
* Add support for database pooling (tx Steve Huffman).
* Add support for passing values to functions called by `handle`. If you do `('foo', 'value')` it will add `'value'` as an argument when it calls `foo`.
* Add support for scgi (tx David Terrell for the patch).
* Add support for web.py functions that are iterators (tx Brendan O'Connor for the patch).
* Use new database cursors on each call instead of reusing one.
* `setcookie` now takes an optional `domain` argument.
* Fix bug in autoassign.
* Fix bug where `debugerror` would break on objects it couldn't display.
* Fix bug where you couldn't do `#include`s inline.
* Fix bug with `reloader` and database calls.
* Fix bug with `reloader` and base templates.
* Fix bug with CGI mode on certain operating systems.
* Fix bug where `debug` would crash if called outside a request.
* Fix bug with `context.ip` giving weird values with proxies.

**2006-01-29: 0.129**

* Add Python 2.2 support.

**2006-01-28: 0.128**

* Fix typo in `web.profile`.

**2006-01-28: 0.127**

* Fix bug in error message if invalid dbn is sent (tx Panos Laganakos).

**2006-01-27: 0.126**

* Fix typos in Content-Type headers (tx Beat Bolli for the prod).

**2006-01-22: 0.125**

* Support Cheetah 2.0.

**2006-01-22: 0.124**

* Fix spacing bug (tx Tommi Raivio for the prod).

**2006-01-16: 0.123**

* Fix bug with CGI usage (tx Eddie Sowden for the prod).


**2006-01-14: 0.122**

* Allow DELETEs from `web.query` (tx Joost Molenaar for the prod).

**2006-01-08: 0.121**

* Allow import of submodules like `pkg.mod.cn` (tx Sridhar Ratna).
* Fix a bug in `update` (tx Sergey Khenkin).

**2006-01-05: 0.12**

* <strong>Backwards-incompatible change:</strong> `db_parameters` is now a dictionary.
* <strong>Backwards-incompatible change:</strong> `sumdicts` is now `dictadd`.
* Add support for PyGreSQL, MySQL (tx Hallgrimur H. Gunnarsson).
* Use HTML for non-Cheetah error message.
* New function `htmlquote()`.
* New function `tryall()`.
* `ctx.output` can now be set to a generator. (tx Brendan O'Connor)

**2006-01-04: 0.117**

* Add support for psycopg 1.x. (tx Gregory Price)

**2006-01-04: 0.116**

* Add support for Python 2.3. (tx Evan Jones)

**2006-01-04: 0.115**

* Fix some bugs where database queries weren't reparameterized. Oops!
* Fix a bug where `run()` wasn't getting the right functions.
* Remove a debug statement accidentally left in.
* Allow `storify` to be used on dictionaries. (tx Joseph Trent)

**2006-01-04: 0.114**

* Make `reloader` work on Windows. (tx manatlan)
* Fix some small typos that affected colorization. (tx Gregory Price)

**2006-01-03: 0.113**

* Reorganize `run()` internals so mod_python can be used. (tx Nicholas Matsakis)

**2006-01-03: 0.112**

* Make `reloader` work when `code.py` is called with a full path. (tx David Terrell)

**2006-01-03: 0.111**

* Fixed bug in `strips()`. (tx Michael Josephson)

**2006-01-03: 0.11**

* First public version.