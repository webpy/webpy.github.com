---
layout: default
title: Installation
---

# Installation

`web.py` supports Python 2.4 – 2.6 and has no immediate prerequisites.

1.  [Stable Version](#stable)
    1.  [From Source](#source)
        1.  [System-wide](#system)
        1.  [Local](#local)
    1.  [Via Distribution](#distribution)
        1.  [Debian-based](#debian)
        1.  [Red Hat-based](#red-hat)
1.  [Development Version](#development)
1.  [Verify Install](#verify)

<h2 id=stable>Stable Version</h2>

The easiest way to install `web.py` is using
<code>[easy_install](http://peak.telecommunity.com/DevCenter/EasyInstall)</code>.  
<em><small><strong>Note</strong> that you will install the version specified in the [Python Package Index](http://pypi.python.org/pypi/web.py).</small></em>

<pre><code><kbd>easy_install web.py</kbd>
<kbd></kbd></code></pre>

<h3 id=source>From Source</h3>

<pre><code><kbd>wget http://webpy.org/static/web.py-0.33.tar.gz</kbd>
<kbd>tar xvzf web.py-0.33.tar.gz</kbd>
<kbd></kbd></code></pre>

<h4 id=system>System-wide</h4>

<pre><code><kbd>cd web.py-0.33</kbd>
<kbd>sudo python setup.py install</kbd>
<kbd></kbd></code></pre>

<h4 id=local>Local</h4>

If you need to bundle `web.py` with your application extract the source to a `vendor` folder and create a symlink, normally within your package's root.

<pre><code><kbd>ln -s vendor/web.py-0.33/web web</kbd>
<kbd></kbd></code></pre>

<h3 id=distribution>Via GNU/Linux Distribution</h3>

<h4 id=debian>Debian <small>or Ubuntu</small></h4>

If you are on a Debian-based system you can install `web.py` using `apt-get`.  
<em><small><strong>Note</strong> that you may not get the latest version as the Ubuntu/Debian release cycles are different from `web.py`. See <a href=http://packages.debian.org/search?searchon=names&keywords=python-webpy>Debian</a> and <a href=https://launchpad.net/ubuntu/+source/webpy>Ubuntu</a> package profiles for more information.</small></em>

<pre><code><kbd>sudo apt-get install python-webpy</kbd>
<kbd></kbd></code></pre>

<h4 id=red-hat>Red Hat <small>or Fedora, RHEL, CentOS</small></h4>

If you are on a Red Hat-based system you can install `web.py` using `yum` or `up2date`.  
<em><small><strong>Note</strong> that CentOS requires the [<abbr title="Extra Packages for Enterprise Linux">EPEL</abbr>](https://fedoraproject.org/wiki/EPEL) repository.</small></em>

<pre><code><kbd class=su>yum install python-webpy</kbd>
<kbd class=su></kbd></code></pre>
<pre><code><kbd class=su>up2date -i python-webpy</kbd>
<kbd class=su></kbd></code></pre>

<h2 id=development>Development Branch</h2>

To follow the bleeding edge clone the master branch.

<pre><code><kbd>git clone git://github.com/webpy/webpy.git</kbd>
<kbd></kbd></code></pre>

<h2 id=verify>Verify Install</h2>

<pre><code><kbd>python -c "import web; web.application(('/', lambda: 'success')).run()"</kbd>
<samp>http://0.0.0.0:8080/</samp></code></pre>

Point a browser to your host at port `8080` and expect a response of `success`.