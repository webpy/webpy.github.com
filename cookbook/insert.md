---
layout: default
title: db.insert
---

# db.insert

### Problem: You want to add data to a database

### Solution: 

With version 0.3, databases are defined like this:

```
db = web.database(dbn='postgres', db='mydata', user='dbuser', pw='')
```

Once the database is defined as such, you can insert new row like this:

```
# Insert an entry into table 'mytable'. `firstname`, `lastname`, `joindate` are the SQL column names.
# `sequence_id` is the value of sequence id of the newly inserted entry.
sequence_id = db.insert("mytable", firstname="Bob", lastname="Smith", joindate=web.SQLLiteral("NOW()"))
```

The insert statement takes the following keyword arguments:
 
* `tablename` - The name of the SQL table in your database.
* `seqname` - the column name which stores sequence ID, defaults to name `id`. If `None` or `False`, no sequence ID will be returned.
* `_test` - if `True`, SQL statement will NOT be actually executed, instead a string of full SQL statement is returned. Useful to verify your SQL statement.

```
db.insert("mytable", firstname="Bob")
<sql: "INSERT INTO mytable (firstname) VALUES ('Bob')">
```

You can also pass a dict with SQL column name as dict key directly:

```
row = {firstname: "Bob", lastname: "Smith", joindate: web.SQLLiteral("NOW()")}
sequence_id = db.insert('mytable', **row)
```

If column name is not given, the database may create default values or issue a warning/error (depends on the SQL structure).
