---
layout: default
title: How to upgrade from earlier versions of web.py to 0.3
---

# How to upgrade from earlier versions of web.py to 0.3

Web.py 0.3 has some backward-incompatible changes. 

* <a href="#return">prints are replaced by return statements</a>
* <a href="#app">new application framework</a>
* <a href="#db">new database system</a>
* <a href="#exceptions">http errors are exceptions</a>
* <a href="#others">other incompatible changes</a>

<a name="return"></a>
## prints are replaced by return statements

In earlier versions of web.py the GET and POST methods used to print the data to be send to the client. Now instead of printing the data, the data must be returned from that function. This makes post-processing of returned data possible.

If your old code is like this:

    class hello:
        def GET(self):
            print "Hello, world!"

It should become:

    class hello:
        def GET(self):
            return "Hello, world!"

`yield` statements can also be used to return an iterator.

    class hello:
        def GET(self):
            for i in range(5):
                yield "hello " + str(i)

## new application framework

New application framework has been introduced in web.py 0.3 and due to that there is a slight change in the way the program's main section is written.

If your old code has:

    urls = ("/", "index")
    ....

    if __name__ == "__main__":
        web.run(urls, globals())

It should become:

    urls = ("/", "index")
    app = web.application(urls, globals())

    ....

    if __name__ == "__main__":
        app.run()

<a name="db"></a>
## new database system

The database module of web.py has been improved to make it more modular.

If you have code like this:

    web.config.db_parameters = dict(dbn='postgres', db='test', user='joe', password='secret')
    def foo():
        web.insert('test', name='foo')

It should become:

    db = web.database(dbn='postgres', db='test', user='joe', password='secret')
    def foo():
        db.insert('test', name='foo')

Same applies to other database functions like `select`, `update`, `delete` and `query`.

If you are using transactions, they should be changed too.

    def foo():
        web.transact()
        web.insert('t1', name='foo')
        web.insert('t2', name='bar')
        web.commit()

should become:

    def foo():
        t = db.transaction()
        db.insert('t1', name='foo')
        db.insert('t2', name='bar')
        t.commit()

If you are using python 2.5 or later, transactions can be used with `with` statement.

    def foo():
        with db.transaction():
		    db.insert('t1', name='foo')
		    db.insert('t2', name='bar')
            
<a name="exceptions"></a>
## http errors are exceptions

In 0.3, all http errors have been changed to exceptions.

If you have code like this:

    def GET(self):
        ....
        if not page:
            web.notfound()
        else:
            ....

It should become:

    def GET(self):
        ....
        if not page:
            raise web.notfound()
        else:
	    ....

<a name="others"></a>
## Other incompatible changes

In web.py 0.3, `web.input()` returns values in unicode. This may create trouble sometimes.

To force `web.input` to return strings instead of unicode values, use:

    web.input(_unicode=False)