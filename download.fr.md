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

    $ wget https://github.com/webpy/webpy/archive/0.40.zip
    $ unzip 0.40.zip
    $ cd webpy-0.40
    $ sudo python setup.py install

Si vous ne voulez pas installer web.py pour tout le système (ou si vous désirez grouper web.py avec votre application):

    $ cd your-app-dir
    $ wget https://github.com/webpy/webpy/archive/0.40.zip
    $ unzip 0.40.zip
    $ cp -rf webpy-0.40/web .
    $ rm -rf 0.40.zip webpy-0.40

Si vous êtes sous Linux Ubuntu ou Debian, vous pouvez installer web.py en utilisant la commande 'apt-get'. Mias vous n'aurez pas la dernière version car  les cycles de versions de debian/ubuntu (releases) diffèrent de ceux de web.py.

    $ sudo apt-get install python-webpy

Si vous utilisez Fedora, RHEL ou CentOS (ainsi que les dépôts [EPEL](https://fedoraproject.org/wiki/EPEL) ), vous pouvez installer web.py avec 'yum' or 'up2date':

    $ yum install python-webpy
    $ up2date -i python-webpy

## Téléchargez la dernière version de développement

    $ git clone git://github.com/webpy/webpy.git
