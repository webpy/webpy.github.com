---
layout: default
title: Download
---

# Download

1.  [Development](#development)
1.  [Stable](#stable)
    1.  [Source](#source)
        1.  [System](#system)
        1.  [Local](#local)
    1.  [Distribution](#distribution)
        1.  [Debian](#debian)
        1.  [Red Hat](#red-hat)

<h2 id=development>Development</h2>

<pre><code><kbd>git clone git://github.com/webpy/webpy.git</kbd></code></pre>

<h2 id=stable>Stable</h2>

The easiest way to install `web.py` is using
<code>[easy_install](http://peak.telecommunity.com/DevCenter/EasyInstall)</code>.  
<em><small><strong>Note</strong> that you will install the version specified in the [Python Package Index](http://pypi.python.org/pypi/web.py).</small></em>

<pre><code><kbd>easy_install web.py</kbd></code></pre>

<h3 id=source>Source</h3>

<pre><code><kbd>wget http://webpy.org/static/web.py-0.33.tar.gz</kbd>
<kbd>tar xvzf web.py-0.33.tar.gz</kbd></code></pre>

<h4 id=system>System Install</h4>

<pre><code><kbd>cd web.py-0.33</kbd>
<kbd>sudo python setup.py install</kbd></code></pre>

<h4 id=local>Local Install</h4>

If you need to bundle `web.py` with your application extract the source to a `vendor` folder and create a symlink, normally within your package's root.

<pre><code><kbd>ln -s vendor/web.py-0.33/web web</kbd></code></pre>

<h3 id=distributions>GNU/Linux Distributions</h3>

<h4 id=debian>Debian <small>Ubuntu</small></h4>

If you are on a Debian-based system you can install `web.py` using `apt-get`.  
<em><small><strong>Note</strong> that you may not get the latest version as the Ubuntu/Debian release cycles are different from `web.py`.</small></em>

<pre><code><kbd>sudo apt-get install python-webpy</kbd></code></pre>

<h4 id=red-hat>Red Hat <small>Fedora, RHEL, CentOS</small></h4>

If you are on a Red Hat-based system you can install `web.py` using `yum` or `up2date`.  
<em><small><strong>Note</strong> that CentOS requires the [<abbr title="Extra Packages for Enterprise Linux">EPEL</abbr>](https://fedoraproject.org/wiki/EPEL) repository.</small></em>

<pre><code><kbd class=su>yum install python-webpy</kbd>
<kbd class=su>up2date -i python-webpy</kbd></code></pre>

<style>@import url(http://angelo.gladding.name/assets/webpy-redesign.css);</style>