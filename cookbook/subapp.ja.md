---
layout: default
title: サブアプリケーションの使い方について(別ファイルのインクルード)
---

# サブアプリケーションの使い方について(別ファイルのインクルード)

## 問題点

別ファイルのWebアプリケーション(ここではblog.py)をインクルードするにはどうすればいいですか？


## 解決手段

In `blog.py`:

    urls = (
      "", "reblog,
      "/(.*)", "blog"
    )

    class reblog:
        def GET(self): raise web.seeother('/')

    class blog:
        def GET(self, path):
            return "blog " + path

    app_blog = web.application(urls, locals())

メインファイル `code.py`:

    import blog
    urls = (
      "/blog", blog.app_blog,
      "/(.*)", "index"
    )
    
    class index:
        def GET(self, path):
            return "hello " + path
    
    app = web.application(urls, locals())