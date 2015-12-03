---
layout: default
title: api docs
---

# api docs

<div>

<style type="text/css">
.module {
    font-size: 130%;
    font-weight: bold;
}

.function, .class, .type {
    font-size: 120%;
    font-weight: bold;
}

.method, .property {
    font-size: 115%;
    font-weight: bold;
}

.ts {
    font-size: small;
    font-weight: lighter;
    color: grey;
}

#contents_link {
    position: fixed;
    top: 0;
    right: 0;
    padding: 5px;
    background: rgba(255, 255, 255, 0.5);
}

#contents_link a:hover {
    font-weight: bold;
}
</style>


<div id="contents_link">
<a href="#top">Back to contents</a>
</div>

<ul>
<li><a href="#web.application">web.application</a></li>
<li><a href="#web.contrib.template">web.contrib.template</a></li>
<li><a href="#web.db">web.db</a></li>
<li><a href="#web.debugerror">web.debugerror</a></li>
<li><a href="#web.form">web.form</a></li>
<li><a href="#web.http">web.http</a></li>
<li><a href="#web.httpserver">web.httpserver</a></li>
<li><a href="#web.net">web.net</a></li>
<li><a href="#web.session">web.session</a></li>
<li><a href="#web.template">web.template</a></li>
<li><a href="#web.utils">web.utils</a></li>
<li><a href="#web.webapi">web.webapi</a></li>
<li><a href="#web.webopenid">web.webopenid</a></li>
<li><a href="#web.wsgi">web.wsgi</a></li>
</ul>
<p><span class="ts">module</span><code class="module"> <a name="web.application">web.application</a></code><br />
<div style="margin-left:15px"><p>Web application
(from web.py)</p></div></p>
<div style="margin-left:30px">
<p><span class="ts">class</span><code class="class"> application(self, mapping=(), fvars={}, autoreload=None)</code><br />
<div style="margin-left:45px"><p>Application to delegate requests based on path.</p>

<pre><code>&gt;&gt;&gt; urls = ("/hello", "hello")
&gt;&gt;&gt; app = application(urls, globals())
&gt;&gt;&gt; class hello:
...     def GET(self): return "hello"
&gt;&gt;&gt;
&gt;&gt;&gt; app.request("/hello").data
'hello'
</code></pre></div></p>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> add_mapping(self, pattern, classname)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> add_processor(self, processor)</code><br />
<div style="margin-left:75px"><p>Adds a processor to the application.</p>

