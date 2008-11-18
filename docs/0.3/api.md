---
layout: default
title: API documentation
---

# API documentation


<style type="text/css">
    .content {margin: 10px;}
    .head {margin: -10px;}
</style>
    
* <a href="#web.application">web.application</a>
* <a href="#web.db">web.db</a>
* <a href="#web.debugerror">web.debugerror</a>
* <a href="#web.form">web.form</a>
* <a href="#web.http">web.http</a>
* <a href="#web.httpserver">web.httpserver</a>
* <a href="#web.net">web.net</a>
* <a href="#web.session">web.session</a>
* <a href="#web.template">web.template</a>
* <a href="#web.utils">web.utils</a>
* <a href="#web.webapi">web.webapi</a>
* <a href="#web.webopenid">web.webopenid</a>
* <a href="#web.wsgi">web.wsgi</a>

<a name="web.application"></a>
## web.application

<code class="head">class Reloader</code>: 
Checks to see if any loaded modules have changed on disk and, 
if so, reloads them.

<code class="head">class application</code>: 
Application to delegate requests based on path.

    >>> urls = ("/hello", "hello")
    >>> app = application(urls, globals())
    >>> class hello:
    ...     def GET(self): return "hello"
    >>>
    >>> app.request("/hello").data
    'hello'

<code class="head">class auto_application(application)</code>: 
Application similar to `application` but urls are constructed 
automatiacally using metaclass.

    >>> app = auto_application()
    >>> class hello(app.page):
    ...     def GET(self): return "hello, world"
    ...
    >>> class foo(app.page):
    ...     path = '/foo/.*'
    ...     def GET(self): return "foo"
    >>> app.request("/hello").data
    'hello, world'
    >>> app.request('/foo/bar').data
    'foo'

<code class="head">autodelegate(prefix='')</code>: 
Returns a method that takes one argument and calls the method named prefix+arg,
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

<code class="head">loadhook(h)</code>: 
Converts a load hook into an application processor.

    >>> app = auto_application()
    >>> def f(): "something done before handling request"
    ...
    >>> app.add_processor(loadhook(f))

<code class="head">class subdir_application</code>: 
Application to delegate requests based on path.

    >>> urls = ("/hello", "hello")
    >>> app = application(urls, globals())
    >>> class hello:
    ...     def GET(self): return "hello"
    >>>
    >>> app.request("/hello").data
    'hello'

<code class="head">class subdomain_application(application)</code>: 
Application to delegate requests based on the host.

    >>> urls = ("/hello", "hello")
    >>> app = application(urls, globals())
    >>> class hello:
    ...     def GET(self): return "hello"
    >>>
    >>> mapping = ("hello.example.com", app)
    >>> app2 = subdomain_application(mapping)
    >>> app2.request("/hello", host="hello.example.com").data
    'hello'
    >>> response = app2.request("/hello", host="something.example.com")
    >>> response.status
    '404 Not Found'
    >>> response.data
    'not found'

<code class="head">unloadhook(h)</code>: 
Converts an unload hook into an application processor.

    >>> app = auto_application()
    >>> def f(): "something done after handling request"
    ...
    >>> app.add_processor(unloadhook(f))    

<a name="web.db"></a>
## web.db

<code class="head">class DB</code>: 
Database

<code class="head">class FirebirdDB(DB)</code>: 
Firebird Database.
    

<code class="head">class MSSQLDB(DB)</code>: 
None

<code class="head">class MySQLDB(DB)</code>: 
None

<code class="head">class OracleDB(DB)</code>: 
None

<code class="head">class PostgresDB(DB)</code>: 
Postgres driver.

<code class="head">class SQLLiteral</code>: 
Protects a string from `sqlquote`.

    >>> sqlquote('NOW()')
    <sql: "'NOW()'">
    >>> sqlquote(SQLLiteral('NOW()'))
    <sql: 'NOW()'>

<code class="head">class SQLParam</code>: 
Parameter in SQLQuery.

    >>> q = SQLQuery(["SELECT * FROM test WHERE name=", SQLParam("joe")])
    >>> q
    <sql: "SELECT * FROM test WHERE name='joe'">
    >>> q.query()
    'SELECT * FROM test WHERE name=%s'
    >>> q.values()
    ['joe']

<code class="head">class SQLQuery</code>: 
You can pass this sort of thing as a clause in any db function.
Otherwise, you can pass a dictionary to the keyword argument `vars`
and the function will call reparam for you.

Internally, consists of `items`, which is a list of strings and
SQLParams, which get concatenated to produce the actual query.

<code class="head">class SqliteDB(DB)</code>: 
None

<code class="head">class Transaction</code>: 
Database transaction.

<code class="head">class TransactionError(Exception)</code>: 
None

<code class="head">class UnknownDB(Exception)</code>: 
raised for unsupported dbms

