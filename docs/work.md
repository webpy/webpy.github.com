---
layout: default
title: webpy docs that need fixing, and how!
---

# webpy docs that need fixing, and how!

This is a list of work needed for the documentation cleanup.  Please add pages, separated by horizontal rules (three asterisks in markdown).

We need both reporters (tell us what's wrong!) and fixers (write code, make content consistent, etc).

When adding work to be done, please place it in a section devoted to the page and/or parent page, and a link to that page. For example:

***
#Cookbook: [Cookbook](/cookbook)
* database select example code is incorrect

***

When finishing working on something, delete it from the list. If a code block refers to old (version 0.2 for example) code, please add it to a separate url.  Also, add new content at new url (and delete old link when done) For instance:

1. /foo is out of date with version 0.2 code
1. move /foo to /foo/0.2
1. put new code at /foo/0.3
1. delete content at /foo, and update any urls that link to it


***
#Code samples: [Code samples](/src)
* Move url to /samples

## Samples
* simple-wiki: 0.2, external
* simple-wiki num 2: 0.2, external
* simple delicious: 0.2
* alternate tutorial SQLite & SQLObject: 0.2
* templating with genshi: should be part of larger 'templating' section


## tips & tricks

* Possibly move entirely to cookbook?

vhost, metaclass and multiple apps should have separate section, but this setup isn't the way to do things in 0.3

* simple sessions: no longer with flup, better docs elsewhere
* template tricks: with template code
* vhost: no longer needed with subdomain apps
* metaclass: also no longer need (auto app)
* test web app: need separate testing section
* serving images: 0.2, should use mimetypes module?
* multiple apps: not needed


## Real web apps

* Leave them external, but annotate which version of webpy they use.

***