---
layout: default
title: db.query
---

# db.query

### Problem

You want to perform advanced SQL statements like joins or counts.

### Solution

webpy doesn't try to build layers between you and your database.  Rather, it tries to make it easy to perform common tasks, and get out of your way when you need to do more advanced things.  Performing advanced database queries is no different.  For example:

    import web

    db = web.database(dbn='postgres', db='mydata', user='dbuser', pw='')
    
    results = db.query("SELECT COUNT(*) AS total_users FROM users")
    print results[0].total_users # -> prints number of entries in 'users' table


or, for a JOIN example:

    import web
    
    db = web.database(dbn='postgres', db='mydata', user='dbuser', pw='')
    
    results = db.query("SELECT * FROM entries JOIN users WHERE entries.author_id = users.id")


To prevent SQL injection attacks, db.query also accepts the "vars" syntax as described in [db.select](/cookbook/select):

    results = db.query("SELECT * FROM users WHERE id=$id", vars={'id':10})

This will escape user input, if you're trusting them for the "id" variable.