<code class="head">class UnknownParamstyle(Exception)</code>: 
raised for unsupported db paramstyles

(currently supported: qmark, numeric, format, pyformat)

<code class="head">database(dburl=None, **params)</code>: 
Creates appropriate database using params.

Pooling will be enabled if DBUtils module is available. 
Pooling can be disabled by passing pooling=False in params.

<code class="head">register_database(name, clazz)</code>: 
Register a database.

    >>> class LegacyDB(DB): 
    ...     def __init__(self, **params): 
    ...        pass 
    ...
    >>> register_database('legacy', LegacyDB)
    >>> db = database(dbn='legacy', db='test', user='joe', passwd='secret') 

<code class="head">reparam(string_, dictionary)</code>: 
Takes a string and a dictionary and interpolates the string
using values from the dictionary. Returns an `SQLQuery` for the result.

    >>> reparam("s = $s", dict(s=True))
    <sql: "s = 't'">

<code class="head">sqlify(obj)</code>: 
converts `obj` to its proper SQL version

    >>> sqlify(None)
    'NULL'
    >>> sqlify(True)
    "'t'"
    >>> sqlify(3)
    '3'

<code class="head">sqllist(lst)</code>: 
Converts the arguments for use in something like a WHERE clause.

    >>> sqllist(['a', 'b'])
    'a, b'
    >>> sqllist('a')
    'a'
    >>> sqllist(u'abc')
    u'abc'

<code class="head">class sqlliteral</code>: 
Protects a string from `sqlquote`.

    >>> sqlquote('NOW()')
    <sql: "'NOW()'">
    >>> sqlquote(SQLLiteral('NOW()'))
    <sql: 'NOW()'>

