---
layout: default
title: Understanding URL Handling
---

# Understanding URL Handling

Other languages: [Français](./url_handling.fr) | ...

## Problem: how to design a url handling / dispatching scheme for the entire site

## Solution

web.py's URL handling scheme is simple yet powerful and flexible.
At the top of each application, you usually see the full URL dispatching
scheme defined as a tuple:

```
urls = (
    "/tasks/?", "signin",
    "/tasks/list", "listing",
    "/tasks/post", "post",
    "/tasks/chgpass", "chgpass",
    "/tasks/act", "actions",
    "/tasks/logout", "logout",
    "/tasks/signup", "signup"
)
```

The format of this tuple is: `url-path-pattern_`, `handler-class`.
This pattern will repeat as more url patterns are defined.  If you don't
understand the relationship between url pattern and handler classes,
please read the [Hello World example](/cookbook/helloworld) or
[Quick Start Tutorial](./tutorial) before reading any other cookbook recipes.

### URL Pattern and Path Matching

You can utilize the power of regular expressions to design more flexible
url patterns. For example, `/test(1|2)` will catch either `/test1` or `/test2`.
The key point to understand is that this matching happens on the `path`
of your URL. For example, the following URL:

```
http://localhost/myapp/greetings/hello?name=Joe
```

The path of this URL is `/myapp/greetings/hello`.  web.py will internally
add `^` and `$` to the url pattern (`^/myapp/greetings/hello$`) so that the
pattern `/tasks/` will not match `/tasks/addnew`.  As it matches against
the path, you can not use a pattern like `/tasks/delete?name=(.+)` as the
part after `?` is called `query` and is not matched against. For a detailed
description of URL components, please read [web.ctx](/cookbook/ctx).

### Capture Parameters

In the url pattern you can catch parameters which can be used in your handler class:

```
urls = (
    "/users/list/(.+)", "list_users"
)
```

Here the `(.+)` matches the rest URL path after `/users/list/`, it can be
used as a parameter in `GET` or `POST`:

```
class list_users:
    # `name` has the matched content of `(.+)`
    def GET(self, name):
        return "Listing info about user: {0}".format(name)
```

You can define more than one parameters as you wish.  Also note that URL
query parameters (which appears after the `?` in url) can be obtained
using [web.input()](/cookbook/input).

### Note on sub-applications

To better handle larger web applications, web.py supports
[sub-applications](/cookbook/subapp). While designing url scheme with sub
applications, keep in mind that the path (web.ctx.path) will get the parent
path stripped off. e.g. if in the main application, you define to forward
url pattern `/blog` to the `blog` sub-application, in your blog sub-application
all url patterns starts with `/`, __NOT__ `/blog`. Read the
[web.ctx](/cookbook/ctx) cookbook recipe for more details.
