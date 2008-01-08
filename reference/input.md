---
layout: default
title: web.input()
---

# web.input()

`web.input` gives you access to any variables the user submitted through a form. 

<b>returns:</b> Storage object


## Checkboxes
In order to access data from multiple identically named items in a list format (e.g.: a series of checkboxes all with the attribute name="name") use:

## basic usage

        class add:
            def POST(self):
                i = web.input()
                n = web.insert('todo', title=i.title)
    	        web.seeother('/')

(Notice how we're using `POST` for this?)


## images
example by dmpayton. allows you to insert an image into a mysql blob column

    class upload: 
        def POST(self): 
            image = web.input(img={})['img'] 
            web.insert('image', mime=image.type, data=image.value, 
    name=image.filename) 

    class view: 
        def GET(self, id): 
            image = fn.oneResult(web.select('image', where="image_id='%d'" % id, limit=1)) 
            web.header('Content-type', image['mime']) 
            print image['data'].tostring() 




