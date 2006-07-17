---
layout: default
title: form
---

# form

#fpp

Here's a sample script using the new form library:

    import web, form, template
    render = template.render('templates/')

    myform = form.Form( 
        form.Textbox("boe"), 
        form.Textbox("bax", 
            form.notnull, 
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
                print "when libraries compete, you win!"
And sample formtest.html: 

    $def with (form)

    <form name="main" method="post"> 
    $if not form.valid: <p class="error">Try again, cowpoke:</p>
    $:form.render()
    <input type="submit" value="Save" />    </form>