<code class="head">sqlors(left, lst)</code>: 
`left is a SQL clause like `tablename.arg = ` 
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

<code class="head">class sqlparam</code>: 
Parameter in SQLQuery.

    >>> q = SQLQuery(["SELECT * FROM test WHERE name=", SQLParam("joe")])
    >>> q
    <sql: "SELECT * FROM test WHERE name='joe'">
    >>> q.query()
    'SELECT * FROM test WHERE name=%s'
    >>> q.values()
    ['joe']

<code class="head">sqlquote(a)</code>: 
Ensures `a` is quoted properly for use in a SQL query.

    >>> 'WHERE x = ' + sqlquote(True) + ' AND y = ' + sqlquote(3)
    <sql: "WHERE x = 't' AND y = 3">

<code class="head">sqlwhere(dictionary, grouping=' AND ')</code>: 
Converts a `dictionary` to an SQL WHERE clause `SQLQuery`.

    >>> sqlwhere({'cust_id': 2, 'order_id':3})
    <sql: 'order_id = 3 AND cust_id = 2'>
    >>> sqlwhere({'cust_id': 2, 'order_id':3}, grouping=', ')
    <sql: 'order_id = 3, cust_id = 2'>
    >>> sqlwhere({'a': 'a', 'b': 'b'}).query()
    'a = %s AND b = %s'

<a name="web.debugerror"></a>
## web.debugerror

<code class="head">debugerror()</code>: 
A replacement for `internalerror` that presents a nice page with lots
of debug information for the programmer.

(Based on the beautiful 500 page from [Django](http://djangoproject.com/), 
designed by [Wilson Miner](http://wilsonminer.com/).)

<code class="head">djangoerror()</code>: 
None

<code class="head">emailerrors(email_address, olderror)</code>: 
Wraps the old `internalerror` handler (pass as `olderror`) to 
additionally email all errors to `email_address`, to aid in 
debugging production websites.

Emails contain a normal text traceback as well as an
attachment containing the nice `debugerror` page.

<a name="web.form"></a>
## web.form

<code class="head">class Button(Input)</code>: 
None

<code class="head">class Checkbox(Input)</code>: 
None

<code class="head">class Dropdown(Input)</code>: 
None

<code class="head">class File(Input)</code>: 
None

<code class="head">class Form</code>: 
HTML form.

    >>> f = Form(Textbox("x"))
    >>> f.render()
    '<table>\n    <tr><th><label for="x">x</label></th><td><input type="text" name="x" id="x" /></td></tr>\n</table>'

<code class="head">class Hidden(Input)</code>: 
None

<code class="head">class Input(object)</code>: 
None

<code class="head">class Password(Input)</code>: 
None

<code class="head">class Radio(Input)</code>: 
None

<code class="head">class Textarea(Input)</code>: 
None

<code class="head">class Textbox(Input)</code>: 
None

<code class="head">class Validator</code>: 
None

<code class="head">attrget(obj, attr, value=None)</code>: 
None

<code class="head">class regexp(Validator)</code>: 
None

<a name="web.http"></a>
## web.http

<code class="head">background(func)</code>: 
A function decorator to run a long-running function as a background thread.

<code class="head">backgrounder(func)</code>: 
None

<code class="head">changequery(query=None, **kw)</code>: 
Imagine you're at `/foo?a=1&b=2`. Then `changequery(a=3)` will return
`/foo?a=3&b=2` -- the same URL but with the arguments you requested
changed.

<code class="head">expires(delta)</code>: 
Outputs an `Expires` header for `delta` from now. 
`delta` is a `timedelta` object or a number of seconds.

<code class="head">lastmodified(date_obj)</code>: 
Outputs a `Last-Modified` header for `datetime`.

<code class="head">modified(date=None, etag=None)</code>: 
None

<code class="head">prefixurl(base='')</code>: 
Sorry, this function is really difficult to explain.
Maybe some other time.

<code class="head">profiler(app)</code>: 
Outputs basic profiling information at the bottom of each response.

<code class="head">url(path=None, **kw)</code>: 
Makes url by concatinating web.ctx.homepath and path and the 
query string created using the arguments.

<code class="head">urlencode(query)</code>: 
Same as urllib.urlencode, but supports unicode strings.

    >>> urlencode({'text':'foo bar'})
    'text=foo+bar'

<code class="head">write(cgi_response)</code>: 
Converts a standard CGI-style string response into `header` and 
`output` calls.

<a name="web.httpserver"></a>
## web.httpserver

<code class="head">runbasic(func, server_address=('0.0.0.0', 8080))</code>: 
  Runs a simple HTTP server hosting WSGI app `func`. The directory `static/` 
  is hosted statically.

  Based on [WsgiServer][ws] from [Colin Stewart][cs].
  
[ws]: http://www.owlfish.com/software/wsgiutils/documentation/wsgi-server-api.html
[cs]: http://www.owlfish.com/
  

<code class="head">runsimple(func, server_address=('0.0.0.0', 8080))</code>: 
Runs [CherryPy][cp] WSGI server hosting WSGI app `func`. 
The directory `static/` is hosted statically.

[cp]: http://www.cherrypy.org

<a name="web.net"></a>
## web.net

<code class="head">htmlquote(text)</code>: 
Encodes `text` for raw use in HTML.

    >>> htmlquote("<'&\">")
    '&lt;&#39;&amp;&quot;&gt;'

<code class="head">htmlunquote(text)</code>: 
Decodes `text` that's HTML quoted.

    >>> htmlunquote('&lt;&#39;&amp;&quot;&gt;')
    '<\'&">'

<code class="head">httpdate(date_obj)</code>: 
Formats a datetime object for use in HTTP headers.

    >>> import datetime
    >>> httpdate(datetime.datetime(1970, 1, 1, 1, 1, 1))
    'Thu, 01 Jan 1970 01:01:01 GMT'

<code class="head">parsehttpdate(string_)</code>: 
Parses an HTTP date into a datetime object.

    >>> parsehttpdate('Thu, 01 Jan 1970 01:01:01 GMT')
    datetime.datetime(1970, 1, 1, 1, 1, 1)

<code class="head">urlquote(val)</code>: 
Quotes a string for use in a URL.

    >>> urlquote('://?f=1&j=1')
    '%3A//%3Ff%3D1%26j%3D1'
    >>> urlquote(None)
    ''
    >>> urlquote(u'\u203d')
    '%E2%80%BD'

<code class="head">validaddr(string_)</code>: 
Returns either (ip_address, port) or "/path/to/socket" from string_

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

<code class="head">validip(ip, defaultaddr='0.0.0.0', defaultport=8080)</code>: 
Returns `(ip_address, port)` from string `ip_addr_port`

<code class="head">validipaddr(address)</code>: 
Returns True if `address` is a valid IPv4 address.

    >>> validipaddr('192.168.1.1')
    True
    >>> validipaddr('192.168.1.800')
    False
    >>> validipaddr('192.168.1')
    False

<code class="head">validipport(port)</code>: 
Returns True if `port` is a valid IPv4 port.

    >>> validipport('9000')
    True
    >>> validipport('foo')
    False
    >>> validipport('1000000')
    False

<code class="head">websafe(val)</code>: 
Converts `val` so that it's safe for use in UTF-8 HTML.

    >>> websafe("<'&\">")
    '&lt;&#39;&amp;&quot;&gt;'
    >>> websafe(None)
    ''
    >>> websafe(u'\u203d')
    '\xe2\x80\xbd'

<a name="web.session"></a>
## web.session

<code class="head">class DBStore(Store)</code>: 
Store for saving a session in database
Needs a table with the following columns:

    session_id CHAR(128) UNIQUE NOT NULL,
    atime DATETIME NOT NULL default current_timestamp,
    data TEXT

<code class="head">class DiskStore(Store)</code>: 
Store for saving a session on disk.

    >>> import tempfile
    >>> root = tempfile.mkdtemp()
    >>> s = DiskStore(root)
    >>> s['a'] = 'foo'
    >>> s['a']
    'foo'
    >>> time.sleep(0.01)
    >>> s.cleanup(0.01)
    >>> s['a']
    Traceback (most recent call last):
        ...
    KeyError: 'a'

<code class="head">class Session(ThreadedDict)</code>: 
Session management for web.py
    

<code class="head">class SessionExpired(HTTPError)</code>: 
None

<code class="head">class Store</code>: 
Base class for session stores

<a name="web.template"></a>
## web.template

<code class="head">class AssignmentNode</code>: 
None

<code class="head">class BaseTemplate</code>: 
None

<code class="head">class BlockNode</code>: 
None

<code class="head">class CodeNode</code>: 
None

<code class="head">class CompiledTemplate(Template)</code>: 
None

<code class="head">class DefNode(BlockNode)</code>: 
None

<code class="head">class DefwithNode</code>: 
None

<code class="head">class ElifNode(BlockNode)</code>: 
None

<code class="head">class ElseNode(BlockNode)</code>: 
None

<code class="head">class ExpressionNode</code>: 
None

<code class="head">class ForLoop</code>: 
Wrapper for expression in for stament to support loop.xxx helpers.

    >>> loop = ForLoop()
    >>> for x in loop.setup(['a', 'b', 'c']):
    ...     print loop.index, loop.revindex, loop.parity, x
    ...
    1 3 odd a
    2 2 even b
    3 1 odd c
    >>> loop.index
    Traceback (most recent call last):
        ...
    AttributeError: index

<code class="head">class ForLoopContext</code>: 
Stackable context for ForLoop to support nested for loops.
    

<code class="head">class ForNode(BlockNode)</code>: 
None

<code class="head">class IfNode(BlockNode)</code>: 
None

<code class="head">class LineNode</code>: 
None

<code class="head">class ParseError(Exception)</code>: 
None

<code class="head">class Parser</code>: 
Parser Base.
    

<code class="head">class PythonTokenizer</code>: 
Utility wrapper over python tokenizer.

<code class="head">class Render</code>: 
The most preferred way of using templates.

    render = web.template.render('templates')
    print render.foo()
    
Optional parameter can be `base` can be used to pass output of 
every template through the base template.

    render = web.template.render('templates', base='layout')

<code class="head">class SafeVisitor(object)</code>: 
Make sure code is safe by walking through the AST.

Code considered unsafe if:
    * it has restricted AST nodes
    * it is trying to access resricted attributes   
    
Adopted from http://www.zafar.se/bkz/uploads/safe.txt (public domain, Babar K. Zafar)

<code class="head">class SecurityError(Exception)</code>: 
The template seems to be trying to do something naughty.

<code class="head">class SuiteNode</code>: 
Suite is a list of sections.

<code class="head">class Template(BaseTemplate)</code>: 
None

<code class="head">class TemplateResult(Storage)</code>: 
Dictionary like object for storing template output.

A template can specify key-value pairs in the output using 
`var` statements. Each `var` statement adds a new key to the 
template output and the main output is stored with key 
__body__.

    >>> d = TemplateResult(__body__='hello, world', x='foo')
    >>> d
    <TemplateResult: {'__body__': 'hello, world', 'x': 'foo'}>
    >>> print d
    hello, world

<code class="head">class TextNode</code>: 
None

<code class="head">class VarNode</code>: 
None

<code class="head">compile_templates(root)</code>: 
Compiles templates to python code.

<code class="head">config</code>: 

A configuration object for various aspects of web.py.

`db_parameters`
   : A dictionary containing the parameters to be passed to `connect`
     when `load()` is called.
`db_printing`
   : Set to `True` if you would like SQL queries and timings to be
     printed to the debug output.
`session_parameters`
   : A dictionary containing session parameters
    cookie_name, cookie_domain, timeout, 
    ignore_change_ip, ignore_expiry, expired_message

<code class="head">frender(path, **keywords)</code>: 
Creates a template from the given file path.
    

<code class="head">class render</code>: 
The most preferred way of using templates.

    render = web.template.render('templates')
    print render.foo()
    
Optional parameter can be `base` can be used to pass output of 
every template through the base template.

    render = web.template.render('templates', base='layout')

<code class="head">splitline(text)</code>: 
Splits the given text at newline.

    >>> splitline('foo\nbar')
    ('foo\n', 'bar')
    >>> splitline('foo')
    ('foo', '')
    >>> splitline('')
    ('', '')

<code class="head">test()</code>: 
Doctest for testing template module.

Define a utility function to run template test.

    >>> class TestResult(TemplateResult):
    ...     def __repr__(self): return repr(unicode(self))
    ...
    >>> def t(code, **keywords):
    ...     tmpl = Template(code, **keywords)
    ...     return lambda *a, **kw: TestResult(tmpl(*a, **kw))
    ...

Simple tests.

    >>> t('1')()
    u'1\n'
    >>> t('$def with ()\n1')()
    u'1\n'
    >>> t('$def with (a)\n$a')(1)
    u'1\n'
    >>> t('$def with (a=0)\n$a')(1)
    u'1\n'
    >>> t('$def with (a=0)\n$a')(a=1)
    u'1\n'

Test complicated expressions.
    
    >>> t('$def with (x)\n$x.upper()')('hello')
    u'HELLO\n'
    >>> t('$(2 * 3 + 4 * 5)')()
    u'26\n'
    >>> t('${2 * 3 + 4 * 5}')()
    u'26\n'
    >>> t('$def with (limit)\nkeep $(limit)ing.')('go')
    u'keep going.\n'
    >>> t('$def with (a)\n$a.b[0]')(storage(b=[1]))
    u'1\n'
    
Test html escaping.

    >>> t('$def with (x)\n$x', filename='a.html')('<html>')
    u'&lt;html&gt;\n'
    >>> t('$def with (x)\n$x', filename='a.txt')('<html>')
    u'<html>\n'
            
Test if, for and while.

    >>> t('$if 1: 1')()
    u'1\n'
    >>> t('$if 1:\n    1')()
    u'1\n'
    >>> t('$if 1:\n    1\\')()
    u'1'
    >>> t('$if 0: 0\n$elif 1: 1')()
    u'1\n'
    >>> t('$if 0: 0\n$elif None: 0\n$else: 1')()
    u'1\n'
    >>> t('$if 0 < 1 and 1 < 2: 1')()
    u'1\n'
    >>> t('$for x in [1, 2, 3]: $x')()
    u'1\n2\n3\n'
    >>> t('$def with (d)\n$for k, v in d.iteritems(): $k')({1: 1})
    u'1\n'
    >>> t('$for x in [1, 2, 3]:\n\t$x')()
    u'    1\n    2\n    3\n'
    >>> t('$def with (a)\n$while a and a.pop():1')([1, 2, 3])
    u'1\n1\n1\n'

The space after : must be ignored.

    >>> t('$if True: foo')()
    u'foo\n'

Test loop.xxx.

    >>> t("$for i in range(5):$loop.index, $loop.parity")()
    u'1, odd\n2, even\n3, odd\n4, even\n5, odd\n'
    >>> t("$for i in range(2):\n    $for j in range(2):$loop.parent.parity $loop.parity")()
    u'odd odd\nodd even\neven odd\neven even\n'
    
Test assignment.

    >>> t('$ a = 1\n$a')()
    u'1\n'
    >>> t('$ a = [1]\n$a[0]')()
    u'1\n'
    >>> t('$ a = {1: 1}\n$a.keys()[0]')()
    u'1\n'
    >>> t('$ a = []\n$if not a: 1')()
    u'1\n'
    >>> t('$ a = {}\n$if not a: 1')()
    u'1\n'
    >>> t('$ a = -1\n$a')()
    u'-1\n'
    >>> t('$ a = "1"\n$a')()
    u'1\n'

Test comments.

    >>> t('$# 0')()
    u'\n'
    >>> t('hello$#comment1\nhello$#comment2')()
    u'hello\nhello\n'
    >>> t('$#comment0\nhello$#comment1\nhello$#comment2')()
    u'\nhello\nhello\n'
    
Test unicode.

    >>> t('$def with (a)\n$a')(u'\u203d')
    u'\u203d\n'
    >>> t('$def with (a)\n$a')(u'\u203d'.encode('utf-8'))
    u'\u203d\n'
    >>> t(u'$def with (a)\n$a $:a')(u'\u203d')
    u'\u203d \u203d\n'
    >>> t(u'$def with ()\nfoo')()
    u'foo\n'
    >>> def f(x): return x
    ...
    >>> t(u'$def with (f)\n$:f("x")')(f)
    u'x\n'
    >>> t('$def with (f)\n$:f("x")')(f)
    u'x\n'

Test dollar escaping.

    >>> t("Stop, $$money isn't evaluated.")()
    u"Stop, $money isn't evaluated.\n"
    >>> t("Stop, \$money isn't evaluated.")()
    u"Stop, $money isn't evaluated.\n"
    
Test space sensitivity.

    >>> t('$def with (x)\n$x')(1)
    u'1\n'
    >>> t('$def with(x ,y)\n$x')(1, 1)
    u'1\n'
    >>> t('$(1 + 2*3 + 4)')()
    u'11\n'
    
Make sure globals are working.
        
    >>> t('$x')()
    Traceback (most recent call last):
        ...
    NameError: global name 'x' is not defined
    >>> t('$x', globals={'x': 1})()
    u'1\n'
    
Can't change globals.

    >>> t('$ x = 2\n$x', globals={'x': 1})()
    u'2\n'
    >>> t('$ x = x + 1\n$x', globals={'x': 1})()
    Traceback (most recent call last):
        ...
    UnboundLocalError: local variable 'x' referenced before assignment

Make sure builtins are customizable.

    >>> t('$min(1, 2)')()
    u'1\n'
    >>> t('$min(1, 2)', builtins={})()
    Traceback (most recent call last):
        ...
    NameError: global name 'min' is not defined
    
Test vars.

    >>> x = t('$var x: 1')()
    >>> x.x
    u'1'
    >>> x = t('$var x = 1')()
    >>> x.x
    1
    >>> x = t('$var x:  \n    foo\n    bar')()
    >>> x.x
    u'foo\nbar\n'

<a name="web.utils"></a>
## web.utils

<code class="head">class CaptureStdout</code>: 
Captures everything `func` prints to stdout and returns it instead.

    >>> def idiot():
    ...     print "foo"
    >>> capturestdout(idiot)()
    'foo\n'

**WARNING:** Not threadsafe!

<code class="head">class IterBetter</code>: 
Returns an object that can be used as an iterator 
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

<code class="head">class Memoize</code>: 
'Memoizes' a function, caching its return values for each input.

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

<code class="head">class Profile</code>: 
Profiles `func` and returns a tuple containing its output
and a string with human-readable profiling information.
    
    >>> import time
    >>> out, inf = profile(time.sleep)(.001)
    >>> out
    >>> inf[:10].strip()
    'took 0.0'

<code class="head">class Storage(dict)</code>: 
A Storage object is like a dictionary except `obj.foo` can be used
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

<code class="head">class ThreadedDict</code>: 
Thread local storage.

    >>> d = ThreadedDict()
    >>> d.x = 1
    >>> d.x
    1
    >>> import threading
    >>> def f(): d.x = 2
    >>> t = threading.Thread(target=f)
    >>> t.start()
    >>> t.join()
    >>> d.x
    1

<code class="head">class TimeoutError(Exception)</code>: 
None

<code class="head">autoassign(self, locals)</code>: 
Automatically assigns local variables to `self`.

    >>> self = storage()
    >>> autoassign(self, dict(a=1, b=2))
    >>> self
    <Storage {'a': 1, 'b': 2}>

Generally used in `__init__` methods, as in:

    def __init__(self, foo, bar, baz=1): autoassign(self, locals())

<code class="head">class capturestdout</code>: 
Captures everything `func` prints to stdout and returns it instead.

    >>> def idiot():
    ...     print "foo"
    >>> capturestdout(idiot)()
    'foo\n'

**WARNING:** Not threadsafe!

<code class="head">commify(n)</code>: 
Add commas to an integer `n`.

    >>> commify(1)
    '1'
    >>> commify(123)
    '123'
    >>> commify(1234)
    '1,234'
    >>> commify(1234567890)
    '1,234,567,890'
    >>> commify(None)
    >>>

<code class="head">cond(predicate, consequence, alternative=None)</code>: 
Function replacement for if-else to use in expressions.
    
    >>> x = 2
    >>> cond(x % 2 == 0, "even", "odd")
    'even'
    >>> cond(x % 2 == 0, "even", "odd") + '_row'
    'even_row'

<code class="head">dateify(datestring)</code>: 
Formats a numified `datestring` properly.

<code class="head">datestr(then, now=None)</code>: 
Converts a (UTC) datetime object to a nice string representation.

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

<code class="head">denumify(string, pattern)</code>: 
Formats `string` according to `pattern`, where the letter X gets replaced
by characters from `string`.

    >>> denumify("8005551212", "(XXX) XXX-XXXX")
    '(800) 555-1212'

<code class="head">dictadd(*dicts)</code>: 
Returns a dictionary consisting of the keys in the argument dictionaries.
If they share a key, the value from the last argument is used.

    >>> dictadd({1: 0, 2: 0}, {2: 1, 3: 1})
    {1: 0, 2: 1, 3: 1}

<code class="head">dictfind(dictionary, element)</code>: 
Returns a key whose value in `dictionary` is `element` 
or, if none exists, None.

    >>> d = {1:2, 3:4}
    >>> dictfind(d, 4)
    3
    >>> dictfind(d, 5)

<code class="head">dictfindall(dictionary, element)</code>: 
Returns the keys whose values in `dictionary` are `element`
or, if none exists, [].

    >>> d = {1:4, 3:4}
    >>> dictfindall(d, 4)
    [1, 3]
    >>> dictfindall(d, 5)
    []

<code class="head">dictincr(dictionary, element)</code>: 
Increments `element` in `dictionary`, 
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

<code class="head">dictreverse(mapping)</code>: 
Returns a new dictionary with keys and values swapped.

    >>> dictreverse({1: 2, 3: 4})
    {2: 1, 4: 3}

<code class="head">group(seq, size)</code>: 
Returns an iterator over a series of lists of length size from iterable.

    >>> list(group([1,2,3,4], 2))
    [1, 2], [3, 4](/1, 2], [3, 4)

<code class="head">intget(integer, default=None)</code>: 
Returns `integer` as an int or `default` if it can't.

    >>> intget('3')
    3
    >>> intget('3a')
    >>> intget('3a', 0)
    0

<code class="head">class iterbetter</code>: 
Returns an object that can be used as an iterator 
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

<code class="head">listget(lst, ind, default=None)</code>: 
Returns `lst[ind]` if it exists, `default` otherwise.

    >>> listget(['a'], 0)
    'a'
    >>> listget(['a'], 1)
    >>> listget(['a'], 1, 'b')
    'b'

<code class="head">lstrips(text, remove)</code>: 
removes the string `remove` from the left of `text`

    >>> lstrips("foobar", "foo")
    'bar'

<code class="head">class memoize</code>: 
'Memoizes' a function, caching its return values for each input.

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

<code class="head">nthstr(n)</code>: 
Formats an ordinal.
Doesn't handle negative numbers.

    >>> nthstr(1)
    '1st'
    >>> nthstr(0)
    '0th'
    >>> [nthstr(x) for x in [2, 3, 4, 5, 10, 11, 12, 13, 14, 15]]
    ['2nd', '3rd', '4th', '5th', '10th', '11th', '12th', '13th', '14th', '15th']
    >>> [nthstr(x) for x in [91, 92, 93, 94, 99, 100, 101, 102]]
    ['91st', '92nd', '93rd', '94th', '99th', '100th', '101st', '102nd']
    >>> [nthstr(x) for x in [111, 112, 113, 114, 115]]
    ['111th', '112th', '113th', '114th', '115th']

<code class="head">numify(string)</code>: 
Removes all non-digit characters from `string`.

    >>> numify('800-555-1212')
    '8005551212'
    >>> numify('800.555.1212')
    '8005551212'

<code class="head">class profile</code>: 
Profiles `func` and returns a tuple containing its output
and a string with human-readable profiling information.
    
    >>> import time
    >>> out, inf = profile(time.sleep)(.001)
    >>> out
    >>> inf[:10].strip()
    'took 0.0'

<code class="head">re_subm(pat, repl, string)</code>: 
Like re.sub, but returns the replacement _and_ the match object.

    >>> t, m = re_subm('g(oo+)fball', r'f\1lish', 'goooooofball')
    >>> t
    'foooooolish'
    >>> m.groups()
    ('oooooo',)

<code class="head">rstrips(text, remove)</code>: 
removes the string `remove` from the right of `text`

    >>> rstrips("foobar", "bar")
    'foo'

<code class="head">safemarkdown(text)</code>: 
Converts text to HTML following the rules of Markdown, but blocking any
outside HTML input, so that only the things supported by Markdown
can be used. Also converts raw URLs to links.

(requires [markdown.py](http://webpy.org/markdown.py))

<code class="head">safestr(obj, encoding='utf-8')</code>: 
Converts any given object to utf-8 encoded string. 

    >>> safestr('hello')
    'hello'
    >>> safestr(u'\u1234')
    '\xe1\x88\xb4'
    >>> safestr(2)
    '2'

<code class="head">safeunicode(obj, encoding='utf-8')</code>: 
Converts any given object to unicode string.

    >>> safeunicode('hello')
    u'hello'
    >>> safeunicode(2)
    u'2'
    >>> safeunicode('\xe1\x88\xb4')
    u'\u1234'

<code class="head">sendmail(from_address, to_address, subject, message, headers=None, **kw)</code>: 
Sends the email message `message` with mail and envelope headers
for from `from_address_` to `to_address` with `subject`. 
Additional email headers can be specified with the dictionary 
`headers.

