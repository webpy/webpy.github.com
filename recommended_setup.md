---
layout: default
title: Recommended Setup
---

# Recommended Setup

Other languages: [Français](/recommended_setup/fr) | ...

### Summary

* [Web Server](#web-servers)
* [Databases](#databases)
* [Connection Pooling](#connection-pooling)
* [Templates](#templates)

web.py recommends the following software for production servers:

## Web Servers

Webpy has an internal web server, but it should be used for development only. For production, a more robust server should be used, such as one of these:

* [Nginx](https://nginx.org)
* [Apache](http://www.apache.org/) [Apache] through [(mod_wsgi)](http://code.google.com/p/modwsgi/) [Apache]

## Databases

Webpy does not require a database to run. It does, however, support using the following databases:

*  [postgresql](http://www.postgresql.org/download/) [BSD] [(doc)](http://www.postgresql.org/docs/) with [psycopg2](http://initd.org/pub/software/psycopg/) [BSD] [(doc)](http://www.initd.org/tracker/psycopg/wiki/PsycopgTwo) as the python client. (`easy_install psycopg2`)
*  [mysql](http://dev.mysql.com/downloads/mysql/5.0.html) [GPL] [(doc)](http://www.mysql.org/doc/) with [MySQLdb](http://sourceforge.net/project/showfiles.php?group_id=22307) [CNRI] [(doc)](http://mysql-python.sourceforge.net/MySQLdb.html) as the python client (`easy_install MySQL-python`)
*  [sqlite](http://www.sqlite.org/) [Public domain] [(doc)](http://www.sqlite.org/docs.html) with [pysqlite](http://code.google.com/p/pysqlite/) as python client (`easy_install pysqlite`).

## Connection Pooling

For high traffic sites, connection pooling allows Webpy to keep multiple database connections open, typically allowing faster access from the database. This is optional, but available as a scaling tactic.

*  [DBUtils](http://www.w4py.org/downloads/DBUtils/) [CNRI] [(doc)](http://www.webwareforpython.org/DBUtils/Docs/UsersGuide.html) (`easy_install DBUtils`)

## Templates

Webpy has its own template system which allows users to let untrusted users write templates using this, and use python-like syntax within templates.

*  template.py [built-in] [(doc)](/docs/0.3/templetor)

[Jinja2](https://jinja.palletsprojects.com/) is more popolar and feature rich, we strongly recommend Jinja2.
