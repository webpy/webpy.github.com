---
layout: default
title: web.py 0.3 tutorial
---

# web.py 0.3 tutorial

This is a work-in-progress

## TODO: `web.webapi.internalerror = web.debugerror` in 0.3?
## TODO: Show/hide complete code at the end of sections
## TODO: move over to install?

To create a website with web.py you need to know the Python programming language and have it installed. Installation instructions for Python can be found at [http://python.org/]. If you don't know if Python is installed on your system, open a terminal and type `python`. A great starting point to learn Python is the official [tutorial] (http://docs.python.org/tut/tut.html). If you are new to programming in general, [Think Python] (http://www.greenteapress.com/thinkpython/) is a wonderful book to understand key concepts in programming. 

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

Complete code:

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

Complete code:

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

Open the page and reload it several times. You will see that the page is dynamically created for each visit.

Complete code:

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

Complete code:

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

## HTML with templates

Imagine a larger site with many pages. If all HTML for these pages is embedded into your Python code, things get messy and your code unmaintainable. Also reusing parts of your HTML code for other pages would be difficult. Therefore web.py lets you define templates that can be shared between your pages.

