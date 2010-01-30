---
layout: default
title: Templetor: web.py 模板系统
---

# Templetor: web.py 模板系统

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


web.py 的模板语言叫做`Templetor`，它能负责将 python 的强大功能传递给模板系统。
在模板中没有重新设计语法，它是类 python的。 
如果你会 python，你可以顺手拈来。

这是一个模板示例:

    $def with (name)
    Hello $name!

第一行表示模板定义了一个变量 `name`。
第二行中的 `$name` 将会用 name 的值来替换。

<div class="warning">
如果是从 web.py 0.2 升级请看这里 <a href="#upgrading">升级</a> 部分。
</div>

<a name="using"></a>
# 使用模板系统

The most common way of rendering templates is this:
通用渲染模板的方法：

    render = web.template.render('templates')
    return render.hello('world')
   
`render` 方法从模板根目录查找模板文件，`render.hello(..)`表示渲染 hello.html 模板。实际上，系统会在根目录去查找叫 `hello`的所有文件，直到找到匹配的。(事实上他只支持 .html 和 .xml 两种)

However you can also create template from a file using `frender`.
除了上面的使用方式，你也可以直接用文件的方式来处理模板 `frender`：

    hello = web.template.frender('templates/hello.html')
    render hello('world')
    
直接使用字符串方式：

    template = "$def with (name)\nHello $name"
    hello = web.template.Template(template)
    return hello('world')

<a name="syntax"></a>
# 语法

## 表达式用法

特殊字符 `$` 被用于特殊的 python 表达式。表达式能够被用于一些确定的组合当中 `()` 和 `｛｝`:

    Look, a $string. 
    Hark, an ${arbitrary + expression}. 
    Gawk, a $dictionary[key].function('argument'). 
    Cool, a $(limit)ing.

## 赋值

有时你可能需要定义一个新变量或给一些变量重新赋值，如下：
    
    $ bug = get_bug(id)
    <h1>$bug.title</h1>
    <div>
        $bug.description
    <div>

注意 `$`在赋值变量名称之前要有一个空格，这有区别于常规的赋值用法。

## 过滤

模板默认会使用 `web.websafe` 过滤 html 内容(encodeing 处理)。

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