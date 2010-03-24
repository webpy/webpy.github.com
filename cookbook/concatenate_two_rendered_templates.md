---
layout: default
title: How to concatenate two rendered templates?
---

# How to concatenate two rendered templates?

### Problem:

How to concatenate two rendered templates?

### Solution:

    render = web.template.render('templates')

    def GET(): 
        article = render.article() 
        comments = render.comments() 
        return render.index(unicode(article), unicode(comments))