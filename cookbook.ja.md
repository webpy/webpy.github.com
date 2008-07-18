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
* [Seeother(HTTP/1.1 コード : 303)とRedirect](/redirect+seeother/ja)
* [サブアプリケーションの使い方について(別ファイルのインクルード)](/cookbook/subapp/ja)
* [Serving XML](/xmlfiles/ja)

##Advanced
* [web.ctx](/ctx/ja)
* loadhooks/unloadhooks (requested)
* [How to properly use web.background (requested)](/background/ja)

##Sessions and user state:
* [Session機能](/sessions/ja)
* [Cookies機能](/cookies/ja)
* ユーザ認証 (requested)

##Utils:
* [メール送信](/sendmail/ja)

##Templates:
* [Using Site Layout Templates](/layout_template/ja)
* [Alternating Style](/alternating_style/ja)
* [makoテンプレートエンジンの使用について](/template_mako/ja)
* [Cheetahテンプレートエンジンの使用について](/template_cheetah/ja)


##User Input:
* [ファイルアップロード](/fileupload/ja)
* [web.inputからユーザ入力情報へのアクセス](/input/ja)
* 基本的なフォームの使用 (requested)

##Database:
* [複数データベース](/multidbs/ja)
* [Select: データ照会](/select/ja)
* [Update: データ更新](/update/ja)
* Delete (requested)
* [Insert: データ追加](/insert/ja) 
* [Query: 問い合わせ(SQL文の発行)](/query/ja)
* [トランザクションの使用](/transactions/ja)
##Deployment:
* [lighttpd + Fastcgiの配置](/fastcgi-lighttpd/ja)
* Apache + Fastcgiの配置 (requested)
* [Apache + CGIの配置](/cgi-apache/ja)
* Apache +mod_pythonの配置 (requested)
* nginx(ロードバランサ)の配置 (requested)

##Subdomains:
* サブドメインおよびユーザー名を使用してにアクセスする方法 (requested)


