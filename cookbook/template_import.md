---
layout: default
title: Import functions into templates
---

# Import functions into templates

### Problem

How can I import a Python module in template?

### Solution

While you write templates, inevitably you will need to write some functions
which is related to display logic only.  web.py gives you the flexibility to
write large blocks of code, including defining functions, directly in the
template using `$code` blocks (if you don't know what is `$code` block, please
read the [tutorial for Templator](/docs/0.3/templetor)). For example, the
following code block will translate a status code from database to a human
readable status message:

```
# Your function.
def status(c):
    ...
```

As you do more web.py development, you will write more such functions here and
there in your templates. This makes the template messy and is a violation of
the DRY (Don't Repeat Yourself) principle.

Naturally, you will want to write a module, say `display_logic.py` and import
that module into every templates that needs such functionalities.
Unfortunately, `import` is disabled in template for security reason. However,
it is easy to solve this problem by importing the functions you need into the
template via the global namespace:

```
#
# in your app.py:
#
def status(c):
    ...

# Import function `status` to global namespace with same name.
render = web.template.render('templates', globals={'status': status})

#
# in the template file:
#
$def with(mystatus)
...
<div>Status: $status(mystatus)</div>
```

You can import more than one name into the `globals` dict. This trick is also
used in [importing session variable into template](/cookbook/session_in_template).
