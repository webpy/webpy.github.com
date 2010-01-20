---
layout: default
title: db.update
---

# db.update

### Problem

You want to update data that's been entered into a database.

### Solution

    import web
    
    db = web.database(dbn='postgres', db='mydata', user='dbuser', pw='')
    db.update('mytable', where="id = 10", value1 = "foo")

See the [select](/cookbook/select) for more information on arguments that are accepted by update.


The update method returns the number of rows updated.