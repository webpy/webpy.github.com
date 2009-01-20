---
layout: default
title: Integrating SQLite UDF (user-defined-functions) with webpy database layer
---

# Integrating SQLite UDF (user-defined-functions) with webpy database layer

A user asked at the mailing list and I thought of putting it here for future use and reference. 

You can add python functions to sqlite and have them called within your queries.

Example:
<pre>
>>> import sqlite3 as db
>>> conn = db.connect(":memory:")
>>> conn.create_function("sign", 1, lambda val: val and (val > 0 and 1 or -1))
>>> cur = conn.cursor()
>>> cur.execute("select 1, -1")
&lt;sqlite3.Cursor object at 0xb759f2c0&gt;
>>> print cur.fetchall()
[(1, -1)]
>>> cur.execute("select sign(1), sign(-1), sign(0), sign(-99), sign(99)")
&lt;sqlite3.Cursor object at 0xb759f2c0&gt;
>>> print cur.fetchall()
[(1, -1, 0, -1, 1)]
>>> conn.close()</pre>

In webpy, you can get a reference to the connection object via the cursor
i.e. db._db_cursor().connection

Example:
<pre>
>>> import web
>>> db = web.database(dbn="sqlite", db=":memory:")
>>> db._db_cursor().connection.create_function("sign", 1, lambda val: val and (val > 0 and 1 or -1))
>>> print db.query("select sign(1), sign(-1), sign(0), sign(-99), sign(99)").list()
[&lt;Storage {'sign(1)': 1, 'sign(-1)': -1, 'sign(99)': 1, 'sign(-99)': -1, 'sign(0)': 0}&gt;]
</pre>