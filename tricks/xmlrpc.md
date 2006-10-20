---
layout: default
title: tricks/xmlrpc
---

# tricks/xmlrpc

This is a simple recipe how to use XMLRPC with web.py

I wrote some generic xmlrpc adaptor for web.py and drop it to webxml.py,
you can see this below

    import web
    from SimpleXMLRPCServer import SimpleXMLRPCDispatcher
    dispatcher = SimpleXMLRPCDispatcher()

    def init(urllist):
        global dispatcher
        for it in range(len(urllist)/2):
            dispatcher.register_function(urllist[it], urllist[it+1])

    class rpc:
        def GET(self):
            global dispatcher
            methods = dispatcher.system_listMethods()
            web.header('Content-Type', 'text/html')
            print "<body><h1>Error!</h1>"            print "Method GET is not alowed for XMLRPC requests"            print "List of available methods:"            print "<ul>"            for method in methods:
                sig = dispatcher.system_methodSignature(method)
                help =  dispatcher.system_methodHelp(method)
                print "<li><b>%s</b>: [%s] %s</li>" % (method, sig, help)
            print "</ul>"            print "Be careful"            print "</body>"
        def POST(self):
            global dispatcher
            response = dispatcher._marshaled_dispatch(web.webapi.data())
            web.header('Content-length', str(len(response)))
            print response