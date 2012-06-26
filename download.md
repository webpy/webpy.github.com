---
layout: default
title: Download
---

# Download

Other languages : [français](/download/fr) | ...
## Get the latest stable version

The easiest way to install web.py is using [easy_install](http://peak.telecommunity.com/DevCenter/EasyInstall):

    $ easy_install web.py

If you don't have `easy_install`, try downloading the sources.

    $ wget http://webpy.org/static/web.py-0.37.tar.gz
    $ tar xvzf web.py-0.37.tar.gz
    $ cd web.py-0.37
    $ sudo python setup.py install

If you don't want to install web.py system-wide (or if you want to bundle web.py with your application):

    $ cd your-app-dir
    $ wget http://webpy.org/static/web.py-0.37.tar.gz
    $ tar xvzf web.py-0.37.tar.gz
    $ ln -s web.py-0.37/web .
   
If you are on Ubuntu Linux or Debian, you can install web.py using `apt-get` [ packaging service](http://en.wikipedia.org/wiki/Advanced_Packaging_Tool). But you may not get the latest as debian/ubuntu release cycles are different from web.py.

    $ sudo apt-get install python-webpy

If you're running Fedora, RHEL or CentOS (and using the [EPEL](https://fedoraproject.org/wiki/EPEL) repository), you can install web.py using `yum` or `up2date`:

    $ yum install python-webpy
    $ up2date -i python-webpy

## Get the latest development version

    $ git clone git://github.com/webpy/webpy.git
