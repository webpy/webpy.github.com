---
layout: default
title: Configuration recommandée
---

# Configuration recommandée

Autre langages : [english](/recommended_setup) | ...


Web.py recommande les logiciels suivants pour les serveurs de production:

##Serveurs web:

Webpy dispose d'un serveur web interne, mais il devrait être utilisé pour le développement seulement. Pour le déploiement, un serveur plus robuste devrait être utilisé, comme l'un de ceux-ci:

*  [lighttpd](http://www.lighttpd.net/download/) [BSD] [(doc)](http://trac.lighttpd.net/trac/wiki/#ReferenceDocumentation) via [flup's fastcgi](http://trac.saddi.com/flup) [BSD] ('easy_install flup')
*  [Apache](http://www.apache.org/) [Apache] via [(mod_wsgi)](http://code.google.com/p/modwsgi/) [Apache]

##Bases de données:

Webpy ne nécessite pas de base de données pour fonctionner. Il supporte néanmoins les bases suivantes:


*  [postgresql](http://www.postgresql.org/download/) [BSD] [(doc)](http://www.postgresql.org/docs/) avec [psycopg2](http://initd.org/pub/software/psycopg/) [BSD] [(doc)](http://www.initd.org/tracker/psycopg/wiki/PsycopgTwo) comme client python. ('easy_install psycopg2')
*  [mysql](http://dev.mysql.com/downloads/mysql/5.0.html) [GPL] [(doc)](http://www.mysql.org/doc/) avec [MySQLdb](http://sourceforge.net/project/showfiles.php?group_id=22307) [CNRI] [(doc)](http://mysql-python.sourceforge.net/MySQLdb.html) comme client python ('easy_install MySQL-python')
*  [sqlite](http://www.sqlite.org/) [Public domain] [(doc)](http://www.sqlite.org/docs.html) avec [pysqlite](http://code.google.com/p/pysqlite/) comme client python ('easy_install pysqlite').

##Pool de connexions:

Pour les sites à haut traffic, le pool de connexion autorise Webpy à conserver de multiples connexions aux bases de données ouvertes, afin d'accélérer l'accès aux bases. Cette option est facultative, mais disponible comme échelon tactique.

*  [DBUtils](http://www.w4py.org/downloads/DBUtils/) [CNRI] [(doc)](http://www.webwareforpython.org/DBUtils/Docs/UsersGuide.html) ('easy_install DBUtils')

##Modèles, gabarits:

Webpy possède son propre système de gabarit qui permet aux utilisateurs d'autoriser l'écriture de gabarits aux utilisateurs moins épprouvés, et d'utiliser une syntaxe proche de celle du python dans les templates.

*  template.py [built-in] [(doc)](/docs/0.3/templetor.fr)

##Entrées utilisateurs:

Markdown permet au utilisateurs de Webpy t'écrire du texte qui est convertit en HTML dans la page. Ce n'est pas indispensable, mais c'est la meilleure façon de générer du HTML à partir des entrées utilisateur.

*  [python-markdown](http://sourceforge.net/project/showfiles.php?group_id=153041) [BSD] [(doc)](http://www.freewisdom.org/projects/python-markdown/)