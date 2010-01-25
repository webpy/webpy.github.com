---
layout: default
title: Recommended Setup
---

# Recommended Setup

web.py recommends the following software for production servers:

##Web Server:

Webpy has an internal web server, but it should be used for development only.
For deployment, a more robust server should be used, such as one of these:

*  [lighttpd](http://www.lighttpd.net/download/) [BSD] [(doc)](http://trac.lighttpd.net/trac/wiki/#ReferenceDocumentation) through [flup's fastcgi](http://trac.saddi.com/flup) [BSD] (`easy_install flup`)

*  [Apache](http://www.apache.org/) [Apache] through [(mod_wsgi)](http://code.google.com/p/modwsgi/) [Apache]

##Databases:
*  [postgresql](http://www.postgresql.org/download/) [BSD] [(doc)](http://www.postgresql.org/docs/) with [psycopg2](http://initd.org/pub/software/psycopg/) [BSD] [(doc)](http://www.initd.org/tracker/psycopg/wiki/PsycopgTwo) as the python client. (`easy_install psycopg2`)
  
*  [mysql](http://dev.mysql.com/downloads/mysql/5.0.html) [GPL] [(doc)](http://www.mysql.org/doc/) with [MySQLdb](http://sourceforge.net/project/showfiles.php?group_id=22307) [CNRI] [(doc)](http://mysql-python.sourceforge.net/MySQLdb.html) as the python client (`easy_install MySQL-python`)

##CGI/FastCGI/SCGI:
*  [flup](http://trac.saddi.com/flup) [BSD] (`easy_install flup`)

##Connection Pooling:
*  [DBUtils](http://www.w4py.org/downloads/DBUtils/) [CNRI] [(doc)](http://www.webwareforpython.org/DBUtils/Docs/UsersGuide.html) (`easy_install DBUtils`)

##Templates:
*  template.py [built-in] [(doc)](/docs/0.3/templetor)

##User Input:
*  [python-markdown](http://sourceforge.net/project/showfiles.php?group_id=153041) [BSD] [(doc)](http://www.freewisdom.org/projects/python-markdown/)