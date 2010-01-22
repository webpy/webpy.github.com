---
layout: default
title: Templating
---

# Templating

<a name="introduction"></a>
# Introduction

<style>
pre {
    background-color:#F0F0F0;
    border:1px solid #CCCBBA;
       padding: 10px 10px 10px 20px;
}
code {
    background: inherit;
    color: inherit;
}
.warning {
    border: 1px solid #FFAAAA;
    padding: 10px;
    background-color: #FFF0F0;
}
</style>


The web.py template language, called `Templetor` is designed to bring the power of Python to templates.
Instead of inventing new syntax for templates, it re-uses python syntax. 
If you know Python programming language, you will be at home.

Here is a simple template:

    $def with (name)
    Hello $name!

The first line says that the template is defined with one argument called `name`.
`$name` in the second line will be replaced with the value of name when the template is rendered.

<div class="warning">
For upgrading from web.py 0.2 templates see <a href="#upgrading">upgrading</a> section.
</div>

<a name="using"></a>
# Using the template system

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

<a name="syntax"></a>
# Syntax

## Expression Substitution

Special character `$` is used to specify python expressions. Expression can be enclosed in `()` or `{}` for explicit grouping.

    Look, a $string. 
    Hark, an ${arbitrary + expression}. 
    Gawk, a $dictionary[key].function('argument'). 
    Cool, a $(limit)ing.

## Assignments

Sometimes you may want to define new variables and re-assign some variables.
    
    $ bug = get_bug(id)
    <h1>$bug.title</h1>
    <div>
        $bug.description
    <div>

Notice the space after `$` in the assignment. It is required to differentiate assignment from expression substitution.

## Filtering 

By default, Templetor uses `web.websafe` filter to do HTML-encoding.

    >>> render.hello("1 < 2")
    "Hello 1 &lt; 2"

To turnoff filter use `:` after `$`. For example:

    The following will not be html escaped.
    $:form.render()
    
## Newline suppression

Newline can be suppressed by adding `\` character at the end of line. 

    If you put a backslash \ 
    at the end of a line \ 
    (like these) \ 
    then there will be no newline.
    
## Escaping $

Use `$$` to get `$` in the output.

    Can you lend me $$50?
    
## Comments

`$#` is used as comment indicator. Anything starting with $# till end of the line is ignored.

    $# this is a comment
    Hello $name.title()! $# display the name in title case

## Control Structures

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
    
## Other Statements

### def

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
    
### code

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
    
### var

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

<a name="builtins"></a>
# builtins and globals

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

<a name="security"></a>
# Security

One of the design goals of Templetor is to allow untrusted users to write templates.

To make the template execution safe, the following are not allowed in the templates.

* Unsafe statements like `import`, `exec` etc.
* Accessing attributes starting with `_`
* Unsafe builtins like `open`, `getattr`, `setattr` etc.

`SecurityException` is raised if your template uses any of these.

<a name="upgrading"></a>
# Upgrading from web.py 0.2 templates

The new implementation is mostly compatible with the earlier implementation. However some cases might not work because of the following reasons.

* Template output is always storage like `TemplateResult` object, however converting it to `unicode` or `str` gives the result as unicode/string.
* Reassigning a global value will not work. The following will not work if x is a global.
    
        $ x = x + 1
    
The following are still supported but not preferred.

* Using `\$` for escaping dollar. Use `$$` instead.
* Modifying `web.template.Template.globals`. pass globals to `web.template.render` as argument instead.

<script src=http://angelo.gladding.name/assets/jquery.js></script>
<script src=http://angelo.gladding.name/assets/webpy/js-prettify/prettify.js></script>
<script src=http://angelo.gladding.name/assets/webpy/enliven.js></script>

<style>
@import url(http://angelo.gladding.name/assets/webpy/js-prettify/prettify.css);
@import url(http://angelo.gladding.name/assets/webpy/changes.css);
</style>