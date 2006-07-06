---
layout: default
title: web.py templating system (codename: templetor) 
---

# web.py templating system (codename: templetor) 

There are almost as many Python templating systems as there are web 
frameworks (and, indeed, it seems like many templating systems are 
adopting web framework-like features), so it is with some trepidation 
that I work on a new one. Sadly, again I find that my requirement are 
met by nothing else: 

1. The templating system has to _look_ decent. No `<%#foo#%>` crud. 
2. Reuse Python terms and semantics as much as possible. 
3. Expressive enough to do real computation. 
4. Usable for any text language, not just HTML and XML. 

And requirements for the implementation as well: 

4. Sandboxable so that you can let untrusted users write templates. 
5. Simple and fast implementation. 

So here's my entry. 

## Variable substitution 

    Look, a $string. 
    Hark, an ${arbitrary + expression}. 
    Gawk, a $dictionary[key].function('argument'). 
    Cool, a $(limit)ing. 

    Stop, \$money isn't evaluated. 

We use basically the same semantics as (rejected) [PEP 
215](http://www.python.org/peps/pep-0215.html). Variables can go 
anywhere in a document. 

## Newline suppression 

    If you put a backslash \ 
    at the end of a line \ 
    (like these) \ 
    then there will be no newline. 

renders as all one line. 

## Expressions 

    Here are some expressions: 

    $for var in iterator: I like $var! 

    $if times > max: 
        Stop! In the name of love. 
    $else: 
        Keep on, you can do it. 

    $try: 
        $get(input) 
    $except: 
        Couldn't find it. 

    That's all, folks. 

All your old Python friends are here: `if`, `while`, `for`, `try`, 
`except`, `else`. `break`, `continue`, and `pass` also act as you'd 
expect. (Obviously, you can't have variables named any of these.) The 
Python code starts at the `$` and ends at the `:`. The `$` has to be 
at the beginning of the line, but that's not such a burden because of 
newline suppression (above). 

Also, we're very careful about spacing -- all the lines will render 
with no spaces at the beginning. (Open question: what if you want 
spaces at the beginning?) 

There are a couple changes from Python: `for` and `while` now take an 
`else` clause that gets called if the loop is never evaluated. 

(Possible feature to add: Django-style for loop variables.) 

## Comments 

    $# Here's where we hoodwink the folks at home: 

    Please enter in your deets: 

    CC: [       ]  $#this is the important one 
    SSN: $#Social Security Number#$ [       ] 

Comments start with `$#` and go to `#$` or the end of the line, 
whichever is first. 

## Code 

    Sometimes you just need to break out the Python. 

    $ mapping = { 
    $   'cool': ['nice', 'sweet', 'hot'], 
    $   'suck': ['bad', 'evil', 'awful'] 
    $ } 

    Isn't that $mapping[thought]? 
    That's$ del mapping $ fine with me. 

    $ complicatedfunc() 

    $ for x in bugs: 
        $ if bug.level == 'severe': 
            Ooh, this one is bad. 
            $ continue 
        And there's $x... 

Code begins with a `$` and a space and goes until the next `$` or the 
end of the line, whichever comes first. Nothing ever gets output if 
the first character after the `$` is a space (so `complicatedfunc` 
above doesn't write anything to the screen like it might without the 
space). 

## Python integration 

A template begins with a line like this: 

    $def with (name, title, company='BigCo') 

which declares that the template takes those arguments. (The `with` 
keyword is special, like `def` or `if`.) 

Inside Python, the template looks like a function that takes these 
arguments. It returns a storage object with the special property that 
evaluating it as a string returns the value of the body of the 
template. The elements in the storage object are the results of the 
`def`s and the `set`s. 

Perhaps an example will make this clearer. Here's a template: 

    $def with (post) 

    $var title: $post.title 

    <p>$markdown(post.body)</p> 

    <p class="byline">by $post.author</p> 

Here's another: 

    $def with (self) 
    <html><head> 
      <title>$self.title</title> 
    </head><body> 
    <h1>$self.title</h1> 

    $self 
    </body></html> 

Now let's say we compile both from within Python, the first as `page`, 
the second as `base`. Here's how we might use them: 

    print base(page(post)) 

`page` takes the argument post and returns an object whose string 
value is a bit of HTML showing the post with its title in the property 
`title`. `base` takes this object and places the title in the 
appropriate place and displays the page itself in the body of the 
page. The Python code prints out the result. 

_Where did `markdown` come from? It wasn't passed as an argument._ You 
can pass a list of functions and variables to the template compiler to 
be made globally available to templates. 

Here's an example:

    import template
    render = template.render('templates/')
    template.Template.globals['len'] = len
    
    print render.base(render.message('Hello, world!'))

The first line imports templetor. The second says that our templates are in the directory `templates/`. The third give all our templates access to the `len` function. The fourth grabs the template `message.html`, passes it the argument `'Hello, world!'`, passes the result of rendering it to the template `base.html` and prints the result. (If your templates don't end in `.html` or `.xml`, templetor will still find them, but it won't do its automatic HTML-encoding.)

## Turning Off Filter
By default `template.render` will use `web.websafe` filter to do HTML-encoding. To turn it off, put a : after the $ as in:

    $:form.render()

Output from form.render() will be displayed as is.