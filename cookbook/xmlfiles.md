---
layout: default
title: Serving XML
---

# Serving XML

Other languages:  [français](/../cookbook/xmlfiles/fr) | ...

### Problem

How to serve XML files correctly?

This is needed when you have a third-party application posting data to your service and expecting some kind of XML response.

### Solution

Create your XML template with the XML file you want to serve (i.e. response.xml). If the XML has any variables, use the corresponding web.py templating code. This is just an example:

    $def with (code)
    <?xml version="1.0"?>
    <RequestNotification-Response>
    <Status>$code</Status>
    </RequestNotification-Response>

To serve this file, create a standard Web.Py program (i.e. response.py) and use the following code. Be aware that you should use <code>web.header('Content-Type', 'text/xml')</code> to tell the client that you are sending a XML file. (You don't need to set the header explicitly for XML files if your template file has the ``.xml`` extension.)


    import web

    render = web.template.render('templates/', cache=False)

    urls = (
        '/(.*)', 'index'
    )

    app = web.application(urls, globals())

    class index:
        def GET(self, code):
            web.header('Content-Type', 'text/xml')
            return render.response(code)

    web.webapi.internalerror = web.debugerror
    if __name__ == '__main__': app.run()