---
layout: default
title: db.delete
---

# db.delete

### Problem

You want to delete data that's been entered into a database.

### Solution

    import web
    
    db = web.database(dbn='postgres', db='mydata', user='dbuser', pw='')
    db.delete('mytable', where="id=10")

It is also accepts "using" and "vars" parameters.

The delete method returns the number of rows deleted.