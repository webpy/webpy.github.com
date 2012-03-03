---
layout: default
title: Philosophy
---

# The web.py Philosophy

The web.py slogan is: "Think about the ideal way to write a web app. Write the code to make it happen."

This is literally how I developed web.py. I wrote a web application in Python just imagining how I wanted the API to be. It started with <code>import web</code>, of course, and then had a place to define URLs, simple functions for GET and POST, a thing to deal with input variables and so on. Once the code looked right to me, I did whatever it took to make it execute _without changing the application code_ -- the result was web.py.

In response to someone complaining about web.py having "yet another template language", [I wrote a bit more about my philosophy](http://groups.google.com/group/webpy/msg/f266701d97e7ceb1):

> You don't have to use it -- each part of web.py is completely separate 
> from the others. But you're right, it is "yet another template 
> language". And I'm not going to apologize for it. 
> 
> The goal of web.py is to build the ideal way to make web apps. If 
> reinventing old things with only small differences were necessary to 
> achieve this goal, I would defend reinventing them. The difference 
> between the ideal way and the almost-ideal way is, as Mark Twain 
> suggested, the difference between the lightning and the lightning bug. 
> 
> But these aren't just small differences. Instead of exposing Python 
> objects, web.py allows you to build HTTP responses. Instead of trying 
> to make the database look like an object, web.py makes the database 
> easier to use. And instead of coming up with yet another way to write 
> HTML, the web.py template system tries to bring Python into HTML. Not 
> many other people are really trying to do that. 
> 
> You can disagree that these ways are better and say why. But simply 
> criticizing them for being different is a waste of time. Yes, they are 
> different. That's the whole point.
