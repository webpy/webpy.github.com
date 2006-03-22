---
layout: default
title: faq
---

# faq

99. How do I use template.py templates?

    For basic doc and some code snippets, see [Aaron's original description of template.py (codename: templetor)](http://groups.google.com/group/webpy/msg/4e2d8496397384e9?hl=en)

    To display your page from inside a web.py app, just do

            homepage = template.Template(open("homepage.tmpl").read())
            print homepage()

    $set seems buggy.
    
99. next question...
