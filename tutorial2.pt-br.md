---
layout: default
title: tutorial do web.py 0.2
---

# tutorial do web.py 0.2

## Começando

Então você sabe Python e quer fazer um site. O web.py fornece o código que torna essa uma tarefa fácil.

Se você quiser fazer o tutorial inteiro, você precisará destes programas: Python, web.py, flup, psycopg2 e Postgres (ou um banco de dados equivalente e adaptador correspondente para Python). Para detalhes, veja [webpy.org](http://webpy.org/).

Se você já tem um projeto web.py, dê uma olhada na página de [atualização](http://webpy.infogami.com/upgrade_to_point2) (em inglês) para informações sobre migração.

Vamos começar.

## Tratamento de URLs

A parte mais importante de qualquer site é a estrutura de suas URLs. Suas URLs não são simplesmente aquela coisa que os visitantes vêem e mandam para seus amigos; elas também criam um modelo mental de como seu site funciona. Em sites populares como o [del.icio.us](http://del.icio.us/), as URLs são até uma parte da interface com o usuário. O web.py faz com que criar boas URLs seja fácil.

Para começar sua aplicação com web.py, abra um novo arquivo de texto (vamos chamá-lo de 'codigo.py') e digite:

    import web

Isso serve para importar o módulo do web.py.

Agora precisamos dizer ao web.py qual será nossa estrutura de URLs. Vamos começar com algo simples:

    urls = (
      '/', 'index'    )

A primeira parte é uma [expressão regular](http://osteele.com/tools/rework/) que corresponde a uma URL, como `/`, `/ajuda/faq`, `/item/(\d+)`, etc. (`\d+` corresponde a uma seqüência de dígitos. Os parênteses pedem que aquela parte da correspondência seja "capturada" para ser usada mais tarde.) A segunda parte é o nome de uma classe para a qual a requisição HTTP deve ser enviada, como `index`, `view`, `welcomes.hello` (este último corresponde à classe `hello` do módulo `welcomes`), ou `get_\1`. `\1` é substituído pela primeira captura feita pela sua expressão regular; as capturas que sobrarem são passadas para a sua função.

Essa linha diz que queremos que a URL `/` (i.é., a página inicial) seja tratada pela classe chamada `index`.

Agora precisamos escrever a classe `index`. Apesar de a maioria das pessoas não perceber enquanto navega por aí, seu navegador usa uma linguagem conhecida como HTTP para comunicar-se com a internet. Os detalhes não são importantes, mas o princípio básico é que os visitantes da Web pedem aos servidores web que realizem certas funções (como `GET` ou `POST`) em URLs (como `/` ou `/foo?f=1`). 

`GET` é a função com a qual estamos todos acostumados: é a usada para pedir o texto de uma página da web. Quando você digita `harvard.edu` no seu navegador, ele literalmente pede ao servidor web de Harvard `GET /`.  A segunda mais famosa, `POST`, é comumente usada ao enviar certos tipos de formulários, como um pedido para comprar algo. Você usar `POST` sempre que o envio de um pedido _faz alguma coisa_ (como cobrar de seu cartão de crédito e processar um pedido). Isso é crucial, pois URLs do tipo `GET` podem ser transmitidas por aí e indexadas por mecanismos de busca -- você quer isso para a maioria das suas página, mas com certeza _não_ para coisas como processar pedidos (imagine se o Google tentasse comprar tudo no seu site!).

No nosso código para o web.py, a distinção entre os dois é clara:

    class index:
        def GET(self):
            print "Olá, mundo!"
Essa função `GET` será chamada pelo web.py sempre que alguém fizer um pedido `GET` para a URL `/`.

Ok, agora só falta terminar com uma linha que manda o web.py começar a servir as páginas da web:

    if __name__ == "__main__": web.run(urls, globals())

Isso manda o web.py servir as URLs que listamos acima, procurando as classes no nome de espaços global para o arquivo atual.

Perceba que, embora eu esteja falando bastante, nós só temos umas cinco linhas de código. É só isso que você precisa para fazer uma aplicação completa com o web.py. Se você for até sua linha de comando e digitar:

    $ python codigo.py
    Launching server: http://0.0.0.0:8080/

Você terá sua aplicação web.py executando um servidor web de verdade no seu computador. Visite essa URL e você deverá ver "Olá, mundo!" (Você pode adicionar um endereço IP/porta depois de "codigo.py" para controlar onde o web.py executa o servidor. Você também pode fazê-lo rodar um servidor `fastcgi` ou `scgi`.)

**Nota:** Você pode especificar o número de porta a usar pela linha de comando desta maneira, se não puder ou não quiser usar o padrão:

    $ python codigo.py 1234

## Desenvolvimento

O web.py também tem algumas ferramentas para nos ajudar com a depuração. Antes do 'if __name__' na última linha, adicione:

    web.webapi.internalerror = web.debugerror

Isso lhe fornecerá mensagens de erro mais úteis, quando for o caso. Coloque também na última linha `web.reloader`, de modo que ela se torne:

    if __name__ == "__main__": web.run(urls, globals(), web.reloader)
    
Isso diz ao web.py que use o "middleware" web.reloader (middleware é uma função intermediária que adiciona certos recursos ao seu servidor web), que recarrega seus arquivos assim que você os edita, de modo que você pode imediatamente ver as alterações no seu navegador. (Contudo, para algumas alterações mais drásticas, você ainda precisará reiniciar o servidor.) Você provavelmente deverá tirar isso ao deixar seu site público, mas é um recurso excelente durante o desenvolvimento. Também há o `web.profiler`, que, no final de cada página, fornece informações sobre quanto tempo cada função tomou, de modo que você possa tornar seu código mais rápido.

## Templating

Writing HTML from inside Python can get cumbersome; it's much more fun to write Python from inside HTML. Luckily, web.py makes that pretty easy.

**Note:** Old versions of web.py used [Cheetah templates](http://www.cheetahtemplate.org/). You are, of course, welcome to use that or any other software with web.py, but it is no longer officially supported.

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

    name = 'Bob'    
    print render.index(name)

('index' is the name of the template and 'name' is the argument passed to it)

Visit your site and it should say hello to Bob. 

**Development tip:** Add , `cache=False` to the end of your `render` call to have web.py reload your templates every time you visit the page.

Now change your URL line to:

    '/(.*)', 'index'
and change the definition of `index.GET` to:

    def GET(self, name):

and delete the line setting name. Visit `/` and it should say hello to the world. Visit `/Joe` and it should say hello to Joe.

If you wish to learn more about web.py templates, vist the [templetor page](/templetor).

## Databasing

Note: Before you can start using a database, make sure you have the appropriate database library installed.  For MySQL databases, use [MySQLdb](http://sourceforge.net/project/showfiles.php?group_id=22307) and for Postgre use [psycopg2](http://initd.org/pub/software/psycopg/).

Above your `web.run` line add:

    web.config.db_parameters = dict(dbn='postgres', user='username', pw='password', db='dbname')

(Adjust these -- especially `username`, `password`, and `dbname` -- for your setup. MySQL users will also want to change `dbn` to `mysql`.)

Create a simple table in your database:

    CREATE TABLE todo (
      id serial primary key,
      title text,
      created timestamp default now(),
      done boolean default 'f'    );

And an initial row:

    INSERT INTO todo (title) VALUES ('Learn web.py');

Back in `code.py`, change `index.GET` to:

    def GET(self):
        todos = web.select('todo')
        print render.index(todos)

and change back the URL handler to take just `/`.

Edit `index.html` so that it reads:

    $def with (todos)
    <ul>
    $for todo in todos:
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

`web.input` gives you access to any variables the user submitted through a form. In order to access dat from multiple identically named items in a list format (e.g.: a series of checkboxes all with the attribute name="name") use:

    post_data=web.input(name=[])

`web.insert` inserts values into the database table `todo` and gives you back the ID of the new row. `seeother` redirects users to that ID.

Quickly: `web.transact()` starts a transaction. `web.commit()` commits it; `web.rollback()` rolls it back. `web.update` works just like `web.insert` except instead of returning the ID it takes it (or a string `WHERE` clause) after the table name.

`web.input`, `web.query`, and other functions in web.py return "Storage objects", which are just like dictionaries except you can do `d.foo` in addition to `d['foo']`. This really cleans up some code.

You can find the full details on these and all the web.py functions in [the documentation](http://new.webpy.org/docs).

This ends the tutorial for now. Take a look at the documentation for lots more cool stuff you can do with web.py.