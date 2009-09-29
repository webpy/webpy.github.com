---
layout: default
title: web.py 0.3 向导
---

# web.py 0.3 向导

<p>

</p><h2>开始</h2>
<p>所以，你知道Python和想一个网站。 web.py提供了代码，以容易。
</p>
<p>If you want to do the whole tutorial, you'll need to have installed Python, web.py, flup, psycopg2, and Postgres (or equivalent database and Python driver). For details, see <a href="http://webpy.org/">webpy.org</a>.
</p>
<p>If you have an existing web.py project, take a look at the <a href="/docs/0.3/upgrade">upgrade</a> page for info on migrating.
</p>
<p>Let's get started.
</p>

<h2>URL Handling</h2>
<p>The most important part of any website is its URL structure. Your URLs aren't just the thing that your visitors see and email to their friends, they also provide a mental model of how your website works. On popular sites like <a href="http://del.icio.us/">del.icio.us</a>, the URLs are even part of the user interface. web.py makes it easy to make great URLs.
</p>
<p>To get started with your web.py application, open up a new text file (let's call it <code>code.py</code>) and type:
</p>
<pre><code>import web
</code></pre><p>This imports the web.py module.
</p>
<p>Now we need to tell web.py our URL structure. Let's start out with something simple:
</p>
<pre><code>urls = (
  '/', 'index'
)
</code></pre><p>The first part is a <a href="http://osteele.com/tools/rework/">regular expressions</a> that matches a URL, like <code>/</code>, <code>/help/faq</code>, <code>/item/(\d+)</code>, etc. (i.e. <code>\d+</code> would match a sequence of digits). The parentheses say to capture that piece of the matched data for use later on. The second part is the name of a class to send the request to, like <code>index</code>, <code>view</code>, <code>welcomes.hello</code> (which gets the <code>hello</code> class of the <code>welcomes</code> module), or <code>get_\1</code>. <code>\1</code> is replaced by the first capture of your regular expression; any remaining captures get passed to your function.
</p>
<p>This line says we want the URL <code>/</code> (i.e. the front page) to be handled by the class named <code>index</code>.
</p>
<p>Now we need to create an application specifying the urls.
</p>
<pre><code>app = web.application(urls, globals())
</code></pre><p>This tells web.py to create an application with the URLs we listed above, looking up the classes in the global namespace of this file.
</p>
<p>Now we need to write the <code>index</code> class. While most people don't notice it just browsing around, your browser uses a language known as HTTP for communicating with the World Wide Web. The details aren't important, but the basic idea is that Web visitors ask web servers to perform certain functions (like <code>GET</code> or <code>POST</code>) on URLs (like <code>/</code> or <code>/foo?f=1</code>). 
</p>
<p><code>GET</code> is the one we're all familiar with, the one used to request the text of a web page. When you type <code>harvard.edu</code> into your web browser, it literally asks the Harvard web server to <code>GET /</code>.  The second-most famous, <code>POST</code>, is often used when submitting certain kinds of forms, like a request to purchase something. You use <code>POST</code> whenever the act of submitting a request <em>does something</em> (like charge your credit card and process an order). This is key, because <code>GET</code> URLs can be passed around and indexed by search engines, which you definitely want for most of your pages but definitely <em>don't</em> want for things like processing orders (imagine if Google tried to buy everything on your site!).
</p>
<p>In our web.py code, we make the distinction between the two clear:
</p>
<pre><code>class index:
    def GET(self):
        return "Hello, world!"
</code></pre><p>This <code>GET</code> function will now get called by web.py anytime some makes a <code>GET</code> request for <code>/</code>.
</p>
<p>Alright, now we just need to finish up with a final line telling web.py to start serving web pages:
</p>
<pre><code>if __name__ == "__main__": app.run()
</code></pre><p>This tells web.py to serve the application we created above.
</p>
<p>Now notice that although I've been talking a lot here, we only really have five or so lines of code. That's all you need to make a complete web.py application. If you go to your command line and type:
</p>
<pre><code>$ python code.py
http://0.0.0.0:8080/
</code></pre><p>You now have your web.py application running a real web server on your computer. Visit that URL and you should see "Hello, world!" (You can add an IP address/port after the "code.py" bit to control where web.py launches the server. You can also tell it to run a <code>fastcgi</code> or <code>scgi</code> server.)
</p>
<p><strong>Note:</strong> You can specify the port number to use on the command line like this
   if you can't or don't want to use the default:
</p>
<pre><code>$ python code.py 1234
</code></pre>
<h2>Templating</h2>
<p>Writing HTML from inside Python can get cumbersome; it's much more fun to write Python from inside HTML. Luckily, web.py makes that pretty easy.
</p>
<p><strong>Note:</strong> Old versions of web.py used <a href="http://www.cheetahtemplate.org/">Cheetah templates</a>. You are, of course, welcome to use that or any other software with web.py, but it is no longer officially supported.
</p>
<p>Let's make a new directory for our templates (we'll call it <code>templates</code>). Inside, make a new file whose name ends with HTML (we'll call it <code>index.html</code>). Now, inside, you can just write normal HTML:
</p>
<pre><code>&lt;em&gt;Hello&lt;/em&gt;, world!
</code></pre><p>Or you can use web.py's templating language to add code to your HTML:
</p>
<pre><code>$def with (name)

$if name:
    I just wanted to say &lt;em&gt;hello&lt;/em&gt; to $name.
$else:
    &lt;em&gt;Hello&lt;/em&gt;, world!
</code></pre><p>As you can see, the templates look a lot like Python files except for the <code>def with</code> statement at the top (saying what the template gets called with) and the <code>$</code>s placed in front of any code.  Currently, template.py requires the <code>$def</code> statement to be the first line of the file.  Also, note that web.py automatically escapes any variables used here, so that if for some reason <code>name</code> is set to a value containing some HTML, it will get properly escaped and appear as plain text. If you want to turn this off, write <code>$:name</code> instead of <code>$name</code>.
</p>
<p>Now go back to <code>code.py</code>. Under the first line, add:
</p>
<pre><code>render = web.template.render('templates/')
</code></pre><p>This tells web.py to look for templates in your templates directory. Then change <code>index.GET</code> to:
</p>
<pre><code>name = 'Bob'    
return render.index(name)
</code></pre><p>('index' is the name of the template and 'name' is the argument passed to it)
</p>
<p>Visit your site and it should say hello to Bob. 
</p>
<p>But let's say we want to let people enter their own name in. Replace the two lines we added above with:
</p>
<pre><code>i = web.input(name=None)
return render.index(i.name)
</code></pre><p>Visit <code>/</code> and it should say hello to the world. Visit <code>/?name=Joe</code> and it should say hello to Joe.
</p>
<p>Of course, having that <code>?</code> in the URL is kind of ugly. Instead, change your URL line at the top to:
</p>
<pre><code>'/(.*)', 'index'
</code></pre><p>and change the definition of <code>index.GET</code> to:
</p>
<pre><code>def GET(self, name):
    return render.index(name)
</code></pre><p>and delete the line setting name. Now visit <code>/Joe</code> and it should say hello to Joe.
</p>
<p>If you wish to learn more about web.py templates, vist the <a href="/docs/0.3/templetor" class="internal">templetor page</a>.
</p>

<h2>Databasing</h2>
<p><strong>Note:</strong> Before you can start using a database, make sure you have the appropriate database library installed.  For MySQL databases, use <a href="http://sourceforge.net/project/showfiles.php?group_id=22307">MySQLdb</a> and for Postgres use <a href="http://initd.org/pub/software/psycopg/">psycopg2</a>.
</p>
<p>First you need to create a database object.
</p>
<pre><code>db = web.database(dbn='postgres', user='username', pw='password', db='dbname')
</code></pre><p>(Adjust these -- especially <code>username</code>, <code>password</code>, and <code>dbname</code> -- for your setup. MySQL users will also want to change <code>dbn</code> definition to <code>mysql</code>.)
</p>
<p>That's all you need to do -- web.py will automatically handle connecting and disconnecting from the database.
</p>
<p>Using your database engine's admin interface, create a simple table in your database:
</p>
<pre><code>CREATE TABLE todo (
  id serial primary key,
  title text,
  created timestamp default now(),
  done boolean default 'f'    );
</code></pre><p>And an initial row:
</p>
<pre><code>INSERT INTO todo (title) VALUES ('Learn web.py');
</code></pre><p>Return to editing <code>code.py</code> and change <code>index.GET</code> to the following, replacing the entire function:
</p>
<pre><code>def GET(self):
    todos = db.select('todo')
    return render.index(todos)
</code></pre><p>and change back the URL handler to take just <code>/</code> as in:
</p>
<pre><code>'/', 'index',
</code></pre><p>Edit and replace the entire contents of <code>index.html</code> so that it reads:
</p>
<pre><code>$def with (todos)
&lt;ul&gt;
$for todo in todos:
    &lt;li id="t$todo.id"&gt;$todo.title&lt;/li&gt;
&lt;/ul&gt;
</code></pre><p>Visit your site again and you should see your one todo item: "Learn web.py". Congratulations! You've made a full application that reads from the database. Now let's let it write to the database as well.
</p>
<p>At the end of <code>index.html</code>, add:
</p>
<pre><code>&lt;form method="post" action="add"&gt;
&lt;p&gt;&lt;input type="text" name="title" /&gt; &lt;input type="submit" value="Add" /&gt;&lt;/p&gt;
&lt;/form&gt;
</code></pre><p>And change your URLs list to read:
</p>
<pre><code>'/', 'index',
'/add', 'add'
</code></pre><p>(You've got to be very careful about those commas.  If you omit them, Python adds the strings together and sees <code>'/index/addadd'</code> instead of your list of URLs!)
</p>
<p>Now add another class:
</p>
<pre><code>class add:
    def POST(self):
        i = web.input()
        n = db.insert('todo', title=i.title)
        raise web.seeother('/')
</code></pre><p>(Notice how we're using <code>POST</code> for this?)
</p>
<p><code>web.input</code> gives you access to any variables the user submitted through a form. 
</p>
<p>Note: In order to access data from multiple identically-named items, in a list format (e.g.: a series of check-boxes all with the attribute name="name") use:
</p>
<pre><code>post_data=web.input(name=[])
</code></pre><p><code>db.insert</code> inserts values into the database table <code>todo</code> and gives you back the ID of the new row. <code>seeother</code> redirects users to that URL.
</p>
<p>Some quick additional notes: <code>db.update</code> works just like <code>db.insert</code> except instead of returning the ID it takes it (or a string <code>WHERE</code> clause) after the table name.
</p>
<p><code>web.input</code>, <code>db.query</code>, and other functions in web.py return "Storage objects", which are just like dictionaries except you can do <code>d.foo</code> in addition to <code>d['foo']</code>. This really cleans up some code.
</p>
<p>You can find the full details on these and all the web.py functions in <a href="/docs/0.3">the documentation</a>.
</p>

<h2>Developing</h2>
<p>web.py also has a few tools to help us with debugging. When running with the built-in webserver, it starts the application in debug mode. In debug mode any changes to code and templates are automatically reloaded and error messages will have more helpful information.
</p>
<p>The debug is not enabled when the application is run in a real webserver. If you want to disable the debug mode, you can do so by adding the following line before creating your application/templates.
</p>
<pre><code>web.config.debug = False
</code></pre><p>This ends the tutorial for now. Take a look at the documentation for lots more cool stuff you can do with web.py.
</p>





<div id="dateline">
    <a href="/tutorial3.en?m=edit" accesskey="e">Edit</a>
    <a href="/tutorial3.en?m=history" accesskey="h">History</a>
    Last Modified september 23
</div>