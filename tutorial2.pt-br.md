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

Escrever HTML de dentro do Python pode tornar-se um empecilho; é muito mais divertido escrever código Python de dentro do HTML. Por sorte, o web.py torna isso bastante fácil.

**Nota:** Versões antigas do web.py usavam [Cheetah templates](http://www.cheetahtemplate.org/). Você é, é claro, livre para usar esse ou qualquer outro software com o web.py, mas ele não é mais suportado oficialmente.

Vamos criar um novo diretório para nossos templates (vamos chamá-lo de `templates`). Dentro dele, crie um novo arquivo cujo nome termine em HTML (vamos chamá-lo de `index.html`). Agora, dentro dele, você pode escrever código HTML normal:

    <em>Olá</em>, mundo!

Ou você pode usar a linguagem de templates do web.py para adicionar código ao seu HTML:

    $def with (nome)
    
    $if nome:
        Eu só queria dizer <em>olá</em> para $nome.
    $else:
        <em>Olá</em>, mundo!

**Nota: Atualmente, é necessário usar quatro espaços para a indentação.**

Como você pode ver, os templates parecem-se bastante com arquivos Python, exceto pela instrução `def with` no começo (ela diz com que parâmetros o template é chamado) e os `$`s colocados na frente de qualquer código.  Atualmente, o template.py requer que a instrução $def seja a primeira linha do arquivo.  Além disso, note que o web.py "escapa" as variáveis que forem usadas -- de modo que se, por alguma razão, o valor da variável `nome` conntém algum código HTML, ela será devidamente "escapada" e aparecerá como texto puro. Se você não deseja esse comportamento, use `$:nome` em vez de `$nome`.

Agora volte ao `codigo.py`. Abaixo da primeira linha, insira:

    render = web.template.render('templates/')

Isso manda o web.py procurar por templates no seu diretório `templates`. Então altere a função `index.GET` para:

    nome = 'João'
    print render.index(nome)

('index' é o nome do template, e 'nome' é o parâmetro passado para ele)

Visite seu site e ele deverá dizer olá para o João.

**Dica para o desenvolvimento:** Adicione `cache=False` ao final da sua chamada a `render` para que o web.py recarregue seus templates toda vez que você entrar na sua página.

Agora mude sua URL para:

    '/(.*)', 'index'
e troque a definição de `index.GET` para:

    def GET(self, nome):

e apague a linha que define `nome`. Visite `/` e a página deverá dizer olá ao mundo. Visite `/José` e ela deverá dizer olá ao José.

Se você quer aprender mais sobre os templates do web.py, visite a página do [templetor](/templetor) (em inglês).

## Bancos de dados

Nota: Antes de poder começar a usar um banco de dados, certifique-se de que tem a biblioteca correspondente instalada. Para bancos de dados MySQL, use [MySQLdb](http://sourceforge.net/project/showfiles.php?group_id=22307); para o Postgres, use o [psycopg2](http://initd.org/pub/software/psycopg/).

Acima da sua linha `web.run`, adicione:

    web.config.db_parameters = dict(dbn='postgres', user='nome_do_usuario', pw='senha', db='nome_do_banco_de_dados')

(Modifique isto -- especialmente `nome_do_usuario`, `senha`, and `nome_do_banco_de_dados` -- para os valores correspondentes à sua configuração. Usuários do MySQL também devem trocar `dbn` por `mysql`.)

Crie uma tabela simples no seu banco de dados:

    CREATE TABLE todo (
      id serial primary key,
      title text,
      created timestamp default now(),
      done boolean default 'f'    );

E uma linha inicial:

    INSERT INTO todo (title) VALUES ('Aprender web.py');

Voltando ao `codigo.py`, modifique a função `index.GET` para:

    def GET(self):
        todos = web.select('todo')
        print render.index(todos)

e modifique o tratador de URLs de volta para simplesmente `/`.

Edite o `index.html` de modo que ele se torne:

    $def with (todos)
    <ul>
    $for todo in todos:
        <li id="t$todo.id">$todo.title</li>    </ul>
Visite novamente seu site, e você deverá ver uma tarefa na lista: "Aprender web.py". Parabéns! Você fez uma aplicação completa que lê dados de um banco de dados. Agora vamos também gravar dados no banco de dados.

No final de `index.html`, insira:

    <form method="post" action="add">    <p><input type="text" name="title" /> <input type="submit" value="Adicionar" /></p>    </form>
E modifique sua lista de URLs para que fique assim:

    '/', 'index',
    '/add', 'add'
(Você deve ser muito cuidadoso com essas vírgulas.  Se você as omitir, o Python juntará as strings e verá `'/index/addadd'` no lugar da sua lista de URLs!)

Agora adicione outra classe:

    class add:
        def POST(self):
            i = web.input()
            n = web.insert('todo', title=i.title)
    	    web.seeother('/')

(Viu como estamos usando o método `POST` para isso?)

`web.input` lhe dá acesso às variáveis que o usuário enviou através de um formulário.  Para obter dados de elementos com nomes idênticos em formato de lista (por exemplo, uma série de caixas de verificação com o atributo name="nome"), use:

    post_data=web.input(nome=[])

`web.insert` insere valores na tabela `todo` do banco de dados e lhe devolve o ID da nova linha. `seeother` redireciona os usuários para esse ID.

Rapidinhas: `web.transact()` inicia uma transação. `web.commit()` confirma a transação e armazena os dados; `web.rollback()` desfaz as alterações. `web.update` funciona como `web.insert`, recebendo (em vez de devolver) um ID (ou uma string com uma sentença `WHERE`) após o nome da tabela.

`web.input`, `web.query` e outras funções do web.py devolvem "Objetos de armazenamento", que são como dicionários mas também permitem que você use `d.foo` além de `d['foo']`. Isso realmente deixa certos códigos mais limpos.

Você pode encontrar todos os detalhes sobre essas e todas as outras funções do web.py na [documentação](http://new.webpy.org/docs) (em inglês).

Isso termina o tutorial por enquanto. Dê uma olhada na documentação para ver o monte de coisas legais que você pode fazer com o web.py.