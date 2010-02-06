---
layout: default
title: Téléchargement
---

# Téléchargement

Autre langages : [english](/download) | ...

## Obtenir la dernière version stable

La façon la plus simple d'installer web.py est d'utiliser [easy_install](http://peak.telecommunity.com/DevCenter/EasyInstall)[:](http://www.dofollownet.com/)

    $ easy_install web.py

Si vous n'avez pas 'easy_install', essayez de télécharger les sources.

    $ wget http://webpy.org/static/web.py-0.33.tar.gz
    $ tar xvzf web.py-0.33.tar.gz
    $ cd web.py-0.33
    $ sudo python setup.py install

Si vous ne voulez pas installer web.py pour tout le système (ou si vous désirez grouper web.py avec votre application):

    $ cd your-app-dir
    $ wget http://webpy.org/static/web.py-0.33.tar.gz
    $ tar xvzf web.py-0.33.tar.gz
    $ ln -s web.py-0.33/web .
   
Si vous êtes sous Linux Ubuntu ou Debian, vous pouvez installer web.py en utilisant la commande 'apt-get'. Mias vous n'aurez pas la dernière version car  les cycles de versions de debian/ubuntu (releases) diffèrent de ceux de web.py.

    $ sudo apt-get install python-webpy

Si vous utilisez Fedora, RHEL ou CentOS (ainsi que les dépôts [EPEL](https://fedoraproject.org/wiki/EPEL) ), vous pouvez installer web.py avec 'yum' or 'up2date':

    $ yum install python-webpy
    $ up2date -i python-webpy

## Téléchargez la dernière version de développement

    $ git clone git://github.com/webpy/webpy.git