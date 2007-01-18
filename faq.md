---
layout: default
title: faq
---

# faq

99. **How do I use template.py templates?**

    For basic doc and some code snippets, see [template.py doc](/templetor)

    To display your page from inside a web.py app, just do

            homepage = template.Template(open("homepage.tmpl").read())
            print homepage()

    
99. **Why are the urls just one long list?**

    If they were a dictionary, they wouldn't be ordered. If it was a list of tuples, then it'd be a lot more typing.

99. **Where can I go for additional help?**

    Google Groups has a [web.py group](http://groups.google.com/group/webpy) that is quite helpful.