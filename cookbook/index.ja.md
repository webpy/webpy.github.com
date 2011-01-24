---
layout: default
title: クックブック
---

# クックブック

web.py 0.3 ベースのCookbookスタイルのドキュメントです。
古いバージョンでは利用可能ではない説明があります。
現在、バージョン 0.3 は開発版です。

#形式

1. 形式に関しては、Cookbookのような形式を使用するようにしてください。以下のような形式です。
    
    ###問題点: データベースにアクセスしたいのですが。
     
    ###解決手段: このコードを使ってください。

1. URLには"web"をつけないようにしてください。もし"/cookbook/select"ならば、"/cookbook/web.select"のようにしないでください。

1. 最後に、このドキュメンテーションはバージョン 0.3向けですので、あなたの知っている新バージョン用のコードを加えてください。

-------------------------------------------------

##Basics:
* [Hello World](/helloworld/ja)
* [staticファイル(js、css、画像など)について](/staticfiles/ja)
* [Seeother(HTTP/1.1 コード : 303)とRedirect](/redirect+seeother)
* [サブアプリケーションの使い方について(別ファイルのインクルード)](/subapp/ja)
* [Serving XML](/xmlfiles)

##Advanced
* [web.ctx](/ctx)
* [Application processors, loadhooks and unloadhooks](/application_processors)
* [How to use web.background](/background)
* [Custom NotFound message](/custom_notfound)

##Sessions and user state:
* [Session機能](/sessions)
* [Using session with reloader](/session_with_reloader)
* [Cookies機能](/cookies)
* ユーザ認証 (requested)

##Utils:
* [メール送信](/sendmail)
* [GMailへのメール送信](/sendmail_using_gmail)

##Templates:
* [Using Site Layout Templates](/layout_template)
* [Alternating Style](/alternating_style)
* [makoテンプレートエンジンの使用について](/template_mako/ja)
* [Cheetahテンプレートエンジンの使用について](/template_cheetah/ja)

##User Input:
* [ファイルアップロード](/fileupload)
* [リクエストデータ(web.inputを利用)へのアクセス](/input)
* Using basic forms (requested)

##Database:
* [複数データベース](/multidbs)
* [Select: データ検索(SELECT文)](/select)
* [Update: データ更新(UPDATE文)](/update)
* [Delete: データ削除(DELETE文)](/delete)
* [Insert: データ追加(INSERT文)](/Insert) 
* [問い合わせ(SQL文の発行)](/query)
* [トランザクションの使用](transactions)

##Deployment:
* [Lighttpd + Fastcgiの配置](/fastcgi-lighttpd)
* [Apache + Fastcgiの配置](/fastcgi-apache) 
* [Apache + CGIの配置](/cgi-apache/ja)
* mod_python deployment through Apache (requested)
* [mod_wsgi deployment through Apache](/mod_wsgi-apache )
* [mod_wsgi deployment through Nginx](/mod_wsgi-nginx )
* nginx deployment (requested)




##Subdomains:
* サブドメインおよびユーザー名を使用してにアクセスする方法 (requested)