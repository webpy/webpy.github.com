---
layout: default
title: ČKD
---

# ČKD

99. **Jak použiji šablony template.py?**

    Pro základní dokumentaci a nějaké ukázky kódu, se podívej na [template.py dokumentaci](/templetor).

    Chcete-li zobrazit stránku z web.py aplikace, stačí

            homepage = template.Template(open("homepage.tmpl").read())
            print homepage()

    
99. **Proč jsou adresy URL pouze jeden dlouhý seznam?**

    Pokud by byly ve slovníku, nebylo by je možné řadit. Pokud by byly v seznamu n-tic (tuple), bylo by s nima mnohem více psaní.

99. **How do I serve static files such as JavaScripts or images like PNG and JPG with the web.py server?**

    Create a directory (also known as a folder) called `static` in the location of the script that runs the web.py server. Then place the static files you wish to server in the `static` folder. For example, the URL `http://localhost/static/logo.png` will send the image `./static/logo.png` to the client.

99. **Kam se mohu obrátit pro další pomoc?**

    Google Groups má [skupinu web.py](http://groups.google.com/group/webpy) která je docela užitečná.

99. **Jak můžu změnit výchozí "not found" stránku?**

    Můžete napsat svůj vlastní notfound handler a připojit ho k  web.webapi.notfound

            def my_notfound(): 
                print "MUJ VLASTNI NOT FOUND" 
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

99. **Mohu vícekrát iterovat IterBetter?**

    Ne. Nejdřív převeď IterBetter na seznam pomocí `ib = list(ib)`.

99. **Jak vytisknu debug do konsole?**

	web.debug("Budu vytištěn do konsole a ne do těla stránky")

99. **Narazil jsem na chybu ve web.py. Kam ji můžu nahlásit?**

	Jdi na [webpy launchpad](https://launchpad.net/webpy), přihlaš se (nebo se zaregistruj) a klikni na "report a bug".