---
layout: default
title: How to use forms
---

# How to use forms

Other languages: [français](/../cookbook/forms/fr) | ...

## Problem

How to use forms.

## Solution

The `web.form` module provides support for creating, validating, and rendering forms.
This module contains a `Form` class and classes for various inputs like `Textbox`, `Password` etc.

Each input can take a list of validators as arguments which are validated against the input when `form.validates()` is called.

The `Form` class can take additional keyword argument `validators` to validate the form using complete input.

Here is an example of a new user registration form:

    import web
    from web import form

    render = web.template.render('templates') # your templates

    vpass = form.regexp(r".{3,20}$", 'must be between 3 and 20 characters')
    vemail = form.regexp(r".*@.*", "must be a valid email address")

    register_form = form.Form(
        form.Textbox("username", description="Username"),
        form.Textbox("email", vemail, description="E-Mail"),
        form.Password("password", vpass, description="Password"),
        form.Password("password2", description="Repeat password"),
        form.Button("submit", type="submit", description="Register"),
        validators = [
            form.Validator("Passwords did't match", lambda i: i.password == i.password2)]

    )

    class register:
        def GET(self):
            # do $:f.render() in the template
            f = register_form()
            return render.register(f)

        def POST(self):
            f = register_form()
            if not f.validates():
                return render.register(f)
            else:
                # do whatever is required for registration
 
And the register template should be something like this:

    $def with(form)

    <h1>Register</h1>
    <form method="POST">
        $:form.render()
    </form>