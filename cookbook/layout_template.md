---
layout: default
title: Site Layout Template
---

# Site Layout Template

### Problem

How to support layout template in web.py applications.

### Solution

This can be done using application processors.

    app = web.application(urls, gloabals)
    render = web.template.render('templates/')
   
    def layout_processor(handle):
        result = handle()
        return render.layout(result)

    app.add_processor(layout_processor)

