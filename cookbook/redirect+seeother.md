---
layout: default
title: web.redirect and web.seeother
---

# web.redirect and web.seeother

Other languages:  [français](/../cookbook/redirect+seeother/fr) | ...

## web.redirect and web.seeother

### Problem
After processing user input (from a form, let's say), you want to redirect them to another page.

### Solution

    class SomePage:
        def POST(self):
            # Do some application logic here, and then:
            raise web.seeother('/someotherpage')

When a post is sent to this function, on completion it will send the browser an http code 303, and the new location. The browser will then perform a GET on the location defined in the seeother argument.

Note: web.seeother and web.redirect are made exceptions in 0.3.

### Hangups
It's unlikely that you want to use the web.redirect function very often -- it appears to do the same thing, but it sends the http code 301, which is a permanent redirect.  Most web browsers will cache the new redirection, and will send you to that location automatically when you try to perform the action again.  A good use case for redirect is when you're changing the URL structure of your site, but want the old links to work due to bookmarking.