---
layout: default
title: Recommended Setup
---

# Recommended Setup

web.py recommends the following software:

##Web Server:
*  [lighttpd](http://www.lighttpd.net/download/) [BSD] [(doc)](http://trac.lighttpd.net/trac/wiki/#ReferenceDocumentation)

##Databases:
*  [postgresql](http://www.postgresql.org/download/) [BSD] [(doc)](http://www.postgresql.org/docs/) with [psycopg2](http://initd.org/pub/software/psycopg/) [BSD] [(doc)](http://www.initd.org/tracker/psycopg/wiki/PsycopgTwo) as the python client. (`easy_install psycopg2`)
  
*  [mysql](http://dev.mysql.com/downloads/mysql/5.0.html) [GPL] [(doc)](http://www.mysql.org/doc/) with [MySQLdb](http://sourceforge.net/project/showfiles.php?group_id=22307) [CNRI] [(doc)](http://sourceforge.net/docman/?group_id=22307) as the python client (`easy_install MySQL-python`)

##CGI/FastCGI/SCGI:
*  [flup](http://trac.saddi.com/flup) [BSD] (`easy_install flup`)

##Connection Pooling:
*  [DBUtils](http://www.w4py.org/downloads/DBUtils/) [CNRI] [(doc)](http://www.webwareforpython.org/DBUtils/Docs/UsersGuide.html) (`easy_install DBUtils`)

##Templates:
*  template.py [built-in] [(doc)](templetor)
*  [Cheetah](http://dl.sourceforge.net/cheetahtemplate/Cheetah-1.0.tar.gz) 1.0 [BSD] [(doc)](http://www.cheetahtemplate.org/learn.html)
##User Input:
*  [python-markdown](http://sourceforge.net/project/showfiles.php?group_id=153041) [BSD] [(doc)](http://www.freewisdom.org/projects/python-markdown/)