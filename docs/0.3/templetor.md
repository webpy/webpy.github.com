---
layout: default
title: Templetor - The web.py templating system
---

# Templetor: The web.py templating system

Other languages : [français](/docs/0.3/templetor.fr) | ...

## Summary

* <a href="#introduction">Introduction</a>
* <a href="#using">Using the template system</a>
* <a href="#syntax">Syntax</a>
    * <a href="#expressionsubstitution">Expression Substitution</a>
    * <a href="#assignments">Assignments</a>
    * <a href="#filtering">Filtering</a>
    * <a href="#newlinesuppression">Newline suppression</a>
    * <a href="#escaping">Escaping '$'</a>
    * <a href="#comments">Comments</a>
    * <a href="#controlstructure">Control Structures</a>
* <a href="#otherstatements">Other Statements</a>
    * <a href="#def">$def : define a new template function using $def</a>
    * <a href="#code">$code : arbitrary python code can be written</a>
    * <a href="#var">$var : can be used to define additional properties</a>
* <a href="#builtins">Builtins and globals</a>
* <a href="#security">Security</a>
* <a href="#upgrading">Upgrading from web.py 0.2 templates</a>
* <a href="#errors">Errors you may experience</a>


<h1 id="introduction">Introduction</h1>

The web.py template language, called `Templetor` is designed to bring the power of Python to templates.
Instead of inventing new syntax for templates, it re-uses python syntax. 
If you know the Python programming language, you will be at home.

Templetor intentionally limits variable access within a template. A user has access to the variables passed into the template and some builtin python functions.  This allows untrusted users to write templates, and not worry about them causing harm to the running system. You can, of course, increase the global variables available, but more on this later.

Here is a simple template:

    $def with (name)
    Hello $name!

The first line says that the template is defined with one argument called `name`.
`$name` in the second line will be replaced with the value of name when the template is rendered.


<h1 id="using">Using the template system</h1>

The most common way of rendering templates is this:

    render = web.template.render('templates')
    print render.hello('world')
   
The `render` function takes the template root as argument. `render.hello(..)` calls the template `hello.html` with the given arguments.
In fact, it looks for the files matching `hello.*` in the template root and picks the first matching file.

However you can also create template from a file using `frender`.

    hello = web.template.frender('templates/hello.html')
    print hello('world')
    
And if you have the template as a string:

    template = "$def with (name)\nHello $name"
    hello = web.template.Template(template)
    print hello('world')

<h1 id="syntax">Syntax</h1>

<h2 id="expressionsubstitution">Expression Substitution</h2>

Special character `$` is used to specify python expressions. Expression can be enclosed in `()` or `{}` for explicit grouping.

    Look, a $string. 
    Hark, an ${arbitrary + expression}. 
    Gawk, a $dictionary[key].function('argument'). 
    Cool, a $(limit)ing.

<h2 id="assignments">Assignments</h2>

Sometimes you may want to define new variables and re-assign some variables.
    
    $ bug = get_bug(id)
    <h1>$bug.title</h1>
    <div>
        $bug.description
    <div>

Notice the space after `$` in the assignment. It is required to differentiate assignment from expression substitution.

<h2 id="filtering">Filtering </h2>

By default, Templetor uses `web.websafe` filter to do HTML-encoding.

    >>> render.hello("1 < 2")
    "Hello 1 &lt; 2"

To turnoff filter use `:` after `$`. For example:

    The following will not be html escaped.
    $:form.render()

<h2 id="newlinesuppression">Newline suppression</h2>

Newline can be suppressed by adding `\` character at the end of line. 

    If you put a backslash \ 
    at the end of a line \ 
    (like these) \ 
    then there will be no newline.
    
<h2 id="escaping">Escaping $</h2>

Use `$$` to get `$` in the output.

    Can you lend me $$50?
    
<h2 id="comments">Comments</h2>

`$#` is used as comment indicator. Anything starting with $# till end of the line is ignored.

    $# this is a comment
    Hello $name.title()! $# display the name in title case

<h2 id="controlstructure">Control Structures</h2>

The template system supports `for`, `while`, `if`, `elif` and `else`.
Just like in python, body of the statement is indented.

    $for i in range(10): 
        I like $i

    $for i in range(10): I like $i
        
    $while a:
        hello $a.pop()

    $if times > max: 
        Stop! In the name of love. 
    $else: 
        Keep on, you can do it.

The for loop sets a number of variables available within the loop:

    loop.index: the iteration of the loop (1-indexed)
    loop.index0: the iteration of the loop (0-indexed)
    loop.first: True if first iteration
    loop.last: True if last iteration
    loop.odd: True if an odd iteration
    loop.even: True if an even iteration
    loop.parity: "odd" or "even" depending on which is true
    loop.parent: the loop above this in nested loops
    
