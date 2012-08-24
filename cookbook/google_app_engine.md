---
layout: default
title: Webpy + Google App Engine
---

# Webpy + Google App Engine

This cookbook entry explains how to run web.py as a google app engine application

### Requirements

* Google App Engine Python API
* web.py .38 or later

### Resources

* [Google App Engine](https://developers.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python)

###  Notes
* The mechanisms for running GAE in python2.7 and 2.5 are different, change the app.yaml accordingly
* code.py is the main file of your application (2.5)
* code.app is the object that cointains the return value of gaerun() (2.7)
* appname is the name that you specified while creating your GAE application
* runtime for 2.5 is python, 2.7 is python27
* threadsafe is only required in 2.7, read about it on the google app engine site

## app.yaml for python 2.5

	application: appname
	version: 1
	runtime: python
	api_version: 1

	handlers:
	- url: /.*
	  script: code.py

## app.yaml for python 2.7

	application: appname
	version: 1
	runtime: python27
	api_version: 1
	threadsafe: true

	handlers:
	- url: /.*
	  script: code.app

To serve static files, you must add this under handlers (where static is the name of your static dir):
    - url: /static
      static_dir: static

## Hello World!

This is a sample application that can be run by using dev_appserver.py (it is bundled with the SDK download):

	import web

	urls = (
		"/.*", "hello",
	)

	app = web.application(urls, globals())

	class hello:
		def GET(self):
			return 'Hello, world!'

	app = app.gaerun()

Save this as code.py (or whatever you specified in app.yaml) and type:
dev_appserver.py .

Now visit localhost:8080 in your browser and you should see hello world!

## NOTES

### There is a blank page or an internal server error

solution: Make sure that you are running the version of python specified in the app.yaml file

### dev_appserver.py is not found

solution: Make sure that it is in your path
