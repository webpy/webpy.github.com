---
layout: default
title: tutorial2.es
---

# tutorial2.es

## Tutorial de web.py 0.2
Esta es la versión en español del tutorial en [Inglés](http://webpy.infogami.com/tutorial2.en) de web.py v 0.2, que se encuentra en este mismo sitio. El trabajo de traducción está en desarrollo. Todo aquel que desee colaborar sólo debe crear su cuenta.

## Iniciando.

Si usted conoce Python y quiere hacer un sitio web, web.py le provee con el código para hacerlo fácilmente.

Si quiere seguir todo el tutorial, necesitará tener instalado Python, web.py, flup, psycopg2 y Postgres (o una base de datos equivalente y el driver de Python correspondiente). Para más detalles, consulte [webpy.org](http://www.webpy.org).

Si usted ya tiene funcionando un proyecto con otra versión de web.py, dele un vistazo a la información sobre migración en la [página](http://webpy.infogami.com/upgrade_to_point2) de actualización.

Ya podemos comenzar.

## Manejo de URLs

La parte más importante de cualquier sitio web es la estructura de sus [URLs](http://es.wikipedia.org/wiki/URL). Las URLs de su sitio web no son simplemente "cosas" que los visitantes al web miran y envían por correo electrónico a sus amigos, sino que también proveen un modelo mental de como su sitio web funciona. En sitios populares (en inglés), tales como [del.icio.us](http://del.icio.us/), las URLs son inclusive parte del interfaz con el usuario. web.py facilita definir buenos URLs.

Para comenzar una aplicación con web.py, abra un nuevo archivo de texto (vamos a llamarlo 'code.py') y escriba:

    import web

Esto importa el modulo web.py.

A continuación, deberá decirle a web.py cual será la estructura de URLs. Se puede comenzar con algo sencillo como:

    urls = (
      '/', 'index'    )

La primera partes es una [expresión regular](http://osteele.com/tools/rework/) que coincide con una URL, como `/`, `/help/faq`, `/item/(\d+)`, etc. (El `\d+` coincide con una secuencia de dígitos). La segunda parte es el nombre de la clase que será llamada cuando el URL de una página coincida con al expresión regular.

Esta linea dice que queremos que el URL `/` (ej: la página principal) debe ser manejada por la clase llamada `index`.

Por lo tanto, todo lo que se require es escribir la clase `index`. Aunque la mayoría de las personas no lo saben, su navegador web, utiliza un lenguaje conocido como HTTP para comunicarse con la World Wide Web. Los detalles no son relevantes, pero la idea básica es que los visitantes de su sitio web le solicitan al servidor de web que realice una función especifica (como `GET` o `POST`) con las URLs (como en `/` o `/foo?f=1`).


`GET` es el que nos resulta familiar a todos, es el que se usa para pedir el texto de una página web. Cuando escribe `harvard.edu` en su navegador web, éste le pide literarmente al servidor web de Harvard que `GET /`. El segundo más famoso, `POST`, se usa a menudo para enviar ciertos tipos de formularios, como una petición de compra de algún artículo. Usted usa `POST` siempre que el acto de enviar un formulario _hace algo_ (como utilizar su tarjeta de crédito y procesar un recibo). Esta es la clave, porque las `GET` URLs pueden circular y se indexadas por los motores de búsqueda, lo que realmente quieres para la mayoría de tus páginas pero, definitivamente, _no quieres_ que procesen recibos (¡imagina que Google intentase comprar todo lo que hay en tu sitio web!).

En el código de nuestro web.py, distinguiremos las dos claramente:

    class index:
        def GET(self):
            print "Hello, world!"
Esta función `GET` será llamada por web.py siempre que alguien realice una petición `GET` de `/`.

Bien, ahora sólo tenemos que acabar con una linea final que le diga a web.py que empiece a servir páginas web:

    if __name__ == "__main__": web.run(urls, globals())

Esto le dice a web.py que sirva las URLs que listamos arriba, buscando las clases en el espacio de nombres global de este archivo.

Ahora fíjese en que, aunque hemos hablado un montón, sólo hemos escrito unas cinco lineas de código. Es todo lo que necesitas para construir una aplicación web.py completa. Si abre su linea de comandos y escribe:

    $ python code.py
    Launching server: http://0.0.0.0:8080/

Ahora su aplicación web.py está ejecutando un servidor web real en su ordenador. Si visita esa URL debería ver "Hello, world!" (Puede añadir una dirección IP y un puerto después de las lineas de "code.py" para controlar dónde lanza web.py el servidor. También puede indicarle que ejecute un servidor `fastcgi` o `scgi`.)

## Desarrollo

web.py also has a few tools to help us with debugging. Before the 'if __name__' on last line, add:

    web.webapi.internalerror = web.debugerror

This will give you more helpful error messages. And on the last line add `web.reloader` so that it reads:

    if __name__ == "__main__": web.run(urls, globals(), web.reloader)

    
This tells web.py to use the web.reloader "middleware" (middleware is a wrapper function to add some functionality to your web server) which reloads your files whenever you edit them, so that you can see the changes in your web browser right away. (For some serious changes, though, you'll still have to restart the server.) You'll probably want to take this out when you make your site public, but it's great while developing. There's also `web.profiler`, which outputs information about how much time each function took at the end of each web page, so that you can make your code faster.

## Uso de Plantillas.

Writing HTML from inside Python can get cumbersome; it's much more fun to write Python from inside HTML. Luckily, web.py makes that pretty easy.

**Note: web.py currently also supports [Cheetah templates](http://www.cheetahtemplate.org/).  Read the former [tutorial](http://webpy.org/tutorial) for more information.

Let's make a new directory for our templates (we'll call it `templates`). Inside, make a new file whose name ends with HTML (we'll call it `index.html`). Now, inside, you can just write normal HTML:

    <em>Hello</em>, world!

Or you can use web.py's templating language to add code to your HTML:

    $def with (name)
    
    $if name:
        I just wanted to say <em>hello</em> to $name.
    $else:
        <em>Hello</em>, world!

**Note: Currently, four spaces are required for indentation.**

As you can see, the templates look a lot like Python files except for the `def with` statement at the top (saying what the template gets called with) and the `$`s placed in front of any code.  Currently, template.py requires the $def statement to be the first line of the file.  Also, note that web.py automatically escapes any variables used here, so that if for some reason `name` is set to a value containing some HTML, it will get properly escaped and appear as plain text. If you want to turn this off, write `$:name` instead of `$name`.

Now go back to `code.py`. Under the first line, add:

    render = web.template.render('templates/')

This tells web.py to look for templates in your templates directory. Then change `index.GET` to:

    name = 'Bob'    print render.index(name)

Visit your site and it should say hello to Bob. 

**Development tip:** Add , `cache=False` to the end of your `render` call to have web.py reload your templates every time you visit the page.

Now change your URL line to:

    '/(.*)', 'index'
and change the definition of `index.GET` to:

    def GET(self, name):

and delete the line setting name. Visit `/` and it should say hello to the world. Visit `/Joe` and it should say hello to Joe.

If you wish to learn more about web.py templates, vist the [templetor page](/templetor).

## Base de Datos

Antes de la linea 'web.run' incluir:

    web.config.db_parameters = dict(dbn='postgres', user='username', pw='password', db='dbname')

(Cambie los valores --particularmente `username`, `password`, y `dbname` -- para que coincida con su configuración. Los usuarios de MySQL deberán cambiar 'dbn' a 'mysql'.)

Cree una tabla sencilla en su base de datos:

    CREATE TABLE todo (
      id serial primary key,
      title text,
      created timestamp default now(),
      done boolean default 'f'    );

E incluya un registro (fila):

    INSERT INTO todo (title) VALUES ('Learn web.py');

Vuelva al código `code.py`, modifique `index.GET` por:

    def GET(self):
        todos = web.select('todo')
        print render.index(todos)

and change back the URL handler to take just `/`.

Edit `index.html` so that it reads:

    $def with (todos)
    <ul>    $for todo in todos:
        <li id="t$todo.id">$todo.title</li>    </ul>
Visit your site again and you should see your one todo item: "Learn web.py". Congratulations! You've made a full application that reads from the database. Now let's let it write to the database as well.

At the end of `index.html`, add:

    <form method="post" action="add">    <p><input type="text" name="title" /> <input type="submit" value="Add" /></p>    </form>
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

`web.input` gives you access to any variables the user submitted through a form. `web.insert` inserts values into the database table `todo` and gives you back the ID of the new row. `seeother` redirects users to that ID.

Quickly: `web.transact()` starts a transaction. `web.commit()` commits it; `web.rollback()` rolls it back. `web.update` works just like `web.insert` except instead of returning the ID it takes it (or a string `WHERE` clause) after the table name.

`web.input`, `web.query`, and other functions in web.py return "Storage objects", which are just like dictionaries except you can do `d.foo` in addition to `d['foo']`. This really cleans up some code.

Usted puede encontrar todos los detalles sobre lo tratado en este tutorial y lo relacionado a las funciones de web.py en [la documentación](http://webpy.infogami.com/docs).

Con esto se termina este tutorial. Dele una lectura a la documentación, donde encontrará gran cantidad de material e información de lo que puede hacer con web.py