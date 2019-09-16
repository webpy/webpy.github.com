---
layout: default
title: Serving Images
---

# Serving Images

## Basic Directory Set-up

First let your urls extend beyond images:

```
import web
    
urls = (
    '/images/(.*)', 'images' # serve image files with url prefix '/images/'
)
```

## Basic Image Class

Now create the class that will handle them:

```
import os
import web


class images:
    def GET(self, name):
        ext = name.split(".")[-1]

        content_types = {
            "png": "image/png",
            "jpg": "image/jpeg",
            "gif": "image/gif",
            "ico": "image/x-icon",
        }

        if name in os.listdir("images"):  # Security
            web.header("Content-Type", content_types[ext.lower()])
            return open("images/%s" % name, "rb").read()  # reading with 'rb'
        else:
            raise web.notfound()
```
