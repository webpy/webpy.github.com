---
layout: default
title: web.py 0.2 tutorial
---

# web.py 0.2 tutorial

## Starting

Du kennst also Python und willst eine Webseite erstellen. web.py gibt dir die Möglichkeit, das leicht zu bewerkstelligen.

Wenn du das ganze Tutorial durcharbeiten willst, wirst du python, web.py, flup, psycopg2 und postgres brauchen. Weitere Details dazu auf [webpy.org](http://webpy.org/).

Wenn du bereits ein web.py Projekt hast, schau am besten auf die [upgrade](http://webpy.infogami.com/upgrade_to_point2) Seite (in Englisch) für Informationen zur Migration. 

Legen wir mal los...

## URL Handling

Der wichtigste Bestandteil einer Website ist die URL Struktur. Die URLs sind nicht nur das, was deine Besucher sehen und an ihre Freunde mailen, sie dienen auch als mentales Model, das zeigt, wie die Webseite funktioniert. Bei bekannten Webseiten wie etwa [del.icio.us](http://del.icio.us) sind die URLs sogar ein Teil des Benutzerinterfaces. web.py macht es leicht, gute URLs zu erstellen.

Um mit deinem web.py-Programm anzufangen, öffne eine neue Textdatei (nenn sie `code.py`) und tippe:

    import web

Dadurch wird das web.py-Modul importiert.

Nun müssen wir web.py unsere URL Struktur bekanntmachen, wir beginnen mit etwas Einfachem:

    urls = (
      '/', 'index'    )

Der erste Teil ist ein [regulärer Ausdruck](http://osteele.com/tools/rework/) dem die URL entsprechen muss, beispielsweise ``/``, ``/help/faq``, ``/item/(\d+)``, etc. (Das ``\d+`` entspricht einer Ziffernfolge. Die runden Klammern bewirken, dass das "gefundene" für später aufgehoben wird. )

Der zweite Teil ist der Name der Klasse an welche die Anfrage geschickt wird, beispielsweise `index`, `view`, `welcomes.hello` (gibt die Anfrage an die Klasse `hello` des Moduls `welcomes`), oder `get_\1`. `\1` wird durch den ersten Treffer (geklammerten Teil) des regulären Ausdrucks ersetzt, alle verbleibenden Funde werden an die Funktion weitergeleitet.

Diese Zeile sagt das wir die URL `/` (die Startseite) mit der Klasse namens `index` bearbeiten wollen.

Nun müssen wir die `index`-Klasse schreiben. Die meisten Leute bemerken es beim Surfen nicht, aber der Browser verwendet eine Sprache, die als HTTP bekannt ist, zur Kommunikation mit dem WWW. Die Details dazu sind nicht wichtig, aber die eigentliche Idee ist, dass die Besucher den Webserver auffordern, bestimmte Funktionen (wie eta `GET` oder `POST`) an URLs (wie `/` oder `/foo?f=1`) auszuführen.

`GET` ist die bekannteste Funktion. Sie wird verwendet, um den Text oder Inhalt einer Webseite anzufordern. Wenn du in deinem Browser `harvard.edu` eintippst, dann forderst du im wahrsten Sinne des Wortes den Harvard Webserver auf "to `GET /`". Am zweit bekanntesten ist `POST`. POST wird oft verwendet, wenn man ein Formular abschickt, wie zum Beispiel eine Anfrage etwas zu kaufen. Du benutzt `POST` immer dann, wenn das Abschicken der Anfrage etwas bewirkt (wenn du die Kreditkarte belastest oder eine Bestellung aufgibst). Das ist sehr wichtig, denn `GET` URLs können herum gereicht werden und von Suchmaschinen indexiert werden. Das ist zwar etwas, was du für einen Großteil deiner Seite willst, aber bestimmt _nicht_ für Dinge wie Bestellungen aufgeben. (Stell dir vor, Google würde versuchen alles auf deiner Seite zu kaufen).


In unserem web.py-Quellcode können wir diese zwei Funktionen unterscheiden:

    class index:
        def GET(self):
            print "Hello, world!"

Die `GET`-Funktion wird nun aufgerufen, wenn jemand eine `GET` Anfrage an `/` schickt.

Gut, nun müssen wir nur noch eine Zeile hinzufügen, um web.py zu sagen, dass es Webseiten zur Verfügung stellen soll.

    if __name__ == "__main__": web.run(urls, globals())

Das sagt web.py, dass es die URLs, die wir oben definiert haben bereitstellen soll, indem es die Klassen aufruft, die wir in der Datei global definiert haben.

Nun, obwohl du bereits viel gelesen hast, haben wir eigentlich nur etwa fünf Zeilen geschrieben. Das ist eigentlich auch alles, was du für eine komplette web.py-Applikation brauchst.

Wenn du nun in deine Kommandozeile gehst und folgendes tippst:

    $ python code.py
    Launching server: http://0.0.0.0:8080/

Dann wird deine web.py-Applikation einen Webserver auf deinem Computer laufen lassen. Besuche nun die URL und du solltest ein "Hello, world!" sehen. (Du kannst eine IP Addresse/Port nach dem "code.py" hinzufügen um zu kontrollieren, wo genau web.py den Server startet. Du kannst ihm ebenso sagen ob er ein `fastcgi` oder `scgi` server starten soll.)

**Hinweis:** Du kannst den Port beim Aufruf von 'code.py' angeben, wenn du den Standardwert 8080 nicht benutzen willst oder kannst:

    $ python code.py 1234


## Developing

Web.py hat ebenso ein paar Tools, die uns beim Debugging helfen. Füge in der letzten Zeile vor `if __name__` folgendes hinzu:

    web.webapi.internalerror = web.debugerror

Das wird dir hilfreiche Fehlermeldungen liefern. Außerdem musst du in der letzten Zeile `web.reloader` hinzufügen, damit es wie folgt aussieht: 

    if __name__ == "__main__": web.run(urls, globals(), web.reloader)

Das sagt web.py, dass es web.reloader verwenden soll. web.reloader ist eine "middleware" (eine Funktion, die bestimmte Funktionalitäten zu dem Webserver hinzufügt). Diese lädt die Dateien jedesmal neu, nachdem du diese verändert hast. Dadurch sieht du die Änderungen sofort im Browser, ohne den Server neu zu starten. (Bei größeren Änderungen kann es trotzdem sein, dass du den Server neustarten musst). Wahrscheinlich wirst du das wieder herausnehmen wollen wenn du deine Seite Online stellst, aber zum Entwickeln ist es großartig. Außerdem gibt es noch den `web.profiler`, der zeigt dir am Ende jeder Webseite Informationen darüber, wie lange jede Funktion gebraucht hat, sodass du dein Programm schneller machen kannst. 
    
## Templating

HTML von Python aus zu schreiben kann sehr lästig werden; es macht viel mehr spaß, Python innerhalb von HTML zu schreiben. Glücklicherweise macht web.py das ziemlich einfach.

**Hinweis:** Ältere Versionen von web.py haben [Cheetah templates](http://www.cheetahtemplate.org/) verwendet. Du kannst das natürlich immer noch verwenden. Ebenso kann jede andere Software zusammen mit web.py verwendet werden. Aber Cheetah wird nicht mehr offiziell unterstützt.

Nun, lasst uns ein neues Verzeichnis für unsere templates erstellen (wir nennen es `templates`). Darin erstellen wir eine neue Datei die auf HTML endet (wir nennen sie `index.html`). Darin kannst du nun normales HTML schreiben:

    <em>Hello</em>, world!

Oder du kannst web.py's _templating_-Sprache verwenden und Code zu HTML hinzufügen:

    $def with (name)
    
    $if name:
        I just wanted to say <em>hello</em> to $name.
    $else:
        <em>Hello</em>, world!

**Achtung: Zur Zeit sind vier Leerzeichen erforderlich für die Einrückung.**

Wie du sehen kannst, sieht das Python-Dateien ähnlich, abgesehen von der `def with`-Anweisung am Anfang (das sagt dem Template womit es aufgerufen wird) und den `$`, die vor Codestücken platziert werden. Zur Zeit ist es erforderlich, dass das `$def`-Statement in der ersten Zeile der Datei steht. Sollte `name` z.B. `<b>test</b>` enthalten so wird auch `<b>test</b>` angezeigt, wenn man will das der HTML Code wirklich interpretiert wird, so muss man `$:name` anstatt `$name` schreiben.

Nun, zurück zur `code.py`. Unter der ersten Zeile fügen wir hinzu:

    render = web.template.render('templates/')

Damit sucht web.py nach Templates in deinem Template-Verzeichnis. Nun ändere `index.GET` zu:

    name = 'Bob'    
    print render.index(name)

(`index` ist der Name des Templates und `name` ist das Argument welches an dieses weitergeleitet wird). 

Besuche deine Seite. Sie sollte nun "hello to Bob" ausgeben.

**Entwicklungstipp:** Füge `cache=False` an das Ende deines `render`-Aufrufs. Damit wird web.py jedesmal das Template neu laden wenn du die Seite aufrufst.

Nun ändere die URL-Zeile zu:

    '/(.*)', 'index'

und ändere die Definition von `index.GET` zu:

    def GET(self, name):

und lösche die Zeile mit `name = 'Bob'`. Besuche `/` und es sollte "hello to the world" zu sehen sein. Besuche `/Joe` und es sollte "hello to Joe" erscheinen.

Wenn du mehr über web.py templates wissen willst, besuche die [templetor page](/templetor).

## Databasing

**Hinweis:** Bevor du eine Datenbank benutzen kannst, vergewissere dich das du die entsprechenden Datenbank Bibliotheken installiert hast. Für MySql Datenbanken kannst du [MySQLdb](http://sourceforge.net/project/shofiles.php?group_id=22307) verwenden und für Postgres verwende [psycopg2](http://initd.org/pub/software/psycopg/).

Über der `web.run` Zeile füge folgendes hinzu:

    web.config.db_parameters = dict(dbn='postgres', user='username', pw='password', db='dbname')

(Passe die Parameter entsprechend an, vor allem `username`, `password`, und `dbname`. MySQL User sollten `dbn` zu `mysql` ändern.)
Die Zeile könnte für Sqlite Benutzer in etwa wie folgt aussehen:

	web.config.db_parameters = dict(dbn='sqlite', db='data.db')

Erstelle eine einfache Tabellen in deiner Datenbank:

    CREATE TABLE todo (
      id serial primary key,
      title text,
      created timestamp default now(),
      done boolean default 'f'    );

Und füge eine Zeile ein:

    INSERT INTO todo (title) VALUES ('Learn web.py');

In `code.py` ändere `index.GET` zu:

    def GET(self):
        todos = web.select('todo')
        print render.index(todos)

und ändere den URL-Handler wieder zurück zu `/`.

Ändere `index.html` damit es wie folgt aussieht: 

    $def with (todos)
    <ul>
    $for todo in todos:
        <li id="t$todo.id">$todo.title</li>
    </ul>

Besuche deine Seite erneut und du wirst dein erstes Todo-Item sehen: "Learn web.py". Gratuliere, du hast ein voll funktionsfähiges Programm, das aus einer Datenbank liest. Nun wollen wir es auch noch in die Datenbank schreiben lassen.

Füge folgendes am Ende von `index.html` hinzu:

    <form method="post" action="add">
    <p><input type="text" name="title" /> <input type="submit" value="Add" /></p>
    </form>

Und ändere deine URLs, damit es so aussieht:

    '/', 'index',
    '/add', 'add'

(Passe mit den Kommas auf. Wenn du sie vergisst, fügt Python die Strings zusammen und sieht `'/index/addadd'`, was nicht das ist, das du haben willst!)

Füge in `code.py` folgende Klasse hinzu: 

    class add:
        def POST(self):
            i = web.input()
            n = web.insert('todo', title=i.title)
    	    web.seeother('/')

(Bemerkt? Wir benutzen hier `POST`)

`web.input` gibt dir Zugriff auf jede Variable die der User durch ein Formular abgeschickt hat. Wenn du Daten von Items mit dem selben Namen verarbeiten willst (wie in etwa bei einer Serie von Checkboxen mit name="name" benutze:

    post_data=web.input(name=[])

`web.insert` fügt eine Zeile zur Datenbanktabelle `todo` hinzu und gibt die ID der neuen Zeile zurück. `seeother` leitet den User weiter zu dieser URL.

Kurz: `web.transact()` startet eine Transaktion. `web.commit()` übergibt diese. `web.rollback()` macht die Transaktion nichtig. `web.update` funktioniert in etwa so wie `web.insert` außer dass es anstatt eine ID zurückzugeben eine nach dem Tabellennamen benötigt (oder eine `WHERE` Klausel). 

`web.input`, `web.query` und einige andere Funktionen in web.py liefern "Storage objects" zurück, sie funktionieren genau wie Dictionaries, außer das du `d.foo` zusätzlich zu `d['foo']` verwenden kannst. Das macht vieles einfach lesbar.

Du kannst die ganzen Details dazu und allen anderen web.py-Funktionen in der [Dokumentation](http://new.webpy.org/docs) nachlesen.

Das Tutorial endet hier, schau dir die Dokumentation an, um zu sehen was man noch so cooles mit web.py machen kann.
