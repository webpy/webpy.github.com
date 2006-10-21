---
layout: default
title: Serving Images
---

# Serving Images

## Basic Directory Set-up

First let your urls extend beyound images:

    import web
    
    urls = (
    '/images/(.*)', 'images' #this is where the image folder is located....
    )

## Basic Image Class
Now create the class that will handle them:

    class images:
        def GET(self,name):
            ext = name.split(".")[-1] # Gather extension
            
            cType = {
                "png":"images/png",
                "jpg":"image/jpeg",
                "gif":"image/gif",
                "ico":"image/x-icon"            }
            
            web.header("Content-Type", cType[ext]) # Set the Header
            print open('images/%s'%name,"rb").read() # Notice 'rb' for reading images
