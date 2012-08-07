---
layout: default
title: FAQ
---

# FAQ

Other languages : [español](/faq.es) | [russian русский](/faq.ru) | [japan 日本語](/faq.ja) | [chinese 简体中文](/faq.zh-cn) | [français](/faq.fr) | [Česko](/faq.cs)

Example code for many common questions can be found in the [cookbook section](/cookbook).
    
99. **Why are the urls just one long list?**

    If they were a dictionary, they wouldn't be ordered. If it was a list of tuples, then it'd be a lot more typing.

99. **How do I serve static files such as JavaScripts or images like PNG and JPG with the web.py server?**

    Create a directory (also known as a folder) called `static` in the location of the script that runs the web.py server. Then place the static files you wish to server in the `static` folder. For example, the URL `http://localhost/static/logo.png` will send the image `./static/logo.png` to the client.

99. **Where can I go for additional help?**

    Google Groups has a [web.py group](http://groups.google.com/group/webpy) that is quite helpful.

99. **How do I debug print to the console?**

	web.debug("I will get printed to the console and not the body of the webpage")

99. **I stumbled over a bug in web.py. Where can I file it?**

	Go to the [webpy launchpad site](https://launchpad.net/webpy), login (or register if you have to) and click on "report a bug".

99. **What's this magic `ctx` I see in examples?**

	[ctx cookbook recipe](/cookbook/ctx) []()