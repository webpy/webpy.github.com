---
layout: default
title: db.select
---

# db.select

##Problem:

You want to select data from a database

##Solution: 

With version 0.3, databases are defined like this:

    db = web.database(dbn='postgres', db='mydata', user='dbuser', pw='')

Once the database is defined as such, performing selects can be performed like this:
    
    # Select all entries from table 'mytable'
    entries = db.select('mytable')

The select statement takes the following keyword arguments:

* vars
* what
* where
* order
* group
* limit
* offset
* _test

###vars
The vars variable is used to populate the rest of the statements.  For example:

    myvar = dict(name="Bob")
    results = db.select('mytable', myvar, where="name = $name")

###what
The what variable defaults to *, but can take a list of items you want selected if the entire entry isn't desired.

    results = db.select('mytable', what="id,name")

###where
The where variable lets you pass where clauses to the SQL select, such as:

    results = db.select('mytable', where="id>100")

###order
The order variable lets the order be specified.  For instance:

    results = db.select('mytable', order="post_date DESC")

###group
Grouping lets you combine things that are common.

    results = db.select('mytable', group="color")    

###limit
Limits set how many results are returned. 
 
    results = db.select('mytable', limit=10) 

###offset
Offsets start returning results after a certain point; they're often used with limits to do something like show 10 entries per page, and then see the next 10.   

    results = db.select('mytable', offset=10) 

###_test
The _test variable lets you see the SQL produced by the statement:

    results = db.select('mytable', offset=10, _test=True) 
    <sql: 'SELECT * FROM mytable OFFSET 10'>