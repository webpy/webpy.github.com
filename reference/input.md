---
layout: default
title: web.input()
---

# web.input()

web.input() contains a Storage object of all submitted form data.

## Checkboxes


## examples

## images
example by dmpayton. allows you to insert an image into a mysql blob column

    class upload: 
        def POST(self): 
            image = web.input(img={})['img'] 
            web.insert('image', mime=image.type, data=image.value, 
    name=image.filename) 

    class view: 
        def GET(self, id): 
            image = fn.oneResult(web.select('image', where="image_id='%d'" 
    % id, limit=1)) 
            web.header('Content-type', image['mime']) 
            print image['data'].tostring() 