If `web.config.smtp_server` is set, it will send the message
to that SMTP server. Otherwise it will look for 
`/usr/sbin/sendmail`, the typical location for the sendmail-style
binary. To use sendmail from a different path, set `web.config.sendmail_path`.

<code class="head">class storage(dict)</code>: 
A Storage object is like a dictionary except `obj.foo` can be used
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

<code class="head">storify(mapping, *requireds, **defaults)</code>: 
Creates a `storage` object from dictionary `mapping`, raising `KeyError` if
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
    
Optionally, keyword parameter `_unicode` can be passed to convert all values to unicode.

    >>> storify({'x': 'a'}, _unicode=True)
    <Storage {'x': u'a'}>
    >>> storify({'x': storage(value='a')}, x={}, _unicode=True)
    <Storage {'x': <Storage {'value': 'a'}>}>
    >>> storify({'x': storage(value='a')}, _unicode=True)
    <Storage {'x': u'a'}>

<code class="head">strips(text, remove)</code>: 
removes the string `remove` from the both sides of `text`

    >>> strips("foobarfoo", "foo")
    'bar'

<code class="head">class threadeddict</code>: 
Thread local storage.

    >>> d = ThreadedDict()
    >>> d.x = 1
    >>> d.x
    1
    >>> import threading
    >>> def f(): d.x = 2
    >>> t = threading.Thread(target=f)
    >>> t.start()
    >>> t.join()
    >>> d.x
    1

