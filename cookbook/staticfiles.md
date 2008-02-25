---
layout: default
title: Serving Static Files (such as js, css and images)
---

# Serving Static Files (such as js, css and images)

### Problem
How to serve static files with the web.py server?

### Solution

Create a directory (also known as a folder) called <code>static<code> in the location of the script that runs the web.py server. Then place the static files you wish to server in the static folder.

For example, the URL http://localhost/static/logo.png will send the image ./static/logo.png to the client.