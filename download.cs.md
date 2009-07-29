---
layout: default
title: Získání web.py
---

# Získání web.py

## Získání poslední stabilní verze

Nejsnazší cesta k instalaci web.py je použít [easy_install](http://peak.telecommunity.com/DevCenter/EasyInstall):

    $ easy_install web.py

Pokud nemáte `easy_install`, zkuste stáhnout zdrojáky:

    $ wget http://webpy.org/static/web.py-0.32.tar.gz
    $ tar xvzf web.py-0.32.tar.gz
    $ cd webpy
    $ sudo python setup.py install

Když nechcete instalovat web.py pro celý systém (nebo když chcete zabalit web.py s vaší aplikací):

    $ cd your-app-dir
    $ wget http://webpy.org/static/web.py-0.32.tar.gz
    $ tar xvzf web.py-0.32.tar.gz
    $ ln -s webpy/web .

V Ubuntu Linuxu nebo Debianu, můžete instalovat web.py přes `apt-get`. Pak ale možná nezískáte poslední verzi, protože cyklus vydání Debianu/Ubuntu je jiný než u web.py.

    $ sudo apt-get install python-webpy

## Získání poslední vývojové verze

    $ git clone git://github.com/webpy/webpy.git