Sometimes these can be very handy.

    <table>
    $for c in ["a", "b", "c", "d"]:
        <tr class="$loop.parity">
            <td>$loop.index</td>
            <td>$c</td>
        </tr>
    </table>
    
<h2 id="otherstatements">Other Statements</h2>

<h3 id="def">def</h3>

You can define a new template function using `$def`. Keyword arguments are also supported.

    $def say_hello(name='world'):
        Hello $name!
    
    $say_hello('web.py')
    $say_hello()

Another example:
        
    $def tr(values):
        <tr>
        $for v in values:
            <td>$v</td>
        </tr>

    $def table(rows):
        <table>
        $for row in rows:
            $:row
        </table>
    
    $ data = [['a', 'b', 'c'], [1, 2, 3], [2, 4, 6], [3, 6, 9] ]
    $:table([tr(d) for d in data])
    
<h3 id="code">code</h3>

Arbitrary python code can be written using the `code` block.

    $code:
        x = "you can write any python code here"
        y = x.title()
        z = len(x + y)
        
        def limit(s, width=10):
            """limits a string to the given width"""
            if len(s) >= width:
                return s[:width] + "..."
            else:
                return s
                
    And we are back to template.
    The variables defined in the code block can be used here.
    For example, $limit(x)
    
<h3 id="var">var</h3>

The `var` block can be used to define additional properties in the template result.

    $def with (title, body)
    
    $var title: $title
    $var content_type: text/html
    
    <div id="body">
    $body
    </div>
    
The result of the above template can be used as follows:

    >>> out = render.page('hello', 'hello world')
    >>> out.title
    u'hello'
    >>> out.content_type
    u'text/html'
    >>> str(out)
    '\n\n<div>\nhello world\n</div>\n'

<h1 id="builtins">builtins and globals</h1>

Just like any Python function, template can also access builtins along with its arguments and local variables.
Some common builtin functions like `range`, `min`, `max` etc. and boolean values `True` and `False` are made available to all the templates.
Apart from the builtins, application specific globals can be specified to make them accessible in all the templates.

Globals can be specified as an argument to `web.template.render`.

    import web
    import markdown
    
    globals = {'markdown': markdown.markdown}
    render = web.template.render('templates', globals=globals)

Builtins that are exposed in the templates can be controlled too.

    # disable all builtins
    render = web.template.render('templates', builtins={})

<h1 id="security">Security</h1>

One of the design goals of Templetor is to allow untrusted users to write templates.

To make the template execution safe, the following are not allowed in the templates.

* Unsafe statements like `import`, `exec` etc.
* Accessing attributes starting with `_`
* Unsafe builtins like `open`, `getattr`, `setattr` etc.

`SecurityException` is raised if your template uses any of these.

<h1 id="upgrading">Upgrading from web.py 0.2 templates</h1>

The new implementation is mostly compatible with the earlier implementation. However some cases might not work because of the following reasons.

* Template output is always storage like `TemplateResult` object, however converting it to `unicode` or `str` gives the result as unicode/string.
* Reassigning a global value will not work. The following will not work if x is a global.

    $ x = x + 1

The following are still supported but not preferred.

* Using `\$` for escaping dollar. Use `$$` instead.
* Modifying `web.template.Template.globals`. pass globals to `web.template.render` as argument instead.

<h1 id="errors">Errors you may experience</h1>

If your error isn't mentioned here, feel free to report it by creating an
issue with sample code used to reproduce it:
<https://github.com/webpy/webpy.github.com/issues>

## Error: `TypeError: __template__() got an unexpected keyword argument 'myvar'`

The `render` calls the template file with unexpected keyword argument `myvar`.

Template file:
```
$def with (var1, var2)

My content:
$:var1
$:var2
```

Python code.

```
import web
render = web.template.render()

# WRONG. `myvar` should be removed.
render.my_template_file(var1=..., var2=..., myvar=...)

# CORRECT.
render.my_template_file(var1=..., var2=...)
```

## Error: `TypeError: __template__() takes 0 positional arguments but 1 was given`

Template file doesn't have `$def with (...)` line (which indicates it doesn't use any variables), but 1 variable name is passed to the template while calling the `render` function.

Template file:
```
My sample content here without using any variable.
```

Python code:

```
# WRONG.
render.my_template_file(myvar=...)

# CORRECT.
render.my_template_file()
```

## Error: `TypeError: __template__() missing 1 required positional argument: 'myvar'`

Template file uses variable name `myvar`, but it's not passed while calling the `render`.

Template file:

```
$def with (myvar)

Render the value:
$:myvar
```

Python code.
```
# WRONG.
render.my_template_file()

# CORRECT
render.my_template_file(myvar=...)
```
