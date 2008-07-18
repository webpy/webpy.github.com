---
layout: default
title: Cheetahテンプレートエンジンの使用について
---

# Cheetahテンプレートエンジンの使用について

### 問題点
webpyでCheetahテンプレートエンジンを使用するにはどうすればいいですか？

### 解決手段

まず、[Cheetah](http://www.cheetahtemplate.org/) と webpy(0.3)をインストールする必要があります。その後以下のコードを実行してみてください。

    # encoding: utf-8
    # ファイル: code.py

    import web
    from web.contrib.template import render_cheetah

    render = render_cheetah('templates/')

    urls = (
        '/(first)', 'first',
        '/(second)', 'second'
        )

    app = web.application(urls, globals(), web.reloader)

    class first:
        def GET(self, name):
            # cheetah template takes only keyword arguments,
            # you should call it as:
            #   return render.hello(name=name)
            # Below is incorrect:
            #   return render.hello(name)
            return render.first(name=name)

    class second:
        def GET(self, name):
            return render.first(**locals())

    if __name__ == "__main__":
        app.run()

テンプレートファイル:

    ## ファイル: templates/first.html

    hello, $name.