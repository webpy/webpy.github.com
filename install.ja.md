---
layout: default
title: インストールガイド
---

# インストールガイド

web.pyをダウンロードします。
    
    http://webpy.org/static/web.py-0.33.tar.gz

ダウンロードファイルを展開し、あなたのアプリケーションがあるディレクトリに展開したフォルダ`webpy`の直下にある `web` フォルダをコピーしてください。
もしくは以下のコマンドを実行し、すべてのアプリケーションからのアクセスを可能にします。
    
    python setup.py install

ノート: Ubuntuなどrootを許可していない unix/linux などでは以下のコマンドで実行する必要があるかもしれません。

    sudo python setup.py install

[推奨セットアップ](/recommended_setup)を参照してください。

[Easy Install](http://peak.telecommunity.com/DevCenter/EasyInstall)を使えばワンステップでインストールすることが可能です。


    easy_install web.py

## 開発

webpy には内蔵のウェブサーバが付属されています。
まず、[チュートリアル](http://webpy.org/tutorial2)にしたがってアプリケーションを学んでください。
チュートリアルで作成したソースコードを`code.py`と名前をつけたファイルに保存してください。以下のコマンドを実行することで、ウェブサーバーが起動します。

     python code.py

ブラウザを起動し、 [http://localhost:8080/](http://localhost:8080/) のページを開いてください。別のポートを指定するには `python code.py 1234` のようにします。

## 本番(公開)稼動

開発時やサンプルプログラムを実行するだけなら内蔵のウェブサーバでかまいませんが、
外部へ公開するには力不足です。本番稼動に向けたWebサーバー構築の方法を示します。

web.py は[WSGI](http://www.python.org/dev/peps/pep-0333/)を実装していますので、互換性のあるもので実行することが可能です。

WSGIとは、ウェブサーバとアプリケーション(JavaのServletインターフェースと非常に似ています)の間で共通のAPIです。
CGI/FastCGI/SCGIを備えたweb.pyを実行するためには、[flup](http://trac.saddi.com/flup)([ここからダウンロード](http://www.saddi.com/software/flup/dist/))をインストールする必要があります。インストールすることで、web.pyにWSGIインターフェースのAPIを提供することができます。

CGI実行を行う場合はファイル`code.py`の先頭に以下を追記してください。

    #!/usr/bin/env python

また、ファイルに実行権限を付加してください。 `chmod +x code.py`

### LightTPD

#### .. with FastCGI

web.pyでは、lighttpd + FastCGI方式が推奨されています。[reddit.com][3] はこの方式で何百万ものアクセスに応答しています。

   [3]: http://reddit.com/

lighttpdの設定は以下のようになります。
    
     server.modules = ("mod_fastcgi", "mod_rewrite")
     server.document-root = "/path/to/root/"     
     fastcgi.server = ( "/code.py" =>     
     (( "socket" => "/tmp/fastcgi.socket",
        "bin-path" => "/path/to/root/code.py",
        "max-procs" => 1
     ))
     )
    
     url.rewrite-once = (
       "^/favicon.ico$" => "/static/favicon.ico",
       "^/static/(.*)$" => "/static/$1",
       "^/(.*)$" => "/code.py/$1"
     )
    
lighttpdのいくつかのバージョンでは、fastcgi.serverの"check-local"の値が"false"に設定しておく必要があります。特に配置したcode.pyがドキュメントルート外に配している場合が特に注意が必要です。

もし、flupがインストールがインストールできない場合は、"easy_install flup" を実行することでインストールすることができるかもしれません。

Since revision 145, it is necessary to set a bin-environment variable on the fastcgi configuration if your code uses redirects.  If when your code redirects to http://domain.com/ and in the url bar you see http://domain.com/code.py/, you'll need to set the environment variable.  This will cause your fastcgi.server configuration above to look something like this:
     
    fastcgi.server = ( "/code.py" =>
    ((
       "socket" => "/tmp/fastcgi.socket",
       "bin-path" => "/path/to/root/code.py",
       "max-procs" => 1,
       "bin-environment" => (
         "REAL_SCRIPT_NAME" => ""
       ),
       "check-local" => "disable"
    ))
    )
    

### Apache

#### .. with CGI

`httpd.conf`もしくは`apache2.conf`に以下を追記してください。

    Alias /foo/static/ /path/to/static
    ScriptAlias /foo/ /path/to/code.py


#### .. with CGI using .htaccess

CGIは以下を`.htaccess`に追記するだけですので構築するのは簡単ですが、高性能なウェブサイトには向いていません。

    Options +ExecCGI
    AddHandler cgi-script .py

and point your browser to `http://example.com/code.py/`. Don't forget the trailing slash, otherwise you'll see a `not found` message (because the `urls` list you defined do not match anything). To make things work without having to enter `code.py`, enable mod_rewrite rules (see below).

Note: The way `web.py` is implemented breaks the `cgitb` module because it captures `stdout`. I worked around the issue by using this:
    
    import cgitb; cgitb.enable()
    import sys
    
    # ... import web etc here...
    
    def cgidebugerror():
        """                                                                         
        """        _wrappedstdout = sys.stdout
    
        sys.stdout = web._oldstdout
        cgitb.handler()
    
        sys.stdout = _wrappedstdout
    
    web.internalerror = cgidebugerror

#### .. with FastCGI

FastCGIを構築するのは簡単で、mod_pythonと同じ動作をします。

`.htaccessに以下を追記してください。`
    
    <Files code.py>      SetHandler fastcgi-script
    </Files>

残念ですが、lighttpdと異なり、apacheでは、明示的にFastCGIであることをweb.pyに教えなければなりません。`code.py`の`if __name__ == "__main__":`の後に以下を追記する必要があります。
    
    web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    
and point your browser to `http://example.com/code.py/`. Don't forget the trailing slash, otherwise you'll see a `not found` message (because the `urls` list you defined do not match anything). To make things work without having to enter `code.py`, enable mod_rewrite rules (see below).

[Walterからの追加のアドバイスはこちら](http://lemurware.blogspot.com/2006/05/webpy-apache-configuration-and-you.html).


#### .. with SCGI
https://www.mems-exchange.org/software/scgi/
download `mod_scgi` source here: http://www.mems-exchange.org/software/files/mod_scgi/
windows apache user: 
edit your httpd.conf:

    LoadModule scgi_module Modules/mod_scgi.so
    SCGIMount / 127.0.0.1:8080

apacheの再起動とcode.pyを以下のコマンドで起動してください。

    python code.py 127.0.0.1:8080 scgi

起動後、ブラウザで 127.0.0.1を開いて確認してください。

#### .. with mod_python

mod_pythonは、FastCGIと同様に動作しますが、構築するのは簡単ではありません。

Python 2.5を使用している場合:

    cd /usr/lib/python2.5/wsgiref
    # or in windows: cd /python2.5/lib/wsgiref
    wget -O modpython_gateway.py http://projects.amor.org/misc/browser/modpython_gateway.py?format=raw
    # or fetch the file from that address using your browser

Python 2.5以前のバージョンを使用している場合:

    cd /usr/lib/python2.4/site-packages
    # or in windows: cd /python2.4/lib/site-packages
    svn co svn://svn.eby-sarna.com/svnroot/wsgiref/wsgiref
    cd wsgiref
    wget -O modpython_gateway.py http://projects.amor.org/misc/browser/modpython_gateway.py?format=raw
    # or fetch the file from that address using your browser  


`code.py`のファイル名を`codep.py`に変更してください。
    
    main = web.wsgifunc(web.webpyfunc(urls, globals()))

.htaccessに以下を追記してください。
    
    
    AddHandler python-program .py
    PythonHandler wsgiref.modpython_gateway::handler
    PythonOption wsgi.application codep::main
    

さらに`RewriteRule`を追加することで、`/` を `/codep.py/` に向けることができます。

`/codep.py/` の末尾 `/`(スラッシュ)を忘れると、`エラー画面(Please contact the administrator.)`が表示されます。

#### .. with mod_wsgi

mod_wsgiは、特色として[mod_pythonより性能](http://code.google.com/p/modwsgi/wiki/PerformanceEstimates)が優れており、構築が非常に簡単な新しいApacheモジュールです。

At the end of your `code.py`, add:

    application = web.wsgifunc(web.webpyfunc(urls, globals()))

mod\_wsgi offers [many possible ways](http://code.google.com/p/modwsgi/wiki/ConfigurationDirectives) to expose a WSGI application in Apache's URL hierarchy, but one simple way would be to add the following to your .htaccess:

    <Files code.py>
        SetHandler wsgi-script
        Options ExecCGI FollowSymLinks
    </Files>

If you get an "ImportError: No module named web" in your apache error.log file, you could try setting the absolute path in code.py before importing web:

    import sys, os
    abspath = os.path.dirname(__file__)
    sys.path.append(abspath)
    os.chdir(abspath)
    import web

Also, you might want to read the "Application Working Directory" section from [Common problems with WSGI applications](http://code.google.com/p/modwsgi/wiki/ApplicationIssues).

It should then be accessible at `http://example.com/code.py/` as usual.

#### mod_rewrite Rules for Apache

If you want webpy to be accessible at 'http://example.com' instead of 'http://example.com/code.py/' add the following rules to the `.htaccess` file:

    <IfModule mod_rewrite.c>      
      RewriteEngine on
      RewriteBase /
      RewriteCond %{REQUEST_URI} !^/icons
      RewriteCond %{REQUEST_URI} !^/favicon.ico$
      RewriteCond %{REQUEST_URI} !^(/.*)+code.py/
      RewriteRule ^(.*)$ code.py/$1 [PT]
    </IfModule>

If the `code.py` is in the subfolder `myapp/`, adjust the RewriteBase to `RewriteBase /myapp/`. If you have static files like CSS files and images to pass through, duplicate the line with the icons for each path you want to allow.