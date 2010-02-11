---
layout: default
title: web.input
---

# web.input

Other languages: [français](/../cookbook/input/fr) | ...

##web.input

### Problem
You want user data from a form, or a url encoded parameter.

### Solution
The web.input() method returns a web.storage object (a dictionary-like object) that contains the variables from the url (in a GET) or in the http header (in a POST).  For example, if you go to the page http://example.com/test?id=10, on the Python backend you'll want to extract that the id=10.  Using web.input(), this becomes trivial:

    class SomePage:
        def GET(self):
            user_data = web.input()
            return "<h1>" + user_data.id + "</h1>"

Sometimes you may want to specify a default variable, in case none is given.  The same code with a default value for x:

    class SomePage:
        def GET(self):
            user_data = web.input(id="no data")
            return "<h1>" + user_data.id + "</h1>"

Note that the web.input() values will be strings even if there are numbers passed to it.  


What if you pass several of the same variable names, like this:

<select multiple size="3"><option>foo</option><option>bar</option><option>baz</option></select>

You need to let web.input know to expect multiple inputs, or it will clobber all but one.  Pass the default value of a list to web.input and it will work correctly.  For example, going to http://example.com?id=10&id=20:

    class SomePage:
        def GET(self):
            user_data = web.input(id=[])
            return "<h1>" + ",".join(user_data.id) + "</h1>"