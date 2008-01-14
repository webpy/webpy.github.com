---
layout: default
title: web.header()
---

# web.header()

used to pass a proper header to the web browser before print statements, so that those print statements are interpreted by the web browser as html.  

## standard html example

    web.header('Content-Type','text/html; charset=utf-8', unique=True) 

## image example

     web.header('Content-type', 'image/jpeg') 
