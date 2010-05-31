---
layout: default
title: Recommended Setup
---

# Recommended Setup

Other languages : [français](/recommended_setup/fr) | ...

### Summary

* <a href="#webserver">Web Server</a>
* <a href="#database">Databases</a>
* <a href="#pool">Connection Pooling</a>
* <a href="#template">Templates</a>
* <a href="#userinput">User Input</a>

web.py recommends the following software for production servers:

<a name="webserver"></a>
##Web Server:

Webpy has an internal web server, but it should be used for development only. For deployment, a more robust server should be used, such as one of these:

*  [lighttpd](http://www.lighttpd.net/download/) [BSD] [(doc)](http://trac.lighttpd.net/trac/wiki/#ReferenceDocumentation) through [flup's fastcgi](http://trac.saddi.com/flup) [BSD] (`easy_install flup`)
*  [Apache](http://www.apache.org/) [Apache] through [(mod_wsgi)](http://code.google.com/p/modwsgi/) [Apache]

<a name="database"></a>
##Databases:

Webpy does not require a database to run. It does, however, support using the following databases:

*  [postgresql](http://www.postgresql.org/download/) [BSD] [(doc)](http://www.postgresql.org/docs/) with [psycopg2](http://initd.org/pub/software/psycopg/) [BSD] [(doc)](http://www.initd.org/tracker/psycopg/wiki/PsycopgTwo) as the python client. (`easy_install psycopg2`)
*  [mysql](http://dev.mysql.com/downloads/mysql/5.0.html) [GPL] [(doc)](http://www.mysql.org/doc/) with [MySQLdb](http://sourceforge.net/project/showfiles.php?group_id=22307) [CNRI] [(doc)](http://mysql-python.sourceforge.net/MySQLdb.html) as the python client (`easy_install MySQL-python`)
*  [sqlite](http://www.sqlite.org/) [Public domain] [(doc)](http://www.sqlite.org/docs.html) with [pysqlite](http://code.google.com/p/pysqlite/) as python client (`easy_install pysqlite`).

<a name="pool"></a>
##Connection Pooling:

For high traffic sites, connection pooling allows Webpy to keep multiple database connections open, typically allowing faster access from the database. This is optional, but available as a scaling tactic.

*  [DBUtils](http://www.w4py.org/downloads/DBUtils/) [CNRI] [(doc)](http://www.webwareforpython.org/DBUtils/Docs/UsersGuide.html) (`easy_install DBUtils`)

<a name="template"></a>
##Templates:

Webpy has its own template system which allows users to let untrusted users write templates using this, and use python-like syntax within templates.

*  template.py [built-in] [(doc)](/docs/0.3/templetor)

<a name="userinput"></a>
##User Input:

Markdown allows Webpy users to write text which gets converted to HTML on page display.  It isn't necessary, but is the recommended way to generate formatted HTML from user input.


*  [python-markdown](http://sourceforge.net/project/showfiles.php?group_id=153041) [BSD] [(doc)](http://www.freewisdom.org/projects/python-markdown/)