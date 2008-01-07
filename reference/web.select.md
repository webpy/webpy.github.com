---
layout: default
title:  - api reference - web.select
---

#  - api reference - web.select

## __init__.py

`main()`

## cheetah.py


## db.py

`select(tables, vars=None, what='*', where=None, order=None, group=None, limit=None, offset=None, _test=False):`
   : Selects `what` from `tables` with clauses `where`, `order`, 
     `group`, `limit`, and `offset`. Uses vars to interpolate. 
     Otherwise, each clause can be a SQLQuery.
     
         >>> select('foo', _test=True)
         <sql: 'SELECT * FROM foo'>
         >>> select(['foo', 'bar'], where="foo.bar_id = bar.id", limit=5, _test=True)
         <sql: 'SELECT * FROM foo, bar WHERE foo.bar_id = bar.id LIMIT 5'>


