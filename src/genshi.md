---
layout: default
title: Templating with Genshi
---

# Templating with Genshi

code.py
-------

Put your "code.py" in root directory.

    # -*- coding: utf-8 -*-

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
    if __name__ == "__main__":
        app.run()

index.html
----------

Put your "index.html" in "template" directory.

    <?xml version="1.0" encoding="utf-8"?>
    <html xmlns:py="http://genshi.edgewall.org/">
    <body>
    <p>Hello, $name.</p>
    </body>
    </html>

refer
-----

* [genshi on gae 2010 - Genshi | Google Groups](http://groups.google.com/group/genshi/t/4f3fa1beddbd4ffc)
* [/trunk/examples/webpy – Genshi](http://genshi.edgewall.org/browser/trunk/examples/webpy?rev=332)
* [api docs (web.py)](http://webpy.org/docs/0.3/api)