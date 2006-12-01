---
layout: default
title: web.py 0.2 tutorial
---

# web.py 0.2 tutorial

## Starting

So you know Python and want to make a website. web.py provides the code to make that easy.

If you want to do the whole tutorial, you'll need to have installed Python, web.py, flup, psycopg2, and Postgres (or equivalent database and Python driver). For details, see the [webpy.org](http://webpy.org/).

If you have an existing web.py project, take a look at the [upgrade](http://webpy.infogami.com/upgrade_to_point2) page for info on migrating.

Let's get started.

## URL Handling

The most important part of any website is its URL structure. Your URLs aren't just the thing that your visitors see and email to their friends, they also provide a mental model of how your website works. On popular sites like [del.icio.us](http://del.icio.us/), the URLs are even part of the user interface. web.py makes it easy to make great URLs.

To get started with your web.py application, open up a new text file (let's call it `code.py`) and type:

    import web

This imports the web.py module.

Now we need to tell web.py our URL structure. Let's start out with something simple:

    urls = (
      '/', 'index'    )

The first part is a [regular expressions](http://osteele.com/tools/rework/) that matches a URL, like `/`, `/help/faq`, `/item/(\d+)`, etc. (The `\d+` matches a sequence of digits. The parentheses say to capture that piece of the match for later on.) The second part is the name of a class to send the request to, like `index`, `view`, `welcomes.hello` (which gets the `hello` class of the `welcomes` module), or `get_\1`. `\1` is replaced by the first capture of your regular expression; any remaining captures get passed to your function.

This line says we want the URL `/` (i.e. the front page) to be handled by the class named `index`.

Now we need to write the `index` class. While most people don't notice it just browsing around, your browser uses a language known as HTTP for communicating with the World Wide Web. The details aren't important, but the basic idea is that Web visitors ask web servers to perform certain functions (like `GET` or `POST`) on URLs (like `/` or `/foo?f=1`). 

`GET` is the one we're all familiar with, the one used to request the text of a web page. When you type `harvard.edu` into your web browser, it literally asks the Harvard web server to `GET /`.  The second-most famous, `POST`, is often used when submitting certain kids of forms, like a request to purchase something. You use `POST` whenever the act of submitting a request _does something_ (like charge your credit card and process an order). This is key, because `GET` URLs can be passed around and indexed by search engines, which you definitely want for most of your pages but definitely _don't_ want for things like processing orders (imagine if Google tried to buy everything on your site!).

In our web.py code, we make the distinction between the two clear:

    class index:
        def GET(self):
            print "Hello, world!"
This `GET` function will now get called by web.py anytime some makes a `GET` request for `/`.

Alright, now we just need to finish up with a final line telling web.py to start serving web pages:

    if __name__ == "__main__": web.run(urls, globals())

This tells web.py to serve the URLs we listed above, looking up the classes in the global namespace of this file.

Now notice that although I've been talking a lot here, we only really have five or so lines of code. That's all you need to make a complete web.py application. If you go to your command line and type:

    $ python code.py
    Launching server: http://0.0.0.0:8080/

You now have your web.py application running a real web server on your computer. Visit that URL and you should see "Hello, world!" (You can add an IP address/port after the "code.py" bit to control where web.py launches the server. You can also tell it to run a `fastcgi` or `scgi` server.)

## Developing

web.py also has a few tools to help us with debugging. Before the last line, add:

    web.webapi.internalerror = web.debugerror

This will give you more helpful error messages. And on the last line add `web.reloader` so that it reads:

    if __name__ == "__main__": web.run(urls, globals(), web.reloader)

    
This tells web.py to use the web.reloader "middleware" (middleware is a wrapper function to add some functionality to your web server) which reloads your files whenever you edit them, so that you can see the changes in your web browser right away. (For some serious changes, though, you'll still have to restart the server.) You'll probably want to take this out when you make your site public, but it's great while developing. There's also `web.profiler`, which outputs information about how much time each function took at the end of each web page, so that you can make your code faster.

## Templating

Writing HTML from inside Python can get cumbersome; it's much more fun to write Python from inside HTML. Luckily, web.py makes that pretty easy.

Let's make a new directory for our templates (we'll call it `templates`). Inside, make a new file whose name ends with HTML (we'll call it `index.html`). Now, inside, you can just write normal HTML:

    <em>Hello</em>, world!

Or you can use web.py's templating language to add code to your HTML:

    $def with (name)
    
    $if name:
        I just wanted to say <em>hello</em> to $name.
    $else:
        <em>Hello</em>, world!

**Note: Four spaces are currently required for indentation!**

As you can see, the templates look a lot like Python files except for the `def with` statement at the top (saying what the template gets called with) and the `$`s placed in front of any code.  Currently, template.py requires the $def statement to be the first line of the file.  Also, note that web.py automatically escapes any variables used here, so that if for some reason `name` is set to a value containing some HTML, it will get properly escaped and appear as plain text. If you want to turn this off, write `$:name` instead of `$name`.

Now go back to `code.py`. Under the first line, add:

    render = web.template.render('templates/')

This tells web.py to look for templates in your templates directory. Then change `index.GET` to:

    name = 'Bob'    print render.index(name)

Visit your site and it should say hello to Bob. 

**Development tip:** Add , `cache=False` to the end of your `render` call to have web.py reload your templates every time you visit the page.

Now change your URL line to:

    '/(.*)', 'index'
and change the definition of `index.GET` to:

    def GET(self, name):

and delete the line setting name. Visit `/` and it should say hello to the world. Visit `/Joe` and it should say hello to Joe.

## Databasing

Above your `web.run` line add:

    web.config.db_parameters = dict(dbn='postgres', user='username', pw='password', db='dbname')

(Adjust these -- especially `username`, `password`, and `dbname` -- for your setup. MySQL users will also want to change `dbn` to `mysql`.)

Create a simple table in your database:

    CREATE TABLE todo (
      id serial primary key,
      title text,
      created timestamp default now(),
      done boolean default 'f'    );

And an initial row:

    INSERT INTO todo (title) VALUES ('Learn web.py');

Back in `code.py`, change `index.GET` to:

    def GET(self):
        todos = web.select('todo')
        print render.index(todos)

and change back the URL handler to take just `/`.

Edit `index.html` so that it reads:

    $def with (todos)
    <ul>    $for todo in todos:
        <li id="t$todo.id">$todo.title</li>    </ul>
Visit your site again and you should see your one todo item: "Learn web.py". Congratulations! You've made a full application that reads from the database. Now let's let it write to the database as well.

At the end of `index.html`, add:

    <form method="post" action="add">    <p><input type="text" name="title" /> <input type="submit" value="Add" /></p>    </form>
And change your URLs list to read:

    '/', 'index',
    '/add', 'add'
(You've got to be very careful about those commas.  If you omit them, Python adds the strings together and sees `'/index/addadd'` instead of your list of URLs!)

Now add another class:

    class add:
        def POST(self):
            i = web.input()
            n = web.insert('todo', title=i.title)
    	    web.seeother('./#t'+str(n))

(Notice how we're using `POST` for this?)

`web.input` gives you access to any variables the user submitted through a form. `web.insert` inserts values into the database table `todo` and gives you back the ID of the new row. `seeother` redirects users to that ID.

Quickly: `web.transact()` starts a transaction. `web.commit()` commits it; `web.rollback()` rolls it back. `web.update` works just like `web.insert` except instead of returning the ID it takes it (or a string `WHERE` clause) after the table name.

`web.input`, `web.query`, and other functions in web.py return "Storage objects", which are just like dictionaries except you can do `d.foo` in addition to `d['foo']`. This really cleans up some code.

You can find the full details on these and all the web.py functions in [the documentation](http://webpy.org/documentation).

This ends the tutorial for now. Take a look at the documentation for lots more cool stuff you can do with web.py.