<code class="head">timelimit(timeout)</code>: 
A decorator to limit a function to `timeout` seconds, raising `TimeoutError`
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

<code class="head">to36(q)</code>: 
Converts an integer to base 36 (a useful scheme for human-sayable IDs).

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

<code class="head">tryall(context, prefix=None)</code>: 
Tries a series of functions and prints their results. 
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

<code class="head">utf8(obj, encoding='utf-8')</code>: 
Converts any given object to utf-8 encoded string. 

    >>> safestr('hello')
    'hello'
    >>> safestr(u'\u1234')
    '\xe1\x88\xb4'
    >>> safestr(2)
    '2'

<a name="web.webapi"></a>
## web.webapi

<code class="head">class BadRequest(HTTPError)</code>: 
`400 Bad Request` error.

<code class="head">class Found(Redirect)</code>: 
A `302 Found` redirect.

<code class="head">class Gone(HTTPError)</code>: 
`410 Gone` error.

<code class="head">class HTTPError(Exception)</code>: 
None

<code class="head">InternalError(message=None)</code>: 
Returns HTTPError with '500 internal error' error from the active application.
    

<code class="head">class NoMethod(HTTPError)</code>: 
A `405 Method Not Allowed` error.

<code class="head">NotFound(message=None)</code>: 
Returns HTTPError with '404 Not Found' error from the active application.
    

