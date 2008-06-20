---
layout: default
title: Apach + CGIの配置
---

# Apach + CGIの配置

ここでは、web.pyアプリケーションを作成、実行するために必要となる簡単な手順を説明します。

* web.pyとflupsをインストールします。

* 下記のドキュメント通りにアプリケーションを作成します。

        if __name__ == "__main__":
            web.run(urls, globals())

この例では、`app.py`という名前で、`/www/app`の中に配置し、`http://serever/app/app.py`でアクセスできる必要があります。

* Apacheを設定します。(ここでは、バージョン2.2を例にします)

        ScriptAlias /app "/www/app/"
        <Directory "/www/app/">
                Options +ExecCGI +FollowSymLinks
                Order allow,deny
                Allow from all
        </Directory>

これで完了です。あなたのアプリケーションは`http://server/app/app.py`からアクセスができます。このアプリケーションで扱えるその他のURLは、例えば、
`http://server/app/app.py/myurl`のように、このURLの末尾に付け加えます。
