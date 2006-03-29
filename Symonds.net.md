---
layout: default
title: Symonds.net
---

# Symonds.net

I was able to get web.py running without too much trouble on my hosting service [Symonds.net](http://symonds.net/). I created a personal status page with it, which can be viewed [here](http://deepak.jois.name). The source code for the page is also included.

## Getting it up

web.py can be run on Symonds.net using FastCGI.

Note that the Python installation on Symonds.net did not have the following modules installed, so I had to install it inside my local folder.  

* Cheetah
* [flup](http://www.saddi.com/software/flup/)

Follow the instructions on your host:

* change directory into the newly created domain, e.g : `cd deepak`
* `wget http://webpy.org/web.py`
* `wget http://www.saddi.com/software/flup/dist/flup-r1839.tar.gz`
* `tar zxvf flup-r1839.tar.gz`
* `mv flup-r1839/flup/ ./flup`

On your local machine, as superuser :

* Download Cheetah from <http://sourceforge.net/project/showfiles.php?group_id=28961&package_id=20864&release_id=391008> and extract it.
* Extract it using `tar xvzf  Cheetah-2.0rc4.tar.gz`
* Install it using : `cd Cheetah-2.0rc4` and `python setup.py install`
* Copy the folder named `/usr/lib/python<version>/site-packages/Cheetah` to your host in the same folder you downloaded `web.py` : `scp -r /usr/lib/python2.4/site-packages/Cheetah username@hostname:public_html/deepak/`

After that, include the following in the `.htaccess` file inside the folder you downloaded `web.py`:

     Options FollowSymLinks ExecCGI
     
     <Files *py>     SetHandler cgi-script
     Addhandler cgi-script py
     </Files>
You might also want to include some URL redirection directives like :

      RewriteEngine on
      RewriteRule    ^status$ status.py/status

After this, you should be able to view your web.py app like [here](http://deepak.jois.name/status).