---
layout: default
title: 欢迎来到web.py!
---

**web.py**是一个用于python的简单而有强大的web开发框架。web.py是完全开放的，你可以没有任何限制的用于任何目的使用它。

<div style="float: right; margin: 1em"> 
<pre>
import web
        
urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:        
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

if __name__ == "__main__":
    app.run()
</pre>
<em>一个完整web.py应用.</em>
</div>

## 开始体验

web.py 0.37是最新的发布版本. 你可以通过运行一下命令来安装它:

    sudo easy_install web.py

或者从git上获取最新的开发版：
    
    git clone git://github.com/webpy/webpy.git
    ln -s `pwd`/webpy/web .

## 谁使用过web.py?

web.py在最初发布时Aaron Swartz还在[reddit.com][20]工作, 这个站点因为使用了web.py使之成为了Alexa排名的前1000名站点之一，并且承载着每天几百万的PV访问量。创始人Steve Huffman解释道："它是一个反框架的框架. web.py不会约束你"。 (这个站点在被收购后由Condé Nast使用其它工具被重写了.)

   [20]: http://reddit.com/

* [Frinki](http://frinki.com), 西班牙的是一个新的社交网络。

* [Yandex][21], 俄罗斯的搜索引擎领先者。 (他们的主页独自承载着每天7000万的PV量).

   [21]: http://yandex.ru

* [Make History](http://makehistory.national911memorial.org), 一个由web.py开发的在Google App Engine上排名靠前的9.11纪念馆项目。在2009年9月11号, 它迎来了将近200,000的访问者。 "这是我第一次使用web.py而且还是个python的初学者。" 它的开发者说道. "web.py真是太棒了！"

* [Oyster Hotel Reviews](http://www.oyster.com/), 一个帮助你浏览并预定酒店的网站，使用web.py开发他们的预定页和动态页。他们说道 "web.py给了他们管理大型网站所需要的掌控能力。" 

* [local.ch](http://www.local.ch), 瑞士官方的在线电话簿 - 使用web.py作为其跟踪过期内容的后台服务器 - 其开源代码在 [urldammit](http://github.com/harryf/urldammit/tree/master).

* [archivd.com](http://www.archivd.com), 一个合作研究和归档的web应用程序,同样基于web.py开发.

* [Chiefmall](http://www.chiefmall.com/), 一个承包商搜索工具, 使用web.py开发.

"[web.py]我们用于开发FriendFeed的web框架 并且这个webapp框架已经发布在App Engine上..."  
<span class="cite">&nbsp;&nbsp;&mdash;&nbsp; [Brett Taylor](http://bret.appspot.com/entry/experimenting-google-app-engine), FriendFeed的联合创始人及Google App Engine上最早的技术领导者</span>

"Django让你在Django中编写web应用。TurboGears让你在TurboGears中编写web应用。Web.py让你在Python中编写web应用。"  
<span class="cite">&nbsp;&nbsp;&mdash;&nbsp; Adam Atlas</span>

"[Guido van Rossum, Python的作者], 你可能会发现web.py是最适合你的风格.... 如果你不喜欢它, 我想象不到其他的几十种框架你还会喜欢哪个？"
<span class="cite">&nbsp;&nbsp;&mdash;&nbsp; Phillip J. Eby, Python Web Server Gateway Interface(WSGI)的作者 [#][30]</span>

   [30]: http://www.artima.com/forums/flat.jsp?forum=106&thread=146149&start=30&msRange=15
