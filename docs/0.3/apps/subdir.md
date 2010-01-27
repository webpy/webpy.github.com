---
layout: default
title: Subdir application
---

# Subdir application

A subdir application lets you run various mount points on the same hostname, but switched based on directory mount point.


This example assumes you have applications already working and called "app" defined in wiki.py, blog.py and auth.py. 


## Example code

    import wiki 
    import blog 
    import auth 

    mapping = ( 
        "/wiki", wiki.app, 
        "/blog", blog.app, 
        "/auth", auth.app) 

    app = web.subdir_application(mapping)

    if __name__ == '__main__:
        app.run()

Now, going to /wiki/ will send the trailing / to the wiki.app, and its return data will be displayed as normal.