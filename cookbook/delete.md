---
layout: default
title: db.delete
---

# db.delete

##Problem:

You want to delete data from a database

##Solution: 

With version 0.3, databases are defined like this:

    db = web.database(dbn='postgres', db='mydata', user='dbuser', pw='')

Once the database is defined as such, performing deletes can be performed like this:
    
    # Delete all entries from table 'mytable'
    db.delete('mytable', where="1=1")

Note that you have to pass a "where" clause, even if you want to delete everything.  This is a safety mechanism so you don't accidentally delete all of your data.

The delete statement takes the following keyword arguments:

* where
* vars
* _test


###where
The where variable lets you pass where clauses to the SQL delete, such as:

    db.delete('mytable', where="id>100")


###vars
The vars variable lets you pass correctly escaped data to SQL delete, such as:

    db.delete('mytable', where="id>$num", vars={'num': 100})

###_test
The _test variable lets you see the SQL produced by the statement:

    results = db.delete('mytable', where="foo=5", _test=True) 
    <sql: 'DELETE FROM mytable WHERE foo=5'>
