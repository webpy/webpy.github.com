---
layout: default
title: web.update()
---

# web.update()

used to make updates to a single database row.   Specify the database and a clause.

`update(tables, where, vars=None, _test=False, **values)`
   : Update `tables` with clause `where` (interpolated using `vars`)
     and setting `values`.
## other example

        web.update('resume', where='resume_id = $current', resume_availability = 'available')


## docs example
         >>> joe = 'Joseph'
         >>> update('foo', where='name = $joe', name='bob', age=5,
         ...   vars=locals(), _test=True)
         <sql: "UPDATE foo SET age = 5, name = 'bob' WHERE name = 'Joseph'">

