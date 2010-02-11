---
layout: default
title: File Upload Recipe
---

# File Upload Recipe

Other languages: [français](/../cookbook/fileupload/fr) | ...

## Problem

File uploads can be a little tricky if you're not familiar with form uploads, or CGI in general.

## Solution

    import web
    
    urls = ('/upload', 'Upload')
    
    class Upload:
        def GET(self):
            return """<html><head></head><body>
    <form method="POST" enctype="multipart/form-data" action="">
    <input type="file" name="myfile" />
    <br/>
    <input type="submit" />
    </form>
    </body></html>"""
    
        def POST(self):
            x = web.input(myfile={})
            web.debug(x['myfile'].filename) # This is the filename
            web.debug(x['myfile'].value) # This is the file contents
            web.debug(x['myfile'].file.read()) # Or use a file(-like) object
            raise web.seeother('/upload')


    if __name__ == "__main__":
       app = web.application(urls, globals()) 
       app.run()

## Hang ups

A couple of things to watch out for:

* The form needs an attribute enctype="multipart/form-data", or this won't work correctly.
* In the webpy code, a default value is needed (the myfile={} part) if you want it to be imported as a CGI FieldStorage object.  If you don't specify the default value, the file will be passed as a string -- this works, but you lose the filename attribute.