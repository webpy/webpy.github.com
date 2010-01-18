---
layout: default
title: Usage
---

# Usage

<hr id=toc>

1.  [Hello World](#hello-world)

<h2 id=hello-world>Hello World</h2>

<pre><code>"""
hello world

>>> for uri in ('/', '/foo', '/bar'):
...   assert web.request(uri).status == '200 OK'

"""

import web

resources = (
  r'/(.*)', 'Hello'
)
webapp = web.application(resources, globals())

class Hello:
  """
  say "Hello"
  
  >>> webapp.request('/').data
  'Hello World'
  >>> webapp.request('/Fnord').data
  'Hello Fnord'

  """
  def GET(self, name):
    if not name: 
        name = 'World'
    return 'Hello ' + name + '!'

if __name__ == '__main__':
  app.run()</code></pre>

<style>
@import url(http://angelo.gladding.name/assets/webpy-redesign.css);
@import url(http://angelo.gladding.name/assets/js-prettify/prettify.css);
</style>
<script src=http://angelo.gladding.name/assets/jquery.js></script>
<script src=http://angelo.gladding.name/assets/js-prettify/prettify.js></script>
<script>$(document).ready(function() { prettyPrint(); });</script>