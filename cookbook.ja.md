---
layout: default
title: 
---

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
* [staticファイルについて](/staticfiles)
* [Seeother(HTTP/1.1 コード : 303)とRedirect](/redirect+seeother)
* サブアプリケーションの使い方について
* [Serving XML](/cookbok/xmlfiles)

##Advanced
* [web.ctx](/ctx)
* loadhooks/unloadhooks (requested)
* How to properly use web.background (requested)

##Sessions and user state:
* [Session機能](/sessions)
* [Cookies機能](/cookies)
* ユーザ認証 (requested)

##Utils:
* [メール送信](/sendmail)

##Templates:
* [Using Site Layout Templates](/layout_template)
* [Alternating Style](/alternating_style)

##User Input:
* [ファイルアップロード](/fileupload)
* [web.inputからユーザ入力情報へのアクセス](/input)
* 基本的なフォームの使用 (requested)

##Database:
* [複数データベース](/multidbs)
* [Select: データ照会](/select)
* [Update: データ更新](/update)
* Delete (requested)
* [Insert: データ追加](/Insert) 
* [Query: 問い合わせ(SQL文の発行)](/query)
* [トランザクションの使用](/cookbook/transactions)

##Deployment:
* [lighttpd + Fastcgiの配置](/fastcgi-lighttpd)
* Apache + Fastcgiの配置 (requested)
* [Apache + CGIの配置](/cgi-apache)
* Apache +mod_pythonの配置 (requested)
* nginx(ロードバランサ)の配置 (requested)

##Subdomains:
* サブドメインおよびユーザー名を使用してにアクセスする方法 (requested)


