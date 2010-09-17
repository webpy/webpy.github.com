---
layout: default
title: Templating with Genshi
---

# Templating with Genshi

<p> 
 
<h2>code.py</h2> 
<p>Put your &quot;code.py&quot; in root directory.
</p> 
<pre><code># -*- coding: utf-8 -*-
 
import web
from web.contrib import template
 
render = template.render_genshi(['./templates/'])
 
urls = (
    '/', 'index'
)
 
class index:
    def GET(self):
        name = 'John Doe'
        return render.index(name=name)
 
app = web.application(urls, globals())
if __name__ == &quot;__main__&quot;:
    app.run()
</code></pre> 
<h2>index.html</h2> 
<p>Put your &quot;index.html&quot; in &quot;template&quot; directory.
</p> 
<pre><code>&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;
&lt;html xmlns:py=&quot;http://genshi.edgewall.org/&quot;&gt;
&lt;body&gt;
&lt;p&gt;Hello, $name.&lt;/p&gt;
&lt;/body&gt;
&lt;/html&gt;
</code></pre> 
<h2>refer</h2> 
<ul> 
 <li> 
     <a href="http://groups.google.com/group/genshi/t/4f3fa1beddbd4ffc">genshi on gae 2010 - Genshi | Google Groups</a> 
 </li> 
 
 <li> 
     <a href="http://genshi.edgewall.org/browser/trunk/examples/webpy?rev=332">/trunk/examples/webpy – Genshi</a> 
 </li> 
 
 <li> 
     <a href="http://webpy.org/docs/0.3/api">api docs (web.py)</a> 
 </li> 
</ul> 
 
 
</p>