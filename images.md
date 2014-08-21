---
layout: default
title: Serving Images
---

# Serving Images

## Basic Directory Set-up

First let your urls extend beyond images:

    import web
    
    urls = (
    '/images/(.*)', 'images' #this is where the image folder is located....
    )

## Basic Image Class
Now create the class that will handle them:

    import os
    class images:
        def GET(self,name):
            try:
                ext = name.split(".")[-1] # Gather extension
            except IndexError:
                raise web.notfound('Invalid request')
            
            cType = {
                "png":"images/png",
                "jpg":"images/jpeg",
                "gif":"images/gif",
                "ico":"images/x-icon"            }

            if name in os.listdir('images'):  # Security
                web.header("Content-Type", cType[ext]) # Set the Header
                return open('images/%s'%name,"rb").read() # Notice 'rb' for reading images
            else:
                raise web.notfound()
