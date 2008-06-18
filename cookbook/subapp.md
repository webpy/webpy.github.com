---
layout: default
title: using subapplications
---

# using subapplications

        class blog:
            def GET(self, path):
                return "blog " + path
        app_blog = web.application(urls, locals())
        
        urls = (
            "/blog", app_blog,
            "/(.*)", "index"
        )
        class index:
            def GET(self, path):
                return "hello " + path
        app = web.application(urls, locals())
