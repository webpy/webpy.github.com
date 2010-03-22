---
layout: default
title: i18n support in template file
---

# i18n support in template file

i18n support in template file

Problem:

How to get i18n support in webpy template file? 
Solution:

Project directory structure: 

<pre>
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

</pre>

File: proj/code.py 

<pre>
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

# Run with buildin http server.
app = web.application(urls, globals())
if __name__ == "__main__":
    app.run()
</pre>

Template file: proj/templates/hello.html. 
<pre>$_("Message")</pre>

Create locale dir and use pygettext.py which shipped within Python-2.6 (in directory: Tools/i18n/) to extract messages from python scripts and templates files: 
<pre>
shell> cd /path/to/proj/
shell> mkdir -p i18n/en_US/LC_MESSAGES/
shell> python /path/to/pygettext.py -a -v -d messages -o i18n/messages.po \*.py templates/\*.html
Working on code.py
Working on templates/hello.html
</pre>

You will get pot file: i18n/messages.po. Its contents looks like below ('msgstr' contains translated message): 
<pre>
#: code.py:40
msgid "Message"
msgstr "This is translated message in file: code.py."
</pre>

Copy file 'i18n/messages.po' to directory 'i18n/en_US/LC_MESSAGES/', and then translate it. Use 'msgfmt' tool from 'gettext' package (not python moudule) or use file 'msgfmt.py' shipped within Python-2.6 (in directory: Tools/i18n/) to compile pot file to mo file: 
<pre>
shell> msgfmt -o i18n/en_US/LC_MESSAGES/messages.mo i18n/en_US/LC_MESSAGES/messages.po
</pre>
Start webpy http server: 
<pre>
shell> cd /path/to/proj/
shell> python code.py
http://0.0.0.0:8000/
</pre>
Start your web browser, e.g. firefox, and visit url: http://192.168.0.3:8000/, you will see translated message.