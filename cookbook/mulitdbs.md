---
layout: default
title: Multiple Databases
---

# Multiple Databases

webpy 0.3 supports multiple databases by removing the database from a part of the "web" module, and making it a more typical object.  For example:

    import web
    
    mydb1 = web.database(dbn='mysql', db='dbname1', user='foo')
    mydb2 = web.database(dbn='mysql', db='dbname2', user='foo')
    
All of the former database methods work on these objects, such as:

* select('table_name', where="foo = bar")
* insert('table_name', foo="bar", baz="asdf")
* update('table_name', where="id = 10", foo="bar")
* query('table_name', "SELECT * FROM users JOIN friends WHERE users.id = friends.id")

See the database module for more information.