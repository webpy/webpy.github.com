---
layout: default
title: template tricks
---

# template tricks

Test the rendering of a template.py template

        def renderTemplate(templatename,*args,**kw):
            '''quick way to test a template.py template'''            import template
            if not "." in templatename:
                templatename = templatename + ".tmpl"            obj = template.Template(open(templatename).read())
            return obj(*args,**kw)

        print renderTemplate("homepage", now=time.ctime())

If your template takes a dict or a storage, then you can just
set global values and let those get passed in:

        username = "User"        lastvisit = "yesterday"        print renderTemplate("results", store=web.Storage(globals()))