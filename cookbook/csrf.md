---
layout: default
title: How to protect forms from CSRF attacks
---

# How to protect forms from CSRF attacks

## Problem

How to make sure a POST form submission genuinely originates from a form created by the application,
and is not a [Cross-Site Request Forgery](https://secure.wikimedia.org/wikipedia/en/wiki/Csrf).

## Solution

We keep a unique csrf_token that is rendered as a hidden field inside post forms and can not be guessed by CSRF attackers.
This token gets checked during POST methods.

We need 4 things:

1. A `csrf_token()` function - to use inside form templates. It either returns the existing `session.csrf_token` or generates a new one.

1. A `@csrf_protected` decorator for `POST()` methods. It pops `session.csrf_token` and compares it with the `csrf_token`
   input we expect to get from a genuine form (see `<input type="hidden" ...>` below.
   Whether the test succeeds or fails, this will make sure that next time `csrf_token()` is called (most probably - from
   inside a form's template), a new token will be generated.

1. Make `csrf_token()` available to templates by adding it to the globals of our `render` object.

1. Add `<input type="hidden" name="csrf_token" value="$csrf_token()"/>` to the forms in the templates.


We define `csrf_token()` like this:

    def csrf_token():
        if not session.has_key('csrf_token'):
            from uuid import uuid4
            session.csrf_token=uuid4().hex
        return session.csrf_token
    
The `@csrf_protected` decorator is defined like this:

    def csrf_protected(f):
        def decorated(*args,**kwargs):
            inp = web.input()
            if not (inp.has_key('csrf_token') and inp.csrf_token==session.pop('csrf_token',None)):
                raise web.HTTPError(
                    "400 Bad request",
                    {'content-type':'text/html'},
                    """Cross-site request forgery (CSRF) attempt (or stale browser form).
    <a href="">Back to the form</a>."""') # Provide a link back to the form
            return f(*args,**kwargs)
        return decorated

In order to make csrf_token() available to templates, we need to add it to the globals of the `render` object like this:

    render = web.template.render('templates',globals={'csrf_token':csrf_token})

A template that renders a POST form (called - say - `myform.html`) would look like:

    <form method=post action="">
      <input type="hidden" name="csrf_token" value="$csrf_token()"/>
      # ... form fields ...
    </form>

If we're using a `Form` object from `web.form` called _form_, our `myform.html` template would look like:

    <form method=post action="">
      <input type="hidden" name="csrf_token" value="$csrf_token()"/>
      $:form.render()
    </form>

The form page's object would then look like:

    class myformpage:
        def GET(self):
            return render.myform(...)
        @csrf_protected # Verify this is not CSRF, or fail
        def POST(self):
            # If we're here - this is not a CSRF attack

A simple working demo is availale [here](https://gist.github.com/857297).
