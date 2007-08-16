---
layout: default
title: Google Summer of Code: web.py - Session management
---

# Google Summer of Code: web.py - Session management

[project blog](http://planet-soc.com/blog/77) at [planet-soc.com](http://planet-soc.com/)

# Currently
tracking on [launchpad.net bugs](https://bugs.launchpad.net/~karol.tarcak/?field.searchtext=&orderby=-importance&search=Search&field.status%3Alist=New&field.status%3Alist=Incomplete&field.status%3Alist=Confirmed&field.status%3Alist=Triaged&field.status%3Alist=In+Progress&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_contact=&field.status_upstream-empty-marker=1&field.omit_dupes.used=&field.omit_dupes=on&field.has_patch.used=&field.tag=&field.has_cve.used=)

 * testing & docs - WORKING
 * FileHandler - clean() - DONE
 * CookieHandler - see [project blog](http://planet-soc.com/node/2158)
 * online migration between handlers?



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
