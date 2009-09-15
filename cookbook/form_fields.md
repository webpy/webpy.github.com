---
layout: default
title: Render individual form fields
---

# Render individual form fields

### Problem

You want to render individual form fields in templates

### Solution

You can use the `render()` method for individual fields to render the fields in your template.

Let's assume you want to create a name/surname form. Very simple, with only two fields, and no validation, just for testing purposes.

    from web import form
    simple_form = form.Form(
        form.Textbox('name', description='Name'),
        form.Textbox('surname', description='Surname'),
    )

Usually you would either use `simple_form.render()` or `simple_form.render_css()`. But what if you want to render individual form fields one by one, so you can have more control over how it appears in your template? For that, you can use the `render()` method on individual fields.

We have defined two fields with names `name` and `surname`. Those names automatically become attributes of `simple_form` object.

    >>> simple_form.name.render()
    '<input type="text" name="name" id="name" />'
    >>> simple_form.surname.render()
    '<input type="text" name="surname" id="surname" />' 

You can also render individual descriptions in a similar way:

    >>> simple_form.surname.description
    'Surname'

What if you have a small template snippet (partial template) that you'd like to use universally for all form fields you have defined? You can iterate fields by using the `inputs` attribute of your form object. Here's an example:

    >>> for input in simple_form.inputs:
    ...     print input.description
    ...     print input.render()
    ... 
    Name
    <input type="text" name="name" id="name" />
    Surname
    <input type="text" name="surname" id="surname" />