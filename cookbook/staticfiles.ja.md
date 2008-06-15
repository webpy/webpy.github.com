---
layout: default
title: 静的ファイルの配置について (Javascript、CSS、画像など)
---

# 静的ファイルの配置について (Javascript、CSS、画像など)

### 問題点
web.pyのサーバーに静的ファイルを配置したいのですが？

### 解決手段

web.pyサーバを実行するスクリプトファイル(チュートリアルでは <code>code.py</code> を指す)のディレクトリに、新しく静的ファイル用のディレクトリ <code>static</code> を作成してください。
次に、作成したディレクトリに静的ファイル <code>logo.png</code> を配置してください。

たとえば、画像のURLが <code>http://localhost:8080/static/logo.png</code> ならば <code>./static/logo.png</code> がクライアントに送られます。