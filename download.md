---
layout: default
title: Download
---

# Download

Other languages : [français](/download/fr) | ...
## Get the latest stable version

The easiest way to install web.py is using [easy_install](http://peak.telecommunity.com/DevCenter/EasyInstall):

    $ easy_install web.py

If you don't have `easy_install`, try downloading the source package from
[pypi](https://pypi.org/project/web.py/), then install manually. We use
version `0.60` for example here:

    $ tar xvzf web.py-0.60.tar.gz
    $ cd web.py-0.60
    $ sudo python setup.py install

If you don't want to install web.py system-wide, or if you want to bundle
web.py with your application, you can simply copy `web.py-0.60/web/` to your
application directory.

If you are on Ubuntu Linux or Debian, you can install web.py with `apt-get`,
but you may not get the latest web.py as Debian/Ubuntu release cycles are
different from web.py.

    $ sudo apt-get install python-webpy

If you're running Fedora, RHEL or CentOS (and using the
[EPEL](https://fedoraproject.org/wiki/EPEL) repository), you can install web.py
using `yum`:

    $ sudo yum install epel-release
    $ sudo yum install python-webpy

## Get the latest development version

    $ git clone git://github.com/webpy/webpy.git
