---
layout: default
title: makoテンプレートエンジンの使用について
---

# makoテンプレートエンジンの使用について

### 問題点
webpyでMakoテンプレートエンジンを使用するにはどうすればいいですか？

### 解決手段

まず、[Mako](http://www.makotemplates.org/) と webpy(0.3)をインストールする必要があります。その後以下のコードを実行してみてください。

    # encoding: utf-8
    # ファイル code.py

    import web

    from web.contrib.template import render_mako

    urls = (
            '/(.*)', 'hello'
            )

    app = web.application(urls, globals(), autoreload=True)

    # input_encoding and output_encoding is important for unicode
    # template file.
    # Reference:
    # http://www.makotemplates.org/docs/documentation.html#unicode
    render = render_mako(
            directories=['templates'],
            input_encoding='utf-8',
            output_encoding='utf-8',
            )

    class hello:
        def GET(self, name):
            return render.hello(name=name)
            # Another way:
            #return render.hello(**locals())

    if __name__ == "__main__":
        app.run()

テンプレートファイル:

    ## ファイル: templates/hello.html

    您好：${name}

###ノート:

webpyアプリケーションを Apache + mod_wsgi で稼動させた場合、テンプレート(Mako)のエラーは Apacheのエラーログに出力されます。

    [Sat Jun 21 21:56:22 2008] [error] [client 192.168.122.1] TopLevelLookupException: Cant locate template for uri 'index.html'

テンプレートディレクトリが相対パスで指定できないもしくはわからない場合は、絶対パスで指定してください。

アプリケーションの作業ディレクトリについてはこちらを参照してください。

    http://code.google.com/p/modwsgi/wiki/ApplicationIssues

たとえば以下のような書き方で、絶対パスをより簡単にする書くことができます。

    import os

    render = render_mako(
            directories=[os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),],
            input_encoding='utf-8',
            output_encoding='utf-8',
            )