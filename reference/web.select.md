---
layout: default
title: web.select
---

# web.select

in db.py

`select(tables, vars=None, what='*', where=None, order=None, group=None, limit=None, offset=None, _test=False):`
   : Selects `what` from `tables` with clauses `where`, `order`, 
     `group`, `limit`, and `offset`. Uses vars to interpolate. 
     Otherwise, each clause can be a SQLQuery.
     
## examples
### script
    refs = web.select('refs', None, '*', "references_id = " + str(resume.references_id))
    this selects '*' from the 'refs' table where references_id = the given resume.references_id

### command line 
    >>> select('foo', _test=True)
    <sql: 'SELECT * FROM foo'>
    >>> select(['foo', 'bar'], where="foo.bar_id = bar.id", limit=5, _test=True)
    <sql: 'SELECT * FROM foo, bar WHERE foo.bar_id = bar.id LIMIT 5'>


page started by huntercross - last edited by huntercross