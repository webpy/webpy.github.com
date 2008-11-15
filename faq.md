---
layout: default
title: FAQ
---

# FAQ

99. **How do I use template.py templates?**

    For basic doc and some code snippets, see [template.py doc](/templetor)

    To display your page from inside a web.py app, just do

            homepage = template.Template(open("homepage.tmpl").read())
            print homepage()

    
99. **Why are the urls just one long list?**

    If they were a dictionary, they wouldn't be ordered. If it was a list of tuples, then it'd be a lot more typing.

99. **How do I serve static files such as JavaScripts or images like PNG and JPG with the web.py server?**

    Create a directory (also known as a folder) called `static` in the location of the script that runs the web.py server. Then place the static files you wish to server in the `static` folder. For example, the URL `http://localhost/static/logo.png` will send the image `./static/logo.png` to the client.

99. **Where can I go for additional help?**

    Google Groups has a [web.py group](http://groups.google.com/group/webpy) that is quite helpful.

99. **How can I change the default "not found" page?**

    You can write your own custom notfound handler and assign it to web.webapi.notfound

            def my_notfound(): 
                print "MY OWN NOT FOUND" 
            web.webapi.notfound = my_notfound 

99. **How can i get auto completion in python after loading the webpy module?**

    In IPython, after importing webpy auto completion may no longer work. You can still use 'python' with auto completion feature. Try it out directly. Fire up 'python':

            import readline, rlcompleter; readline.parse_and_bind("tab: complete")

    and tab it! :-)

    To make in sort that this will be run default when you fire up 'python'. Make a file called '~/.pythonstartup.py' and put the import line in it. Then set the 'PYTHONSTARTUP' environment variable to point to that file.

    With my bash, i do it like following; edit ~/.bashrc and add:

            export PYTHONSTARTUP=~/.pythonstartup.py

99. **Why can't I access the database?**

    If you're trying to access the database from a non-web-serving thread (e.g. you created a new thread or you never started serving web pages) then you need to run `web.load()`. Sorry, this will be fixed in web.py 0.3.

99. **Can I iterate over an IterBetter multiple times?**

    No. Do `ib = list(ib)` first to turn it from an IterBetter into a list.

99. **どのようにデバッグ文をコンソールに出力しますか？**

    web.debug("デバッグ文")

99. **もしwebpyの不具合(バグ)を見つけた場合どこで報告すればいいのですか？**

    [ここ(webpy launchpad site)](https://launchpad.net/webpy)からバグ報告することができます。ログインが必要な場合は登録を行ってからバグ報告をしてください。