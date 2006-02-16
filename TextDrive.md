---
layout: default
title: Using web.py on TextDrive
---

# Using web.py on TextDrive

TextDrive graciously provided me with a free shared hosting account to try to get web.py running on their system. I'm keeping notes on what I did here.

I got assigned `aaronsw.textdriven.com` on the server `cardero.textdrive.com` -- you should replace these in my instructions with whatever your server names are.

First, [file a support ticket](http://help.textdrive.com/index.php?pg=request) requesting a port to run web.py on. Apparently filing such a ticket is standard practice for running web apps on TextDrive. You'll get back a number, which we'll call `8048` (obviously you'll want to replace this with the actual number you get).

Second, SSH to `aaronsw.textdriven.com` and run:

    cd web/public/
    mkdir work
    cd work
    wget http://webpy.org/web.py
    # copy my script to code.py in this directory
    python code.py 8048

Now check `http://aaronsw.textdriven.com:8048/` -- you should see your script working.

Now you can log into your webmin (`https://webmin.cardero.textdrive.com/`), click "Apache Webserver", click "Aliases and Redirects", and scroll down to "Map local to remote URLs".