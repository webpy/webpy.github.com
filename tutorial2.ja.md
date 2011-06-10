---
layout: default
title: web.py 0.2 チュートリアル
---

# web.py 0.2 チュートリアル

## はじめに

Python を使ってウェブサイトを作りたい。web.py は、これを簡単に実現するコードを提供するものだ。

チュートリアルにあることをすべて実行するには、Python、web.py、flup、psycopg2、PostgreSQL（または同等のデータベースと Python 用のドライバ）が必要だ。詳しくは [webpy.org](/) を参照のこと。

すでに web.py をインストールしてある場合は、[upgrade](/upgrade_to_point2) のページに移行の仕方について書いてあるので読んでほしい。

それでははじめよう。

## URL のハンドリング

どんなウェブサイトであっても、もっとも重要な部分となるのが URL の構造だ。URL は、訪問者がメールで知人にあなたのサイトのことを教えるときに使われるというばかりではない。君のサイトがどんなふうに動くのかというメンタルなモデルを表現するものでもあるのだ。[del.icio.us](http://del.icio.us/) などのポピュラーなサイトでは、URL はユーザーインターフェースの一部にさえなっている。web.py ならグレートな URL を簡単に構築できる。

web.py アプリケーションをはじめるにあたって、新しくテキストファイルを開いて（'code.py' と呼ぶことにする）次のようにタイプする。

    import web

これは web.py のモジュールをインポートしている。

それでは web.py にわれらがサイトの URL 構造を伝えることにする。まずはシンプルなところから。

    urls = (
        '/', 'index',
        '', 'index',
    )

最初の部分は URL にマッチする[正規表現](http://osteele.com/tools/rework/)で、`/`、`/help/faq`、`/item/(\d+)` などとすることができる。（`\d+` は数字の並びにマッチする。括弧でくくって、マッチした部分をあとで使えるように保存させている。）２番目のはリクエストが送られるクラスの名前で、`index`、`view`、`welcomes.hello` （これは `welcomes` モジュールの `hello` クラスを指している）、あるいは `get_\1` などとする。`\1` は、保存した正規表現の１番目のマッチ部分に置き換えられる。保存した残りのマッチ部分は関数を通して渡される。

上の例は、`/` という URL（つまりサイトのフロントページだ）は `index` というクラスで処理されると言っていることになる。

さて次に `index` クラスを書く。ほとんどの人は気にすることもなくブラウジングをしているけれども、ブラウザはワールド・ワイド・ウェブと交信するにあたって HTTP という言葉を用いている。細かいことは重要ではないが、基本的な概念としては、訪問者はウェブサーバに対して、（GET とか POST といった）ある function 〔機能／関数〕を URL （`/` とか `/foo?f=1`）について実行するよう問い合わせている。

GET はもうおなじみの代物だが、これはウェブページのテキストを要求するのに使われる。ブラウザに `harvard.edu` と打ち込むと、これは文字通りハーバードのウェブサーバに対して `GET /` と問い合わせることになる。つぎに有名なのが POST で、これは何かを登録するといったように、ある種のフォームを送信する時に使われる。（クレジットカードに課金して注文を行うといったような）リクエストを送信してなんらかの処理が行われる場合であればいつでも POST を使うことができる。ここがポイントなのだが、というのも、GET の URL は検索エンジンに巡回されてインデックス化されうるからで、これはいかにもほとんどのページについて望むところではあるが、一方で検索エンジンから注文を受けるようなことにはなってほしくないだろう（Google が自分のサイトの全商品を片っ端から買おうとしているところを想像してみればいい！）。

われらが web.py のコードではこのふたつは明確に区別される。

    class index:
        def GET(self):
            print "Hello, world!"

これで、web.py は `/` に対する GET リクエストに対していつでもこの `GET` 関数を呼び出すようになる。

さて、あとは仕上げに web.py がウェブページのサービスを始めるように最後の一行を書き足すだけだ。

    if __name__ == "__main__": web.run(urls, globals())

これは web.py に、はじめに書いた URL をサービスさせてクラス名をこのファイルのグローバルな名前空間で探し出せと伝えていることになる。

ここまでいろいろと述べてきたが、これまででコードは 5行ちょっとしか書いてないことに注目してほしい。ひとそろいのウェブアプリケーションを作るのに必要なのはこれですべてなのだ。コマンドラインから次のように打ち込んでみよう。

    $ python code.py
    Launching server: http://0.0.0.0:8080/

これで、君の web.py アプリケーションが君のコンピュータ上ででほんもののウェブサーバとして動く。この URL を訪問してみれば、"Hello, world!" と表示されるはずだ（"code.py" の部分に続けて IP アドレスとポート番号を指定して、web.py がどこでサーバを起動するかを指定できる。fastcgi や scgi サーバとして起動させることも可能だ）。

## 開発

web.py にはデバッグに役立つツールもいくつか用意されている。最終行の `'if __name__'` の前に、次の一行を足してみる。

    web.webapi.internalerror = web.debugerror

これでより役に立つエラーメッセージを見られるようになるだろう。また、最後の一行に `web.reloader` を付け足して次のようにする。

    if __name__ == "__main__": web.run(urls, globals(), web.reloader)

これは web.py に、`web.reloader` “ミドルウェア” を使うように伝えている（ミドルウェアというのはウェブサーバになんらかの機能を追加するためのラッパー関数だ）。これはファイルを編集したら即座にそれらを再読み込みして、変更箇所をすぐにブラウザ上で確認できるようにする。（もっとも、これを使っていても、大掛かりな変更を施した場合にはサーバを再起動させる必要があるけれども）。サイトを公開する時にはこの機能は外しておきたいと思うだろうが、開発段階ではとても役に立つ。`web.profiler` というのもあり、これは各ページの末尾に、各関数でどれだけ時間がかかったかについての情報を出力する。これを見ればコードのどこを改善すれば処理が速くなるかがわかるはずだ。

## テンプレート処理

Python のコード中に HTML のコードを書くのはやっかいなものだ。HTML のコード中に Python のコードを書ければずっと楽だろう。幸運なことに、web.py なら簡単にそれを実現できる。

ノート: web.py は現在のところ [Cheetah](http://www.cheetahtemplate.org/) テンプレートもサポートしている。詳しくは旧版のチュートリアルを参照のこと。

それではテンプレート用のディレクトリを作成しよう（`'templates'` とする）。この中に、名前が html で終わる新しいファイルを作成する（`'index.html'` としよう）。このファイルには普通の HTML を書けばよい。

    <em>Hello</em>, world!

web.py のテンプレート用言語を使って、HTML にコードを埋め込むこともできる。

    $def with (name)
    
    $if name:
        I just wanted to say <em>hello</em> to $name.
    $else:
        <em>Hello</em>, world!

ノート: 現時点では、インデントは 4つのスペースで行う必要がある。

見てわかるとおり、テンプレートは先頭の `def with` ステートメント（これはテンプレートが呼ばれる時に渡される引数を宣言している）と各行の先頭に `$` 記号が置かれていることを除けば、Python のコードによく似ている。今のところ、template.py では `$def` ステートメントがファイルの１行目になければならないことになっている。また、web.py はここで使われるすべての変数を自動的にエスケープ処理することにも注意しよう。これはつまり、もしなんらかの理由により name に HTML のコードを含む値がセットされた場合でも、それらは適切にエスケープ処理されて、プレーンなテキストとして表示されるということだ。この機能を無効にしたければ、`$name` のかわりに `$:name` と書く。 

さて `code.py` に戻ろう。１行目の下に次のように書き加える。

    render = web.template.render('templates/')

これは web.py に先ほど作った `templates` ディレクトリからテンプレートを探すよう伝えている。続いて `index.GET` を次のように変更する。

    name = 'Bob'
    print render.index(name)

（`'index'` はテンプレートの名前で、`'name'` はそれに渡される引数を表している。）

このサイトを訪問してみれば、Bob に挨拶しているページが表示されるはずだ。

開発豆知識: `render` を呼び出す時に `cache=False` と引数を加えると、web.py はページを表示するごとにテンプレートを再読み込みするようになる。

続いて URL 一覧の部分を次のようにしてみよう。

    '/(.*)', 'index'

そして `index.GET` の定義を次のようにする。

    def GET(self, name):

そして `name = 'Bob'` と決め打ちしていた行を削除する。こうすると、`/` を訪問すれば 'Hello, world!' を表示し、`/Joe` にアクセスすれば Joe に挨拶するようになる。

web.py のテンプレート処理についてもっと知りたければ、[template](/templetor) のページを参照のこと。

## データベース処理

ノート: データベースを使う前に、適切なデータベース用のライブラリがインストールされていることを確認すること。MySQL データベースには [MySQLdb](http://sourceforge.net/project/showfiles.php?group_id=22307)、PostgreSQL には [psycopg2](http://initd.org/pub/software/psycopg/) が必要だ。 

ソースコードの `web.run` がある行の前に、次のように書き加える。

    web.config.db_parameters = dict(dbn='postgres', user='username', pw='password', db='dbname')

（これらの値、とくに `username`、`password`、`dbname` の値は各自の環境に合わせて書き換えること。MySQL を使っているのであれば `dbn` の値も `'mysql'` にする。）

データベースに単純なテーブルを作成する。

    CREATE TABLE todo {
      id serial primary key,
      title text,
      created timestamp default now(),
      done boolean default 'f'
    };

そして最初のレコードを追加する。

    INSERT INTO todo (title) VALUES ('Learn web.py');

`code.py` に戻り、`index.GET` を次のように変更する。

    def GET(self):
        todos = web.select('todo')
        print render.index(todos)

そして URL ハンドラを `/` のみに戻す。

`index.html` は以下のようにする。

    $def with (todos)
    <ul>
    $for todo in todos:
        <li id="t$todo.id">$todo.title</li>
    </ul>

再びサイトにアクセスしてみると、"Learn web.py" という todo アイテムが表示されているはずだ。おめでとう！　データベースからデータを取得するウェブアプリケーションの一丁あがりだ。今度はデータベースへの書き込みもできるようにしてみよう。

{index.html` に、次のように書き加える。

    <form method="post" action="add">
    <p><input type="text" name="title" /> <input type="submit" value="Add" /></p>
    </form>

そして URL 一覧を次のようにする。

    '/', 'index',
    '/add', 'add'

（カンマの打ち忘れに注意すること。これを入れ忘れると、Python は 文字列を連結してしまうので、URL のリストではなく `'/index/addadd'` だと見なされてしまう！）

続いて新しいクラスを追加。

    class add:
        def POST(self):
            i = web.input()
            n = web.insert('todo', title=i.title)
            web.seeothrer('/')

（`POST` を使う理由はわかってるよね？）

ユーザーがフォームを通して送信した値には、`web.input` のようにしてアクセスできる。`web.insert` はデータベースの todo テーブルに値を挿入して、新しくできたレコードの ID を返す。`seeother` は指定した URL にユーザーをリダイレクトする。
[signals forex](http://signalsforex.org/)

駆け足で紹介: `web.transact()` でトランザクションを開始する。`web.commit()` でそれをコミットし、`web.rollback()` でロールバック。`web.update` は `web.insert` に似ているが、新しい ID を返すのではなく、テーブル名に続けて ID を引数に取ってそのレコードを更新する。 [Professional resumes](http://cvresumewritingservices.org/professional-resume.php)

`web.input` や `web.query`、またその他いくつかの web.py 関数は「ストレージオブジェクト」というものを返す。これは辞書オブジェクトに似ているが、`d['foo']` だけでなく `d.foo` のようにアクセスできるところが違っている。これのおかげで、コードがずいぶんすっきりしたものになるはずだ。
[ドキュメント](/docs)には、これまでに挙げてきたものに限らず、web.py のすべての関数についてその詳細が書かれている。
[http://forexrobot.eu.com](http://forexrobot.eu.com)
チュートリアルは以上だ。web.py でできるクールなことについてもっと知りたければドキュメントを見てほしい。