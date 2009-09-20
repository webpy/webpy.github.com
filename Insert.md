---
layout: default
title: Insert: Adding a new entry to a database
---

# Insert: Adding a new entry to a database

###Problem: You want to add data to a database

###Solution: 

With version 0.3, databases are defined like this:

    db = web.database(dbn='postgres', db='mydata', user='dbuser', pw='')

Once the database is defined as such, performing insert can be performed like this:
    
    # Insert an entry into table 'mytable'
    sequence_id = db.insert('mytable', firstname="Bob",lastname="Smith",joindate=web.SQLLiteral("NOW()"))

The insert statement takes the following keyword arguments:
 
tablename
seqname   
_test  
\**values
 


##tablename
The name of the table in your database to which you would like to add data to.

##seqname
An optional argument, the default value is None. Set `seqname` to the ID if it's not the default, or to `False`.

##_test
The _test variable lets you see the SQL produced by the statement:

    results = db.select('mytable', offset=10, _test=True) 
    ><sql: 'SELECT * FROM mytable OFFSET 10'>

##\**values
A set of named arguments that represent the fields in your table. If values are not given, the database may create default values or issue a warning.