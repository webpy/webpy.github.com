---
layout: default
title: faq
---

# faq

99. **template.pyを使いたいのですがどうすれば良いですか?**

    基本的なドキュメントやサンプルコードについては [template.py ドキュメント](/templetor) を参照してください。

    web.py app内部からテンプレートファイル (homepage.tmpl) を使用して表示するには以下のように記述します。

          # Version 0.2x
          homepage = template.Template(open("homepage.tmpl").read())
          print homepage()

          # web.py 0.3
          homepage = web.template.Template(open("homepage.tmpl").read())
          return homepage()

    
99. **なぜ urls は単に1つの長いリストなのですか?**

    もし辞書なら使用されないし、それがタプルであってもタイピング数が多いからです。

99. **どのようにして、静的ファイル JavaScriptsや画像(PNGやJPEG)をweb.pyサーバに配置すればいいですか?**

    web.pyサーバを実行するスクリプトファイル(チュートリアルでは code.py を指す)のディレクトリに、新しく静的ファイル用のディレクトリ static を作成してください。 
    次に、作成したディレクトリに静的ファイル logo.png を配置してください。

    たとえば、画像のURLが http://localhost:8080/static/logo.png ならば ./static/logo.png がクライアントに送られます。 

99. **どこで私は、補足支援できますか?**

    Googleグループに [web.py group](http://groups.google.com/group/webpy)があるので、そちらでお願いします。

99. **デフォルトのページがない場合 "not found"と表示されますが、どのようにしてそれを変更できますか?**


    web.webapi.notfound を変更することで独自のページを作成することができます。

            # 0.2x
            def my_notfound(): 
                print "MY OWN NOT FOUND" 
            web.webapi.notfound = my_notfound 

            # 0.3
            -

99. **webpyをロードした後、どうすれば自動補完できますか?**

    IPythonでは、webpyをインポートします。
    自動補完が動作しない場合は、'python' の自動補完を試してみてください。( readline ):

            import readline, rlcompleter; readline.parse_and_bind("tab: complete")

    タブで補完されます。

    'Python' を実行した時、デフォルトで何か処理を行いたい場合は、'~/.pythonstartup.py' ファイルに記述します。そのファイルに前述した import文を記述し、環境変数に 'PYTHONSTARTUP' を追加します。

    私はbashで以下のようにしています。~/.bashrcを編集し、以下の行を足します。

            export PYTHONSTARTUP=~/.pythonstartup.py

99. **データベースにアクセスできません、どうしてですか?**

    Web-servingスレッド以外のスレッドからデータベースにアクセスする場合（例えば、新しいスレッドを作ったとか、Webページのserveを開始しなかった場合とか）には、`web.load()`を実行する必要があります。web.py 0.3では修正される予定です。ごめんなさい。

99. **IterBetterは複数回イテレートできますか？**

    できません。`ib = list(ib)`でIterBetterをリストに変換してください。

99. **どのようにデバッグ文をコンソールに出力しますか？**

    web.debug("デバッグ文")

99. **もしwebpyの不具合(バグ)を見つけた場合どこで報告すればいいのですか？**

    [ここ(webpy launchpad site)](https://launchpad.net/webpy) からバグ報告することができます。ログインが必要な場合は登録を行ってからバグ報告をしてください。