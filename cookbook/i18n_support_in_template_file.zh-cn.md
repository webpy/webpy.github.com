---
layout: default
title: i18n support in template file
---

# i18n support in template file

## 模板文件中的i18n支持

### 问题

在web.py的模板文件中, 如何得到i18n的支持?

### 方案

项目目录结构:

```
proj/
   |- code.py
   |- i18n/
       |- messages.po
       |- en_US/
            |- LC_MESSAGES/
                   |- messages.po
                   |- messages.mo
   |- templates/
       |- hello.html

```

文件: proj/code.py

```
#!/usr/bin/env python
# encoding: utf-8

import web
import gettext

urls = (
    '/.*', 'hello',
    )

# File location directory.
curdir = os.path.abspath(os.path.dirname(__file__))

# i18n directory.
localedir = curdir + '/i18n'

gettext.install('messages', localedir, unicode=True)
gettext.translation('messages', localedir, languages=['en_US']).install(True)
render = web.template.render(curdir + '/templates/', globals={'_': _})

class hello:
    def GET(self):
        return render.hello()

# 使用内建的HTTP服务器来运行.
app = web.application(urls, globals())
if __name__ == "__main__":
    app.run()
```

模板文件: proj/templates/hello.html.

```
$_("Message")
```

创建一个locale目录并使用python2.6内建的pygettext.py从python脚本和模板文件中导出翻译:

```
shell> cd /path/to/proj/
shell> mkdir -p i18n/en_US/LC_MESSAGES/
shell> python /path/to/pygettext.py -a -v -d messages -o i18n/messages.po *.py templates/*.html
Working on code.py
Working on templates/hello.html
```

你将会得到pot file: i18n/messages.po. 它的内容和下面的差不多
('msgstr'包含了翻译后的信息):

```
 # 文件 code.py:40
msgid "Message"
msgstr "This is translated message in file: code.py."
```

拷贝文件'i18n/messages.po'到目录'i18n/en_US/LC_MESSAGES/'下, 然后翻译它. 使用gettext包的msgfmt工具或者使用python2.6内建的'msgfmt.py'文件将一个pot文件编译称mo文件:

```
shell> msgfmt -o i18n/en_US/LC_MESSAGES/messages.mo i18n/en_US/LC_MESSAGES/messages.po
```

运行web.py的服务器:

```
shell> cd /path/to/proj/
shell> python code.py
http://0.0.0.0:8000/
```

打开你的浏览器, 比如说firefox, 然后访问地址: http://192.168.0.3:8000/, 你将会看过翻译过的信息.
