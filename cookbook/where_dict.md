---
layout: default
title: Using a dictionary as where clause
---

# Using a dictionary as where clause

Problem
-------

You want to create a dictionary of where clauses dynamically and use it in a query.

Solution
--------

    >>> import web
    >>> db = web.database(dbn='postgres', db='mydb', user='postgres')
    >>> where_dict = {'col1': 1, col2: 'sometext'}
    >>> db.delete('mytable', where=web.db.sqlwhere(where_dict), _test=True)
    <sql: "DELETE FROM mytable WHERE col1 = 1 AND col2 = 'sometext'">

Explanation
-----------

`web.db.sqlwhere` takes a Python dictionary as an argument and converts it into a string useful for where clause in different queries. You can also use an optional `grouping` argument to define the exact gouping of the individual keys. For instance:

    >>> import web
    >>> web.db.sqlwhere({'a': 1, 'b': 2}, grouping=' OR ')
    'a = 1 OR b = 2'

Default for `grouping` is `' AND '`.