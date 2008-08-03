---
layout: default
title: web.py 0.3 tutorial
---

# web.py 0.3 tutorial

This is a work-in-progress


## TODO: `web.webapi.internalerror = web.debugerror` in 0.3?

## TODO: Show/hide complete code at the end of sections

TODO: move the next paragraph over to install?

To create a website with web.py you need to know the Python programming language and have it installed. Installation instructions for Python can be found at [http://python.org/]. If you don't know if Python is installed on your system, open a terminal and type `python`. A great starting point to learn Python is the official [tutorial] (http://docs.python.org/tut/tut.html). If you are new to programming in general, [Think Python] (http://www.greenteapress.com/thinkpython/) is a wonderful book to understand key concepts in programming. 

## TOC

TODO: ...


## Prerequisites

This tutorial assumes that both Python and web.py are installed on your system. If this is not the case, please follow the [installation instructions] (http://webpy.org/install) before you continue.


## Hello Web in web.py

Open your favorite text editor and create a new file `hello.py`. In this file you will define the content and logic of your web application as well as its web addresses (URLs).

Before you are able to use the tools web.py provides, you need to import the web.py module with the following code:

    import web

In web.py web pages are mapped to Python classes. Let's create the code for the first page which is here called `Hello`:

    class Hello:
        def GET(self):
            return "Hello, Web!"

The `Hello` class has a function named `GET` which returns "Hello, Web!". Why `GET`?

When you open a web page, your browser asks for the content of that page. This request is called the `GET` method. web.py uses the same terminology. The string your `GET` method returns is displayed in your browser.

Although the code for your first page is written, it cannot yet be opened in a browser. Let's proceed with mapping a web address (URL) to your class. Insert the following code after the import statement:

    urls = (
      '/', 'Hello')

This tells web.py to map the root of your website (like http://webpy.org/) to your Python class named `Hello`.

Next create an instance of a web.py application. This instance will be the mediator between your classes and the web. It will handle browser requests and serve your pages. (In short: It will do everything that you really don't want to care about.) Use the following code:

    app = web.application(urls, globals())

Note that `web.application()` gets called with two arguments. Your URL mapping (`urls`) and your global namespace which contains your `Hello` class (`globals()`).

To finish your web.py application insert the following code at the end of your code:

    if __name__ == "__main__":
        app.run()

`app.run()` starts the web application to serve requested pages.

### Complete code

hello.py

    import web
    
    urls = (
      '/', 'Hello')

    app = web.application(urls, globals())
    
    class Hello:
        def GET(self):
            return 'Hello, web!'
    
    if __name__ == "__main__":
        app.run()

Save the file and run the following command to start your application:

    python hello.py

The first output of your application is the address of your web site. By default this is:

    http://0.0.0.0:8080/

Open this address with your web browser. That's it. Congrats! You can stop your application at any time by pressing `ctrl+c` in the terminal.

Note: You can also visit your site at `http://localhost:8080/`


## Having multiple pages

In this part you will learn how to manage multiple pages. Let's add another class to your 'Hello Web' application:

    class Bye:
        def GET(self):
            return 'Bye, web!'

As mentioned above, each page needs a unique address. Modify your list of URLs as follows:

    urls = (
      '/', 'Hello',
      '/bye/', 'Bye')

This will make your class `Bye` respond to requests at `/bye/`. Now start your application and open `http://localhost:8080/bye/` in your browser.

Note: Currently you need to restart your application to see any changes. Try to pass a third argument to `web.application` and restart your application:

    app = web.application(urls, globals(), web.reloader)


Future changes can now be seen instantly, although you might need to reload a page in your browser.

### Complete code

hello.py

    import web
    
    urls = (
      '/', 'Hello',
      '/bye/', 'Bye')
    
    app = web.application(urls, globals(), web.reloader)
    
    class Hello:
        def GET(self):
            return time.ctime()
    
    class Bye:
        def GET(self):
            return 'Bye, web!'
    
    if __name__ == "__main__":
        app.run()


## Dynamic content

Until now your pages contained only static strings that did not change between your visits. Add the current time stamp to your page. Import Python's `time` module:

    import time

Then change your `Hello` class as follows:

    class Hello:
        def GET(self):
            return "The time is:    " + time.ctime()

Open the page and reload it several times. You will see that the page is dynamically created at each request.

### Complete code

hello.py

    import time
    import web
    
    urls = (
      '/', 'Hello')
    
    app = web.application(urls, globals(), web.reloader)
    
    class Hello:
        def GET(self):
            return "The time is:    " + time.ctime()
    
    if __name__ == "__main__":
        app.run()


## HTML in Python

Until now your classes returned only simple strings. Let's add some HTML. This can be done directly from inside your `hello.py`. Replace your class `Hello` with this code:

    class Hello:
        def GET(self):
            return """<html>
    <head>
    <title>Hello, web!</title>
    </head>
    <body>
    <h1>web.py</h1>
    <p>Think about the <em>ideal</em> way to write a web app. Write the code to <b>make it happen</b>.</p>
    </body>
    </html>"""

Note that your page now has a custom title and HTML formatted content.

### Complete code

hello.py

    import web
    
    urls = (
      '/', 'Hello',
      '/bye/', 'Bye')
    
    app = web.application(urls, globals(), web.reloader)
    
    class Hello:
        def GET(self):
            return """<html>
    <head>
    <title>Hello, web!</title>
    </head>
    <body>
    <h1>web.py</h1>
    <p>Think about the <em>ideal</em> way to write a web app. Write the code to <b>make it happen</b>.</p>
    </body>
    </html>"""
    
    if __name__ == "__main__":
        app.run()


## HTML with site layout templates

Imagine a larger site with many pages. If all HTML for these pages is embedded into your Python code, things get messy and your code unmaintainable. Also reusing parts of your HTML code for other pages would be difficult. Therefore web.py lets you define site layout templates that can be shared between your pages.

First create a directory `templates` next to your `hello.py` file. Create a file `layout.html` and save it in `templates`. This file will contain the HTML markup that is used to render your page. Start with the following basic template:

     $def with (page)
    
    <html>
    <head>
    <title>Template demo</title>
    </head>
    <body>
    <p>You are visiting page <b>$page</b>.</p>
    </body>
    </html>
    
Besides defining a page structure, this template will use the Python variable `page` wherever `$page` is used. When using this template you will need to pass some value to the template as an argument.

Next add a so-called layout processor to your application. A layout processor will tell your application which template it should use:

    app = web.application(urls, globals(), web.reloader)
    
    render = web.template.render('templates/')  # 'templates/' is your template directory
    
    def layout_processor(handle):
        result = handle()
        return render.layout(result)  # 'layout' is your template's file name
    
    app.add_processor(layout_processor)
    
One last step. Modify your `Hello` and `Bye` classes to return the name of the current page:

    class Hello:
        def GET(self):
            return "Hello"
    
    class Bye:
        def GET(self):
            return "Bye"

Open the page in your browser. web.py fetches your template and inserts the name of the current page whereever your template contains `$page`.

### Complete code

hello.py

    import web
    
    urls = (
      '/', 'Hello',
      '/bye/', 'Bye')
    
    app = web.application(urls, globals(), web.reloader)
    
    render = web.template.render('templates/')
    
    def layout_processor(handle):
        result = handle()
        return render.layout(result)
    
    app.add_processor(layout_processor)
    
    class Hello:
        def GET(self):
            return "Hello"
    
    class Bye:
        def GET(self):
            return "Bye"
    
    if __name__ == "__main__":
        app.run()
        
templates/layout.html

    $def with (page)
    
    <html>
    <head>
    <title>Template demo</title>
    </head>
    <body>
    <p>You are visiting page <b>$page</b>.</p>
    </body>
    </html>

    
## Static content

Now that your application serves HTML formatted content, you probably want to include static files like images or css style files. To achieve this create a directeory called `static` next to your `hello.py` file. Put a picture file (here called `logo.png`) in your `static` directory. Then include the file on your page:

    class Hello:
        def GET(self):
            return """<img src="./static/logo.png">"""

### Complete code

hello.py

    import web
    
    urls = (
      '/', 'Hello')
    
    app = web.application(urls, globals(), web.reloader)
    
    class Hello:
        def GET(self):
            return """<img src="./static/logo.png">"""
    
    if __name__ == "__main__":
        app.run()