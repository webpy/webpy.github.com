---
layout: default
title: Custom NotFound message
---

# Custom NotFound message



## Problem

How to customize notfound and other messages?

## Solution

    import web
    web.webapi.NotFound.message = "Sorry, the page you were looking for was not found."

In the same way InternalError message can also be customized.

    import web
    web.webapi.InternalError.message = "Bad, bad server. No donut for you."