<code class="head">class Redirect(HTTPError)</code>: 
A `301 Moved Permanently` redirect.

<code class="head">class SeeOther(Redirect)</code>: 
A `303 See Other` redirect.

<code class="head">class TempRedirect(Redirect)</code>: 
A `307 Temporary Redirect` redirect.

<code class="head">class badrequest(HTTPError)</code>: 
`400 Bad Request` error.

<code class="head">config</code>: 

A configuration object for various aspects of web.py.

`db_parameters`
   : A dictionary containing the parameters to be passed to `connect`
     when `load()` is called.
`db_printing`
   : Set to `True` if you would like SQL queries and timings to be
     printed to the debug output.
`session_parameters`
   : A dictionary containing session parameters
    cookie_name, cookie_domain, timeout, 
    ignore_change_ip, ignore_expiry, expired_message

<code class="head">cookies(*requireds, **defaults)</code>: 
Returns a `storage` object with all the cookies in it.
See `storify` for how `requireds` and `defaults` work.

<code class="head">data()</code>: 
Returns the data sent with the request.

<code class="head">debug(*args)</code>: 
Prints a prettyprinted version of `args` to stderr.

<code class="head">class found(Redirect)</code>: 
A `302 Found` redirect.

<code class="head">class gone(HTTPError)</code>: 
`410 Gone` error.

