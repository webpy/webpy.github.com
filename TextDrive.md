---
layout: default
title: Using web.py on TextDrive
---

# Using web.py on TextDrive

[TextDrive](http://textdrive.com/) graciously provided me with a free shared hosting account to try to get web.py running on their system. I'm keeping notes on what I did here.

I got assigned `aaronsw.textdriven.com` on the server `cardero.textdrive.com` -- you should replace these in my instructions with whatever your server names are.

## Getting it up

First, [file a support ticket](http://help.textdrive.com/index.php?pg=request) requesting a port to run web.py on. Apparently filing such a ticket [is standard practice](http://help.textdrive.com/index.php?pg=kb.page&id=106) for running web apps on TextDrive. You'll get back a number, which we'll call `8048` (obviously you'll want to replace this with the actual number you get).
Second, SSH to `aaronsw.textdriven.com` and run:

    cd web/public/
    mkdir work
    cd work
    wget http://webpy.org/web.py
    # copy my script to code.py in this directory
    python code.py 8048

Now check `http://aaronsw.textdriven.com:8048/` -- you should see your script working.

Now you can log into your webmin (`https://webmin.cardero.textdrive.com/`), click "Apache Webserver", click "Aliases and Redirects", and scroll down to "Map local to remote URLs". Add a line with / in the first box, check the second radio button, and put `http://aaronsw.textdriven.com:8048/` (don't forget to include the n in textdriven!) in the second box. Click "Save". Then click "Apply Changes" (in the upper right corner).

Now check `http://aaronsw.textdriven.com/` -- you should see your script working again.

## Install Cheetah

Installing Cheetah on TextDrive is quite straight forward. Check [here](http://thetruedelight.blogspot.com/2006/12/how-to-install-cheetah-on-textdrive_19.html) to see the full installation script. 

## Keeping it up

In your SSH window, type Ctrl-C to kill the Python script and run:

    python ~aaronsw/web/public/work/code.py 8048 2>/dev/null &
This will run your web.py app as a daemon, so you can log out and it will stay running.

To make sure that the server starts your script back up when it reboots, go into webmin, click "Scheduled Cron Jobs", click "Create a new scheduled cron job", and add this as the command. Click the radio button next to "Simple schedule..." and select "When system boots" from the drop down menu. Then click "Create".

(Note: My server hasn't rebooted yet, so I haven't gotten a chance to test that this works.)

## Making it fast

For reasons I don't quite understand lighttpd proxying to web.py is faster than running web.py directly. So if you want your server to support more serious loads, you should run a simple lighttpd instance on port 8048 and have it talk to web.py through FastCGI. TextDrive has a [knowledge base article](http://help.textdrive.com/index.php?pg=kb.page&id=252) on setting up lighttpd.