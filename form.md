---
layout: default
title: Form Library
---

# Form Library

Other languages : [français](/docs/0.3/form.fr) | ...

# Summary

* <a href="#introduction">Introduction</a>
* <a href="#inputfeatures">Input Features</a>
* <a href="#dropdown">Dropdown</a>
* <a href="#formfeatures">Form Features</a>
* <a href="#example">Example</a>

<a name="introduction"></a>
## Introduction


The form module of web.py allows the ability to generate html forms, get user input, and validate it before processing it or adding it to a database.

The form module defines 2 primary classes: the Form class, and the Input class.  Forms are instantiated with one or more inputs, and optional validators.  Inputs are instantiated with a name variable, and optional arguments and validators. The Input class is subclassed into the following html inputs (html type in parens):

* Textbox - free form single line input (input type="text")
* Password - free form single line that hides input (input type="password")
* Textarea - free form multi line input (textarea)
* Dropdown - mutually exclusive input for lists (select and options)
* Radio - mutually exclusive input for a few options (input type="radio")
* Checkbox - binary input (input type="checkbox")
* Button - submit the form (button)

A basic login form would look like this:

    login = form.Form(
        form.Textbox('username'),
        form.Password('password'),
        form.Button('Login'),
    )

This defines a basic form. Once defined, you should call it again to get an copied instance, and then you can call the render method on it, like so:

    f = login()
    print f.render()

This outputs the following HTML:

    <table>
        <tr><th><label for="username">username</label></th><td><input type="text" id="username" name="username"/><div class="post" style="display: none;"></div></td></tr>
        <tr><th><label for="password">password</label></th><td><input type="password" id="password" name="password"/><div class="post" style="display: none;"></div></td></tr>
        <tr><th><label for="Login"></label></th><td><button id="Login" name="Login">Login</button><div class="post" style="display: none;"></div></td></tr>
    </table>

Which looks like:

<table>
    <tr><th><label for="username">username</label></th><td><input type="text" id="username" name="username"/><div class="post" style="display: none;"></div></td></tr>
    <tr><th><label for="password">password</label></th><td><input type="password" id="password" name="password"/><div class="post" style="display: none;"></div></td></tr>
    <tr><th><label for="Login"></label></th><td><button id="Login" name="Login">Login</button><div class="post" style="display: none;"></div></td></tr>
</table>

<a name="inputfeatures"></a>
## Input Features
The form inputs support several additional attributes.  For example:

    form.textbox("firstname",
        form.notnull, #put validators first followed by optional attributes
        class_="textEntry", #gives a class name to the text box -- note the underscore
        pre="pre", #directly before the text box
        post="post", #directly after the text box
        description="please enter your name", #describes field, defaults to form name ("firstname")
        value="bob", #default value
        id="nameid", #specify the id
    )

In addition to the attributes above, any html attributes can be entered in the same manner.  For example:
    
    myform2 = form.Form(
        form.textbox('phonenumber',
            size="12",
            maxlength="12"        )
    )

<a name="dropdown"></a>
##Dropdown

Dropdown inputs allow a unique description and value for each item in the dropdown list.  To do this, create the dropdown list with tuples like this:
    
    form.Dropdown('mydrop', [('value1', 'description1'), ('value2', 'description2')])

<a name="formfeatures"></a>
## Form Features
In addition individual input validators, form.py supports entire form validation which allows comparisons of fields.  The validators get passed as a list as the variable 'validators'.  For example:

    signup = form.Form(
        form.Textbox('username'),
        form.Password('password'),
        form.Password('password_again'),
        validators = [form.Validator("Passwords didn't match.", lambda i: i.password == i.password_again)]
    )

Once the form data has been posted, it can easily be put into a database (if the database scheme has names consistent with your webpy form).  For example:

    def POST(self):
        f = myform()
        if f.validates():
            web.insert('data_table', **f.d)
        #don't do web.insert('data_table', **web.input()) because malicious data could be submitted too
        else:
            render.foo(f)

<a name="example"></a>
## Example

    import web
    from web import form

    render = web.template.render('templates/')

    urls = ('/', 'index')
    app = web.application(urls, globals())

    myform = form.Form( 
        form.Textbox("boe"), 
        form.Textbox("bax", 
            form.notnull,
            form.regexp('\d+', 'Must be a digit'),
            form.Validator('Must be more than 5', lambda x:int(x)>5)),
        form.Textarea('moe'),
        form.Checkbox('curly'), 
        form.Dropdown('french', ['mustard', 'fries', 'wine'])) 

    class index: 
        def GET(self): 
            form = myform()
            # make sure you create a copy of the form by calling it (line above)
            # Otherwise changes will appear globally
            return render.formtest(form)

        def POST(self): 
            form = myform() 
            if not form.validates(): 
                return render.formtest(form)
            else:
                # form.d.boe and form['boe'].value are equivalent ways of
                # extracting the validated arguments from the form.
                return "Grrreat success! boe: %s, bax: %s" % (form.d.boe, form['bax'].value)

    if __name__=="__main__":
        web.internalerror = web.debugerror
        app.run()

And sample formtest.html (place this in the *templates* subdirectory): 

    $def with (form)

    <form name="main" method="post"> 
    $if not form.valid: <p class="error">Try again, AmeriCAN:</p>
    $:form.render()
    <input type="submit" />    </form>