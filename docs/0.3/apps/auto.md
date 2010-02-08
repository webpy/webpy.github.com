---
layout: default
title: Auto Application
---

# Auto Application

Other languages : [français](/docs/0.3/apps/auto/fr) | ...

The auto application acts like the [basic application](/docs/0.3/apps/basic), only it doesn't require a URL mapping to be created.  The mapping is derived from the class names (using metaclasses). In it's most basic form:

## Example code 

     app = web.auto_application() 

     class hello(app.page): 
         def GET(self): 
             return "hello, world!"
     
     if __name__ == '__main__':
         app.run() # goto http://hostname:8080/hello


You can also override the default path (which is the name of the class) by setting a class variable "path".  See below:


## More Example code 

    app = web.auto_application() 
    
    class hello(app.page): 
        path = "/foobar"
        def GET(self): 
            return "hello, world!" 
    
    if __name__ == '__main__':
        app.run() # goto http://hostname:8080/foobar