---
layout: default
title: Google Summer of Code: web.py - Session management
---

# Google Summer of Code: web.py - Session management

[project blog](http://planet-soc.com/blog/77) at [planet-soc.com](http://planet-soc.com/)

## Post GSoC work
 * WSGI
 * online migration between handlers?


## End of GSoC
 * FileHandler
 * CookieHandler - see project blog [first](http://planet-soc.com/node/2158) and [second](http://planet-soc.com/node/2477) post


## OLD Schedule - [DONE](https://bugs.launchpad.net/~karol.tarcak/)
 * May 28 - June 9 (1st & 2nd week): getting familiar with SVN/Bazaar, internals of web.py, flup and jonpy's sessions; creating a DDL for storing sessions
 * June 10 - June 17 (3rd): creating DBHandler class
 * June 18 - July 8 (4th - 6th): creating Session class's identify/verify methods
 * July 9 - mid-term evulation deadline
 * July 10 - August 19 (7th - ...): finishing the Session class
 * August 20 - final evaluation deadline

## Tasks

### Administrative
 * Bazaar/SVN
 * blog

### DBHandler
 * create table DDL
 * write store(), retrieve(), remove()
 * test (& some docs)

### Session
 * write default session id generator(s)
 * write & test session cookie creation, identification, verification
 * write & test session id regeneration (mainly cookies & session identification)
 * write start()
 * write save()
 * write destroy(), cleanup()
 * test & docs
