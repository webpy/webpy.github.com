---
layout: default
title: form
---

# form

Here's a sample script using the new form library:

    import web
    from web import form

    render = web.template.render('templates/')

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
            print render.formtest(form)

        def POST(self): 
            form = myform() 
            if not form.validates(): 
                print render.formtest(form)
            else:
                # form.d.boe and form['boe'].value are equivalent ways of
                # extracting the validated arguments from the form.
                print "Grrreat success! boe: %s, bax: %s" % (form.d.boe, form['bax'].value)

And sample formtest.html: 

    $def with (form)

    <form name="main" method="post"> 
    $if not form.valid: <p class="error">Try again, AmeriCAN:</p>
    $:form.render()
    <input type="submit" />    </form>
The forms support several additional attributes.  For example:

    myform = form.Form(
        form.textbox("firstname",
            class_="textEntry", #gives a class name to the text box -- note the underscore
            pre="pre", #directly before the text box
            post="post", #directly after the text box
            description="please enter your name", #describes field, defaults to form name ("firstname")
            value="bob", #default value
            id="nameid", #specify the id
        )
            
