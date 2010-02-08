---
layout: default
title: Multiple Databases
---

# Multiple Databases

## Problem
You want to access multiple databases in a single project.

## Solution

webpy 0.3 supports multiple databases by removing the database from a part of the "web" module, and making it a more typical object.  For example:

    import web
    
    db1 = web.database(dbn='mysql', db='dbname1', user='foo')
    db2 = web.database(dbn='mysql', db='dbname2', user='foo')
    
    print db1.select('foo', where='id=1')
    print db2.select('bar', where='id=5')
    
insert, update, delete and query methods can also be used in the similar way. 

Of course, you can use 'host' and 'port' to specify server address and listen port.