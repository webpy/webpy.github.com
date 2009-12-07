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
    from genshi.template import TemplateLoader

    loader = TemplateLoader(['.'], auto_reload=True)
    tmpl = loader.load('./templates/index.html')

    urls = (
        '/', 'index'
    )

    class index:
        def GET(self):
            name = 'John Doe'
            stream = tmpl.generate(name=name)
            return stream.render('html')

    app = web.application(urls, globals())
    if __name__ == "__main__": app.run()

index.html
----------

Put your "index.html" in "template" directory.

    <?python title="My Genshi template"?>
    <html xmlns:py="http://genshi.edgewall.org/">
    <body>
    <p>Hello, $name.</p>
    </body>
    </html>

refer
-----

* [genshi on gae 2010 - Genshi | Google Groups](http://groups.google.com/group/genshi/t/4f3fa1beddbd4ffc)
* [/trunk/examples/webpy – Genshi](http://genshi.edgewall.org/browser/trunk/examples/webpy?rev=332)