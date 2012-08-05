---
layout: default
title: template tricks
---

# template tricks

### Testing template rendering

Test the rendering of a template.py template

        def renderTemplate(templatename,*args,**kw):
            '''quick way to test a template.py template'''            
            import template
            if not "." in templatename:
                templatename = templatename + ".tmpl"            
                obj = template.Template(open(templatename).read())
            return obj(*args,**kw)

        print renderTemplate("homepage", now=time.ctime())

If your template takes a dict or a storage, then you can just
set global values and let those get passed in:

        username = "User"        
        lastvisit = "yesterday"        
        print renderTemplate("results", store=web.Storage(globals()))

---

### Using the Prototype Javascript library

If you are using a Javascript library, such as Prototype, that binds $
so that it can provide shorthand Javascript functions like $, $A, $F and $H,
then you'll need to do a few things to make it work:

1. Provide additional keyword args, as shown below, in your template
function declaration, so that when template.py can pass-through
the Prototype dollar-sign syntax. 

        $def with (arg1, arg2, ELT="$", F="$F", H="$H", A="$A")

    Note that since $ is special, we are providing
`$ELT` as a replacement Javascript function name.

1. Leave a space after your usage of `$ELT` et al. so that template.py
will not try to funcall it when it sees the parentheses.   

        var cmd = $F ('command');
	`$ELT ('result').value = originalRequest.responseText;`

    Javascript is fine with the space between the function name and arguments, and if
you forget the space, you'll get this error from template.py:

        'str' object is not callable

1. Alternatively if you're only using the $ functions a few times, you can just add a $; before the $ and the templator will render it correctly:

        myElement = $$('elementID');

---
