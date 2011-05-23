---
layout: default
title: Deploying web.py on IIS7 via PyISAPIe
---

# Deploying web.py on IIS7 via PyISAPIe

This guide is an account of the various steps, including snippets of relevant code that tweaked and added, in order to get a `web.py` script to work on IIS7 using `PyISAPIe`.  Please note that you must have Python as well as the [PyWin32 extensions][0] installed on Windows. _This guide was tested on two different 64-bit versions of Windows server with 32-bit versions of Python 2.6.6 installed and on IIS7 and IIS6_. 

First and foremost, I had to install the `web.py` module on the system. Having had trouble before with IIS with `web.py` installed through `easy_install`, I decided to be safe and installed it from source. Getting `web.py` to work with PyISAPIe required a small hack. In the file `Lib\site-packages\web\wsgi.py` lies the following function: 

    def _is_dev_mode():
        # quick hack to check if the program is running in dev mode.
        if os.environ.has_key('SERVER_SOFTWARE') \
            or os.environ.has_key('PHP_FCGI_CHILDREN') \
            or 'fcgi' in sys.argv or 'fastcgi' in sys.argv \
            or 'mod_wsgi' in sys.argv:
                return False
        return True

In its pristine state, when `web.py` is imported from a source file through PyISAPIe, an exception is thrown. The exception, while I don't have the exact message, is about it complaining about `sys.argv` not having an attribute `argv`, which reads fishy. Since the function `_is_dev_mode()` only checks whether `web.py` is being run in development mode, I thought I didn't care about it since I wanted everything to run in production mode. I edited the function such that its body would be bypassed, while it returned a `False` boolean value. It looked like this:

    def _is_dev_mode():
        return False
        # quick hack to check if the program is running in dev mode.
        if os.environ.has_key('SERVER_SOFTWARE') \
            or os.environ.has_key('PHP_FCGI_CHILDREN') \
            or 'fcgi' in sys.argv or 'fastcgi' in sys.argv \
            or 'mod_wsgi' in sys.argv:
                return False
        return True

This innocuous little addition did away with the exception.

Next up, I used default Hello World-esque example of `web.py`. I called it `code.py` (I placed it inside the folder `C:\websites\myproject`). It looked like this:

      import web
      urls = (
          '/.*', 'hello',
          )
      class hello:
          def GET(self):
              return "Hello, world."
      application = web.application(urls, globals()).wsgifunc()

It was pretty simple. You have to pay particular attention on the call to `web.application`. I called the `wsgifunc()` to return a WSGI-compatible function to boot the application.  

I set up a website under IIS using the IIS Management Console. Since I was working on a 64-bit server edition of Windows and had chosen to use 32-bit version of Python and all modules, I made sure to enable **32-bit support** for the application pool being used for the website. This was important. 

I decided to keep the PyISAPIe folder inside the folder where `code.py` rested. This PyISAPIe folder contained the `PyISAPIe.dll` file, and the `Http` folder. Inside the `Http` folder, I placed the most important file of all: the `Isapi.py`. That file could be thought of as the starting point for each request that is made, what glues the Request to the proper Handler and code. I worked with the `Examples\WSGI\Isapi.py` available as part of PyISAPIe. I tweaked the file to look like this:


    from Http.WSGI import RunWSGI
    from Http import Env
    #from md5 import md5
    from hashlib import md5
    import imp
    import os
    import sys
    sys.path.append(r"C:\websites\myproject")
    from code import application
    ScriptHandlers = {
        "/api/": application,
    }
    def RunScript(Path):
      global ScriptHandlers
      try:
        # attempt to call an already-loaded request function.
        return ScriptHandlers[Path]()
      except KeyError:
        # uses the script path's md5 hash to ensure a unique
        # name - not the best way to do it, but it keeps
        # undesired characters out of the name that will
        # mess up the loading.
        Name = '__'+md5(Path).hexdigest().upper()
        ScriptHandlers[Path] = \
          imp.load_source(Name, Env.SCRIPT_TRANSLATED).Request
        return ScriptHandlers[Path]()
    # URL prefixes to map to the roots of each application.
    Apps = {
      "/api/" : lambda P: RunWSGI(application),
    }
    # The main request handler.
    def Request():
      # Might be better to do some caching here?
      Name = Env.SCRIPT_NAME
      # Apps might be better off as a tuple-of-tuples,
      # but for the sake of representation I leave it
      # as a dict.
      for App, Handler in Apps.items():
        if Name.startswith(App):
          return Handler(Name)
      # Cause 500 error: there should be a 404 handler, eh?
      raise Exception, "Handler not found."

The important bits to note in the above code are the following:

* I import `application` from my `code` module. I set the PATH to include the directory in which the file `code.py` is so that the `import` statement does not complain. (I've to admit that the idea of import `application` and feeding it into `RunWSGI` came to while I was in the loo.)
* I defined a script handler which matches the URL prefix I want to associate with my `web.py` script. (_In hindsight, this isn't necessary, as the `RunScript()` is not being used in this example_).
* In the `Apps` dictionary, I again route the URL prefix to the `lambda` function which actually calls the `RunWSGI` function and feeds it `application`. 
* I also imported the `md5` function from the `hashlib` module instead of the `md5` module as originally defined in the file. This was because Python complained about `md5` module being deprecated and suggested instead of use `hashlib`.

I then defined a wild-card (Script map) extension in IIS for the website, mapping all requests to the `PyISAPIe.dll` file in _my project folder_. Which `PyISAPIe.dll` file is used is important. By default, it will look for the `Http` folder in the same directory where the DLL is. I restarted IIS (and possibly even Windows, just to be sure).

And that's pretty much it.

There's a caveat though. If you have specific URLs in your `web.py` script, you will have to modify each of those URLs to add the `/api/` prefix to them (or whatever URL prefix you set in the `Isapi.py`). Without that, `web.py` will not match any URLs in the file.

Good luck!

_PS: If you want to avoid using PyISAPIe, there is a simpler way of deploying web.py on IIS. It is documented crudely over [here][1]._

[0]: http://sourceforge.net/projects/pywin32/
[1]: http://forums.iis.net/t/1122937.aspx
