---
layout: default
title: db.select
---

# db.select

Other languages: [简体中文](./select.zh-cn)

## Problem

You want to select data from a database

## Solution

With web.py version 0.3 and later releases, databases are defined like this:

```
db = web.database(dbn='postgres', db='mydata', user='dbuser', pw='')
```

Once the database is defined as such, you can perform selects like this:

```
# Select all rows from table 'mytable'.
results = db.select('mytable')
```

The query result (`results` in above example) is an iterator of dict-like
storage items, you can access them like below:

```
len(results)        # number of rows returned
results[0]          # first row returned
results[0]['name']  # value of sql column `name` in first row returned
```

Note: since the query result is a iterator, you cannot access it repeatly:

```
print(results[0])   # first access works.
print(results[1])   # FAILED with IndexError
```

If you need to access it repeatly, please convert it to a list first:

```
qr = db.select('mytable')
results = list(qr)
print(results[0])   # it works
print(results[1])   # works too
```

If SQL column is defined as binary format, e.g. `VARBINARY` in MySQL/MariaDB, returned value will be a `bytes` string, not `str`. For example:

1. Create a SQL table in MySQL/MariaDB with command: `CREATE TABLE mytable (email VARBINARY(255));`
1. Insert a sample record: `INSERT INTO mytable (email) VALUES ("test@domain.com");`
1. Query it with web.py db module:

```
qr = db.select("mytable", what="email", limit=1)
email = qr[0]['email']
print(email)         // result is bytes: b'test@domain.com', not str 'test@domain.com'
```

The select statement takes the following keyword arguments:

* `vars`
* `what`
* `where`
* `order`
* `group`
* `limit`
* `offset`
* `_test`

### vars

The vars variable is used to populate the rest of the statements.  For example:

```
myvar = dict(name="Bob")

# Same as SQL statement: SELECT * FROM mytable WHERE name="Bob"
results = db.select('mytable', vars=myvar, where="name = $name")
```

### what

The what variable defaults to `*`, but can take a list of items you want selected if the entire entry isn't desired.

```
# Same as SQL statement: SELECT id, name FROM mytable
results = db.select('mytable', what="id,name")
```

### where

The where variable lets you pass where clauses to the SQL select, such as:

```
# Same as SQL statement: SELECT * FROM mytable WHERE id>100
results = db.select('mytable', where="id>100")
```

### order

The order variable lets the order be specified.  For instance:

```
# Same as SQL statement: SELECT * FROM mytable ORDER BY post_date DESC
results = db.select('mytable', order="post_date DESC")
```

### group

Grouping lets you combine things that are common.

```
# Same as SQL statement: SELECT * FROM mytable GROUP BY color
results = db.select('mytable', group="color")
```

### limit

Limits set how many results are returned.

```
# Same as SQL statement: SELECT * FROM mytable LIMIT 10
results = db.select('mytable', limit=10)
```

### offset

Offsets start returning results after a certain point; they're often used with
limits to do something like show 10 entries per page, and then see the next 10.

```
# Same as SQL statement: SELECT * FROM mytable OFFSET 10 LIMIT 20
results = db.select('mytable', offset=10, limit=20)

# Same as SQL statement: SELECT * FROM mytable OFFSET 30 LIMIT 20
results = db.select('mytable', offset=30, limit=20)
```

### _test

The `_test` variable lets you see the SQL produced by the statement, no
statement is actually performed:

```
results = db.select('mytable', offset=10, _test=True)
# `results` is a string: <sql: 'SELECT * FROM mytable OFFSET 10'>
```
