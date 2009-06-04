---
layout: default
title: Download web.py
---

# Download web.py

## Get the latest stable version

The easiest way to install web.py is using [easy_install](http://peak.telecommunity.com/DevCenter/EasyInstall):

    $ easy_install web.py

If you don't have `easy_install`, try downloading the sources.

    $ wget http://webpy.org/static/web.py-0.32.tar.gz
    $ tar xvzf web.py-0.32.tar.gz
    $ cd webpy
    $ sudo python setup.py install

If you don't want to install web.py system-wide (or if you want to bundle web.py with your application):

    $ cd your-app-dir
    $ wget http://webpy.org/static/web.py-0.32.tar.gz
    $ tar xvzf web.py-0.32.tar.gz
    $ ln -s webpy/web .
   
If you are on Ubuntu Linux or Debian, you can install web.py using `apt-get`. But you may not get the latest as debian/ubuntu release cycles are different from web.py.

    $ sudo apt-get install python-webpy

## Get the latest development version

    $ git clone git://github.com/webpy/webpy.git


<h2><strong style="display:none"><a href="http://www.du-pognon.com">gagner de l'argent sur internet</a> c'est facile !</strong></h2>