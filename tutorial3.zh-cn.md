---
layout: default
title: web.py 0.3 新手指南
---

# web.py 0.3 新手指南

## 开始

你知道Python同时你希望制作一个网站。 那么web.py正好提供了一种简单的方法。

如果你希望读完整个指南， 你需要安装Python, web.py, flup, psycopg2, 和Postgres (或者等价的数据库和Python驱动)。 详细，可以查看 [webpy.org](http://webpy.org/).

如果你已经有了一个web.py项目，请看看[升级](/docs/0.3/upgrade) 页面的相关信息。

准备开始。

## URL 处理

任何网站最重要的部分就是它的URL结构。你的URL并不仅仅只是访问者所能看到并且能发给朋友的。它还规定了你网站运行的心智模型。在一些类似[del.icio.us](http://del.icio.us/)的流行网站 , URL甚至是UI的一部分。 web.py使这类强大的URL成为可能。

在开始你的web.py程序之前,打开一个文本文件（文件名为code.py）输入:

    import web

这条语句会导入web.py模块。

现在我们需要把我们的URL结构告诉web.py。让我从下面这个简单的例子开始:

    urls = (
      '/', 'index'
    )

第一部分是匹配URL的[正则表达式](http://osteele.com/tools/rework/)，像`/`、`/help/faq`、`/item/(\d+)`等(`\d+`将匹配数字)。圆括号表示捕捉对应的数据以便后面使用。第二部分是接受请求的类名称，像`index`、`view`、`welcomes.hello` (`welcomes`模块的`hello`类)，或者`get_\1`。`\1` 会被正则表达式捕捉到的内容替换，剩下来捕捉的的内容将被传递到你的函数中去。

这行表示我们要URL`/`(首页)被一个叫`index`的类处理。

现在我们需要创建一个列举这些url的application。

    app = web.application(urls, globals())

这会告诉web.py去创建一个基于我们刚提交的URL列表的application。这个application会在这个文件的全局命名空间中查找对应类。

现在我们需要来写`index`类。虽然大多数人只会看看，并不会注意你的浏览器在使用用于与万维网通信的HTTP语言。具体的细节并不重要，但是要理解web访问者请求web服务器去根据URL(像`/`、`/foo?f=1`)执行一个合适的函数（像`GET`、`POST`）的基本思想。

`GET`是我们都熟悉的。它用于请求网页文本。当你在浏览器输入`harvard.edu`，它会直接访问Harvard的web服务器，去`GET /`。 第二个最有名的是`POST`，它经常被用在提交form，比如请求买什么东西。每当提交一个去做什么事情(像使用信用卡处理一笔交易)的请求时，你可以使用`POST`。这是关键，因为`GET`的URL可以被搜索引擎索引，并通过搜索引擎访问。虽然大部分页面你希望被索引，但是少数类似订单处理的页面你是不希望被索引的 (想象一下Google尝试去购买你网站上的所有东西)。

在我们web.py的代码中，我们是这两则明确区分:

    class index:
        def GET(self):
            return "Hello, world!"

当有人用`GET`请求`/`时，这个`GET`函数随时会被web.py调用。

好了，限制我们只需要最后一句就写完了。这行会告诉web.py开始提供web页面:

    if __name__ == "__main__": app.run()

这会告诉web.py为我们启动上面我们写的应用。

现在注意，即使我已经在这里说了很多，但我们真正有5行这些代码。这就是你需要编写的一个完整的web.py应用。如果你在命令行下面，请输入:

    $ python code.py
    http://0.0.0.0:8080/

现在你的web.py应用正运行在你电脑上的一个真正的web服务器上。 访问那个URL，然后你应该看到"Hello, world!" (你可以通过把IP地址/端口加在"code.py"的后面，来控制web.py在哪里启动服务器。你也可以让它运行在`fastcgi`或`scgi`服务器上)。

**注意:** 如果你不能或者不想使用默认端口，你可以使用这样的命令来指定端口号:

    $ python code.py 1234

## 模板

在 Python 中写 HTML 不是聪明的选择，相反在 HTML 中写 Python 则有趣的多。幸运的是，`web.py` 让这件事情做得简单而又漂亮。

**注意：** 老版本的 `web.py` 使用 [Cheetah 模板系统](http://www.cheetahtemplate.org/)，你可以也欢迎使用其他模板系统，但它可能不会被长久支持。

给模板新建一个目录（命名为 `templates`），在该目录下新建一个以 `.html` 结尾的文件，、HTML 内容如下：

    <em>Hello</em>, world!

你也可以在模板中使用 `web.py` 模板支持代码：

    $def with (name)
    
    $if name:
        I just wanted to say <em>hello</em> to $name.
    $else:
        <em>Hello</em>, world!

As you can see, the templates look a lot like Python files except for the `def with` statement at the top (saying what the template gets called with) and the `$`s placed in front of any code.  Currently, template.py requires the `$def` statement to be the first line of the file.  Also, note that web.py automatically escapes any variables used here, so that if for some reason `name` is set to a value containing some HTML, it will get properly escaped and appear as plain text. If you want to turn this off, write `$:name` instead of `$name`.

Now go back to `code.py`. Under the first line, add:

    render = web.template.render('templates/')

This tells web.py to look for templates in your templates directory. Then change `index.GET` to:

    name = 'Bob'    
    return render.index(name)

('index' is the name of the template and 'name' is the argument passed to it)

Visit your site and it should say hello to Bob. 

But let's say we want to let people enter their own name in. Replace the two lines we added above with:

    i = web.input(name=None)
    return render.index(i.name)

Visit `/` and it should say hello to the world. Visit `/?name=Joe` and it should say hello to Joe.

Of course, having that `?` in the URL is kind of ugly. Instead, change your URL line at the top to:

    '/(.*)', 'index'

and change the definition of `index.GET` to:

    def GET(self, name):
        return render.index(name)

and delete the line setting name. Now visit `/Joe` and it should say hello to Joe.

If you wish to learn more about web.py templates, vist the [templetor page](/docs/0.3/templetor).

## Databasing

**Note:** Before you can start using a database, make sure you have the appropriate database library installed.  For MySQL databases, use [MySQLdb](http://sourceforge.net/project/showfiles.php?group_id=22307) and for Postgres use [psycopg2](http://initd.org/pub/software/psycopg/).

First you need to create a database object.

    db = web.database(dbn='postgres', user='username', pw='password', db='dbname')

(Adjust these -- especially `username`, `password`, and `dbname` -- for your setup. MySQL users will also want to change `dbn` definition to `mysql`.)

That's all you need to do -- web.py will automatically handle connecting and disconnecting from the database.

Using your database engines admin interface, create a simple table in your database:

    CREATE TABLE todo (
      id serial primary key,
      title text,
      created timestamp default now(),
      done boolean default 'f'    );

And an initial row:

    INSERT INTO todo (title) VALUES ('Learn web.py');

Return to editing `code.py` and change `index.GET` to the following, replacing the entire function:

    def GET(self):
        todos = db.select('todo')
        return render.index(todos)

and change back the URL handler to take just `/` as in:

    '/', 'index',

Edit and replace the entire contents of `index.html` so that it reads:

    $def with (todos)
    <ul>
    $for todo in todos:
        <li id="t$todo.id">$todo.title</li>
    </ul>

Visit your site again and you should see your one todo item: "Learn web.py". Congratulations! You've made a full application that reads from the database. Now let's let it write to the database as well.

At the end of `index.html`, add:

    <form method="post" action="add">
    <p><input type="text" name="title" /> <input type="submit" value="Add" /></p>
    </form>

And change your URLs list to read:

    '/', 'index',
    '/add', 'add'

(You've got to be very careful about those commas.  If you omit them, Python adds the strings together and sees `'/index/addadd'` instead of your list of URLs!)

Now add another class:

    class add:
        def POST(self):
            i = web.input()
            n = db.insert('todo', title=i.title)
    	    raise web.seeother('/')

(Notice how we're using `POST` for this?)

`web.input` gives you access to any variables the user submitted through a form. 

Note: In order to access data from multiple identically-named items, in a list format (e.g.: a series of check-boxes all with the attribute name="name") use:

    post_data=web.input(name=[])

`db.insert` inserts values into the database table `todo` and gives you back the ID of the new row. `seeother` redirects users to that URL.

Some quick additional notes: `db.update` works just like `db.insert` except instead of returning the ID it takes it (or a string `WHERE` clause) after the table name.

`web.input`, `db.query`, and other functions in web.py return "Storage objects", which are just like dictionaries except you can do `d.foo` in addition to `d['foo']`. This really cleans up some code.

You can find the full details on these and all the web.py functions in [the documentation](/docs/0.3).

## Developing

web.py also has a few tools to help us with debugging. When running with the built-in webserver, it starts the application in debug mode. In debug mode any changes to code and templates are automatically reloaded and error messages will have more helpful information.

The debug is not enabled when the application is run in a real webserver. If you want to disable the debug mode, you can do so by adding the following line before creating your application/tempaltes.

    web.config.debug = False

This ends the tutorial for now. Take a look at the documentation for lots more cool stuff you can do with web.py.

## What next?

* [more documentation](/docs/0.3)
* [Cookbook](/cookbook)
* [code samples](/src)