---
layout: default
title: ideas
---

# ideas

Here are ideas for web.py projects to take on if you have some free time, say, this summer.

## web.py infrastructure

<a name="enhancing-templating"></a>
### enhancing templating

The current templating system, and even Adam Atlas's rewrite, doesn't perfectly conform to the spec. For example, it doesn't support arbitrary Python code execution within a template. This project would be to take the templating system the final mile and fix the remaining bugs and unimplemented features.

<a name="engine-agnostic-templating"></a>
### Engine-agnostic templating

Python has many templating engines, each emphasizing different features and approaches. Web.py currently supports Cheetah and Templator (its built-in engine). It would be nice to be able to be able to use the same model (a 'render' object which responds to template names, outputs the content-type, etc) with other engines (like Genshi, Clearsilver, Kid and others). Turbogears has some code doing similar stuff that can be canibalized.

<a name="javascript-form-support"></a>
### javascript form support

It's annoying to have to fill out a form.py form, only to get it back to find that it's been incorrectly filled out. This project would be to add metadata to web.py validators to allow them to be implemented in JavaScript (for `notnull` and `regexp`, this should be trivial) and then update the forms so that they work like [this qweb example][q] -- giving the user immediate feedback when they've failed a requirement.

  [q]: http://notabug.com/qweb/bbbbb

<a name="user-accounts"></a>
### user accounts

web.py has long been lacking a user account system. The goal would be to build something simple and flexible enough that it could be plugged into all sorts of database backends and UI front ends, but still handle the details of HMACs and OpenID and stuff like that. If you're interested in this project, work with the mailing list to come up with a clear spec before you get started.

<a name="built-in-session-middleware"></a>
### Built-in session middleware

Sessions are a useful abstraction for web applications. Flup comes with some simple session middleware, but it doesn't back to databases (which is very useful if your deployment scenario relies on multiple web servers using the same DB server). It would be nice if web.py would come with a built-in, file or DB -backed session facility.

### other

Is there a set of functionality you find yourself implementing over and over that you think would be good for web.py? Let us know; perhaps it would make a good project.

## web.py tools

<a name="screen-scraping-data-processing"></a>
### screen scraping / data processing

Lots of exciting web sites (e.g. [Chicago Crime][cc]) are built by scraping existing public data sources and reformulating them in a new way. This project would be to work on various public works screen scraping and data processing tasks to feed data to a new such public works site.

  [cc]: http://chicagocrime.org/

<a name="collaborative-filtering"></a>
### collaborative filtering

Many database-backed web sites display various sorts of items -- news stories, users, photos -- and provide users with various techniques for finding them. Most of the traditional techniques (searching, filtering, following links) are pretty easy to implement in web.py. But one key one that's missing is support for collaborative filtering. This project would be to take existing collaborative filtering algorithms and implementations (e.g. [consensus][c]), possibly improving them or replacing them if necessary, and fitting them into a framework where they can be used on large-scale web.py sites. That means developing tools to move stuff from the database into the recommendation system, store the recommendations, update the recommendations regularly, etc.

  [c]: http://exogen.case.edu/projects/consensus/

<a name="stats-package"></a>
### stats package

Every hit to the server contains within it a wealth of information -- user IP, cookies, browser information, referrers -- but for most people, all this data is largely thrown a way. For the most part, people still use the same log analysis tools developed in the early 1990s. What about a system that used the power of modern databases to let you explore this log information in a meaningful way? Click on a particular URL and see how its traffic has changed over time, how it compares with other URLs on the site, what referrers have linked to it and what those referrers say about it. Click on a particular IP and see its entire path through the site, watching where it came from and where it got stuck. And so on. I've got _lots_ of ideas for this if you're interested in building it.

## web apps

<a name="startupideas-org"></a>
### startupideas.org

A bunch of people come up with fairly good ideas for new web apps to build. A bunch of people are fairly good at building them. But, as far as I can tell, these groups aren't very good at talking to each other. This would be a simple web.py site where people could submit their new website ideas, other people could vote and comment on them, and developers could sign up to implement them. It's all about bringing people together. To build websites.

<a name="teh-communicator"></a>
### teh communicator

IRC is nice for asking questions because you can get answers in real-time. But it's bad because it requires special client software, has pretty useless archives, and if no one answers your question in real-time then it doesn't get answered. "teh communicator" (just a code name) is a project to develop a new website that uses AJAX push to give you the realtime feel of IRC on a website (using web.py's `untwisted` module) but stores conversations in a database so that they're nicely archived, threaded, and you can keep track of which ones have already been answered.

<a name="wiki-debate"></a>
### WikiDebate

Wikipedia is great when you want to know the facts of a subject, but often you don't want the facts, you want the arguments. The goal of the WikiDebate project would be to develop a new site that was more of a cross between a threaded discussion and Wikipedia. Instead of simply having an edit war over which are the real facts, the site would capture the structure of real arguments on the subject, with the back-and-forth of claim and refutation. Ideally, pointless online arguments could be moved into this system and real progress could be made, instead of hashing the same points out over and over again.

<a name="webpy-org"></a>
### webpy.org

When people fish for a Python web framework, the first thing they encounter is the framework's website. They check how good (and easy to use) the documentation is, how easy it is to report bugs and interact with the developers, and those who aren't very technical just check how warm and fuzzy the website makes them feel. Web.py's website is not doing very well on the warm-and fuzzyness effort, it's distributed between a static page (decent design, but sparse), a wiki (on a commercial service, developed using web.py itself but looking pretty generic), a Trac site (which needs lots of love if it is to be at all useful) and a mailing list. The challenge is to both do a better job at marketing _and_ getting real value out of the effort (by making it easier for people collaborate of developing and supporting web.py).

## web.py community

<a name="pyweek-for-webpy"></a>
### PyWeek for web.py

[PyWeek](http://www.pyweek.org/) is a contest challenging entrants to design, build, and complete a game starting from scratch in only one week.  Web.py could start with a similar model and rule set and invite interested parties to take a simple idea for a web app (possibly connected to startupideas.org?) and turn it into a functioning application in a specified amount of time.  Judgment and prizes aren't the point, we want to inspire folks with some free time to pick up the tools and just start using them.