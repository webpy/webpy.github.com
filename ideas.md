---
layout: default
title: ideas
---

# ideas

Here are ideas for web.py projects to take on if you have some free time, say, this summer.

## web.py infrastructure

### enhancing templating

The current templating system, and even Adam Atlas's rewrite, doesn't perfectly conform to the spec. For example, it doesn't support arbitrary Python code execution within a template. This project would be to take the templating system the final mile and fix the remaining bugs and unimplemented features.

### javascript form support

It's annoying to have to fill out a form.py form, only to get it back to find that it's been incorrectly filled out. This project would be to add metadata to web.py validators to allow them to be implemented in JavaScript (for `notnull` and `regexp`, this should be trivial) and then update the forms so that they work like [this qweb example][q] -- giving the user immediate feedback when they've failed a requirement.

  [q]: http://notabug.com/qweb/bbbbb

### user accounts

web.py has long been lacking a user account system. The goal would be to build something simple and flexible enough that it could be plugged into all sorts of database backends and UI front ends, but still handle the details of HMACs and OpenID and stuff like that. If you're interested in this project, work with the mailing list to come up with a clear spec before you get started.

### other

Is there a set of functionality you find yourself implementing over and over that you think would be good for web.py? Let us know; perhaps it would make a good project.

## web.py tools

### screen scraping / data processing

Lots of exciting web sites (e.g. [Chicago Crime][cc]) are built by scraping existing public data sources and reformulating them in a new way. This project would be to work on various public works screen scraping and data processing tasks to feed data to a new such public works site.

  [cc]: http://chicagocrime.org/

### collaborative filtering

Many database-backed web sites display various sorts of items -- news stories, users, photos -- and provide users with various techniques for finding them. Most of the traditional techniques (searching, filtering, following links) are pretty easy to implement in web.py. But one key one that's missing is support for collaborative filtering. THis project would be to take existing collaborative filtering algorithms and implementations (e.g. [consensus][c]), possibly improving them or replacing them if necessary, and fitting them into a framework where they can be used on large-scale web.py sites. That means developing tools to move stuff from the database into the recommendation system, store the recommendations, update the recommendations regularly, etc.

  [c]: http://exogen.case.edu/projects/consensus/

### stats package

Every hit to the server contains within it a wealth of information -- user IP, cookies, browser information, referrers -- but for most people, all this data is largely thrown a way. For the most part, people still use the same log analysis tools developed in the early 1990s. What about a system that used the power of modern databases to let you explore this log information in a meaningful way? Click on a particular URL and see how its traffic has changed over time, how it compares with other URLs on the site, what referrers have linked to it and what those referrers say about it. Click on a particular IP and see its entire path through the site, watching came from and where it got stuck. And so on. I've got _lots_ of ideas for this if you're interested in building it.

## web apps

Descriptions of these coming soon...

### WikiDebate

### the communicator

### startupideas.org