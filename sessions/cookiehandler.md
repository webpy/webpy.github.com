---
layout: default
title: CookieHandler for Sessions
---

# CookieHandler for Sessions

# Specification

see [project blog post](http://planet-soc.com/node/2158)

bazaar branch at http://bazaar.launchpad.net/~karol.tarcak/webpy/webpy.sessions.cookie

## How to generate a RSA key file

    import web
    web.session.generate_key('some_rsa_file', 1024)


## Summary


## Implementation details

CookieHandler is a derivate of Handler.

### Public methods
 * store() -
 * retrieve() -
 * remove() -
 * clean() - it will do nothing, it's not possible to implement

### Requirements


[Sessions specs](/sessions)