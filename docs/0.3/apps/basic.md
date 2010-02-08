---
layout: default
title: Basic Application
---

# Basic Application

Other languages : [français](/docs/0.3/apps/basic/fr) | ...

The basic application defines a pairing of urls to class mappings.  In the example below, the urls variable defines a pairing of a regular expression to a class name. 

When a user access a resource, runs through the list of url regular expressions.  If a url matches the regex, the class is instantiated, and the method 'GET' or 'POST' is called based on the http method. Data returned from the GET or POST is displayed in the browser.

If the requested url doesn't match any regex, a 404 is returned.


## Example

    import web
            
    urls = (
        '/(.*)', 'hello'
    )
    app = web.application(urls, globals())
    
    class hello:        
        def GET(self, name):
            if not name: 
                name = 'World'
            return 'Hello, ' + name + '!'
    
    if __name__ == "__main__":
        app.run()