<pre><code>&gt;&gt;&gt; urls = ("/(.*)", "echo")
&gt;&gt;&gt; app = application(urls, globals())
&gt;&gt;&gt; class echo:
...     def GET(self, name): return name
...
&gt;&gt;&gt;
&gt;&gt;&gt; def hello(handler): return "hello, " +  handler()
...
&gt;&gt;&gt; app.add_processor(hello)
&gt;&gt;&gt; app.request("/web.py").data
'hello, web.py'
</code></pre></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> browser(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> cgirun(self, *middleware)</code><br />
<div style="margin-left:75px"><p>Return a CGI handler. This is mostly useful with Google App Engine.
There you can just do:</p>

<pre><code>main = app.cgirun()
</code></pre></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> get_parent_app(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> handle(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> handle_with_processors(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> init_mapping(self, mapping)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> internalerror(self)</code><br />
<div style="margin-left:75px"><p>Returns HTTPError with '500 internal error' message</p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> load(self, env)</code><br />
<div style="margin-left:75px"><p>Initializes ctx using env.</p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> notfound(self)</code><br />
<div style="margin-left:75px"><p>Returns HTTPError with '404 not found' message</p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> request(self, localpart='/', method='GET', data=None, host='0.0.0.0:8080', headers=None, https=False, **kw)</code><br />
<div style="margin-left:75px"><p>Makes request to this application for the specified path and method.
Response will be a storage object with data, status and headers.</p>

<pre><code>&gt;&gt;&gt; urls = ("/hello", "hello")
&gt;&gt;&gt; app = application(urls, globals())
&gt;&gt;&gt; class hello:
...     def GET(self): 
...         web.header('Content-Type', 'text/plain')
...         return "hello"
...
&gt;&gt;&gt; response = app.request("/hello")
&gt;&gt;&gt; response.data
'hello'
&gt;&gt;&gt; response.status
'200 OK'
&gt;&gt;&gt; response.headers['Content-Type']
'text/plain'
</code></pre>

<p>To use https, use https=True.</p>

<pre><code>&gt;&gt;&gt; urls = ("/redirect", "redirect")
&gt;&gt;&gt; app = application(urls, globals())
&gt;&gt;&gt; class redirect:
...     def GET(self): raise web.seeother("/foo")
...
&gt;&gt;&gt; response = app.request("/redirect")
&gt;&gt;&gt; response.headers['Location']
'http://0.0.0.0:8080/foo'
&gt;&gt;&gt; response = app.request("/redirect", https=True)
&gt;&gt;&gt; response.headers['Location']
'https://0.0.0.0:8080/foo'
</code></pre>

<p>The headers argument specifies HTTP headers as a mapping object
such as a dict.</p>

<pre><code>&gt;&gt;&gt; urls = ('/ua', 'uaprinter')
&gt;&gt;&gt; class uaprinter:
...     def GET(self):
...         return 'your user-agent is ' + web.ctx.env['HTTP_USER_AGENT']
... 
&gt;&gt;&gt; app = application(urls, globals())
&gt;&gt;&gt; app.request('/ua', headers = {
...      'User-Agent': 'a small jumping bean/1.0 (compatible)'
... }).data
'your user-agent is a small jumping bean/1.0 (compatible)'
</code></pre></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> run(self, *middleware)</code><br />
<div style="margin-left:75px"><p>Starts handling requests. If called in a CGI or FastCGI context, it will follow
that protocol. If called from the command line, it will start an HTTP
server on the port named in the first command line argument, or, if there
is no argument, on port 8080.</p>

<p><code>middleware</code> is a list of WSGI middleware which is applied to the resulting WSGI
function.</p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> wsgifunc(self, *middleware)</code><br />
<div style="margin-left:75px"><p>Returns a WSGI-compatible function for this application.</p></div></p>
</div>
</div>
<div style="margin-left:30px">
<p><span class="ts">class</span><code class="class"> auto_application(self)</code><br />
<div style="margin-left:45px"><p>Application similar to <code>application</code> but urls are constructed 
automatiacally using metaclass.</p>

<pre><code>&gt;&gt;&gt; app = auto_application()
&gt;&gt;&gt; class hello(app.page):
...     def GET(self): return "hello, world"
...
&gt;&gt;&gt; class foo(app.page):
...     path = '/foo/.*'
...     def GET(self): return "foo"
&gt;&gt;&gt; app.request("/hello").data
'hello, world'
&gt;&gt;&gt; app.request('/foo/bar').data
'foo'
</code></pre></div></p>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> add_mapping(self, pattern, classname)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> add_processor(self, processor)</code><br />
<div style="margin-left:75px"><p>Adds a processor to the application.</p>

<pre><code>&gt;&gt;&gt; urls = ("/(.*)", "echo")
&gt;&gt;&gt; app = application(urls, globals())
&gt;&gt;&gt; class echo:
...     def GET(self, name): return name
...
&gt;&gt;&gt;
&gt;&gt;&gt; def hello(handler): return "hello, " +  handler()
...
&gt;&gt;&gt; app.add_processor(hello)
&gt;&gt;&gt; app.request("/web.py").data
'hello, web.py'
</code></pre></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> browser(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> cgirun(self, *middleware)</code><br />
<div style="margin-left:75px"><p>Return a CGI handler. This is mostly useful with Google App Engine.
There you can just do:</p>

<pre><code>main = app.cgirun()
</code></pre></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> get_parent_app(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> handle(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> handle_with_processors(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> init_mapping(self, mapping)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> internalerror(self)</code><br />
<div style="margin-left:75px"><p>Returns HTTPError with '500 internal error' message</p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> load(self, env)</code><br />
<div style="margin-left:75px"><p>Initializes ctx using env.</p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> notfound(self)</code><br />
<div style="margin-left:75px"><p>Returns HTTPError with '404 not found' message</p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> request(self, localpart='/', method='GET', data=None, host='0.0.0.0:8080', headers=None, https=False, **kw)</code><br />
<div style="margin-left:75px"><p>Makes request to this application for the specified path and method.
Response will be a storage object with data, status and headers.</p>

<pre><code>&gt;&gt;&gt; urls = ("/hello", "hello")
&gt;&gt;&gt; app = application(urls, globals())
&gt;&gt;&gt; class hello:
...     def GET(self): 
...         web.header('Content-Type', 'text/plain')
...         return "hello"
...
&gt;&gt;&gt; response = app.request("/hello")
&gt;&gt;&gt; response.data
'hello'
&gt;&gt;&gt; response.status
'200 OK'
&gt;&gt;&gt; response.headers['Content-Type']
'text/plain'
</code></pre>

<p>To use https, use https=True.</p>

<pre><code>&gt;&gt;&gt; urls = ("/redirect", "redirect")
&gt;&gt;&gt; app = application(urls, globals())
&gt;&gt;&gt; class redirect:
...     def GET(self): raise web.seeother("/foo")
...
&gt;&gt;&gt; response = app.request("/redirect")
&gt;&gt;&gt; response.headers['Location']
'http://0.0.0.0:8080/foo'
&gt;&gt;&gt; response = app.request("/redirect", https=True)
&gt;&gt;&gt; response.headers['Location']
'https://0.0.0.0:8080/foo'
</code></pre>

<p>The headers argument specifies HTTP headers as a mapping object
such as a dict.</p>

<pre><code>&gt;&gt;&gt; urls = ('/ua', 'uaprinter')
&gt;&gt;&gt; class uaprinter:
...     def GET(self):
...         return 'your user-agent is ' + web.ctx.env['HTTP_USER_AGENT']
... 
&gt;&gt;&gt; app = application(urls, globals())
&gt;&gt;&gt; app.request('/ua', headers = {
...      'User-Agent': 'a small jumping bean/1.0 (compatible)'
... }).data
'your user-agent is a small jumping bean/1.0 (compatible)'
</code></pre></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> run(self, *middleware)</code><br />
<div style="margin-left:75px"><p>Starts handling requests. If called in a CGI or FastCGI context, it will follow
that protocol. If called from the command line, it will start an HTTP
server on the port named in the first command line argument, or, if there
is no argument, on port 8080.</p>

<p><code>middleware</code> is a list of WSGI middleware which is applied to the resulting WSGI
function.</p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> wsgifunc(self, *middleware)</code><br />
<div style="margin-left:75px"><p>Returns a WSGI-compatible function for this application.</p></div></p>
</div>
</div>
<div style="margin-left:30px">
<p><span class="ts">class</span><code class="class"> subdir_application(self, mapping=(), fvars={}, autoreload=None)</code><br />
<div style="margin-left:45px"><p>Application to delegate requests based on path.</p>

<pre><code>&gt;&gt;&gt; urls = ("/hello", "hello")
&gt;&gt;&gt; app = application(urls, globals())
&gt;&gt;&gt; class hello:
...     def GET(self): return "hello"
&gt;&gt;&gt;
&gt;&gt;&gt; app.request("/hello").data
'hello'
</code></pre></div></p>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> add_mapping(self, pattern, classname)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> add_processor(self, processor)</code><br />
<div style="margin-left:75px"><p>Adds a processor to the application.</p>

<pre><code>&gt;&gt;&gt; urls = ("/(.*)", "echo")
&gt;&gt;&gt; app = application(urls, globals())
&gt;&gt;&gt; class echo:
...     def GET(self, name): return name
...
&gt;&gt;&gt;
&gt;&gt;&gt; def hello(handler): return "hello, " +  handler()
...
&gt;&gt;&gt; app.add_processor(hello)
&gt;&gt;&gt; app.request("/web.py").data
'hello, web.py'
</code></pre></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> browser(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> cgirun(self, *middleware)</code><br />
<div style="margin-left:75px"><p>Return a CGI handler. This is mostly useful with Google App Engine.
There you can just do:</p>

<pre><code>main = app.cgirun()
</code></pre></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> get_parent_app(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> handle(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> handle_with_processors(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> init_mapping(self, mapping)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> internalerror(self)</code><br />
<div style="margin-left:75px"><p>Returns HTTPError with '500 internal error' message</p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> load(self, env)</code><br />
<div style="margin-left:75px"><p>Initializes ctx using env.</p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> notfound(self)</code><br />
<div style="margin-left:75px"><p>Returns HTTPError with '404 not found' message</p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> request(self, localpart='/', method='GET', data=None, host='0.0.0.0:8080', headers=None, https=False, **kw)</code><br />
<div style="margin-left:75px"><p>Makes request to this application for the specified path and method.
Response will be a storage object with data, status and headers.</p>

<pre><code>&gt;&gt;&gt; urls = ("/hello", "hello")
&gt;&gt;&gt; app = application(urls, globals())
&gt;&gt;&gt; class hello:
...     def GET(self): 
...         web.header('Content-Type', 'text/plain')
...         return "hello"
...
&gt;&gt;&gt; response = app.request("/hello")
&gt;&gt;&gt; response.data
'hello'
&gt;&gt;&gt; response.status
'200 OK'
&gt;&gt;&gt; response.headers['Content-Type']
'text/plain'
</code></pre>

<p>To use https, use https=True.</p>

<pre><code>&gt;&gt;&gt; urls = ("/redirect", "redirect")
&gt;&gt;&gt; app = application(urls, globals())
&gt;&gt;&gt; class redirect:
...     def GET(self): raise web.seeother("/foo")
...
&gt;&gt;&gt; response = app.request("/redirect")
&gt;&gt;&gt; response.headers['Location']
'http://0.0.0.0:8080/foo'
&gt;&gt;&gt; response = app.request("/redirect", https=True)
&gt;&gt;&gt; response.headers['Location']
'https://0.0.0.0:8080/foo'
</code></pre>

<p>The headers argument specifies HTTP headers as a mapping object
such as a dict.</p>

<pre><code>&gt;&gt;&gt; urls = ('/ua', 'uaprinter')
&gt;&gt;&gt; class uaprinter:
...     def GET(self):
...         return 'your user-agent is ' + web.ctx.env['HTTP_USER_AGENT']
... 
&gt;&gt;&gt; app = application(urls, globals())
&gt;&gt;&gt; app.request('/ua', headers = {
...      'User-Agent': 'a small jumping bean/1.0 (compatible)'
... }).data
'your user-agent is a small jumping bean/1.0 (compatible)'
</code></pre></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> run(self, *middleware)</code><br />
<div style="margin-left:75px"><p>Starts handling requests. If called in a CGI or FastCGI context, it will follow
that protocol. If called from the command line, it will start an HTTP
server on the port named in the first command line argument, or, if there
is no argument, on port 8080.</p>

<p><code>middleware</code> is a list of WSGI middleware which is applied to the resulting WSGI
function.</p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> wsgifunc(self, *middleware)</code><br />
<div style="margin-left:75px"><p>Returns a WSGI-compatible function for this application.</p></div></p>
</div>
</div>
<div style="margin-left:30px">
<p><span class="ts">class</span><code class="class"> subdomain_application(self, mapping=(), fvars={}, autoreload=None)</code><br />
<div style="margin-left:45px"><p>Application to delegate requests based on the host.</p>

<pre><code>&gt;&gt;&gt; urls = ("/hello", "hello")
&gt;&gt;&gt; app = application(urls, globals())
&gt;&gt;&gt; class hello:
...     def GET(self): return "hello"
&gt;&gt;&gt;
&gt;&gt;&gt; mapping = (r"hello\.example\.com", app)
&gt;&gt;&gt; app2 = subdomain_application(mapping)
&gt;&gt;&gt; app2.request("/hello", host="hello.example.com").data
'hello'
&gt;&gt;&gt; response = app2.request("/hello", host="something.example.com")
&gt;&gt;&gt; response.status
'404 Not Found'
&gt;&gt;&gt; response.data
'not found'
</code></pre></div></p>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> add_mapping(self, pattern, classname)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> add_processor(self, processor)</code><br />
<div style="margin-left:75px"><p>Adds a processor to the application.</p>

<pre><code>&gt;&gt;&gt; urls = ("/(.*)", "echo")
&gt;&gt;&gt; app = application(urls, globals())
&gt;&gt;&gt; class echo:
...     def GET(self, name): return name
...
&gt;&gt;&gt;
&gt;&gt;&gt; def hello(handler): return "hello, " +  handler()
...
&gt;&gt;&gt; app.add_processor(hello)
&gt;&gt;&gt; app.request("/web.py").data
'hello, web.py'
</code></pre></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> browser(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> cgirun(self, *middleware)</code><br />
<div style="margin-left:75px"><p>Return a CGI handler. This is mostly useful with Google App Engine.
There you can just do:</p>

<pre><code>main = app.cgirun()
</code></pre></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> get_parent_app(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> handle(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> handle_with_processors(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> init_mapping(self, mapping)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> internalerror(self)</code><br />
<div style="margin-left:75px"><p>Returns HTTPError with '500 internal error' message</p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> load(self, env)</code><br />
<div style="margin-left:75px"><p>Initializes ctx using env.</p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> notfound(self)</code><br />
<div style="margin-left:75px"><p>Returns HTTPError with '404 not found' message</p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> request(self, localpart='/', method='GET', data=None, host='0.0.0.0:8080', headers=None, https=False, **kw)</code><br />
<div style="margin-left:75px"><p>Makes request to this application for the specified path and method.
Response will be a storage object with data, status and headers.</p>

<pre><code>&gt;&gt;&gt; urls = ("/hello", "hello")
&gt;&gt;&gt; app = application(urls, globals())
&gt;&gt;&gt; class hello:
...     def GET(self): 
...         web.header('Content-Type', 'text/plain')
...         return "hello"
...
&gt;&gt;&gt; response = app.request("/hello")
&gt;&gt;&gt; response.data
'hello'
&gt;&gt;&gt; response.status
'200 OK'
&gt;&gt;&gt; response.headers['Content-Type']
'text/plain'
</code></pre>

<p>To use https, use https=True.</p>

<pre><code>&gt;&gt;&gt; urls = ("/redirect", "redirect")
&gt;&gt;&gt; app = application(urls, globals())
&gt;&gt;&gt; class redirect:
...     def GET(self): raise web.seeother("/foo")
...
&gt;&gt;&gt; response = app.request("/redirect")
&gt;&gt;&gt; response.headers['Location']
'http://0.0.0.0:8080/foo'
&gt;&gt;&gt; response = app.request("/redirect", https=True)
&gt;&gt;&gt; response.headers['Location']
'https://0.0.0.0:8080/foo'
</code></pre>

<p>The headers argument specifies HTTP headers as a mapping object
such as a dict.</p>

<pre><code>&gt;&gt;&gt; urls = ('/ua', 'uaprinter')
&gt;&gt;&gt; class uaprinter:
...     def GET(self):
...         return 'your user-agent is ' + web.ctx.env['HTTP_USER_AGENT']
... 
&gt;&gt;&gt; app = application(urls, globals())
&gt;&gt;&gt; app.request('/ua', headers = {
...      'User-Agent': 'a small jumping bean/1.0 (compatible)'
... }).data
'your user-agent is a small jumping bean/1.0 (compatible)'
</code></pre></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> run(self, *middleware)</code><br />
<div style="margin-left:75px"><p>Starts handling requests. If called in a CGI or FastCGI context, it will follow
that protocol. If called from the command line, it will start an HTTP
server on the port named in the first command line argument, or, if there
is no argument, on port 8080.</p>

<p><code>middleware</code> is a list of WSGI middleware which is applied to the resulting WSGI
function.</p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> wsgifunc(self, *middleware)</code><br />
<div style="margin-left:75px"><p>Returns a WSGI-compatible function for this application.</p></div></p>
</div>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> loadhook(h)</code><br />
<div style="margin-left:45px"><p>Converts a load hook into an application processor.</p>

<pre><code>&gt;&gt;&gt; app = auto_application()
&gt;&gt;&gt; def f(): "something done before handling request"
...
&gt;&gt;&gt; app.add_processor(loadhook(f))
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> unloadhook(h)</code><br />
<div style="margin-left:45px"><p>Converts an unload hook into an application processor.</p>

<pre><code>&gt;&gt;&gt; app = auto_application()
&gt;&gt;&gt; def f(): "something done after handling request"
...
&gt;&gt;&gt; app.add_processor(unloadhook(f))
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> autodelegate(prefix='')</code><br />
<div style="margin-left:45px"><p>Returns a method that takes one argument and calls the method named prefix+arg,
calling <code>notfound()</code> if there isn't one. Example:</p>

<pre><code>urls = ('/prefs/(.*)', 'prefs')

class prefs:
    GET = autodelegate('GET_')
    def GET_password(self): pass
    def GET_privacy(self): pass
</code></pre>

<p><code>GET_password</code> would get called for <code>/prefs/password</code> while <code>GET_privacy</code> for 
<code>GET_privacy</code> gets called for <code>/prefs/privacy</code>.</p>

<p>If a user visits <code>/prefs/password/change</code> then <code>GET_password(self, '/change')</code>
is called.</p></div></p>
</div>
<p><span class="ts">module</span><code class="module"> <a name="web.contrib.template">web.contrib.template</a></code><br />
<div style="margin-left:15px"><p>Interface to various templating engines.</p></div></p>
<div style="margin-left:30px">
<p><span class="ts">class</span><code class="class"> render_cheetah(self, path)</code><br />
<div style="margin-left:45px"><p>Rendering interface to Cheetah Templates.</p>

<p>Example:</p>

<pre><code>render = render_cheetah('templates')
render.hello(name="cheetah")
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">class</span><code class="class"> render_genshi(self, *a, **kwargs)</code><br />
<div style="margin-left:45px"><p>Rendering interface genshi templates.
Example:</p>

<p>for xml/html templates.</p>

<pre><code>render = render_genshi(['templates/'])
render.hello(name='genshi')
</code></pre>

<p>For text templates:</p>

<pre><code>render = render_genshi(['templates/'], type='text')
render.hello(name='genshi')
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">class</span><code class="class"> render_mako(self, *a, **kwargs)</code><br />
<div style="margin-left:45px"><p>Rendering interface to Mako Templates.</p>

<p>Example:</p>

<pre><code>render = render_mako(directories=['templates'])
render.hello(name="mako")
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">class</span><code class="class"> cache(self, render)</code><br />
<div style="margin-left:45px"><p>Cache for any rendering interface.</p>

<p>Example:</p>

<pre><code>render = cache(render_cheetah("templates/"))
render.hello(name='cache')
</code></pre></div></p>
</div>
<p><span class="ts">module</span><code class="module"> <a name="web.db">web.db</a></code><br />
<div style="margin-left:15px"><p>Database API
(part of web.py)</p></div></p>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> UnknownParamstyle</code><br />
<div style="margin-left:45px"><p>raised for unsupported db paramstyles</p>

<p>(currently supported: qmark, numeric, format, pyformat)</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> UnknownDB</code><br />
<div style="margin-left:45px"><p>raised for unsupported dbms</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> TransactionError</code><br />
<div style="margin-left:45px"><p></p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> sqllist(lst)</code><br />
<div style="margin-left:45px"><p>Converts the arguments for use in something like a WHERE clause.</p>

<pre><code>&gt;&gt;&gt; sqllist(['a', 'b'])
'a, b'
&gt;&gt;&gt; sqllist('a')
'a'
&gt;&gt;&gt; sqllist(u'abc')
u'abc'
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> sqlors(left, lst)</code><br />
<div style="margin-left:45px"><p><code>left is a SQL clause like</code>tablename.arg = ` 
and <code>lst</code> is a list of values. Returns a reparam-style
pair featuring the SQL that ORs together the clause
for each item in the lst.</p>

<pre><code>&gt;&gt;&gt; sqlors('foo = ', [])
&lt;sql: '1=2'&gt;
&gt;&gt;&gt; sqlors('foo = ', [1])
&lt;sql: 'foo = 1'&gt;
&gt;&gt;&gt; sqlors('foo = ', 1)
&lt;sql: 'foo = 1'&gt;
&gt;&gt;&gt; sqlors('foo = ', [1,2,3])
&lt;sql: '(foo = 1 OR foo = 2 OR foo = 3 OR 1=2)'&gt;
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> reparam(string_, dictionary)</code><br />
<div style="margin-left:45px"><p>Takes a string and a dictionary and interpolates the string
using values from the dictionary. Returns an <code>SQLQuery</code> for the result.</p>

<pre><code>&gt;&gt;&gt; reparam("s = $s", dict(s=True))
&lt;sql: "s = 't'"&gt;
&gt;&gt;&gt; reparam("s IN $s", dict(s=[1, 2]))
&lt;sql: 's IN (1, 2)'&gt;
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> sqlquote(a)</code><br />
<div style="margin-left:45px"><p>Ensures <code>a</code> is quoted properly for use in a SQL query.</p>

<pre><code>&gt;&gt;&gt; 'WHERE x = ' + sqlquote(True) + ' AND y = ' + sqlquote(3)
&lt;sql: "WHERE x = 't' AND y = 3"&gt;
&gt;&gt;&gt; 'WHERE x = ' + sqlquote(True) + ' AND y IN ' + sqlquote([2, 3])
&lt;sql: "WHERE x = 't' AND y IN (2, 3)"&gt;
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> SQLQuery(self, items=None)</code><br />
<div style="margin-left:45px"><p>You can pass this sort of thing as a clause in any db function.
Otherwise, you can pass a dictionary to the keyword argument <code>vars</code>
and the function will call reparam for you.</p>

<p>Internally, consists of <code>items</code>, which is a list of strings and
SQLParams, which get concatenated to produce the actual query.</p></div></p>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> append(self, value)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">function</span><code class="function"> join(items, sep=' ', prefix=None, suffix=None, target=None)</code><br />
<div style="margin-left:75px"><p>Joins multiple queries.</p>

<blockquote>
  <blockquote>
    <blockquote>
      <p>SQLQuery.join(['a', 'b'], ', ')
      <sql: 'a, b'></p>
    </blockquote>
  </blockquote>
</blockquote>

<p>Optinally, prefix and suffix arguments can be provided.</p>

<blockquote>
  <blockquote>
    <blockquote>
      <p>SQLQuery.join(['a', 'b'], ', ', prefix='(', suffix=')')
      <sql: '(a, b)'></p>
    </blockquote>
  </blockquote>
</blockquote>

<p>If target argument is provided, the items are appended to target instead of creating a new SQLQuery.</p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> query(self, paramstyle=None)</code><br />
<div style="margin-left:75px"><p>Returns the query part of the sql query.</p>

<blockquote>
  <blockquote>
    <blockquote>
      <p>q = SQLQuery(["SELECT * FROM test WHERE name=", SQLParam('joe')])
      q.query()
          'SELECT * FROM test WHERE name=%s'
      q.query(paramstyle='qmark')
          'SELECT * FROM test WHERE name=?'</p>
    </blockquote>
  </blockquote>
</blockquote></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> values(self)</code><br />
<div style="margin-left:75px"><p>Returns the values of the parameters used in the sql query.</p>

<blockquote>
  <blockquote>
    <blockquote>
      <p>q = SQLQuery(["SELECT * FROM test WHERE name=", SQLParam('joe')])
      q.values()
          ['joe']</p>
    </blockquote>
  </blockquote>
</blockquote></div></p>
</div>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> SQLParam(self, value)</code><br />
<div style="margin-left:45px"><p>Parameter in SQLQuery.</p>

<pre><code>&gt;&gt;&gt; q = SQLQuery(["SELECT * FROM test WHERE name=", SQLParam("joe")])
&gt;&gt;&gt; q
&lt;sql: "SELECT * FROM test WHERE name='joe'"&gt;
&gt;&gt;&gt; q.query()
'SELECT * FROM test WHERE name=%s'
&gt;&gt;&gt; q.values()
['joe']
</code></pre></div></p>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> get_marker(self, paramstyle='pyformat')</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> sqlquery(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> sqlparam(self, value)</code><br />
<div style="margin-left:45px"><p>Parameter in SQLQuery.</p>

<pre><code>&gt;&gt;&gt; q = SQLQuery(["SELECT * FROM test WHERE name=", SQLParam("joe")])
&gt;&gt;&gt; q
&lt;sql: "SELECT * FROM test WHERE name='joe'"&gt;
&gt;&gt;&gt; q.query()
'SELECT * FROM test WHERE name=%s'
&gt;&gt;&gt; q.values()
['joe']
</code></pre></div></p>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> get_marker(self, paramstyle='pyformat')</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> sqlquery(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
</div>
<div style="margin-left:30px">
<p><span class="ts">class</span><code class="class"> SQLLiteral(self, v)</code><br />
<div style="margin-left:45px"><p>Protects a string from <code>sqlquote</code>.</p>

<pre><code>&gt;&gt;&gt; sqlquote('NOW()')
&lt;sql: "'NOW()'"&gt;
&gt;&gt;&gt; sqlquote(SQLLiteral('NOW()'))
&lt;sql: 'NOW()'&gt;
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">class</span><code class="class"> sqlliteral(self, v)</code><br />
<div style="margin-left:45px"><p>Protects a string from <code>sqlquote</code>.</p>

<pre><code>&gt;&gt;&gt; sqlquote('NOW()')
&lt;sql: "'NOW()'"&gt;
&gt;&gt;&gt; sqlquote(SQLLiteral('NOW()'))
&lt;sql: 'NOW()'&gt;
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> database(dburl=None, **params)</code><br />
<div style="margin-left:45px"><p>Creates appropriate database using params.</p>

<p>Pooling will be enabled if DBUtils module is available. 
Pooling can be disabled by passing pooling=False in params.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">class</span><code class="class"> DB(self, db_module, keywords)</code><br />
<div style="margin-left:45px"><p>Database</p></div></p>
<div style="margin-left:60px">
<p><span class="ts">property</span><code class="property"> ctx</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> delete(self, table, where, using=None, vars=None, _test=False)</code><br />
<div style="margin-left:75px"><p>Deletes from <code>table</code> with clauses <code>where</code> and <code>using</code>.</p>

<pre><code>&gt;&gt;&gt; db = DB(None, {})
&gt;&gt;&gt; name = 'Joe'
&gt;&gt;&gt; db.delete('foo', where='name = $name', vars=locals(), _test=True)
&lt;sql: "DELETE FROM foo WHERE name = 'Joe'"&gt;
</code></pre></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> gen_clause(self, sql, val, vars)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> insert(self, tablename, seqname=None, _test=False, **values)</code><br />
<div style="margin-left:75px"><p>Inserts <code>values</code> into <code>tablename</code>. Returns current sequence ID.
Set <code>seqname</code> to the ID if it's not the default, or to <code>False</code>
if there isn't one.</p>

<pre><code>&gt;&gt;&gt; db = DB(None, {})
&gt;&gt;&gt; q = db.insert('foo', name='bob', age=2, created=SQLLiteral('NOW()'), _test=True)
&gt;&gt;&gt; q
&lt;sql: "INSERT INTO foo (age, name, created) VALUES (2, 'bob', NOW())"&gt;
&gt;&gt;&gt; q.query()
'INSERT INTO foo (age, name, created) VALUES (%s, %s, NOW())'
&gt;&gt;&gt; q.values()
[2, 'bob']
</code></pre></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> multiple_insert(self, tablename, values, seqname=None, _test=False)</code><br />
<div style="margin-left:75px"><p>Inserts multiple rows into <code>tablename</code>. The <code>values</code> must be a list of dictioanries, 
one for each row to be inserted, each with the same set of keys.
Returns the list of ids of the inserted rows. <br />
Set <code>seqname</code> to the ID if it's not the default, or to <code>False</code>
if there isn't one.</p>

<pre><code>&gt;&gt;&gt; db = DB(None, {})
&gt;&gt;&gt; db.supports_multiple_insert = True
&gt;&gt;&gt; values = [{"name": "foo", "email": "foo@example.com"}, {"name": "bar", "email": "bar@example.com"}]
&gt;&gt;&gt; db.multiple_insert('person', values=values, _test=True)
&lt;sql: "INSERT INTO person (name, email) VALUES ('foo', 'foo@example.com'), ('bar', 'bar@example.com')"&gt;
</code></pre></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> query(self, sql_query, vars=None, processed=False, _test=False)</code><br />
<div style="margin-left:75px"><p>Execute SQL query <code>sql_query</code> using dictionary <code>vars</code> to interpolate it.
If <code>processed=True</code>, <code>vars</code> is a <code>reparam</code>-style list to use 
instead of interpolating.</p>

<pre><code>&gt;&gt;&gt; db = DB(None, {})
&gt;&gt;&gt; db.query("SELECT * FROM foo", _test=True)
&lt;sql: 'SELECT * FROM foo'&gt;
&gt;&gt;&gt; db.query("SELECT * FROM foo WHERE x = $x", vars=dict(x='f'), _test=True)
&lt;sql: "SELECT * FROM foo WHERE x = 'f'"&gt;
&gt;&gt;&gt; db.query("SELECT * FROM foo WHERE x = " + sqlquote('f'), _test=True)
&lt;sql: "SELECT * FROM foo WHERE x = 'f'"&gt;
</code></pre></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> select(self, tables, vars=None, what='*', where=None, order=None, group=None, limit=None, offset=None, _test=False)</code><br />
<div style="margin-left:75px"><p>Selects <code>what</code> from <code>tables</code> with clauses <code>where</code>, <code>order</code>, 
<code>group</code>, <code>limit</code>, and <code>offset</code>. Uses vars to interpolate. 
Otherwise, each clause can be a SQLQuery.</p>

<pre><code>&gt;&gt;&gt; db = DB(None, {})
&gt;&gt;&gt; db.select('foo', _test=True)
&lt;sql: 'SELECT * FROM foo'&gt;
&gt;&gt;&gt; db.select(['foo', 'bar'], where="foo.bar_id = bar.id", limit=5, _test=True)
&lt;sql: 'SELECT * FROM foo, bar WHERE foo.bar_id = bar.id LIMIT 5'&gt;
</code></pre></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> sql_clauses(self, what, tables, where, group, order, limit, offset)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> transaction(self)</code><br />
<div style="margin-left:75px"><p>Start a transaction.</p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> update(self, tables, where, vars=None, _test=False, **values)</code><br />
<div style="margin-left:75px"><p>Update <code>tables</code> with clause <code>where</code> (interpolated using <code>vars</code>)
and setting <code>values</code>.</p>

<pre><code>&gt;&gt;&gt; db = DB(None, {})
&gt;&gt;&gt; name = 'Joseph'
&gt;&gt;&gt; q = db.update('foo', where='name = $name', name='bob', age=2,
...     created=SQLLiteral('NOW()'), vars=locals(), _test=True)
&gt;&gt;&gt; q
&lt;sql: "UPDATE foo SET age = 2, name = 'bob', created = NOW() WHERE name = 'Joseph'"&gt;
&gt;&gt;&gt; q.query()
'UPDATE foo SET age = %s, name = %s, created = NOW() WHERE name = %s'
&gt;&gt;&gt; q.values()
[2, 'bob', 'Joseph']
</code></pre></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> where(self, table, what='*', order=None, group=None, limit=None, offset=None, _test=False, **kwargs)</code><br />
<div style="margin-left:75px"><p>Selects from <code>table</code> where keys are equal to values in <code>kwargs</code>.</p>

<pre><code>&gt;&gt;&gt; db = DB(None, {})
&gt;&gt;&gt; db.where('foo', bar_id=3, _test=True)
&lt;sql: 'SELECT * FROM foo WHERE bar_id = 3'&gt;
&gt;&gt;&gt; db.where('foo', source=2, crust='dewey', _test=True)
&lt;sql: "SELECT * FROM foo WHERE source = 2 AND crust = 'dewey'"&gt;
&gt;&gt;&gt; db.where('foo', _test=True)
&lt;sql: 'SELECT * FROM foo'&gt;
</code></pre></div></p>
</div>
</div>
<p><span class="ts">module</span><code class="module"> <a name="web.debugerror">web.debugerror</a></code><br />
<div style="margin-left:15px"><p>pretty debug errors
(part of web.py)</p>

<p>portions adapted from Django <djangoproject.com> 
Copyright (c) 2005, the Lawrence Journal-World
Used under the modified BSD license:
http://www.xfree86.org/3.3.6/COPYRIGHT2.html#5</p></div></p>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> debugerror()</code><br />
<div style="margin-left:45px"><p>A replacement for <code>internalerror</code> that presents a nice page with lots
of debug information for the programmer.</p>

<p>(Based on the beautiful 500 page from <a href="http://djangoproject.com/">Django</a>, 
designed by <a href="http://wilsonminer.com/">Wilson Miner</a>.)</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> djangoerror()</code><br />
<div style="margin-left:45px"><p></p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> emailerrors(to_address, olderror, from_address=None)</code><br />
<div style="margin-left:45px"><p>Wraps the old <code>internalerror</code> handler (pass as <code>olderror</code>) to 
additionally email all errors to <code>to_address</code>, to aid in
debugging production websites.</p>

<p>Emails contain a normal text traceback as well as an
attachment containing the nice <code>debugerror</code> page.</p></div></p>
</div>
<p><span class="ts">module</span><code class="module"> <a name="web.form">web.form</a></code><br />
<div style="margin-left:15px"><p>HTML forms
(part of web.py)</p></div></p>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> AttributeList</code><br />
<div style="margin-left:45px"><p>List of atributes of input.</p>

<blockquote>
  <blockquote>
    <blockquote>
      <p>a = AttributeList(type='text', name='x', value=20)
      a
      <attrs: 'type="text" name="x" value="20"'></p>
    </blockquote>
  </blockquote>
</blockquote></div></p>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> copy(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> Button(self, name, *validators, **attrs)</code><br />
<div style="margin-left:45px"><p>HTML Button.</p>

<blockquote>
  <blockquote>
    <blockquote>
      <p>Button("save").render()
      '<button id="save" name="save">save</button>'
      Button("action", value="save", html="<b>Save Changes</b>").render()
      '<button id="action" value="save" name="action"><b>Save Changes</b></button>'</p>
    </blockquote>
  </blockquote>
</blockquote></div></p>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> addatts(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> get_default_id(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> get_type(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> get_value(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> is_hidden(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> render(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> rendernote(self, note)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> set_value(self, value)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> validate(self, value)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> Checkbox(self, name, *validators, **attrs)</code><br />
<div style="margin-left:45px"><p>Checkbox input.</p>

<blockquote>
  <blockquote>
    <blockquote>
      <p>Checkbox('foo', value='bar', checked=True).render()
      '<input checked="checked" type="checkbox" id="foo_bar" value="bar" name="foo"/>'
      Checkbox('foo', value='bar').render()
      '<input type="checkbox" id="foo_bar" value="bar" name="foo"/>'
      c = Checkbox('foo', value='bar')
      c.validate('on')
      True
      c.render()
      '<input checked="checked" type="checkbox" id="foo_bar" value="bar" name="foo"/>'</p>
    </blockquote>
  </blockquote>
</blockquote></div></p>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> addatts(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> get_default_id(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> get_type(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> get_value(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> is_hidden(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> render(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> rendernote(self, note)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> set_value(self, value)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> validate(self, value)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> Dropdown(self, name, args, *validators, **attrs)</code><br />
<div style="margin-left:45px"><p>Dropdown/select input.</p>

<blockquote>
  <blockquote>
    <blockquote>
      <p>Dropdown(name='foo', args=['a', 'b', 'c'], value='b').render()
      '<select id="foo" name="foo">\n  <option value="a">a</option>\n  <option selected="selected" value="b">b</option>\n  <option value="c">c</option>\n</select>\n'
      Dropdown(name='foo', args=[('a', 'aa'), ('b', 'bb'), ('c', 'cc')], value='b').render()
      '<select id="foo" name="foo">\n  <option value="a">aa</option>\n  <option selected="selected" value="b">bb</option>\n  <option value="c">cc</option>\n</select>\n'</p>
    </blockquote>
  </blockquote>
</blockquote></div></p>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> addatts(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> get_default_id(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> get_type(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> get_value(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> is_hidden(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> render(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> rendernote(self, note)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> set_value(self, value)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> validate(self, value)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> File(self, name, *validators, **attrs)</code><br />
<div style="margin-left:45px"><p>File input.</p>

<blockquote>
  <blockquote>
    <blockquote>
      <p>File(name='f').render()
      '<input type="file" id="f" name="f"/>'</p>
    </blockquote>
  </blockquote>
</blockquote></div></p>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> addatts(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> get_default_id(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> get_type(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> get_value(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> is_hidden(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> render(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> rendernote(self, note)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> set_value(self, value)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> validate(self, value)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> Form(self, *inputs, **kw)</code><br />
<div style="margin-left:45px"><p>HTML form.</p>

<pre><code>&gt;&gt;&gt; f = Form(Textbox("x"))
&gt;&gt;&gt; f.render()
'&lt;table&gt;\n    &lt;tr&gt;&lt;th&gt;&lt;label for="x"&gt;x&lt;/label&gt;&lt;/th&gt;&lt;td&gt;&lt;input type="text" id="x" name="x"/&gt;&lt;/td&gt;&lt;/tr&gt;\n&lt;/table&gt;'
</code></pre></div></p>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> fill(self, source=None, **kw)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> get(self, i, default=None)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> render(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> render_css(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> rendernote(self, note)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> validates(self, source=None, _validate=True, **kw)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> Hidden(self, name, *validators, **attrs)</code><br />
<div style="margin-left:45px"><p>Hidden Input.</p>

<blockquote>
  <blockquote>
    <blockquote>
      <p>Hidden(name='foo', value='bar').render()
      '<input type="hidden" id="foo" value="bar" name="foo"/>'</p>
    </blockquote>
  </blockquote>
</blockquote></div></p>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> addatts(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> get_default_id(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> get_type(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> get_value(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> is_hidden(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> render(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> rendernote(self, note)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> set_value(self, value)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> validate(self, value)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> Input(self, name, *validators, **attrs)</code><br />
<div style="margin-left:45px"><p></p></div></p>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> addatts(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> get_default_id(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> get_type(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> get_value(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> is_hidden(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> render(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> rendernote(self, note)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> set_value(self, value)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> validate(self, value)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> Password(self, name, *validators, **attrs)</code><br />
<div style="margin-left:45px"><p>Password input.</p>

<blockquote>
  <blockquote>
    <blockquote>
      <p>Password(name='password', value='secret').render()
      '<input type="password" id="password" value="secret" name="password"/>'</p>
    </blockquote>
  </blockquote>
</blockquote></div></p>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> addatts(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> get_default_id(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> get_type(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> get_value(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> is_hidden(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> render(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> rendernote(self, note)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> set_value(self, value)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> validate(self, value)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> Radio(self, name, args, *validators, **attrs)</code><br />
<div style="margin-left:45px"><p></p></div></p>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> addatts(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> get_default_id(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> get_type(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> get_value(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> is_hidden(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> render(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> rendernote(self, note)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> set_value(self, value)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> validate(self, value)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> Textarea(self, name, *validators, **attrs)</code><br />
<div style="margin-left:45px"><p>Textarea input.</p>

<blockquote>
  <blockquote>
    <blockquote>
      <p>Textarea(name='foo', value='bar').render()
      '<textarea id="foo" name="foo">bar</textarea>'</p>
    </blockquote>
  </blockquote>
</blockquote></div></p>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> addatts(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> get_default_id(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> get_type(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> get_value(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> is_hidden(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> render(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> rendernote(self, note)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> set_value(self, value)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> validate(self, value)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> Textbox(self, name, *validators, **attrs)</code><br />
<div style="margin-left:45px"><p>Textbox input.</p>

<blockquote>
  <blockquote>
    <blockquote>
      <p>Textbox(name='foo', value='bar').render()
      '<input type="text" id="foo" value="bar" name="foo"/>'
      Textbox(name='foo', value=0).render()
      '<input type="text" id="foo" value="0" name="foo"/>'</p>
    </blockquote>
  </blockquote>
</blockquote></div></p>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> addatts(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> get_default_id(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> get_type(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> get_value(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> is_hidden(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> render(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> rendernote(self, note)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> set_value(self, value)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> validate(self, value)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
</div>
<div style="margin-left:30px">
<p><span class="ts">class</span><code class="class"> Validator(self, msg, test, jstest=None)</code><br />
<div style="margin-left:45px"><p></p></div></p>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> valid(self, value)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> attrget(obj, attr, value=None)</code><br />
<div style="margin-left:45px"><p></p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">class</span><code class="class"> regexp(self, rexp, msg)</code><br />
<div style="margin-left:45px"><p></p></div></p>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> valid(self, value)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
</div>
<p><span class="ts">module</span><code class="module"> <a name="web.http">web.http</a></code><br />
<div style="margin-left:15px"><p>HTTP Utilities
(from web.py)</p></div></p>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> expires(delta)</code><br />
<div style="margin-left:45px"><p>Outputs an <code>Expires</code> header for <code>delta</code> from now. 
<code>delta</code> is a <code>timedelta</code> object or a number of seconds.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> lastmodified(date_obj)</code><br />
<div style="margin-left:45px"><p>Outputs a <code>Last-Modified</code> header for <code>datetime</code>.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> prefixurl(base='')</code><br />
<div style="margin-left:45px"><p>Sorry, this function is really difficult to explain.
Maybe some other time.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> modified(date=None, etag=None)</code><br />
<div style="margin-left:45px"><p>Checks to see if the page has been modified since the version in the
requester's cache.</p>

<p>When you publish pages, you can include <code>Last-Modified</code> and <code>ETag</code>
with the date the page was last modified and an opaque token for
the particular version, respectively. When readers reload the page, 
the browser sends along the modification date and etag value for
the version it has in its cache. If the page hasn't changed, 
the server can just return <code>304 Not Modified</code> and not have to 
send the whole page again.</p>

<p>This function takes the last-modified date <code>date</code> and the ETag <code>etag</code>
and checks the headers to see if they match. If they do, it returns 
<code>True</code>, or otherwise it raises NotModified error. It also sets 
<code>Last-Modified</code> and <code>ETag</code> output headers.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> changequery(query=None, **kw)</code><br />
<div style="margin-left:45px"><p>Imagine you're at <code>/foo?a=1&amp;b=2</code>. Then <code>changequery(a=3)</code> will return
<code>/foo?a=3&amp;b=2</code> -- the same URL but with the arguments you requested
changed.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> url(path=None, doseq=False, **kw)</code><br />
<div style="margin-left:45px"><p>Makes url by concatinating web.ctx.homepath and path and the 
query string created using the arguments.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> profiler(app)</code><br />
<div style="margin-left:45px"><p>Outputs basic profiling information at the bottom of each response.</p></div></p>
</div>
<p><span class="ts">module</span><code class="module"> <a name="web.httpserver">web.httpserver</a></code><br />
<div style="margin-left:15px"><p></p></div></p>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> runsimple(func, server_address=('0.0.0.0', 8080))</code><br />
<div style="margin-left:45px"><p>Runs <a href="http://www.cherrypy.org">CherryPy</a> WSGI server hosting WSGI app <code>func</code>. 
The directory <code>static/</code> is hosted statically.</p></div></p>
</div>
<p><span class="ts">module</span><code class="module"> <a name="web.net">web.net</a></code><br />
<div style="margin-left:15px"><p>Network Utilities
(from web.py)</p></div></p>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> validipaddr(address)</code><br />
<div style="margin-left:45px"><p>Returns True if <code>address</code> is a valid IPv4 address.</p>

<pre><code>&gt;&gt;&gt; validipaddr('192.168.1.1')
True
&gt;&gt;&gt; validipaddr('192.168.1.800')
False
&gt;&gt;&gt; validipaddr('192.168.1')
False
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> validipport(port)</code><br />
<div style="margin-left:45px"><p>Returns True if <code>port</code> is a valid IPv4 port.</p>

<pre><code>&gt;&gt;&gt; validipport('9000')
True
&gt;&gt;&gt; validipport('foo')
False
&gt;&gt;&gt; validipport('1000000')
False
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> validip(ip, defaultaddr='0.0.0.0', defaultport=8080)</code><br />
<div style="margin-left:45px"><p>Returns <code>(ip_address, port)</code> from string <code>ip_addr_port</code></p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> validaddr(string_)</code><br />
<div style="margin-left:45px"><p>Returns either (ip<em>address, port) or "/path/to/socket" from string</em></p>

<pre><code>&gt;&gt;&gt; validaddr('/path/to/socket')
'/path/to/socket'
&gt;&gt;&gt; validaddr('8000')
('0.0.0.0', 8000)
&gt;&gt;&gt; validaddr('127.0.0.1')
('127.0.0.1', 8080)
&gt;&gt;&gt; validaddr('127.0.0.1:8000')
('127.0.0.1', 8000)
&gt;&gt;&gt; validaddr('fff')
Traceback (most recent call last):
    ...
ValueError: fff is not a valid IP address/port
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> urlquote(val)</code><br />
<div style="margin-left:45px"><p>Quotes a string for use in a URL.</p>

<pre><code>&gt;&gt;&gt; urlquote('://?f=1&amp;j=1')
'%3A//%3Ff%3D1%26j%3D1'
&gt;&gt;&gt; urlquote(None)
''
&gt;&gt;&gt; urlquote(u'\u203d')
'%E2%80%BD'
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> httpdate(date_obj)</code><br />
<div style="margin-left:45px"><p>Formats a datetime object for use in HTTP headers.</p>

<pre><code>&gt;&gt;&gt; import datetime
&gt;&gt;&gt; httpdate(datetime.datetime(1970, 1, 1, 1, 1, 1))
'Thu, 01 Jan 1970 01:01:01 GMT'
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> parsehttpdate(string_)</code><br />
<div style="margin-left:45px"><p>Parses an HTTP date into a datetime object.</p>

<pre><code>&gt;&gt;&gt; parsehttpdate('Thu, 01 Jan 1970 01:01:01 GMT')
datetime.datetime(1970, 1, 1, 1, 1, 1)
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> htmlquote(text)</code><br />
<div style="margin-left:45px"><p>Encodes <code>text</code> for raw use in HTML.</p>

<pre><code>&gt;&gt;&gt; htmlquote(u"&lt;'&amp;\"&gt;")
u'&amp;lt;&amp;#39;&amp;amp;&amp;quot;&amp;gt;'
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> htmlunquote(text)</code><br />
<div style="margin-left:45px"><p>Decodes <code>text</code> that's HTML quoted.</p>

<pre><code>&gt;&gt;&gt; htmlunquote(u'&amp;lt;&amp;#39;&amp;amp;&amp;quot;&amp;gt;')
u'&lt;\'&amp;"&gt;'
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> websafe(val)</code><br />
<div style="margin-left:45px"><p>Converts <code>val</code> so that it is safe for use in Unicode HTML.</p>

<blockquote>
  <blockquote>
    <blockquote>
      <p>websafe("&lt;'&amp;\">")
      u'&lt;&#39;&amp;&quot;&gt;'
      websafe(None)
      u''
      websafe(u'\u203d')
      u'\u203d'
      websafe('\xe2\x80\xbd')
      u'\u203d'</p>
    </blockquote>
  </blockquote>
</blockquote></div></p>
</div>
<p><span class="ts">module</span><code class="module"> <a name="web.session">web.session</a></code><br />
<div style="margin-left:15px"><p>Session Management
(from web.py)</p></div></p>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> Session(self, app, store, initializer=None)</code><br />
<div style="margin-left:45px"><p>Session management for web.py</p></div></p>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> expired(self)</code><br />
<div style="margin-left:75px"><p>Called when an expired session is atime</p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> kill(self)</code><br />
<div style="margin-left:75px"><p>Kill the session, make it no longer available</p></div></p>
</div>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> SessionExpired(self, message)</code><br />
<div style="margin-left:45px"><p></p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">class</span><code class="class"> Store(self)</code><br />
<div style="margin-left:45px"><p>Base class for session stores</p></div></p>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> cleanup(self, timeout)</code><br />
<div style="margin-left:75px"><p>removes all the expired sessions</p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> decode(self, session_data)</code><br />
<div style="margin-left:75px"><p>decodes the data to get back the session dict</p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> encode(self, session_dict)</code><br />
<div style="margin-left:75px"><p>encodes session dict as a string</p></div></p>
</div>
</div>
<div style="margin-left:30px">
<p><span class="ts">class</span><code class="class"> DiskStore(self, root)</code><br />
<div style="margin-left:45px"><p>Store for saving a session on disk.</p>

<pre><code>&gt;&gt;&gt; import tempfile
&gt;&gt;&gt; root = tempfile.mkdtemp()
&gt;&gt;&gt; s = DiskStore(root)
&gt;&gt;&gt; s['a'] = 'foo'
&gt;&gt;&gt; s['a']
'foo'
&gt;&gt;&gt; time.sleep(0.01)
&gt;&gt;&gt; s.cleanup(0.01)
&gt;&gt;&gt; s['a']
Traceback (most recent call last):
    ...
KeyError: 'a'
</code></pre></div></p>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> cleanup(self, timeout)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> decode(self, session_data)</code><br />
<div style="margin-left:75px"><p>decodes the data to get back the session dict</p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> encode(self, session_dict)</code><br />
<div style="margin-left:75px"><p>encodes session dict as a string</p></div></p>
</div>
</div>
<div style="margin-left:30px">
<p><span class="ts">class</span><code class="class"> DBStore(self, db, table_name)</code><br />
<div style="margin-left:45px"><p>Store for saving a session in database
Needs a table with the following columns:</p>

<pre><code>session_id CHAR(128) UNIQUE NOT NULL,
atime DATETIME NOT NULL default current_timestamp,
data TEXT
</code></pre></div></p>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> cleanup(self, timeout)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> decode(self, session_data)</code><br />
<div style="margin-left:75px"><p>decodes the data to get back the session dict</p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> encode(self, session_dict)</code><br />
<div style="margin-left:75px"><p>encodes session dict as a string</p></div></p>
</div>
</div>
<p><span class="ts">module</span><code class="module"> <a name="web.template">web.template</a></code><br />
<div style="margin-left:15px"><p>simple, elegant templating
(part of web.py)</p>

<p>Template design:</p>

<p>Template string is split into tokens and the tokens are combined into nodes. 
Parse tree is a nodelist. TextNode and ExpressionNode are simple nodes and 
for-loop, if-loop etc are block nodes, which contain multiple child nodes.</p>

<p>Each node can emit some python string. python string emitted by the 
root node is validated for safeeval and executed using python in the given environment.</p>

<p>Enough care is taken to make sure the generated code and the template has line to line match, 
so that the error messages can point to exact line number in template. (It doesn't work in some cases still.)</p>

<p>Grammar:</p>

<pre><code>template -&gt; defwith sections 
defwith -&gt; '$def with (' arguments ')' | ''
sections -&gt; section*
section -&gt; block | assignment | line

assignment -&gt; '$ ' &lt;assignment expression&gt;
line -&gt; (text|expr)*
text -&gt; &lt;any characters other than $&gt;
expr -&gt; '$' pyexpr | '$(' pyexpr ')' | '${' pyexpr '}'
pyexpr -&gt; &lt;python expression&gt;
</code></pre></div></p>
<div style="margin-left:30px">
<p><span class="ts">class</span><code class="class"> Template(self, text, filename='&lt;template&gt;', filter=None, globals=None, builtins=None, extensions=None)</code><br />
<div style="margin-left:45px"><p></p></div></p>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> compile_template(self, template_string, filename)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> create_parser(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">function</span><code class="function"> generate_code(text, filename, parser=None)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> make_env(self, globals, builtins)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">function</span><code class="function"> normalize_text(text)</code><br />
<div style="margin-left:75px"><p>Normalizes template text by correcting 
, tabs and BOM chars.</p></div></p>
</div>
</div>
<div style="margin-left:30px">
<p><span class="ts">class</span><code class="class"> Render(self, loc, *a, **kw)</code><br />
<div style="margin-left:45px"><p></p></div></p>
<div style="margin-left:60px">
<p><span class="ts">class</span><code class="class"> super(self, loc='templates', cache=None, base=None, **keywords)</code><br />
<div style="margin-left:75px"><p>The most preferred way of using templates.</p>

<pre><code>render = web.template.render('templates')
print render.foo()
</code></pre>

<p>Optional parameter can be <code>base</code> can be used to pass output of 
every template through the base template.</p>

<pre><code>render = web.template.render('templates', base='layout')
</code></pre></div></p>
</div>
</div>
<div style="margin-left:30px">
<p><span class="ts">class</span><code class="class"> render(self, loc, *a, **kw)</code><br />
<div style="margin-left:45px"><p></p></div></p>
<div style="margin-left:60px">
<p><span class="ts">class</span><code class="class"> super(self, loc='templates', cache=None, base=None, **keywords)</code><br />
<div style="margin-left:75px"><p>The most preferred way of using templates.</p>

<pre><code>render = web.template.render('templates')
print render.foo()
</code></pre>

<p>Optional parameter can be <code>base</code> can be used to pass output of 
every template through the base template.</p>

<pre><code>render = web.template.render('templates', base='layout')
</code></pre></div></p>
</div>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> frender(path, **keywords)</code><br />
<div style="margin-left:45px"><p>Creates a template from the given file path.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> ParseError</code><br />
<div style="margin-left:45px"><p></p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> SecurityError</code><br />
<div style="margin-left:45px"><p>The template seems to be trying to do something naughty.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> test()</code><br />
<div style="margin-left:45px"><p>Doctest for testing template module.</p>

<p>Define a utility function to run template test.</p>

<pre><code>&gt;&gt;&gt; class TestResult:
...     def __init__(self, t): self.t = t
...     def __getattr__(self, name): return getattr(self.t, name)
...     def __repr__(self): return repr(unicode(self))
...
&gt;&gt;&gt; def t(code, **keywords):
...     tmpl = Template(code, **keywords)
...     return lambda *a, **kw: TestResult(tmpl(*a, **kw))
...
</code></pre>

<p>Simple tests.</p>

<pre><code>&gt;&gt;&gt; t('1')()
u'1\n'
&gt;&gt;&gt; t('$def with ()\n1')()
u'1\n'
&gt;&gt;&gt; t('$def with (a)\n$a')(1)
u'1\n'
&gt;&gt;&gt; t('$def with (a=0)\n$a')(1)
u'1\n'
&gt;&gt;&gt; t('$def with (a=0)\n$a')(a=1)
u'1\n'
</code></pre>

<p>Test complicated expressions.</p>

<pre><code>&gt;&gt;&gt; t('$def with (x)\n$x.upper()')('hello')
u'HELLO\n'
&gt;&gt;&gt; t('$(2 * 3 + 4 * 5)')()
u'26\n'
&gt;&gt;&gt; t('${2 * 3 + 4 * 5}')()
u'26\n'
&gt;&gt;&gt; t('$def with (limit)\nkeep $(limit)ing.')('go')
u'keep going.\n'
&gt;&gt;&gt; t('$def with (a)\n$a.b[0]')(storage(b=[1]))
u'1\n'
</code></pre>

<p>Test html escaping.</p>

<pre><code>&gt;&gt;&gt; t('$def with (x)\n$x', filename='a.html')('&lt;html&gt;')
u'&amp;lt;html&amp;gt;\n'
&gt;&gt;&gt; t('$def with (x)\n$x', filename='a.txt')('&lt;html&gt;')
u'&lt;html&gt;\n'
</code></pre>

<p>Test if, for and while.</p>

<pre><code>&gt;&gt;&gt; t('$if 1: 1')()
u'1\n'
&gt;&gt;&gt; t('$if 1:\n    1')()
u'1\n'
&gt;&gt;&gt; t('$if 1:\n    1\\')()
u'1'
&gt;&gt;&gt; t('$if 0: 0\n$elif 1: 1')()
u'1\n'
&gt;&gt;&gt; t('$if 0: 0\n$elif None: 0\n$else: 1')()
u'1\n'
&gt;&gt;&gt; t('$if 0 &lt; 1 and 1 &lt; 2: 1')()
u'1\n'
&gt;&gt;&gt; t('$for x in [1, 2, 3]: $x')()
u'1\n2\n3\n'
&gt;&gt;&gt; t('$def with (d)\n$for k, v in d.iteritems(): $k')({1: 1})
u'1\n'
&gt;&gt;&gt; t('$for x in [1, 2, 3]:\n\t$x')()
u'    1\n    2\n    3\n'
&gt;&gt;&gt; t('$def with (a)\n$while a and a.pop():1')([1, 2, 3])
u'1\n1\n1\n'
</code></pre>

<p>The space after : must be ignored.</p>

<pre><code>&gt;&gt;&gt; t('$if True: foo')()
u'foo\n'
</code></pre>

<p>Test loop.xxx.</p>

<pre><code>&gt;&gt;&gt; t("$for i in range(5):$loop.index, $loop.parity")()
u'1, odd\n2, even\n3, odd\n4, even\n5, odd\n'
&gt;&gt;&gt; t("$for i in range(2):\n    $for j in range(2):$loop.parent.parity $loop.parity")()
u'odd odd\nodd even\neven odd\neven even\n'
</code></pre>

<p>Test assignment.</p>

<pre><code>&gt;&gt;&gt; t('$ a = 1\n$a')()
u'1\n'
&gt;&gt;&gt; t('$ a = [1]\n$a[0]')()
u'1\n'
&gt;&gt;&gt; t('$ a = {1: 1}\n$a.keys()[0]')()
u'1\n'
&gt;&gt;&gt; t('$ a = []\n$if not a: 1')()
u'1\n'
&gt;&gt;&gt; t('$ a = {}\n$if not a: 1')()
u'1\n'
&gt;&gt;&gt; t('$ a = -1\n$a')()
u'-1\n'
&gt;&gt;&gt; t('$ a = "1"\n$a')()
u'1\n'
</code></pre>

<p>Test comments.</p>

<pre><code>&gt;&gt;&gt; t('$# 0')()
u'\n'
&gt;&gt;&gt; t('hello$#comment1\nhello$#comment2')()
u'hello\nhello\n'
&gt;&gt;&gt; t('$#comment0\nhello$#comment1\nhello$#comment2')()
u'\nhello\nhello\n'
</code></pre>

<p>Test unicode.</p>

<pre><code>&gt;&gt;&gt; t('$def with (a)\n$a')(u'\u203d')
u'\u203d\n'
&gt;&gt;&gt; t('$def with (a)\n$a')(u'\u203d'.encode('utf-8'))
u'\u203d\n'
&gt;&gt;&gt; t(u'$def with (a)\n$a $:a')(u'\u203d')
u'\u203d \u203d\n'
&gt;&gt;&gt; t(u'$def with ()\nfoo')()
u'foo\n'
&gt;&gt;&gt; def f(x): return x
...
&gt;&gt;&gt; t(u'$def with (f)\n$:f("x")')(f)
u'x\n'
&gt;&gt;&gt; t('$def with (f)\n$:f("x")')(f)
u'x\n'
</code></pre>

<p>Test dollar escaping.</p>

<pre><code>&gt;&gt;&gt; t("Stop, $$money isn't evaluated.")()
u"Stop, $money isn't evaluated.\n"
&gt;&gt;&gt; t("Stop, \$money isn't evaluated.")()
u"Stop, $money isn't evaluated.\n"
</code></pre>

<p>Test space sensitivity.</p>

<pre><code>&gt;&gt;&gt; t('$def with (x)\n$x')(1)
u'1\n'
&gt;&gt;&gt; t('$def with(x ,y)\n$x')(1, 1)
u'1\n'
&gt;&gt;&gt; t('$(1 + 2*3 + 4)')()
u'11\n'
</code></pre>

<p>Make sure globals are working.</p>

<pre><code>&gt;&gt;&gt; t('$x')()
Traceback (most recent call last):
    ...
NameError: global name 'x' is not defined
&gt;&gt;&gt; t('$x', globals={'x': 1})()
u'1\n'
</code></pre>

<p>Can't change globals.</p>

<pre><code>&gt;&gt;&gt; t('$ x = 2\n$x', globals={'x': 1})()
u'2\n'
&gt;&gt;&gt; t('$ x = x + 1\n$x', globals={'x': 1})()
Traceback (most recent call last):
    ...
UnboundLocalError: local variable 'x' referenced before assignment
</code></pre>

<p>Make sure builtins are customizable.</p>

<pre><code>&gt;&gt;&gt; t('$min(1, 2)')()
u'1\n'
&gt;&gt;&gt; t('$min(1, 2)', builtins={})()
Traceback (most recent call last):
    ...
NameError: global name 'min' is not defined
</code></pre>

<p>Test vars.</p>

<pre><code>&gt;&gt;&gt; x = t('$var x: 1')()
&gt;&gt;&gt; x.x
u'1'
&gt;&gt;&gt; x = t('$var x = 1')()
&gt;&gt;&gt; x.x
1
&gt;&gt;&gt; x = t('$var x:  \n    foo\n    bar')()
&gt;&gt;&gt; x.x
u'foo\nbar\n'
</code></pre>

<p>Test BOM chars.</p>

<pre><code>&gt;&gt;&gt; t('\xef\xbb\xbf$def with(x)\n$x')('foo')
u'foo\n'
</code></pre>

<p>Test for with weird cases.</p>

<pre><code>&gt;&gt;&gt; t('$for i in range(10)[1:5]:\n    $i')()
u'1\n2\n3\n4\n'
&gt;&gt;&gt; t("$for k, v in {'a': 1, 'b': 2}.items():\n    $k $v")()
u'a 1\nb 2\n'
&gt;&gt;&gt; t("$for k, v in ({'a': 1, 'b': 2}.items():\n    $k $v")()
Traceback (most recent call last):
    ...
SyntaxError: invalid syntax
</code></pre>

<p>Test datetime.</p>

<pre><code>&gt;&gt;&gt; import datetime
&gt;&gt;&gt; t("$def with (date)\n$date.strftime('%m %Y')")(datetime.datetime(2009, 1, 1))
u'01 2009\n'
</code></pre></div></p>
</div>
<p><span class="ts">module</span><code class="module"> <a name="web.utils">web.utils</a></code><br />
<div style="margin-left:15px"><p>General Utilities
(part of web.py)</p></div></p>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> Storage</code><br />
<div style="margin-left:45px"><p>A Storage object is like a dictionary except <code>obj.foo</code> can be used
in addition to <code>obj['foo']</code>.</p>

<pre><code>&gt;&gt;&gt; o = storage(a=1)
&gt;&gt;&gt; o.a
1
&gt;&gt;&gt; o['a']
1
&gt;&gt;&gt; o.a = 2
&gt;&gt;&gt; o['a']
2
&gt;&gt;&gt; del o.a
&gt;&gt;&gt; o.a
Traceback (most recent call last):
    ...
AttributeError: 'a'
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> storify(mapping, *requireds, **defaults)</code><br />
<div style="margin-left:45px"><p>Creates a <code>storage</code> object from dictionary <code>mapping</code>, raising <code>KeyError</code> if
d doesn't have all of the keys in <code>requireds</code> and using the default 
values for keys found in <code>defaults</code>.</p>

<p>For example, <code>storify({'a':1, 'c':3}, b=2, c=0)</code> will return the equivalent of
<code>storage({'a':1, 'b':2, 'c':3})</code>.</p>

<p>If a <code>storify</code> value is a list (e.g. multiple values in a form submission), 
<code>storify</code> returns the last element of the list, unless the key appears in 
<code>defaults</code> as a list. Thus:</p>

<pre><code>&gt;&gt;&gt; storify({'a':[1, 2]}).a
2
&gt;&gt;&gt; storify({'a':[1, 2]}, a=[]).a
[1, 2]
&gt;&gt;&gt; storify({'a':1}, a=[]).a
[1]
&gt;&gt;&gt; storify({}, a=[]).a
[]
</code></pre>

<p>Similarly, if the value has a <code>value</code> attribute, `storify will return <em>its</em>
value, unless the key appears in <code>defaults</code> as a dictionary.</p>

<pre><code>&gt;&gt;&gt; storify({'a':storage(value=1)}).a
1
&gt;&gt;&gt; storify({'a':storage(value=1)}, a={}).a
&lt;Storage {'value': 1}&gt;
&gt;&gt;&gt; storify({}, a={}).a
{}
</code></pre>

<p>Optionally, keyword parameter <code>_unicode</code> can be passed to convert all values to unicode.</p>

<pre><code>&gt;&gt;&gt; storify({'x': 'a'}, _unicode=True)
&lt;Storage {'x': u'a'}&gt;
&gt;&gt;&gt; storify({'x': storage(value='a')}, x={}, _unicode=True)
&lt;Storage {'x': &lt;Storage {'value': 'a'}&gt;}&gt;
&gt;&gt;&gt; storify({'x': storage(value='a')}, _unicode=True)
&lt;Storage {'x': u'a'}&gt;
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> Counter</code><br />
<div style="margin-left:45px"><p>Keeps count of how many times something is added.</p>

<blockquote>
  <blockquote>
    <blockquote>
      <p>c = counter()
      c.add('x')
      c.add('x')
      c.add('x')
      c.add('x')
      c.add('x')
      c.add('y')
      c
      &lt;Counter {'y': 1, 'x': 5}>
      c.most()
      ['x']</p>
    </blockquote>
  </blockquote>
</blockquote></div></p>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> add(self, n)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> least(self)</code><br />
<div style="margin-left:75px"><p>Returns the keys with mininum count.</p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> most(self)</code><br />
<div style="margin-left:75px"><p>Returns the keys with maximum count.</p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> percent(self, key)</code><br />
<div style="margin-left:75px"><p>Returns what percentage a certain key is of all entries.</p>

<blockquote>
  <blockquote>
    <blockquote>
      <p>c = counter()
      c.add('x')
      c.add('x')
      c.add('x')
      c.add('y')
      c.percent('x')
      0.75
      c.percent('y')
      0.25</p>
    </blockquote>
  </blockquote>
</blockquote></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> sorted_items(self)</code><br />
<div style="margin-left:75px"><p>Returns items sorted by value.</p>

<blockquote>
  <blockquote>
    <blockquote>
      <p>c = counter()
      c.add('x')
      c.add('x')
      c.add('y')
      c.sorted_items()
      [('x', 2), ('y', 1)]</p>
    </blockquote>
  </blockquote>
</blockquote></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> sorted_keys(self)</code><br />
<div style="margin-left:75px"><p>Returns keys sorted by value.</p>

<blockquote>
  <blockquote>
    <blockquote>
      <p>c = counter()
      c.add('x')
      c.add('x')
      c.add('y')
      c.sorted_keys()
      ['x', 'y']</p>
    </blockquote>
  </blockquote>
</blockquote></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> sorted_values(self)</code><br />
<div style="margin-left:75px"><p>Returns values sorted by value.</p>

<blockquote>
  <blockquote>
    <blockquote>
      <p>c = counter()
      c.add('x')
      c.add('x')
      c.add('y')
      c.sorted_values()
      [2, 1]</p>
    </blockquote>
  </blockquote>
</blockquote></div></p>
</div>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> counter</code><br />
<div style="margin-left:45px"><p>Keeps count of how many times something is added.</p>

<blockquote>
  <blockquote>
    <blockquote>
      <p>c = counter()
      c.add('x')
      c.add('x')
      c.add('x')
      c.add('x')
      c.add('x')
      c.add('y')
      c
      &lt;Counter {'y': 1, 'x': 5}>
      c.most()
      ['x']</p>
    </blockquote>
  </blockquote>
</blockquote></div></p>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> add(self, n)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> least(self)</code><br />
<div style="margin-left:75px"><p>Returns the keys with mininum count.</p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> most(self)</code><br />
<div style="margin-left:75px"><p>Returns the keys with maximum count.</p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> percent(self, key)</code><br />
<div style="margin-left:75px"><p>Returns what percentage a certain key is of all entries.</p>

<blockquote>
  <blockquote>
    <blockquote>
      <p>c = counter()
      c.add('x')
      c.add('x')
      c.add('x')
      c.add('y')
      c.percent('x')
      0.75
      c.percent('y')
      0.25</p>
    </blockquote>
  </blockquote>
</blockquote></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> sorted_items(self)</code><br />
<div style="margin-left:75px"><p>Returns items sorted by value.</p>

<blockquote>
  <blockquote>
    <blockquote>
      <p>c = counter()
      c.add('x')
      c.add('x')
      c.add('y')
      c.sorted_items()
      [('x', 2), ('y', 1)]</p>
    </blockquote>
  </blockquote>
</blockquote></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> sorted_keys(self)</code><br />
<div style="margin-left:75px"><p>Returns keys sorted by value.</p>

<blockquote>
  <blockquote>
    <blockquote>
      <p>c = counter()
      c.add('x')
      c.add('x')
      c.add('y')
      c.sorted_keys()
      ['x', 'y']</p>
    </blockquote>
  </blockquote>
</blockquote></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> sorted_values(self)</code><br />
<div style="margin-left:75px"><p>Returns values sorted by value.</p>

<blockquote>
  <blockquote>
    <blockquote>
      <p>c = counter()
      c.add('x')
      c.add('x')
      c.add('y')
      c.sorted_values()
      [2, 1]</p>
    </blockquote>
  </blockquote>
</blockquote></div></p>
</div>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> rstrips(text, remove)</code><br />
<div style="margin-left:45px"><p>removes the string <code>remove</code> from the right of <code>text</code></p>

<pre><code>&gt;&gt;&gt; rstrips("foobar", "bar")
'foo'
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> lstrips(text, remove)</code><br />
<div style="margin-left:45px"><p>removes the string <code>remove</code> from the left of <code>text</code></p>

<pre><code>&gt;&gt;&gt; lstrips("foobar", "foo")
'bar'
&gt;&gt;&gt; lstrips('http://foo.org/', ['http://', 'https://'])
'foo.org/'
&gt;&gt;&gt; lstrips('FOOBARBAZ', ['FOO', 'BAR'])
'BAZ'
&gt;&gt;&gt; lstrips('FOOBARBAZ', ['BAR', 'FOO'])
'BARBAZ'
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> strips(text, remove)</code><br />
<div style="margin-left:45px"><p>removes the string <code>remove</code> from the both sides of <code>text</code></p>

<pre><code>&gt;&gt;&gt; strips("foobarfoo", "foo")
'bar'
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> safeunicode(obj, encoding='utf-8')</code><br />
<div style="margin-left:45px"><p>Converts any given object to unicode string.</p>

<pre><code>&gt;&gt;&gt; safeunicode('hello')
u'hello'
&gt;&gt;&gt; safeunicode(2)
u'2'
&gt;&gt;&gt; safeunicode('\xe1\x88\xb4')
u'\u1234'
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> safestr(obj, encoding='utf-8')</code><br />
<div style="margin-left:45px"><p>Converts any given object to utf-8 encoded string.</p>

<pre><code>&gt;&gt;&gt; safestr('hello')
'hello'
&gt;&gt;&gt; safestr(u'\u1234')
'\xe1\x88\xb4'
&gt;&gt;&gt; safestr(2)
'2'
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> utf8(obj, encoding='utf-8')</code><br />
<div style="margin-left:45px"><p>Converts any given object to utf-8 encoded string.</p>

<pre><code>&gt;&gt;&gt; safestr('hello')
'hello'
&gt;&gt;&gt; safestr(u'\u1234')
'\xe1\x88\xb4'
&gt;&gt;&gt; safestr(2)
'2'
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> TimeoutError</code><br />
<div style="margin-left:45px"><p></p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> timelimit(timeout)</code><br />
<div style="margin-left:45px"><p>A decorator to limit a function to <code>timeout</code> seconds, raising <code>TimeoutError</code>
if it takes longer.</p>

<pre><code>&gt;&gt;&gt; import time
&gt;&gt;&gt; def meaningoflife():
...     time.sleep(.2)
...     return 42
&gt;&gt;&gt; 
&gt;&gt;&gt; timelimit(.1)(meaningoflife)()
Traceback (most recent call last):
    ...
TimeoutError: took too long
&gt;&gt;&gt; timelimit(1)(meaningoflife)()
42
</code></pre>

<p><em>Caveat:</em> The function isn't stopped after <code>timeout</code> seconds but continues 
executing in a separate thread. (There seems to be no way to kill a thread.)</p>

<p>inspired by <a href="http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/473878">http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/473878</a></p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">class</span><code class="class"> Memoize(self, func, expires=None, background=True)</code><br />
<div style="margin-left:45px"><p>'Memoizes' a function, caching its return values for each input.
If <code>expires</code> is specified, values are recalculated after <code>expires</code> seconds.
If <code>background</code> is specified, values are recalculated in a separate thread.</p>

<pre><code>&gt;&gt;&gt; calls = 0
&gt;&gt;&gt; def howmanytimeshaveibeencalled():
...     global calls
...     calls += 1
...     return calls
&gt;&gt;&gt; fastcalls = memoize(howmanytimeshaveibeencalled)
&gt;&gt;&gt; howmanytimeshaveibeencalled()
1
&gt;&gt;&gt; howmanytimeshaveibeencalled()
2
&gt;&gt;&gt; fastcalls()
3
&gt;&gt;&gt; fastcalls()
3
&gt;&gt;&gt; import time
&gt;&gt;&gt; fastcalls = memoize(howmanytimeshaveibeencalled, .1, background=False)
&gt;&gt;&gt; fastcalls()
4
&gt;&gt;&gt; fastcalls()
4
&gt;&gt;&gt; time.sleep(.2)
&gt;&gt;&gt; fastcalls()
5
&gt;&gt;&gt; def slowfunc():
...     time.sleep(.1)
...     return howmanytimeshaveibeencalled()
&gt;&gt;&gt; fastcalls = memoize(slowfunc, .2, background=True)
&gt;&gt;&gt; fastcalls()
6
&gt;&gt;&gt; timelimit(.05)(fastcalls)()
6
&gt;&gt;&gt; time.sleep(.2)
&gt;&gt;&gt; timelimit(.05)(fastcalls)()
6
&gt;&gt;&gt; timelimit(.05)(fastcalls)()
6
&gt;&gt;&gt; time.sleep(.2)
&gt;&gt;&gt; timelimit(.05)(fastcalls)()
7
&gt;&gt;&gt; fastcalls = memoize(slowfunc, None, background=True)
&gt;&gt;&gt; threading.Thread(target=fastcalls).start()
&gt;&gt;&gt; time.sleep(.01)
&gt;&gt;&gt; fastcalls()
9
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> re_subm(pat, repl, string)</code><br />
<div style="margin-left:45px"><p>Like re.sub, but returns the replacement <em>and</em> the match object.</p>

<pre><code>&gt;&gt;&gt; t, m = re_subm('g(oo+)fball', r'f\1lish', 'goooooofball')
&gt;&gt;&gt; t
'foooooolish'
&gt;&gt;&gt; m.groups()
('oooooo',)
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> group(seq, size)</code><br />
<div style="margin-left:45px"><p>Returns an iterator over a series of lists of length size from iterable.</p>

<pre><code>&gt;&gt;&gt; list(group([1,2,3,4], 2))
[[1, 2], [3, 4]]
&gt;&gt;&gt; list(group([1,2,3,4,5], 2))
[[1, 2], [3, 4], [5]]
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> uniq(seq, key=None)</code><br />
<div style="margin-left:45px"><p>Removes duplicate elements from a list while preserving the order of the rest.</p>

<pre><code>&gt;&gt;&gt; uniq([9,0,2,1,0])
[9, 0, 2, 1]
</code></pre>

<p>The value of the optional <code>key</code> parameter should be a function that
takes a single argument and returns a key to test the uniqueness.</p>

<pre><code>&gt;&gt;&gt; uniq(["Foo", "foo", "bar"], key=lambda s: s.lower())
['Foo', 'bar']
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> iterview(x)</code><br />
<div style="margin-left:45px"><p>Takes an iterable <code>x</code> and returns an iterator over it
which prints its progress to stderr as it iterates through.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">class</span><code class="class"> IterBetter(self, iterator)</code><br />
<div style="margin-left:45px"><p>Returns an object that can be used as an iterator 
but can also be used via <strong>getitem</strong> (although it 
cannot go backwards -- that is, you cannot request 
<code>iterbetter[0]</code> after requesting <code>iterbetter[1]</code>).</p>

<pre><code>&gt;&gt;&gt; import itertools
&gt;&gt;&gt; c = iterbetter(itertools.count())
&gt;&gt;&gt; c[1]
1
&gt;&gt;&gt; c[5]
5
&gt;&gt;&gt; c[3]
Traceback (most recent call last):
    ...
IndexError: already passed 3
</code></pre>

<p>For boolean test, IterBetter peeps at first value in the itertor without effecting the iteration.</p>

<pre><code>&gt;&gt;&gt; c = iterbetter(iter(range(5)))
&gt;&gt;&gt; bool(c)
True
&gt;&gt;&gt; list(c)
[0, 1, 2, 3, 4]
&gt;&gt;&gt; c = iterbetter(iter([]))
&gt;&gt;&gt; bool(c)
False
&gt;&gt;&gt; list(c)
[]
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> safeiter(it, cleanup=None, ignore_errors=True)</code><br />
<div style="margin-left:45px"><p>Makes an iterator safe by ignoring the exceptions occured during the iteration.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> safewrite(filename, content)</code><br />
<div style="margin-left:45px"><p>Writes the content to a temp file and then moves the temp file to 
given filename to avoid overwriting the existing file in case of errors.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> dictreverse(mapping)</code><br />
<div style="margin-left:45px"><p>Returns a new dictionary with keys and values swapped.</p>

<pre><code>&gt;&gt;&gt; dictreverse({1: 2, 3: 4})
{2: 1, 4: 3}
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> dictfind(dictionary, element)</code><br />
<div style="margin-left:45px"><p>Returns a key whose value in <code>dictionary</code> is <code>element</code> 
or, if none exists, None.</p>

<pre><code>&gt;&gt;&gt; d = {1:2, 3:4}
&gt;&gt;&gt; dictfind(d, 4)
3
&gt;&gt;&gt; dictfind(d, 5)
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> dictfindall(dictionary, element)</code><br />
<div style="margin-left:45px"><p>Returns the keys whose values in <code>dictionary</code> are <code>element</code>
or, if none exists, [].</p>

<pre><code>&gt;&gt;&gt; d = {1:4, 3:4}
&gt;&gt;&gt; dictfindall(d, 4)
[1, 3]
&gt;&gt;&gt; dictfindall(d, 5)
[]
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> dictincr(dictionary, element)</code><br />
<div style="margin-left:45px"><p>Increments <code>element</code> in <code>dictionary</code>, 
setting it to one if it doesn't exist.</p>

<pre><code>&gt;&gt;&gt; d = {1:2, 3:4}
&gt;&gt;&gt; dictincr(d, 1)
3
&gt;&gt;&gt; d[1]
3
&gt;&gt;&gt; dictincr(d, 5)
1
&gt;&gt;&gt; d[5]
1
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> dictadd(*dicts)</code><br />
<div style="margin-left:45px"><p>Returns a dictionary consisting of the keys in the argument dictionaries.
If they share a key, the value from the last argument is used.</p>

<pre><code>&gt;&gt;&gt; dictadd({1: 0, 2: 0}, {2: 1, 3: 1})
{1: 0, 2: 1, 3: 1}
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> requeue(queue, index=-1)</code><br />
<div style="margin-left:45px"><p>Returns the element at index after moving it to the beginning of the queue.</p>

<blockquote>
  <blockquote>
    <blockquote>
      <p>x = [1, 2, 3, 4]
      requeue(x)
      4
      x
      [4, 1, 2, 3]</p>
    </blockquote>
  </blockquote>
</blockquote></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> restack(stack, index=0)</code><br />
<div style="margin-left:45px"><p>Returns the element at index after moving it to the top of stack.</p>

<blockquote>
  <blockquote>
    <blockquote>
      <p>x = [1, 2, 3, 4]
      restack(x)
      1
      x
      [2, 3, 4, 1]</p>
    </blockquote>
  </blockquote>
</blockquote></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> listget(lst, ind, default=None)</code><br />
<div style="margin-left:45px"><p>Returns <code>lst[ind]</code> if it exists, <code>default</code> otherwise.</p>

<pre><code>&gt;&gt;&gt; listget(['a'], 0)
'a'
&gt;&gt;&gt; listget(['a'], 1)
&gt;&gt;&gt; listget(['a'], 1, 'b')
'b'
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> intget(integer, default=None)</code><br />
<div style="margin-left:45px"><p>Returns <code>integer</code> as an int or <code>default</code> if it can't.</p>

<pre><code>&gt;&gt;&gt; intget('3')
3
&gt;&gt;&gt; intget('3a')
&gt;&gt;&gt; intget('3a', 0)
0
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> datestr(then, now=None)</code><br />
<div style="margin-left:45px"><p>Converts a (UTC) datetime object to a nice string representation.</p>

<pre><code>&gt;&gt;&gt; from datetime import datetime, timedelta
&gt;&gt;&gt; d = datetime(1970, 5, 1)
&gt;&gt;&gt; datestr(d, now=d)
'0 microseconds ago'
&gt;&gt;&gt; for t, v in {
...   timedelta(microseconds=1): '1 microsecond ago',
...   timedelta(microseconds=2): '2 microseconds ago',
...   -timedelta(microseconds=1): '1 microsecond from now',
...   -timedelta(microseconds=2): '2 microseconds from now',
...   timedelta(microseconds=2000): '2 milliseconds ago',
...   timedelta(seconds=2): '2 seconds ago',
...   timedelta(seconds=2*60): '2 minutes ago',
...   timedelta(seconds=2*60*60): '2 hours ago',
...   timedelta(days=2): '2 days ago',
... }.iteritems():
...     assert datestr(d, now=d+t) == v
&gt;&gt;&gt; datestr(datetime(1970, 1, 1), now=d)
'January  1'
&gt;&gt;&gt; datestr(datetime(1969, 1, 1), now=d)
'January  1, 1969'
&gt;&gt;&gt; datestr(datetime(1970, 6, 1), now=d)
'June  1, 1970'
&gt;&gt;&gt; datestr(None)
''
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> numify(string)</code><br />
<div style="margin-left:45px"><p>Removes all non-digit characters from <code>string</code>.</p>

<pre><code>&gt;&gt;&gt; numify('800-555-1212')
'8005551212'
&gt;&gt;&gt; numify('800.555.1212')
'8005551212'
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> denumify(string, pattern)</code><br />
<div style="margin-left:45px"><p>Formats <code>string</code> according to <code>pattern</code>, where the letter X gets replaced
by characters from <code>string</code>.</p>

<pre><code>&gt;&gt;&gt; denumify("8005551212", "(XXX) XXX-XXXX")
'(800) 555-1212'
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> commify(n)</code><br />
<div style="margin-left:45px"><p>Add commas to an integer <code>n</code>.</p>

<pre><code>&gt;&gt;&gt; commify(1)
'1'
&gt;&gt;&gt; commify(123)
'123'
&gt;&gt;&gt; commify(1234)
'1,234'
&gt;&gt;&gt; commify(1234567890)
'1,234,567,890'
&gt;&gt;&gt; commify(123.0)
'123.0'
&gt;&gt;&gt; commify(1234.5)
'1,234.5'
&gt;&gt;&gt; commify(1234.56789)
'1,234.56789'
&gt;&gt;&gt; commify('%.2f' % 1234.5)
'1,234.50'
&gt;&gt;&gt; commify(None)
&gt;&gt;&gt;
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> dateify(datestring)</code><br />
<div style="margin-left:45px"><p>Formats a numified <code>datestring</code> properly.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> nthstr(n)</code><br />
<div style="margin-left:45px"><p>Formats an ordinal.
Doesn't handle negative numbers.</p>

<pre><code>&gt;&gt;&gt; nthstr(1)
'1st'
&gt;&gt;&gt; nthstr(0)
'0th'
&gt;&gt;&gt; [nthstr(x) for x in [2, 3, 4, 5, 10, 11, 12, 13, 14, 15]]
['2nd', '3rd', '4th', '5th', '10th', '11th', '12th', '13th', '14th', '15th']
&gt;&gt;&gt; [nthstr(x) for x in [91, 92, 93, 94, 99, 100, 101, 102]]
['91st', '92nd', '93rd', '94th', '99th', '100th', '101st', '102nd']
&gt;&gt;&gt; [nthstr(x) for x in [111, 112, 113, 114, 115]]
['111th', '112th', '113th', '114th', '115th']
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> cond(predicate, consequence, alternative=None)</code><br />
<div style="margin-left:45px"><p>Function replacement for if-else to use in expressions.</p>

<pre><code>&gt;&gt;&gt; x = 2
&gt;&gt;&gt; cond(x % 2 == 0, "even", "odd")
'even'
&gt;&gt;&gt; cond(x % 2 == 0, "even", "odd") + '_row'
'even_row'
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">class</span><code class="class"> CaptureStdout(self, func)</code><br />
<div style="margin-left:45px"><p>Captures everything <code>func</code> prints to stdout and returns it instead.</p>

<pre><code>&gt;&gt;&gt; def idiot():
...     print "foo"
&gt;&gt;&gt; capturestdout(idiot)()
'foo\n'
</code></pre>

<p><strong>WARNING:</strong> Not threadsafe!</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">class</span><code class="class"> capturestdout(self, func)</code><br />
<div style="margin-left:45px"><p>Captures everything <code>func</code> prints to stdout and returns it instead.</p>

<pre><code>&gt;&gt;&gt; def idiot():
...     print "foo"
&gt;&gt;&gt; capturestdout(idiot)()
'foo\n'
</code></pre>

<p><strong>WARNING:</strong> Not threadsafe!</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">class</span><code class="class"> Profile(self, func)</code><br />
<div style="margin-left:45px"><p>Profiles <code>func</code> and returns a tuple containing its output
and a string with human-readable profiling information.</p>

<pre><code>&gt;&gt;&gt; import time
&gt;&gt;&gt; out, inf = profile(time.sleep)(.001)
&gt;&gt;&gt; out
&gt;&gt;&gt; inf[:10].strip()
'took 0.0'
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> tryall(context, prefix=None)</code><br />
<div style="margin-left:45px"><p>Tries a series of functions and prints their results. 
<code>context</code> is a dictionary mapping names to values; 
the value will only be tried if it's callable.</p>

<pre><code>&gt;&gt;&gt; tryall(dict(j=lambda: True))
j: True
----------------------------------------
results:
   True: 1
</code></pre>

<p>For example, you might have a file <code>test/stuff.py</code> 
with a series of functions testing various things in it. 
At the bottom, have a line:</p>

<pre><code>if __name__ == "__main__": tryall(globals())
</code></pre>

<p>Then you can run <code>python test/stuff.py</code> and get the results of 
all the tests.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> ThreadedDict(self)</code><br />
<div style="margin-left:45px"><p>Thread local storage.</p>

<pre><code>&gt;&gt;&gt; d = ThreadedDict()
&gt;&gt;&gt; d.x = 1
&gt;&gt;&gt; d.x
1
&gt;&gt;&gt; import threading
&gt;&gt;&gt; def f(): d.x = 2
...
&gt;&gt;&gt; t = threading.Thread(target=f)
&gt;&gt;&gt; t.start()
&gt;&gt;&gt; t.join()
&gt;&gt;&gt; d.x
1
</code></pre></div></p>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> clear(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">function</span><code class="function"> clear_all()</code><br />
<div style="margin-left:75px"><p>Clears all ThreadedDict instances.</p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> copy(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> get(self, key, default=None)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> has_key(self, key)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> items(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> iter(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> iteritems(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> iterkeys(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> itervalues(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> keys(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> pop(self, key, *args)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> popitem(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> setdefault(self, key, default=None)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> update(self, *args, **kwargs)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> values(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> autoassign(self, locals)</code><br />
<div style="margin-left:45px"><p>Automatically assigns local variables to <code>self</code>.</p>

<pre><code>&gt;&gt;&gt; self = storage()
&gt;&gt;&gt; autoassign(self, dict(a=1, b=2))
&gt;&gt;&gt; self
&lt;Storage {'a': 1, 'b': 2}&gt;
</code></pre>

<p>Generally used in <code>__init__</code> methods, as in:</p>

<pre><code>def __init__(self, foo, bar, baz=1): autoassign(self, locals())
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> to36(q)</code><br />
<div style="margin-left:45px"><p>Converts an integer to base 36 (a useful scheme for human-sayable IDs).</p>

<pre><code>&gt;&gt;&gt; to36(35)
'z'
&gt;&gt;&gt; to36(119292)
'2k1o'
&gt;&gt;&gt; int(to36(939387374), 36)
939387374
&gt;&gt;&gt; to36(0)
'0'
&gt;&gt;&gt; to36(-393)
Traceback (most recent call last):
    ... 
ValueError: must supply a positive integer
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> safemarkdown(text)</code><br />
<div style="margin-left:45px"><p>Converts text to HTML following the rules of Markdown, but blocking any
outside HTML input, so that only the things supported by Markdown
can be used. Also converts raw URLs to links.</p>

<p>(requires <a href="http://webpy.org/markdown.py">markdown.py</a>)</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> sendmail(from_address, to_address, subject, message, headers=None, **kw)</code><br />
<div style="margin-left:45px"><p>Sends the email message <code>message</code> with mail and envelope headers
for from <code>from_address_</code> to <code>to_address</code> with <code>subject</code>. 
Additional email headers can be specified with the dictionary 
`headers.</p>

<p>Optionally cc, bcc and attachments can be specified as keyword arguments.
Attachments must be an iterable and each attachment can be either a 
filename or a file object or a dictionary with filename, content and 
optionally content_type keys.</p>

<p>If <code>web.config.smtp_server</code> is set, it will send the message
to that SMTP server. Otherwise it will look for 
<code>/usr/sbin/sendmail</code>, the typical location for the sendmail-style
binary. To use sendmail from a different path, set <code>web.config.sendmail_path</code>.</p></div></p>
</div>
<p><span class="ts">module</span><code class="module"> <a name="web.webapi">web.webapi</a></code><br />
<div style="margin-left:15px"><p>Web API (wrapper around WSGI)
(from web.py)</p></div></p>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> header(hdr, value, unique=False)</code><br />
<div style="margin-left:45px"><p>Adds the header <code>hdr: value</code> with the response.</p>

<p>If <code>unique</code> is True and a header with that name already exists,
it doesn't add a new one.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> debug(*args)</code><br />
<div style="margin-left:45px"><p>Prints a prettyprinted version of <code>args</code> to stderr.</p></div></p>
<div style="margin-left:60px">
<p><span class="ts">function</span><code class="function"> write(x)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> input(*requireds, **defaults)</code><br />
<div style="margin-left:45px"><p>Returns a <code>storage</code> object with the GET and POST arguments. 
See <code>storify</code> for how <code>requireds</code> and <code>defaults</code> work.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> data()</code><br />
<div style="margin-left:45px"><p>Returns the data sent with the request.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> setcookie(name, value, expires='', domain=None, secure=False, httponly=False, path=None)</code><br />
<div style="margin-left:45px"><p>Sets a cookie.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> cookies(*requireds, **defaults)</code><br />
<div style="margin-left:45px"><p>Returns a <code>storage</code> object with all the cookies in it.
See <code>storify</code> for how <code>requireds</code> and <code>defaults</code> work.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> HTTPError(self, status, headers={}, data='')</code><br />
<div style="margin-left:45px"><p></p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> OK(self, data='', headers={})</code><br />
<div style="margin-left:45px"><p><code>200 OK</code> status</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> Created(self, data='Created', headers={})</code><br />
<div style="margin-left:45px"><p><code>201 Created</code> status</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> Accepted(self, data='Accepted', headers={})</code><br />
<div style="margin-left:45px"><p><code>202 Accepted</code> status</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> ok(self, data='', headers={})</code><br />
<div style="margin-left:45px"><p><code>200 OK</code> status</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> created(self, data='Created', headers={})</code><br />
<div style="margin-left:45px"><p><code>201 Created</code> status</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> accepted(self, data='Accepted', headers={})</code><br />
<div style="margin-left:45px"><p><code>202 Accepted</code> status</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> Redirect(self, url, status='301 Moved Permanently', absolute=False)</code><br />
<div style="margin-left:45px"><p>A <code>301 Moved Permanently</code> redirect.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> Found(self, url, absolute=False)</code><br />
<div style="margin-left:45px"><p>A <code>302 Found</code> redirect.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> SeeOther(self, url, absolute=False)</code><br />
<div style="margin-left:45px"><p>A <code>303 See Other</code> redirect.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> NotModified(self)</code><br />
<div style="margin-left:45px"><p>A <code>304 Not Modified</code> status.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> TempRedirect(self, url, absolute=False)</code><br />
<div style="margin-left:45px"><p>A <code>307 Temporary Redirect</code> redirect.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> redirect(self, url, status='301 Moved Permanently', absolute=False)</code><br />
<div style="margin-left:45px"><p>A <code>301 Moved Permanently</code> redirect.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> found(self, url, absolute=False)</code><br />
<div style="margin-left:45px"><p>A <code>302 Found</code> redirect.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> seeother(self, url, absolute=False)</code><br />
<div style="margin-left:45px"><p>A <code>303 See Other</code> redirect.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> notmodified(self)</code><br />
<div style="margin-left:45px"><p>A <code>304 Not Modified</code> status.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> tempredirect(self, url, absolute=False)</code><br />
<div style="margin-left:45px"><p>A <code>307 Temporary Redirect</code> redirect.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> BadRequest(self)</code><br />
<div style="margin-left:45px"><p><code>400 Bad Request</code> error.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> Unauthorized(self, data='Unauthorized', headers={})</code><br />
<div style="margin-left:45px"><p><code>401 Unauthorized</code> status</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> Forbidden(self, data='Forbidden', headers={})</code><br />
<div style="margin-left:45px"><p><code>403 Forbidden</code> status</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> NotFound(message=None)</code><br />
<div style="margin-left:45px"><p>Returns HTTPError with '404 Not Found' error from the active application.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> NoMethod(self, cls=None)</code><br />
<div style="margin-left:45px"><p>A <code>405 Method Not Allowed</code> error.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> NotAcceptable(self, data='Not Acceptable', headers={})</code><br />
<div style="margin-left:45px"><p><code>406 Not Acceptable</code> status</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> Conflict(self, data='Conflict', headers={})</code><br />
<div style="margin-left:45px"><p><code>409 Conflict</code> status</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> Gone(self)</code><br />
<div style="margin-left:45px"><p><code>410 Gone</code> error.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> PreconditionFailed(self, data='Precondition Failed', headers={})</code><br />
<div style="margin-left:45px"><p><code>412 Precondition Failed</code> status</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> badrequest(self)</code><br />
<div style="margin-left:45px"><p><code>400 Bad Request</code> error.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> unauthorized(self, data='Unauthorized', headers={})</code><br />
<div style="margin-left:45px"><p><code>401 Unauthorized</code> status</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> forbidden(self, data='Forbidden', headers={})</code><br />
<div style="margin-left:45px"><p><code>403 Forbidden</code> status</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> notfound(message=None)</code><br />
<div style="margin-left:45px"><p>Returns HTTPError with '404 Not Found' error from the active application.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> nomethod(self, cls=None)</code><br />
<div style="margin-left:45px"><p>A <code>405 Method Not Allowed</code> error.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> notacceptable(self, data='Not Acceptable', headers={})</code><br />
<div style="margin-left:45px"><p><code>406 Not Acceptable</code> status</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> conflict(self, data='Conflict', headers={})</code><br />
<div style="margin-left:45px"><p><code>409 Conflict</code> status</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> gone(self)</code><br />
<div style="margin-left:45px"><p><code>410 Gone</code> error.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">type</span><code class="type"> preconditionfailed(self, data='Precondition Failed', headers={})</code><br />
<div style="margin-left:45px"><p><code>412 Precondition Failed</code> status</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> InternalError(message=None)</code><br />
<div style="margin-left:45px"><p>Returns HTTPError with '500 internal error' error from the active application.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> internalerror(message=None)</code><br />
<div style="margin-left:45px"><p>Returns HTTPError with '500 internal error' error from the active application.</p></div></p>
</div>
<p><span class="ts">module</span><code class="module"> <a name="web.webopenid">web.webopenid</a></code><br />
<div style="margin-left:15px"><p>openid.py: an openid library for web.py</p>

<p>Notes:</p>

<ul>
<li><p>This will create a file called .openid<em>secret</em>key in the 
current directory with your secret key in it. If someone 
has access to this file they can log in as any user. And 
if the app can't find this file for any reason (e.g. you 
moved the app somewhere else) then each currently logged 
in user will get logged out.</p></li>
<li><p>State must be maintained through the entire auth process 
-- this means that if you have multiple web.py processes 
serving one set of URLs or if you restart your app often 
then log ins will fail. You have to replace sessions and 
store for things to work.</p></li>
<li><p>We set cookies starting with "openid_".</p></li>
</ul></div></p>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> form(openid_loc)</code><br />
<div style="margin-left:45px"><p></p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">class</span><code class="class"> host(self)</code><br />
<div style="margin-left:45px"><p></p></div></p>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> GET(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
<div style="margin-left:60px">
<p><span class="ts">method</span><code class="method"> POST(self)</code><br />
<div style="margin-left:75px"><p></p></div></p>
</div>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> logout()</code><br />
<div style="margin-left:45px"><p></p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> status()</code><br />
<div style="margin-left:45px"><p></p></div></p>
</div>
<p><span class="ts">module</span><code class="module"> <a name="web.wsgi">web.wsgi</a></code><br />
<div style="margin-left:15px"><p>WSGI Utilities
(from web.py)</p></div></p>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> listget(lst, ind, default=None)</code><br />
<div style="margin-left:45px"><p>Returns <code>lst[ind]</code> if it exists, <code>default</code> otherwise.</p>

<pre><code>&gt;&gt;&gt; listget(['a'], 0)
'a'
&gt;&gt;&gt; listget(['a'], 1)
&gt;&gt;&gt; listget(['a'], 1, 'b')
'b'
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> runfcgi(func, addr=('localhost', 8000))</code><br />
<div style="margin-left:45px"><p>Runs a WSGI function as a FastCGI server.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> runscgi(func, addr=('localhost', 4000))</code><br />
<div style="margin-left:45px"><p>Runs a WSGI function as an SCGI server.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> runwsgi(func)</code><br />
<div style="margin-left:45px"><p>Runs a WSGI-compatible <code>func</code> using FCGI, SCGI, or a simple web server,
as appropriate based on context and <code>sys.argv</code>.</p></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> validaddr(string_)</code><br />
<div style="margin-left:45px"><p>Returns either (ip<em>address, port) or "/path/to/socket" from string</em></p>

<pre><code>&gt;&gt;&gt; validaddr('/path/to/socket')
'/path/to/socket'
&gt;&gt;&gt; validaddr('8000')
('0.0.0.0', 8000)
&gt;&gt;&gt; validaddr('127.0.0.1')
('127.0.0.1', 8080)
&gt;&gt;&gt; validaddr('127.0.0.1:8000')
('127.0.0.1', 8000)
&gt;&gt;&gt; validaddr('fff')
Traceback (most recent call last):
    ...
ValueError: fff is not a valid IP address/port
</code></pre></div></p>
</div>
<div style="margin-left:30px">
<p><span class="ts">function</span><code class="function"> validip(ip, defaultaddr='0.0.0.0', defaultport=8080)</code><br />
<div style="margin-left:45px"><p>Returns <code>(ip_address, port)</code> from string <code>ip_addr_port</code></p></div></p>
</div>
</div>