<code class="head">header(hdr, value, unique=False)</code>: 
Adds the header `hdr: value` with the response.

If `unique` is True and a header with that name already exists,
it doesn't add a new one. 

<code class="head">input(*requireds, **defaults)</code>: 
Returns a `storage` object with the GET and POST arguments. 
See `storify` for how `requireds` and `defaults` work.

<code class="head">internalerror(message=None)</code>: 
Returns HTTPError with '500 internal error' error from the active application.
    

<code class="head">class nomethod(HTTPError)</code>: 
A `405 Method Not Allowed` error.

<code class="head">notfound(message=None)</code>: 
Returns HTTPError with '404 Not Found' error from the active application.
    

<code class="head">class redirect(HTTPError)</code>: 
A `301 Moved Permanently` redirect.

<code class="head">class seeother(Redirect)</code>: 
A `303 See Other` redirect.

<code class="head">setcookie(name, value, expires='', domain=None, secure=False)</code>: 
Sets a cookie.

<code class="head">class tempredirect(Redirect)</code>: 
A `307 Temporary Redirect` redirect.

<a name="web.webopenid"></a>
## web.webopenid

<code class="head">form(openid_loc)</code>: 
None

<code class="head">class host</code>: 
None

<code class="head">logout()</code>: 
None

<code class="head">status()</code>: 
None

<a name="web.wsgi"></a>
## web.wsgi

<code class="head">runfcgi(func, addr=('localhost', 8000))</code>: 
Runs a WSGI function as a FastCGI server.

<code class="head">runscgi(func, addr=('localhost', 4000))</code>: 
Runs a WSGI function as an SCGI server.

<code class="head">runwsgi(func)</code>: 
Runs a WSGI-compatible `func` using FCGI, SCGI, or a simple web server,
as appropriate based on context and `sys.argv`.

