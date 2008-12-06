---
layout: default
title: web.py 0.2 API documentation
---

# web.py 0.2 API documentation

## __init__.py

`main()`
   : 


## cheetah.py

`upvars(level=2)`
   : Guido van Rossum sez: don't use this function.

`render(template, terms=None, asTemplate=False, base=None, isString=False):`
   : Renders a template, caching where it can.
     
     `template` is the name of a file containing the a template in
     the `templates/` folder, unless `isString`, in which case it's the 
     template itself.
 
     `terms` is a dictionary used to fill the template. If it's None, then
     the caller's local variables are used instead, plus context, if it's not 
     already set, is set to `context`.
 
     If asTemplate is False, it `output`s the template directly. Otherwise,
     it returns the template object.
 
     If the template is a potential base template (that is, something other templates)
     can extend, then base should be a string with the name of the template. The
     template will be cached and made available for future calls to `render`.
 
     Requires [Cheetah](http://cheetahtemplate.org/).

`class WebSafe(Filter)`
   : 


## db.py

Supports Firebird, MySQL, PostgreSQL, and SQLite.

`class UnknownParamstyle(Exception)`
   : raised for unsupported db paramstyles
     
     (currently supported: qmark, numeric, format, pyformat)

`aparam()`
   : Returns the appropriate string to be used to interpolate
     a value with the current `web.ctx.db_module` or simply %s
     if there isn't one.
     
         >>> aparam()
         '%s'

`reparam(string_, dictionary)`
   : Takes a string and a dictionary and interpolates the string
     using values from the dictionary. Returns an `SQLQuery` for the result.
     
         >>> reparam("s = $s", dict(s=True))
         <sql: "s = 't'">

`sqlify(obj)`
   : converts `obj` to its proper SQL version
     
         >>> sqlify(None)
         'NULL'
         >>> sqlify(True)
         "'t'"
         >>> sqlify(3)
         '3'

`class SQLQuery`
   : You can pass this sort of thing as a clause in any db function.
     Otherwise, you can pass a dictionary to the keyword argument `vars`
     and the function will call reparam for you.

`class SQLLiteral`
   : Protects a string from `sqlquote`.
 
         >>> insert('foo', time=SQLLiteral('NOW()'), _test=True)
         <sql: 'INSERT INTO foo (time) VALUES (NOW())'>

`sqlquote(a)`
   : Ensures `a` is quoted properly for use in a SQL query.
     
         >>> 'WHERE x = ' + sqlquote(True) + ' AND y = ' + sqlquote(3)
         <sql: "WHERE x = 't' AND y = 3">

`class UnknownDB(Exception)`
   : raised for unsupported dbms

`connect(dbn, **keywords)`
   : Connects to the specified database. 
     
     `dbn` currently must be "postgres", "mysql", or "sqlite". 
     
     If DBUtils is installed, connection pooling will be used.

`class TransactionError(Exception): pass  class transaction:`
   : A context that can be used in conjunction with "with" statements
     to implement SQL transactions. Starts a transaction on enter,
     rolls it back if there's an error; otherwise it commits it at the
     end.

`transact()`
   : Start a transaction.

`commit()`
   : Commits a transaction.

`rollback(care=True)`
   : Rolls back a transaction.

`query(sql_query, vars=None, processed=False, _test=False)`
   : Execute SQL query `sql_query` using dictionary `vars` to interpolate it.
     If `processed=True`, `vars` is a `reparam`-style list to use 
     instead of interpolating.
     
         >>> query("SELECT * FROM foo", _test=True)
         <sql: 'SELECT * FROM foo'>
         >>> query("SELECT * FROM foo WHERE x = $x", vars=dict(x='f'), _test=True)
         <sql: "SELECT * FROM foo WHERE x = 'f'">
         >>> query("SELECT * FROM foo WHERE x = " + sqlquote('f'), _test=True)
         <sql: "SELECT * FROM foo WHERE x = 'f'">

`sqllist(lst)`
   : Converts the arguments for use in something like a WHERE clause.
     
         >>> sqllist(['a', 'b'])
         'a, b'
         >>> sqllist('foo')
         'foo'
         >>> sqllist(u'foo')
         u'foo'

`sqlors(left, lst)`
   : `left is a SQL clause like `tablename.arg = ` 
     and `lst` is a list of values. Returns a reparam-style
     pair featuring the SQL that ORs together the clause
     for each item in the lst.
 
         >>> sqlors('foo = ', [])
         <sql: '2+2=5'>
         >>> sqlors('foo = ', [1])
         <sql: 'foo = 1'>
         >>> sqlors('foo = ', 1)
         <sql: 'foo = 1'>
         >>> sqlors('foo = ', [1,2,3])
         <sql: '(foo = 1 OR foo = 2 OR foo = 3)'>

`sqlwhere(dictionary, grouping=' AND ')`
   : Converts a `dictionary` to an SQL WHERE clause `SQLQuery`.
     
         >>> sqlwhere({'cust_id': 2, 'order_id':3})
         <sql: 'order_id = 3 AND cust_id = 2'>
         >>> sqlwhere({'cust_id': 2, 'order_id':3}, grouping=', ')
         <sql: 'order_id = 3, cust_id = 2'>

`select(tables, vars=None, what='*', where=None, order=None, group=None, limit=None, offset=None, _test=False):`
   : Selects `what` from `tables` with clauses `where`, `order`, 
     `group`, `limit`, and `offset`. Uses vars to interpolate. 
     Otherwise, each clause can be a SQLQuery.
     
         >>> select('foo', _test=True)
         <sql: 'SELECT * FROM foo'>
         >>> select(['foo', 'bar'], where="foo.bar_id = bar.id", limit=5, _test=True)
         <sql: 'SELECT * FROM foo, bar WHERE foo.bar_id = bar.id LIMIT 5'>

`insert(tablename, seqname=None, _test=False, **values)`
   : Inserts `values` into `tablename`. Returns current sequence ID.
     Set `seqname` to the ID if it's not the default, or to `False`
     if there isn't one.
     
         >>> insert('foo', joe='bob', a=2, _test=True)
         <sql: "INSERT INTO foo (a, joe) VALUES (2, 'bob')">

`update(tables, where, vars=None, _test=False, **values)`
   : Update `tables` with clause `where` (interpolated using `vars`)
     and setting `values`.
     
         >>> joe = 'Joseph'
         >>> update('foo', where='name = $joe', name='bob', age=5,
         ...   vars=locals(), _test=True)
         <sql: "UPDATE foo SET age = 5, name = 'bob' WHERE name = 'Joseph'">

`delete(table, where=None, using=None, vars=None, _test=False)`
   : Deletes from `table` with clauses `where` and `using`.
     
         >>> name = 'Joe'
         >>> delete('foo', where='name = $name', vars=locals(), _test=True)
         <sql: "DELETE FROM foo WHERE name = 'Joe'">


## debugerror.py

`djangoerror()`
   : 

`debugerror()`
   : A replacement for `internalerror` that presents a nice page with lots
     of debug information for the programmer.
 
     (Based on the beautiful 500 page from [Django](http://djangoproject.com/), 
     designed by [Wilson Miner](http://wilsonminer.com/).)

`emailerrors(email_address, olderror)`
   : Wraps the old `internalerror` handler (pass as `olderror`) to 
     additionally email all errors to `email_address`, to aid in 
     debugging production websites.
     
     Emails contain a normal text traceback as well as an
     attachment containing the nice `debugerror` page.


## form.py

`attrget(obj, attr, value=None)`
   : 

`class Form`
   : __init__(self, *inputs, **kw)
     `inputs` is a list of form objects.
     The only keyword accepted is "validators" which is a list of Validator objects.

`class Input(object)`
   : __init__(self, name, *validators, **attrs)
     `name` is the name of the object. It is the default value for the "description" attribute for the HTML form element.
     The keywords, stored in the dictionary `attrs`, accepted are: "description", "value", "pre", "post", "id", and "class_"

`class Textbox(Input)`
   : 

`class Password(Input)`
   : 

`class Textarea(Input)`
   : 

`class Dropdown(Input)`
   : 

`class Radio(Input)`
   : 

`class Checkbox(Input)`
   : 

`class Button(Input)`
   : 

`class Hidden(Input)`
   : 

`class File(Input)`
   : 

`class Validator`
   : 

`class regexp(Validator)`
   : 


## http.py

`prefixurl(base='')`
   : Sorry, this function is really difficult to explain.
     Maybe some other time.

`expires(delta)`
   : Outputs an `Expires` header for `delta` from now. 
     `delta` is a `timedelta` object or a number of seconds.

`lastmodified(date_obj)`
   : Outputs a `Last-Modified` header for `datetime`.

`modified(date=None, etag=None)`
   : 

`redirect(url, status='301 Moved Permanently')`
   : Returns a `status` redirect to the new URL. 
     `url` is joined with the base URL so that things like 
     `redirect("about")` will work properly.

`found(url)`
   : A `302 Found` redirect.

`seeother(url)`
   : A `303 See Other` redirect.

`tempredirect(url)`
   : A `307 Temporary Redirect` redirect.

`write(cgi_response)`
   : Converts a standard CGI-style string response into `header` and 
     `output` calls.

`urlencode(query)`
   : Same as urllib.urlencode, but supports unicode strings.
     
         >>> urlencode({'text':'foo bar'})
         'text=foo+bar'

`changequery(query=None, **kw)`
   : Imagine you're at `/foo?a=1&b=2`. Then `changequery(a=3)` will return
     `/foo?a=3&b=2` -- the same URL but with the arguments you requested
     changed.

`url(path=None, **kw)`
   : Makes url by concatinating web.ctx.homepath and path and the 
     query string created using the arguments.

`background(func)`
   : A function decorator to run a long-running function as a background thread. 
     GOTCHA in postgres: Until the foreground task ends, any db access by background 
     task will necessarily get old data from before the foreground task started
     because psycopg2 begins a transaction in the foreground task until it quits.

`backgrounder(func)`
   : 

`class Reloader`
   : Before every request, checks to see if any loaded modules have changed on 
     disk and, if so, reloads them.

`profiler(app)`
   : Outputs basic profiling information at the bottom of each response.


## httpserver.py

`runbasic(func, server_address=("0.0.0.0", 8080))`
   : Runs a simple HTTP server hosting WSGI app `func`. The directory `static/` 
     is hosted statically.
 
     Based on [WsgiServer][ws] from [Colin Stewart][cs].
     
   [ws]: http://www.owlfish.com/software/wsgiutils/documentation/wsgi-server-api.html
   [cs]: http://www.owlfish.com/

`runsimple(func, server_address=("0.0.0.0", 8080))`
   : Runs [CherryPy][cp] WSGI server hosting WSGI app `func`. 
     The directory `static/` is hosted statically.
 
     [cp]: http://www.cherrypy.org


## net.py

`validipaddr(address)`
   : returns True if `address` is a valid IPv4 address

`validipport(port)`
   : returns True if `port` is a valid IPv4 port

`validip(ip, defaultaddr="0.0.0.0", defaultport=8080)`
   : returns `(ip_address, port)` from string `ip_addr_port`

`validaddr(string_)`
   : returns either (ip_address, port) or "/path/to/socket" from string_
     
         >>> validaddr('/path/to/socket')
         '/path/to/socket'
         >>> validaddr('8000')
         ('0.0.0.0', 8000)
         >>> validaddr('127.0.0.1')
         ('127.0.0.1', 8080)
         >>> validaddr('127.0.0.1:8000')
         ('127.0.0.1', 8000)
         >>> validaddr('fff')
         Traceback (most recent call last):
             ...
         ValueError: fff is not a valid IP address/port

`urlquote(val)`
   : Quotes a string for use in a URL.
     
         >>> urlquote('://?f=1&j=1')
         '%3A//%3Ff%3D1%26j%3D1'
         >>> urlquote(None)
         ''
         >>> urlquote(u'\u203d')
         '%E2%80%BD'

`httpdate(date_obj)`
   : Formats a datetime object for use in HTTP headers.
     
         >>> import datetime
         >>> httpdate(datetime.datetime(1970, 1, 1, 1, 1, 1))
         'Thu, 01 Jan 1970 01:01:01 GMT'

`parsehttpdate(string_)`
   : Parses an HTTP date into a datetime object.
 
         >>> parsehttpdate('Thu, 01 Jan 1970 01:01:01 GMT')
         datetime.datetime(1970, 1, 1, 1, 1, 1)

`htmlquote(text)`
   : Encodes `text` for raw use in HTML.
     
         >>> htmlquote("<'&\\">")
         '&lt;&#39;&amp;&quot;&gt;'

`htmlunquote(text)`
   : Decodes `text` that's HTML quoted.
 
         >>> htmlunquote('&lt;&#39;&amp;&quot;&gt;')
         '<\\'&">'

`websafe(val)`
   : Converts `val` so that it's safe for use in UTF-8 HTML.
     
         >>> websafe("<'&\\">")
         '&lt;&#39;&amp;&quot;&gt;'
         >>> websafe(None)
         ''
         >>> websafe(u'\u203d')
         '\\xe2\\x80\\xbd'


## request.py

`handle(mapping, fvars=None)`
   : Call the appropriate function based on the url to function mapping in `mapping`.
     If no module for the function is specified, look up the function in `fvars`. If
     `fvars` is empty, using the caller's context.
 
     `mapping` should be a tuple of paired regular expressions with function name
     substitutions. `handle` will import modules as necessary.

`nomethod(cls)`
   : Returns a `405 Method Not Allowed` error for `cls`.

`autodelegate(prefix='')`
   : Returns a method that takes one argument and calls the method named prefix+arg,
     calling `notfound()` if there isn't one. Example:
 
         urls = ('/prefs/(.*)', 'prefs')
 
         class prefs:
             GET = autodelegate('GET_')
             def GET_password(self): pass
             def GET_privacy(self): pass
 
     `GET_password` would get called for `/prefs/password` while `GET_privacy` for 
     `GET_privacy` gets called for `/prefs/privacy`.
     
     If a user visits `/prefs/password/change` then `GET_password(self, '/change')`
     is called.

`webpyfunc(inp, fvars, autoreload=False)`
   : If `inp` is a url mapping, returns a function that calls handle.

`run(inp, fvars, *middleware)`
   : Starts handling requests. If called in a CGI or FastCGI context, it will follow
     that protocol. If called from the command line, it will start an HTTP
     server on the port named in the first command line argument, or, if there
     is no argument, on port 8080.
 
     `input` is a callable, then it's called with no arguments.
     Otherwise, it's a `mapping` object to be passed to `handle(...)`.
 
     **Caveat:** So that `reloader` will work correctly, input has to be a variable,
     it can't be a tuple passed in directly.
 
     `middleware` is a list of WSGI middleware which is applied to the resulting WSGI
     function.


## template.py

`class ParseError(Exception): pass class Parser:`
   : 

`class TemplateParser(Parser)`
   : 

`class Stowage(storage)`
   : 

`class WTF(AssertionError): pass class SecurityError(Exception):`
   : The template seems to be trying to do something naughty.

`class Template`
   : 

`class Handle`
   : 

`class Fill(Handle)`
   : 

`class render`
   : 

`frender(fn, *a, **kw)`
   : 

`test()`
   : r"""Doctest for testing template module. 

         >>> t = Template
         >>> t('1')()
         '1\n'
         >>> t('$def with ()\n1')()
         '1\n'
         >>> t('$def with (a)\n$a')(1)
         '1\n'
         >>> t('$def with (a=0)\n$a')(1)
         '1\n'
         >>> t('$def with (a=0)\n$a')(a=1)
         '1\n'
         >>> t('$if 1: 1')()
         '1\n'
         >>> t('$if 1:\n    1')()
         '1\n'
         >>> t('$if 0: 0\n$elif 1: 1')()
         '1\n'
         >>> t('$if 0: 0\n$elif None: 0\n$else: 1')()
         '1\n'
         >>> t('$if (0 < 1) and (1 < 2): 1')()
         '1\n'
         >>> t('$for x in [1, 2, 3]: $x')()
         '1\n2\n3\n'
         >>> t('$for x in []: 0\n$else: 1')()
         '1\n'
         >>> t('$def with (a)\n$while a and a.pop(): 1')([1, 2, 3])
         '1\n1\n1\n'
         >>> t('$while 0: 0\n$else: 1')()
         '1\n'
         >>> t('$ a = 1\n$a')()
         '1\n'
         >>> t('$# 0')()
         ''
         >>> t('$def with (d)\n$for k, v in d.iteritems(): $k')({1: 1})
         '1\n'
         >>> t('$def with (a)\n$(a)')(1)
         '1\n'
         >>> t('$def with (a)\n$a')(1)
         '1\n'
         >>> t('$def with (a)\n$a.b')(storage(b=1))
         '1\n'
         >>> t('$def with (a)\n$a[0]')([1])
         '1\n'
         >>> t('${0 or 1}')()
         '1\n'
         >>> t('$ a = [1]\n$a[0]')()
         '1\n'
         >>> t('$ a = {1: 1}\n$a.keys()[0]')()
         '1\n'
         >>> t('$ a = []\n$if not a: 1')()
         '1\n'
         >>> t('$ a = {}\n$if not a: 1')()
         '1\n'
         >>> t('$ a = -1\n$a')()
         '-1\n'
         >>> t('$ a = "1"\n$a')()
         '1\n'
         >>> t('$if 1 is 1: 1')()
         '1\n'
         >>> t('$if not 0: 1')()
         '1\n'
         >>> t('$if 1:\n    $if 1: 1')()
         '1\n'
         >>> t('$ a = 1\n$a')()
         '1\n'
         >>> t('$ a = 1.\n$a')()
         '1.0\n'
         >>> t('$({1: 1}.keys()[0])')()
         '1\n'
         >>> t('$for x in [1, 2, 3]:\n\t$x')()
         '    1\n    2\n    3\n'
         >>> t('$def with (a)\n$:a')(1)
         '1\n'
         >>> t('$def with (a)\n$a')(u'\u203d')
         '\xe2\x80\xbd\n'
         >>> t(u'$def with (a)\n$a $:a')(u'\u203d')
         '\xe2\x80\xbd \xe2\x80\xbd\n'
         >>> t(u'$def with ()\nfoo')()
         'foo\n'
         >>> def f(x): return x
         ...
         >>> t(u'$def with (f)\n$:f("x")')(f)
         'x\n'
         >>> t(u'$def with (f)\n$:f(x="x")')(f)
         'x\n'
         >>> x = t('$var foo: bar')()
         >>> str(x)
         ''
         >>> x.foo
         'bar\n'

see also [template.py doc](/templetor)

## utils.py

`class Storage(dict)`
   : A Storage object is like a dictionary except `obj.foo` can be used
     in addition to `obj['foo']`.
     
         >>> o = storage(a=1)
         >>> o.a
         1
         >>> o['a']
         1
         >>> o.a = 2
         >>> o['a']
         2
         >>> del o.a
         >>> o.a
         Traceback (most recent call last):
             ...
         AttributeError: 'a'

`storify(mapping, *requireds, **defaults)`
   : Creates a `storage` object from dictionary `mapping`, raising `KeyError` if
     d doesn't have all of the keys in `requireds` and using the default 
     values for keys found in `defaults`.
 
     For example, `storify({'a':1, 'c':3}, b=2, c=0)` will return the equivalent of
     `storage({'a':1, 'b':2, 'c':3})`.
     
     If a `storify` value is a list (e.g. multiple values in a form submission), 
     `storify` returns the last element of the list, unless the key appears in 
     `defaults` as a list. Thus:
     
         >>> storify({'a':[1, 2]}).a
         2
         >>> storify({'a':[1, 2]}, a=[]).a
         [1, 2]
         >>> storify({'a':1}, a=[]).a
         [1]
         >>> storify({}, a=[]).a
         []
     
     Similarly, if the value has a `value` attribute, `storify will return _its_
     value, unless the key appears in `defaults` as a dictionary.
     
         >>> storify({'a':storage(value=1)}).a
         1
         >>> storify({'a':storage(value=1)}, a={}).a
         <Storage {'value': 1}>
         >>> storify({}, a={}).a
         {}

`rstrips(text, remove)`
   : removes the string `remove` from the right of `text`
 
         >>> rstrips("foobar", "bar")
         'foo'

`lstrips(text, remove)`
   : removes the string `remove` from the left of `text`
     
         >>> lstrips("foobar", "foo")
         'bar'

`strips(text, remove)`
   : removes the string `remove` from the both sides of `text` 
         >>> strips("foobarfoo", "foo")
         'bar'

`utf8(text)`
   : Encodes text in utf-8.         
         >> utf8(u'\u1234') # doctest doesn't seem to like utf-8
         '\xe1\x88\xb4'
 
         >>> utf8('hello')
         'hello'
         >>> utf8(42)
         '42'

`class TimeoutError(Exception): pass def timelimit(timeout):`
   : A decorator to limit a function to `timeout` seconds, raising `TimeoutError`
     if it takes longer.
     
         >>> import time
         >>> def meaningoflife():
         ...     time.sleep(.2)
         ...     return 42
         >>> 
         >>> timelimit(.1)(meaningoflife)()
         Traceback (most recent call last):
             ...
         TimeoutError: took too long
         >>> timelimit(1)(meaningoflife)()
         42
 
     _Caveat:_ The function isn't stopped after `timeout` seconds but continues 
     executing in a separate thread. (There seems to be no way to kill a thread.)
 
     inspired by <http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/473878>

`class Memoize`
   : 'Memoizes' a function, caching its return values for each input.
     
         >>> import time
         >>> def meaningoflife():
         ...     time.sleep(.2)
         ...     return 42
         >>> fastlife = memoize(meaningoflife)
         >>> meaningoflife()
         42
         >>> timelimit(.1)(meaningoflife)()
         Traceback (most recent call last):
             ...
         TimeoutError: took too long
         >>> fastlife()
         42
         >>> timelimit(.1)(fastlife)()
         42

`re_subm(pat, repl, string)`
   : Like re.sub, but returns the replacement _and_ the match object.
     
         >>> t, m = re_subm('g(oo+)fball', r'f\\1lish', 'goooooofball')
         >>> t
         'foooooolish'
         >>> m.groups()
         ('oooooo',)

`group(seq, size)`
   : Returns an iterator over a series of lists of length size from iterable.
 
         >>> list(group([1,2,3,4], 2))
         [1, 2], [3, 4](/1, 2], [3, 4)

`class IterBetter`
   : Returns an object that can be used as an iterator 
     but can also be used via __getitem__ (although it 
     cannot go backwards -- that is, you cannot request 
     `iterbetter[0]` after requesting `iterbetter[1]`).
     
         >>> import itertools
         >>> c = iterbetter(itertools.count())
         >>> c[1]
         1
         >>> c[5]
         5
         >>> c[3]
         Traceback (most recent call last):
             ...
         IndexError: already passed 3

`dictreverse(mapping)`
   : >>> dictreverse({1: 2, 3: 4})
         {2: 1, 4: 3}

`dictfind(dictionary, element)`
   : Returns a key whose value in `dictionary` is `element` 
     or, if none exists, None.
     
         >>> d = {1:2, 3:4}
         >>> dictfind(d, 4)
         3
         >>> dictfind(d, 5)

`dictfindall(dictionary, element)`
   : Returns the keys whose values in `dictionary` are `element`
     or, if none exists, [].
     
         >>> d = {1:4, 3:4}
         >>> dictfindall(d, 4)
         [1, 3]
         >>> dictfindall(d, 5)
         []

`dictincr(dictionary, element)`
   : Increments `element` in `dictionary`, 
     setting it to one if it doesn't exist.
     
         >>> d = {1:2, 3:4}
         >>> dictincr(d, 1)
         3
         >>> d[1]
         3
         >>> dictincr(d, 5)
         1
         >>> d[5]
         1

`dictadd(*dicts)`
   : Returns a dictionary consisting of the keys in the argument dictionaries.
     If they share a key, the value from the last argument is used.
     
         >>> dictadd({1: 0, 2: 0}, {2: 1, 3: 1})
         {1: 0, 2: 1, 3: 1}

`listget(lst, ind, default=None)`
   : Returns `lst[ind]` if it exists, `default` otherwise.
     
         >>> listget(['a'], 0)
         'a'
         >>> listget(['a'], 1)
         >>> listget(['a'], 1, 'b')
         'b'

`intget(integer, default=None)`
   : Returns `integer` as an int or `default` if it can't.
     
         >>> intget('3')
         3
         >>> intget('3a')
         >>> intget('3a', 0)
         0

`datestr(then, now=None)`
   : Converts a (UTC) datetime object to a nice string representation.
     
         >>> from datetime import datetime, timedelta
         >>> d = datetime(1970, 5, 1)
         >>> datestr(d, now=d)
         '0 microseconds ago'
         >>> for t, v in {
         ...   timedelta(microseconds=1): '1 microsecond ago',
         ...   timedelta(microseconds=2): '2 microseconds ago',
         ...   -timedelta(microseconds=1): '1 microsecond from now',
         ...   -timedelta(microseconds=2): '2 microseconds from now',
         ...   timedelta(microseconds=2000): '2 milliseconds ago',
         ...   timedelta(seconds=2): '2 seconds ago',
         ...   timedelta(seconds=2*60): '2 minutes ago',
         ...   timedelta(seconds=2*60*60): '2 hours ago',
         ...   timedelta(days=2): '2 days ago',
         ... }.iteritems():
         ...     assert datestr(d, now=d+t) == v
         >>> datestr(datetime(1970, 1, 1), now=d)
         'January  1'
         >>> datestr(datetime(1969, 1, 1), now=d)
         'January  1, 1969'
         >>> datestr(datetime(1970, 6, 1), now=d)
         'June  1, 1970'

`numify(string)`
   : Removes all non-digit characters from `string`.
     
         >>> numify('800-555-1212')
         '8005551212'
         >>> numify('800.555.1212')
         '8005551212'

`denumify(string, pattern)`
   : Formats `string` according to `pattern`, where the letter X gets replaced
     by characters from `string`.
     
         >>> denumify("8005551212", "(XXX) XXX-XXXX")
         '(800) 555-1212'

`dateify(datestring)`
   : Formats a numified `datestring` properly.

`class CaptureStdout`
   : Captures everything `func` prints to stdout and returns it instead.
     
         >>> def idiot():
         ...     print "foo"
         >>> capturestdout(idiot)()
         'foo\\n'
     
     **WARNING:** Not threadsafe!

`class Profile`
   : Profiles `func` and returns a tuple containing its output
     and a string with human-readable profiling information.
         
         >>> import time
         >>> out, inf = profile(time.sleep)(.001)
         >>> out
         >>> inf[:10].strip()
         'took 0.0'

`tryall(context, prefix=None)`
   : Tries a series of functions and prints their results. 
     `context` is a dictionary mapping names to values; 
     the value will only be tried if it's callable.
     
         >>> tryall(dict(j=lambda: True))
         j: True
         ----------------------------------------
         results:
            True: 1
 
     For example, you might have a file `test/stuff.py` 
     with a series of functions testing various things in it. 
     At the bottom, have a line:
 
         if __name__ == "__main__": tryall(globals())
 
     Then you can run `python test/stuff.py` and get the results of 
     all the tests.

`class ThreadedDict`
   : Takes a dictionary that maps threads to objects. 
     When a thread tries to get or set an attribute or item 
     of the threadeddict, it passes it on to the object 
     for that thread in dictionary.

`autoassign(self, locals)`
   : Automatically assigns local variables to `self`.
     
         >>> self = storage()
         >>> autoassign(self, dict(a=1, b=2))
         >>> self
         <Storage {'a': 1, 'b': 2}>
     
     Generally used in `__init__` methods, as in:
 
         def __init__(self, foo, bar, baz=1): autoassign(self, locals())

`to36(q)`
   : Converts an integer to base 36 (a useful scheme for human-sayable IDs).
     
         >>> to36(35)
         'z'
         >>> to36(119292)
         '2k1o'
         >>> int(to36(939387374), 36)
         939387374
         >>> to36(0)
         '0'
         >>> to36(-393)
         Traceback (most recent call last):
             ... 
         ValueError: must supply a positive integer

`safemarkdown(text)`
   : Converts text to HTML following the rules of Markdown, but blocking any
     outside HTML input, so that only the things supported by Markdown
     can be used. Also converts raw URLs to links.
 
     (requires [markdown.py](http://webpy.org/markdown.py))

`sendmail(from_address, to_address, subject, message, headers=None, **kw)`
   : Sends the email message `message` with mail and envelope headers
     for from `from_address_` to `to_address` with `subject`. 
     Additional email headers can be specified with the dictionary 
     `headers.
 
     If `web.config.smtp_server` is set, it will send the message
     to that SMTP server. Otherwise it will look for 
     `/usr/lib/sendmail`, the typical location for the sendmail-style
     binary.


## webapi.py

`badrequest()`
   : Return a `400 Bad Request` error.

`notfound()`
   : Returns a `404 Not Found` error.

`gone()`
   : Returns a `410 Gone` error.

`internalerror()`
   : Returns a `500 Internal Server` error.

`header(hdr, value, unique=False)`
   : Adds the header `hdr: value` with the response.
     
     If `unique` is True and a header with that name already exists,
     it doesn't add a new one.

`output(string_)`
   : Appends `string_` to the response.

`flush()`
   : 

`input(*requireds, **defaults)`
   : Returns a `storage` object with the GET and POST arguments. 
     See `storify` for how `requireds` and `defaults` work.

`data()`
   : Returns the data sent with the request.

`setcookie(name, value, expires="", domain=None, secure=False)`
   : Sets a cookie.

`cookies(*requireds, **defaults)`
   : Returns a `storage` object with all the cookies in it.
     See `storify` for how `requireds` and `defaults` work.

`debug(*args)`
   : Prints a prettyprinted version of `args` to stderr.

`load()`
   : Loads a new context for the thread.
     
     You can ask for a function to be run at loadtime by 
     adding it to the dictionary `loadhooks`.

`unload()`
   : Unloads the context for the thread.
     
     You can ask for a function to be run at loadtime by
     adding it ot the dictionary `unloadhooks`.

`wsgifunc(func, *middleware)`
   : Returns a WSGI-compatible function from a webpy-function.

`ctx`
   :     A `storage` object containing various information about the request:
      
    `environ` (aka `env`)
       : A dictionary containing the standard WSGI environment variables.
    
    `host`
       : The domain (`Host` header) requested by the user.
    
    `home`
       : The base path for the application.
    
    `ip`
       : The IP address of the requester.
    
    `method`
       : The HTTP method used.
    
    `path`
       : The path request.
       
    `query`
       : If there are no query arguments, the empty string. Otherwise, a `?` followed
         by the query string.
    
    `fullpath`
       : The full path requested, including query arguments (`== path + query`).
    
    ### Response Data
    
    `status` (default: "200 OK")
       : The status code to be used in the response.
    
    `headers`
       : A list of 2-tuples to be used in the response.
    
    `output`
       : A string to be used as the response.
## wsgi.py

`runfcgi(func, addr=('localhost', 8000))`
   : Runs a WSGI function as a FastCGI server.

`runscgi(func, addr=('localhost', 4000))`
   : Runs a WSGI function as an SCGI server.

`runwsgi(func)`
   : Runs a WSGI-compatible `func` using FCGI, SCGI, or a simple web server,
     as appropriate based on context and `sys.argv`.





































