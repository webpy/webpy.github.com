---
layout: default
title: web.py 0.2 tutorial
---

# web.py 0.2 tutorial

## Startujemy

A więc potrafisz programować w Pythonie i pragniesz zrobić swoją stronę. Z web.py to zadanie staje się wyjątkowo łatwe.

Jeżeli masz zamiar przejść przez cały tutorial, będziesz potrzebował mieć zainstalowane: Python, web.py, flup, psycopg2 i Postgress (lub inną bazę danych oraz pythonowy driver do niej). Po szczegóły zerknij na [webpy.org](http:webpy.org/).

Jeżeli masz już istniejący projekt stworzony z użyciem web.py, zajrzyj na stronę opisującą [upgrade](http://webpy.infogami.com/upgrade_to_point2). Znajdziesz tam informacje przydatne podczas migracji.

A więc zaczynamy.

## Obsługa URL

Jednym z ważniejszych aspektów w projekcie serwisu webowego jest jego struktura odnośników (urli). Są one nie tylko tym, co osoby odwiedzający stronę widzą i ewentualnie przekazują swoim znajomym, ale także dają wyobrażenie o tym, jak twój serwis działa. Niektóre popularne serwisy jak [del.icio.us](http://del.icio.us/) uczyniły odnośniki częścią interfejsu użytkownika. web.py umożliwia stworzenie świetnych odnośników w prosty sposób.

Żeby zacząć przygodę z web.py, otwórz nowy plik tekstowy (nazwijmy go code.py) i napisz w nim:

    import web

Instrukcja ta spowoduje zaimportowanie modułu web.py.

Teraz trzeba wskazać strukturę odnośników, jaką ma obsługiwać web.py. Zacznijmy od czegoś naprawdę prostego:

    urls = (
      '/', 'index',
      '',  'index'    )

Pierwsza część każdego wpisu to [wyrażenie regularne](http://osteele.com/tools/rework/) do którego będzie porównywany odnośnik, np. `/`, `/help/faq`, `/item/(\d+)`, itp. (`\d+` zostanie dopasowane do sekwencji cyfr, czyli liczby). Nawiasy powodują "złapanie" części odnośnika z celu dalszego użycia. Druga część wpisu to nazwa pythonowej klasy, która ma obsłużyć zapytanie dla danego odnośnika, np. `index`, `view`, `welcomes.hello` (czyli klasa hello w module welcomes) lub `get_\1`. `\1` zostanie zastąpione przez pierwsze dopasowanie wyrażenia regularnego, reszta dopasowań zostanie przekazana jako parametry do klasy.

Powyższy kod oznacza, że chcemy aby odnośnik `/` (to jest strona powitalna) była obsługiwana przez klasę nazwaną `index`.

Teraz trzeba ową klasę napisać. Prawdopodobie większość osób nawet nie zauważa tego, że przeglądarka używa protokołu zwanego HTTP do komunikacji z siecią WWW. Nie są tutaj istotne szczegóły, ale podstawowa idea jest taka, że serwery WWW są proszone o wykonanie pewnych funkcji (jak `GET` lub `POST`) przy użyciu odnośników (jak `/` lub `/foo?f=1`).

Funkcja `GET` jest tą najbardziej popularną i najczęściej używaną do pobrania z serwera strony web. Wpisując w przeglądarce adres `harvard.edu` w istocie przeglądarka poprosi serwer Harvardu o wykonanie funkcji `GET /`. Drugą najpopularniejszą funkcją jest `POST`. Najczęściej używana jest do wysyłania rozmaitych formularzy, np. z prośba o kupienie czegoś. 
 
W naszym kodzie rozróżnienie tych dwóch funkcji jest bardzo proste i czytelne:

    class index:
        def GET(self):
            print "Hello, world!"

Zdefiniowana funkcja `GET` będzie wywołana przez web.py za każdym razem gdy serwer dostanie prośbę o odnośnik `/`.

Dobrze, teraz jeszcze musimy dopisać ostatnią linijkę uruchamiającą web.py:

    if __name__ == "__main__": web.run(urls, globals())

Kod ten mówi web.py żeby dostarczał odnośniki wymienione powyżej, używając do tego klass zdefiniowanych w głównej przestrzeni nazw tego pliku.

Warto zauważyć, że pomimo długiego opisu, tak naprawdę napisaliśmy mniej więcej 5 linii kodu. Tylko tyle potrzeba, aby stworzyć kompletną aplikację web.py. Można ją teraz uruchomić w ten sposób:

    $ python code.py
    Launching server: http://0.0.0.0:8080/

Właśnie uruchomiłeś swoją własną aplikację web.py i serwer www na swoim komputerze. Wpisz w przeglądarkę ten adres aby zobaczyć "Hello, world!" (możesz dopisać po code.py adress ip/port, możesz też polecić uruchomienie serwera `fastcgi` lub `scgi`).

**Uwaga:** Możesz podać numer portu na którym ma działać serwer jeżeli nie chcesz lub nie możesz użyć tego domyślnego:

    $ python code.py 1234

## Rozwijanie aplikacji

web.py posiada kilka narzędzi pomocnych w tropieniu i usuwaniu ewentualnych błędów. Przed `if __name__` w ostatniej linijce dopisz:

    web.webapi.internalerror = web.debugerror

Spowoduje to wyświetlanie bardziej przyjaznych komunikatów o błędach. Dodatkowo w ostatniej linijce dopisz `web.reloader`:

    if __name__ == "__main__": web.run(urls, globals(), web.reloader)
    
Spowoduje to użycie middleware'u web.reloader, który będzie przeładowywał twoje pliki z kodem za każdym razem gdy coś w nich zmienisz, tak abyś widział te zmiany od razu w działającym serwerze. Chociaż mimo wszystko, poważniejsze zmiany w kodzie i tak będą wymagały restartu serwera. Prawdopodobnie będziesz chciał wyłączyć tą opcję w docelowej wersji serwisu, ale jest to spore ułatwienie na czas kodowania. Dostępny jest także `web.profiler`, który dostarcza informacje o tym jak szybko (lub wolno) są wykonywane twoje funkcje.

## Szablony

Pisanie kodu HTML bezpośrednio w Pytonie jest niezbyt wygodne. Zdecydowanie ciekawsze jest pisanie kodu Pythona wewnątrz HTML. Na szczęście web.py czyni to całkiem łatwym.

**Uwaga:** Stare wersje web.py używały [Cheetah](http://www.cheetahtemplate.org/). Możesz oczywiście nadal używać tych lub innych szablonów, ale Cheetah nie są już oficjalnie wspierane.

(translation is in progress...)

Let's make a new directory for our templates (we'll call it `templates`). Inside, make a new file whose name ends with HTML (we'll call it `index.html`). Now, inside, you can just write normal HTML:

    <em>Hello</em>, world!

Or you can use web.py's templating language to add code to your HTML:

    $def with (name)
    
    $if name:
        I just wanted to say <em>hello</em> to $name.
    $else:
        <em>Hello</em>, world!

**Note: Currently, four spaces are required for indentation.**

As you can see, the templates look a lot like Python files except for the `def with` statement at the top (saying what the template gets called with) and the `$`s placed in front of any code.  Currently, template.py requires the `$def` statement to be the first line of the file.  Also, note that web.py automatically escapes any variables used here, so that if for some reason `name` is set to a value containing some HTML, it will get properly escaped and appear as plain text. If you want to turn this off, write `$:name` instead of `$name`.

Now go back to `code.py`. Under the first line, add:

    render = web.template.render('templates/')

This tells web.py to look for templates in your templates directory. Then change `index.GET` to:

    name = 'Bob'    
    print render.index(name)

('index' is the name of the template and 'name' is the argument passed to it)

Visit your site and it should say hello to Bob. 

**Development tip:** Add , `cache=False` to the end of your `render` call to have web.py reload your templates every time you visit the page.

But let's say we want to let people enter their own name in. Replace the two lines we added above with:

    i = web.input(name=None)
    print render.index(i.name)

Visit `/` and it should say hello to the world. Visit `/?name=Joe` and it should say hello to Joe.

Of course, having that `?` in the URL is kind of ugly. Instead, change your URL line at the top to:

    '/(.*)', 'index'

and change the definition of `index.GET` to:

    def GET(self, name):
        print render.index(name)

and delete the line setting name. Now visit `/Joe` and it should say hello to Joe.

If you wish to learn more about web.py templates, vist the [templetor page](/templetor).

## Databasing

**Note:** Before you can start using a database, make sure you have the appropriate database library installed.  For MySQL databases, use [MySQLdb](http://sourceforge.net/project/showfiles.php?group_id=22307) and for Postgres use [psycopg2](http://initd.org/pub/software/psycopg/).

Above your `web.run` line add:

    web.config.db_parameters = dict(dbn='postgres', user='username', pw='password', db='dbname')

(Adjust these -- especially `username`, `password`, and `dbname` -- for your setup. MySQL users will also want to change `dbn` definition to `mysql`.)

If you're running a web application, that's all you need to do -- web.py will automatically handle connecting and disconnecting from the database. But if you're working from the command line or starting your own thread, you need to call `web.load()` to connect and `web.unload()` to disconnect.

Using your database engines admin interface, create a simple table in your database:

    CREATE TABLE todo (
      id serial primary key,
      title text,
      created timestamp default now(),
      done boolean default 'f'    );

And an initial row:

    INSERT INTO todo (title) VALUES ('Learn web.py');

Return to editing `code.py` and change `index.GET` to the following, replacing the entire function:

    def GET(self):
        todos = web.select('todo')
        print render.index(todos)

and change back the URL handler to take just `/` as in:

    '/', 'index',

Edit and replace the entire contents of `index.html` so that it reads:

    $def with (todos)
    <ul>
    $for todo in todos:
        <li id="t$todo.id">$todo.title</li>
    </ul>

Visit your site again and you should see your one todo item: "Learn web.py". Congratulations! You've made a full application that reads from the database. Now let's let it write to the database as well.

At the end of `index.html`, add:

    <form method="post" action="add">
    <p><input type="text" name="title" /> <input type="submit" value="Add" /></p>
    </form>

And change your URLs list to read:

    '/', 'index',
    '/add', 'add'

(You've got to be very careful about those commas.  If you omit them, Python adds the strings together and sees `'/index/addadd'` instead of your list of URLs!)

Now add another class:

    class add:
        def POST(self):
            i = web.input()
            n = web.insert('todo', title=i.title)
    	    web.seeother('/')

(Notice how we're using `POST` for this?)

`web.input` gives you access to any variables the user submitted through a form. 

Note: In order to access data from multiple identically-named items, in a list format (e.g.: a series of check-boxes all with the attribute name="name") use:

    post_data=web.input(name=[])

`web.insert` inserts values into the database table `todo` and gives you back the ID of the new row. `seeother` redirects users to that URL.

Some quick additional notes: `web.transact()` starts a transaction. `web.commit()` commits it; `web.rollback()` rolls it back. `web.update` works just like `web.insert` except instead of returning the ID it takes it (or a string `WHERE` clause) after the table name.

`web.input`, `web.query`, and other functions in web.py return "Storage objects", which are just like dictionaries except you can do `d.foo` in addition to `d['foo']`. This really cleans up some code.

You can find the full details on these and all the web.py functions in [the documentation](/docs).

This ends the tutorial for now. Take a look at the documentation for lots more cool stuff you can do with web.py.