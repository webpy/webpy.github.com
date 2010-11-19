---
layout: default
title: web.py 0.3 tutorial
---

# web.py 0.3 tutorial

This is a work-in-progress


## TODO: app.internalerror = web.debugerror

## TODO: '$user' vs. '$:user' and '$var user:$user' vs. '$var user:$user\'

## TODO: Multiple submit buttons

## TODO: Show/hide complete code at the end of sections

TODO: move the next paragraph over to install?

To create a website with web.py you need to know the Python programming language and have it installed. Installation instructions for Python can be found at [http://python.org/](http://python.org/) .If you don't know if Python is installed on your system, open a terminal and type `python`. A great starting point to learn Python is the official [tutorial] (http://docs.python.org/tut/tut.html). If you are new to programming in general, [Think Python] (http://www.greenteapress.com/thinkpython/) is a wonderful book to understand key concepts in programming. 

## TOC

TODO: ...


## Prerequisites

This tutorial assumes that both Python and web.py are installed on your system. If this is not the case, please follow the [installation instructions] (http://webpy.org/install) before you continue.

Furthermore, basic HTML knowledge is needed to understand some examples.


## Hello Web in web.py

Open your favorite text editor and create a new file `hello.py`. In this file you will define the content and logic of your web application as well as its web addresses (URLs).

Before you are able to use the tools web.py provides, you need to import the web.py module with the following code:

    import web

In web.py web pages are mapped to Python classes. Let's create the code for the first page which is here called `hello`:

    class hello:
        def GET(self):
            return "Hello, Web!"

The `hello` class has a function named `GET` which returns "Hello, Web!". Why `GET`?

When you open a web page, your browser asks for the content of that page. This request is called the `GET` method. web.py uses the same terminology. The string your `GET` method returns is displayed in your browser.

Although the code for your first page is written, it cannot yet be opened in a browser. Let's proceed with mapping a web address (URL) to your class. Insert the following code after the import statement:

    urls = (
      '/', 'hello')

This tells web.py to map the root of your website (like http://webpy.org/) to your Python class named `hello`.

Next create an instance of a web.py application. This instance will be the mediator between your classes and the web. It will handle browser requests and serve your pages. (In short: It will do everything that you really don't want to care about.) Use the following code:

    app = web.application(urls, globals())

Note that `web.application()` gets called with two arguments. Your URL mapping (`urls`) and your global namespace which contains your `hello` class (`globals()`).

To finish your web.py application insert the following code at the end of your code:

    if __name__ == "__main__":
        app.run()

`app.run()` starts the web application to serve requested pages.

### Complete code

hello.py

    import web
    
    urls = (
      '/', 'hello')

    app = web.application(urls, globals())
    
    class hello:
        def GET(self):
            return 'Hello, web!'
    
    if __name__ == "__main__":
        app.run()

Save the file and run the following command to start your application:

    python hello.py

The first output of your application is the address of your web site. By default this is:

    http://locahost:8080/

Open this address with your web browser. That's it. Congrats! You can stop your application at any time by pressing `ctrl+c` in the terminal.

Note: You can also visit your site at `http://localhost:8080/`


## Having multiple pages

In this part you will learn how to manage multiple pages. Let's add another class to your 'Hello Web' application:

    class bye:
        def GET(self):
            return 'Bye, web!'

As mentioned above, each page needs a unique address. Modify your list of URLs as follows:

    urls = (
      '/', 'hello',
      '/bye', 'bye')

This will make your class `bye` respond to requests at `/bye/`. Now start your application and open `http://localhost:8080/bye/` in your browser.

Note: Currently you need to restart your application to see any changes. Try to pass a third argument to `web.application` and restart your application:

    app = web.application(urls, globals(), True)


Future changes can now be seen instantly, although you might need to reload a page in your browser.

### Complete code

hello.py

    import web
    
    urls = (
      '/', 'hello',
      '/bye', 'bye')
    
    app = web.application(urls, globals(), True)
    
    class hello:
        def GET(self):
            return 'Hello, web!'
    
    class bye:
        def GET(self):
            return 'Bye, web!'
    
    if __name__ == "__main__":
        app.run()


## Dynamic pages

The examples shown above are simple; all it does it display the same message, every time.  Suppose you want your app to greet people by name?

### A dynamic "Hello, world!" -- using GET and POST variables

Change the "hello" class above so it looks like this:

    class hello:
        def GET(self):
            i = web.input(name = 'web')
            return 'Hello, ' + web.websafe(i.name) + '!'
        
Run the script, and then go to http://localhost:8080/?name=Luke .  You should see "Hello, Luke!."

Here is what is happening:

When you add the "?name=Luke" to the end of your web request, you are passing the variable "name" to the web server, with a value of "Luke."

The line `i = web.input(name = "web")` creates a Storage object (a fancy type of Python dictionary) that contains all variables passed into it.  You can also do this by just calling `i = web.input()`.  Here, by putting `name = 'web'` into the call, we tell it to use the string "web" as a default, in case the user didn't pass in a "name" variable at all.

We read the "name" value from i by just saying `i.name`.  It's also possible to do `i['name']`; use the syntax you prefer.

Finally, we pass i.name through the `web.websafe` function before returning it to the user.  If your page is being served as HTML, rather than text, then this is an important security step to protect against [cross-site scripting attacks](http://en.wikipedia.org/wiki/Cross-site_scripting).  (As we will see, web.py's form templates offer built-in protection to those attacks).

### Another dynamic "Hello, world!" -- parsing URL strings

Making the user type in something like "http://localhost:8080/?name=Luke" is so 1996; wouldn't it be nicer if we could just get the user to enter "http://localhost:8080/Luke"?

Try this code:

    import web
    
    urls = (
      '/(.*)', 'hello')
    
    app = web.application(urls, globals())
    
    class hello:
        def GET(self, name):
            return 'Hello, ' + web.websafe(name) + '!'
    
    if __name__ == "__main__":
        app.run()

Notice that two things have changed:

 1. The urls has a "(.*)" thing in it
 2. The `GET` method now takes two parameters
 3. There's no more `web.input` call.

As you can see, web.py is parsing the URL for you, based on a [regular expression](http://docs.python.org/lib/re-syntax.html) that you provide in the `urls` tuple.

## HTML in Python

Until now your classes returned only simple strings. Let's add some HTML. This can be done directly from inside your `hello.py`. Replace your class `hello` with this code:

    class hello:
        def GET(self):
            return """<html>
    <head>
    <title>Hello, web!</title>
    </head>
    <body>
    <h1>web.py</h1>
    <p>Think about the <em>ideal</em> way to write a web app. Write the code to <b>make it happen</b>.</p>
    </body>
    </html>"""

Note that your page now has a custom title and HTML formatted content.

### Complete code

hello.py

    import web
    
    urls = (
      '/', 'hello',
      '/bye', 'bye')
    
    app = web.application(urls, globals(), True)
    
    class hello:
        def GET(self):
            return """<html>
    <head>
    <title>Hello, web!</title>
    </head>
    <body>
    <h1>web.py</h1>
    <p>Think about the <em>ideal</em> way to write a web app. Write the code to <b>make it happen</b>.</p>
    </body>
    </html>"""
    
    if __name__ == "__main__":
        app.run()



## HTML with site layout templates

Imagine a larger site with many pages. If all HTML for these pages is embedded into your Python code, things get messy and your code unmaintainable. Also reusing parts of your HTML code for other pages would be difficult. Therefore web.py lets you define site layout templates that can be shared between your pages.

First create a directory `templates` next to your `hello.py` file. Create a file `hello.html` and save it in `templates`. This file will contain the HTML markup that is used to render your page. Start with the following basic template:

    $def with (title, name, content)
    <html>
    <head>
    <title>$title</title>
    </head>
    <body>
    <p>You are visiting page <b>$name</b>.</p>
    <p>$content</p>
    </body>
    </html>

Create a second template `bye.html`:

    $def with (title, name, *numbers)
    <html>
    <head>
    <title>$title</title>
    </head>
    <body>
    <p>You are visiting page <b>$name</b>.</p>
    <p>Find the answer to all questions below:
    $for number in numbers:
        <p>$number</p>
    </body>
    </html>

Besides defining a page structure, these templates will use variables. The first line of `hello.html` (`def with (title, name, number)`) will tell web.py that this template needs to be called with three arguments. Wherever `$title` is used in the template the actual value of `title` is inserted.

Arguments of `bye.html` are `title`, `name` and an arbitrary number of numbers (`*numbers`). All arguments beside `title` and `name` are put into the list `numbers`. This list is then iterated (`$for number in numbers:`) and each number (`number`) is written in its own paragraph. You see that `$` is not only used to access template variables but also to evaluate (safe) Python code like `for` loops or `if` statements.

Now insert the following line before your class definitions to create a so called template renderer. The location of your templates is passed to the renderer as an argument:

    render = web.template.render('templates/')

Next modify your classes to render your pages using the two different templates:

    class hello:
        def GET(self):
            return render.hello("Templates demo", "Hello", "A long time ago...")
    
    class bye:
        def GET(self):
            return render.bye("Templates demo", "Bye", "14", "8", "25", "42", "19")
    
Open the pages in your browser. web.py fetches your templates and dynamically inserts the values that you passed to your templates.

### Complete code

hello.py

    import web
    
    urls = (
      '/', 'hello',
      '/bye/', 'bye')
    
    app = web.application(urls, globals(), True)
    
    render = web.template.render('templates/')
    
    class hello:
        def GET(self):
            return render.hello("Templates demo", "Hello", "A long time ago...")
    
    class bye:
        def GET(self):
            return render.bye("Templates demo", "Bye", "14", "8", "25", "42", "19")
            
    if __name__ == "__main__":
        app.run()
        
templates/hello.html

    $def with (title, name, content)
    <html>
    <head>
    <title>$title</title>
    </head>
    <body>
    <p>You are visiting page <b>$name</b>.</p>
    <p>$content</p>
    </body>
    </html>

templates/bye.html

    $def with (title, name, *numbers)
    <html>
    <head>
    <title>$title</title>
    </head>
    <body>
    <p>You are visiting page <b>$name</b>.</p>
    <p>Find the answer to all questions below:
    $for number in numbers:
        <p>$number</p>
    </body>
    </html>


## Using a base layout (template inheritance)

The previous example defined two templates but both had duplicate code. In most cases your pages share a lot of common code like a navigation bar or a footer. Let's create a file `base.html` which contains all the code your pages share with each other:

    $def with (page)
    <html>
    <head>
    <title>$page.title</title>
    </head>
    <body>
    <p>You are visiting page <b>$page.name</b>.</p>
    $:page
    </body>
    </html>

This base template receives only one variable `page`. `$page.title` is a placeholder for a variable named `title` defined in a child template. `$:page` is a placeholder for everything else that you put in your child template. Modify `hello.html` to be a child template:

    $def with (title, name, content)
    $var title:$title
    $var name:$name
    <p>$content</p>

The previously duplicated code for the HTML body, the page title and the current page information is gone. Instead `$var title:$title` tells the base template to use the local `title` as `$page.title`. The remaining line `<p>$content</p>` will be available in the base template as `$:page`.

Modify `bye.html` accordingly:

    $def with (title, name, *numbers)
    $var title:$title
    $var name:$name
    <p>Find the answer to all questions below:</p>
    $for number in numbers:
        <p>$number</p>

The last step is to tell web.py to use `base.html` as the base template. Use the following code (you might need to replace your previous code):

    render = web.template.render('templates/', base='base')

Both `hello.html` and `bye.html` will now use `base.html`.

### Complete code

hello.py

    import web
    
    urls = (
      '/', 'hello',
      '/bye/', 'bye')
    
    app = web.application(urls, globals(), autoreload=True)
    
    render = web.template.render('templates/', base='base')
    
    class hello:
        def GET(self):
            return render.hello("Templates demo", "Hello", "A long time ago...")
    
    class bye:
        def GET(self):
            return render.bye("Templates demo", "Bye", "14", "8", "25", "42", "19")
    
    if __name__ == "__main__":
        app.run()

base.html

    $def with (page)
    <html>
    <head>
    <title>$page.title</title>
    </head>
    <body>
    <p>You are visiting page <b>$page.name</b>.</p>
    $:page
    </body>
    </html>

hello.html

    $def with (title, name, content)
    $var title:$title
    $var name:$name
    <p>$content</p>

bye.html

    $def with (title, name, *numbers)
    $var title:$title
    $var name:$name
    <p>Find the answer to all questions below:</p>
    $for number in numbers:
        <p>$number</p>


## Static content

Now that your application serves HTML formatted content, you probably want to include static files like images or css style files. To achieve this create a directeory called `static` next to your `hello.py` file. Put a picture file (here called `logo.png`) in your `static` directory. Then include the file on your page:

    class hello:
        def GET(self):
            return """<img src="./static/logo.png">"""

### Complete code

hello.py

    import web
    
    urls = (
      '/', 'hello')
    
    app = web.application(urls, globals(), web.reloader)
    
    class hello:
        def GET(self):
            return """<img src="./static/logo.png">"""
    
    if __name__ == "__main__":
        app.run()


## User input (HTML forms and the `POST` method) [cookbook] (http://webpy.org/form)

Until now `GET` functions were introduced to serve pages but there was no way a user could send data back to your application. A function called `POST` will allow this. To use `POST` you need to create form fields on your page where a user can input his data. Let's make `hello.py` return a page that contains HTML forms using web.py `form` module. To reduce typing add the following import statement:

    from web import form

Now define a form before your classes in `hello.py`. This example only uses a single input field. Visit the [cookbook] (http://webpy.org/form) for more advanced types. The following code gives you a text box with validation of the input:

    number_form = form.Form( 
        form.Textbox('number',
                     form.notnull,
                     form.regexp('^-?\d+$', 'Not a number.'),
                     form.Validator('Not greater than 10.', lambda x: int(x)>10),
                     description='Enter a number greater than 10:'
                     ))

`form.Textbox()` creates an HTML text box. The first parameter specifies its name: `'number'`.  Most often you will want to validate the input of a user instantly and allow him to correct errors. `form.notnull` makes it a required field that cannot be left empty. `form.regexp()` matches the input with the given regular expression. Here it is checked if the input is a number. `form.Validator()` additionally checks if the input is a number greater ten. And finally, `description` is the text that is printed in front of the text box.

Now make your template `hello.html` accept and display a form:

    $def with (form)
    <form name="test" method="POST"> 
    $if not form.valid: <p>Sorry, your input was invalid.</p>
    $:form.render()
    <input type="submit" value="Check" />
    </form>

Notice that the template will print an error message if the form input is invalid.

And finally your `hello` class needs the following `GET` and `POST` methods:

    class hello:
        def GET(self):
            my_form = number_form()
            return render.hello(my_form)
    
        def POST(self): 
            my_form = number_form() 
            if not my_form.validates(): 
                return render.hello(my_form)
            else:
                number = my_form['number'].value
                if int(number) % 2:
                    return "Your number %s is odd." % number
                else:
                    return "Your number %s is even." % number

When you visit `hello` in your browser, the `GET` method creates an instance of your form and returns the rendered page. Enter a number greater 10 and press the `Check` button. Now the `POST` method is invoked to process your input. Because the `GET` and `POST` methods cannot access the same form instance a new one is created. `form.validates()` checks the input you entered. But how does it know what you have entered? By default the `validates()` method fetches your input from `web.input()` where it is stored as soon as you press the `Check` button. In case your input is invalid, the form is returned again. Else `my_form['number'].value` is retrieved which is the number you entered and your application will tell you if you entered an even or odd number.

Note: You cannot access form values before having validated the form!

Now go back and try some invalid input. First leave the text field blank and press `Check`. You will be informed that you left a required field blank. Enter some text and you will get a "Not a number" message. This is due to the regular expression check. And finally try some number that is not greater than ten. The form input will not be validated and you are advised to enter a number greater ten.

### Complete code

hello.py 

    import web
    from web import form
    
    urls = (
      '/', 'hello')
    
    app = web.application(urls, globals(), web.reloader)
    render = web.template.render('templates/')
    
    number_form = form.Form( 
        form.Textbox('number',
                     form.notnull,
                     form.regexp('^-?\d+$', 'Not a number.'),
                     form.Validator('Not greater 10.', lambda x: int(x)>10),
                     description='Enter a number greater 10:'
                     ))
    
    class hello:
        def GET(self):
            my_form = number_form()
            return render.hello(my_form)
    
        def POST(self): 
            my_form = number_form() 
            if not my_form.validates(): 
                return render.hello(my_form)
            else:
                number = my_form['number'].value
                if int(number) % 2:
                    return "Your number %s is odd." % number
                else:
                    return "Your number %s is even." % number
    
    if __name__ == "__main__":
        app.run()

hello.html

    $def with (form)
    <form name="test" method="POST"> 
    $if not form.valid: <p>Sorry, your input was invalid.</p>
    $:form.render()
    <input type="submit" value="Check" />
    </form>


## Sessions [cookbook] (http://webpy.org/cookbook/sessions)

ATTENTION: Sessions cannot be used with `web.reloader` at the time of this writing! It is a known bug.

Many sites need to distinguish its visitors. Imagine you want to show the user the number of pages he visited on your page. Each visitor has a unique number. To allow separate tracking web.py uses so called sessions. Each visitor gets his very own session object in which his unique number is saved. First create a session object in `hello.py`. Put this line after your `app` is initialized:

    session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'count': 0})

This creates a session object. The first parameter is simply the application the session object is used for. `web.session.DiskStore('sessions')` tells web.py to store sessions on disk (database storage is possible as well, see this [cookbook] (http://webpy.org/cookbook/sessions) entry). The third optional parameter initializes the session data dictionary for each user. Here each session object starts with zero visited pages (`count`). web.py creates a directory `sessions` to store session data on disk. Modify your classes in `hello.py` like this:

    class hello:
        def GET(self):
            session.count += 1
            return "You visited " + str(session.count) + " pages."
    
    class bye:
        def GET(self):
            session.kill()
            return ("Bye, web!")
            
Each time you visit `hello`, the number of pages you visited is incremented (`session.count += 1`). If you visit `bye` the session is killed (`session.kill()`). The next time you visit `hello`, a new session will be created and the counter will be zero again.

### Complete code

hello.py

    import web
    web.config.debug=False
    
    urls = (
      '/', 'hello',
      '/bye/', 'bye')

        
    app = web.application(urls, globals())
    session = web.session.Session(app, web.session.DiskStore('sessions'),
                                  initializer={'count': 0})
    
    class hello:
        def GET(self):
            session.count += 1
            return "You visited " + str(session.count) + " pages."
    
    class bye:
        def GET(self):
            session.kill()
            return ("Bye, web!")
    
    if __name__ == "__main__":
        app.run()


## User authentication

This is an example of user authentication using a session cookie, the most common method.  Most often user authentication is done by providing functions to login and logout a user. Additionally, users often are able to register or delete their account.

### Complete code

hello.py

    import web
    from web import form
    
    import random
    from hashlib import sha1
    
    # A simple user object that doesn't store passwords in plain text
    # see http://en.wikipedia.org/wiki/Salt_(cryptography)
    class PasswordHash(object):
        def __init__(self, password_):
            self.salt = "".join(chr(random.randint(33,127)) for x in xrange(64))
            self.saltedpw = sha1(password_ + self.salt).hexdigest()
        def check_password(self, password_):
            """checks if the password is correct"""
            return self.saltedpw == sha1(password_ + self.salt).hexdigest()
    
    # Note: a secure application would never store passwords in plaintext in the source code
    users = {
        'Kermit' : PasswordHash('frog'), 
        'ET' : PasswordHash('eetee'),  
        'falken' : PasswordHash('joshua') } 
    
    
    urls = ('/', 'hello',
            '/logout/', 'logout',
            '/register/', 'register')
    
    app = web.application(urls, globals())
    render = web.template.render('templates/')

    if web.config.get('_session') is None:
        session = web.session.Session(app, web.session.DiskStore('sessions'),
                                  initializer={'user': 'anonymous'})
        web.config._session = session
    else:
        session = web.config._session
    
    signin_form = form.Form(form.Textbox('username',
                                         form.Validator('Unknown username.',
                                                        lambda x: x in users.keys()),
                                         description='Username:'),
                            form.Password('password',
                                          description='Password:'),
                            validators = [form.Validator("Username and password didn't match.",
                                          lambda x: users[x.username].check_password(x.password)) ])
    
    signup_form = form.Form(form.Textbox('username',
                                         form.Validator('Username already exists.',
                                                        lambda x: x not in users.keys()),
                                         description='Username:'),
                            form.Password('password',
                                          description='Password:'),
                            form.Password('password_again',
                                          description='Repeat your password:'),
                            validators = [form.Validator("Passwords didn't match.",
                                          lambda i: i.password == i.password_again)])
    
    
    class hello:
        def GET(self):
            my_signin = signin_form()
            return render.hello(session.user, my_signin)
    
        def POST(self): 
            my_signin = signin_form() 
            if not my_signin.validates(): 
                return render.hello(session.user, my_signin)
            else:
                session.user = my_signin['username'].value
                return render.hello(session.user, my_signin)
    
    
    class logout:
        def GET(self):
            session.kill()
            raise web.seeother('/')
    
    
    class register:
        def GET(self):
            my_signup = signup_form()
            return render.signup(my_signup)
    
        def POST(self):
            my_signup = signup_form()
            if not my_signup.validates(): 
                return render.signup(my_signup)
            else:
                username = my_signup['username'].value
                password = my_signup['password'].value
                users[username] = PasswordHash(password)
                raise web.seeother('/')
    
    if __name__ == "__main__":
        app.run()
        
hello.html

    $def with (user, form)
    $if user == 'anonymous':
        <p>You are not logged in.</p>
        <p>
          <form name="test" method="POST"> 
          $:form.render()
          <input type="submit" name="button" value="Login" />
          </form>
        </p>
        <p><a href="./register/">Register</a></p>
    $else:
        <p>You are logged in as: $user</p>
        <p><a href="./logout/">Logout</a></p>

signup.html

    $def with (form)
    <form name="test" method="POST"> 
    $:form.render()
    <input type="submit" value="Register" />
    </form>

## Deployment

Advantages / disadvantages of different solutions: App Engine, servers...



TODO: ...