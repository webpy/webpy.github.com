---
layout: default
title: Download
---

# Download

## Development

<pre><code><kbd>git clone git://github.com/webpy/webpy.git</kbd></code></pre>

## Stable

The easiest way to install `web.py` is using
<code>[easy_install](http://peak.telecommunity.com/DevCenter/EasyInstall)</code>:

<pre><code><kbd>easy_install web.py</kbd></code></pre>

If you don't have `easy_install`, try downloading the sources.

<pre><code><kbd>wget http://webpy.org/static/web.py-0.33.tar.gz</kbd>
<kbd>tar xvzf web.py-0.33.tar.gz</kbd>
<kbd>cd web.py-0.33</kbd>
<kbd>sudo python setup.py install</kbd></code></pre>

If you don't want to install `web.py` system-wide (or if you want to bundle `web.py` with your application):

<pre><code><kbd>cd your-app-dir</kbd>
<kbd>wget http://webpy.org/static/web.py-0.33.tar.gz</kbd>
<kbd>tar xvzf web.py-0.33.tar.gz</kbd>
<kbd>ln -s web.py-0.33/web .</kbd></code></pre>

If you are on Ubuntu or Debian you can install `web.py` using `apt-get`.  
<em>Note that you may not get the latest version as the Ubuntu/Debian release cycles are different from `web.py`.</em>

<pre><code><kbd>sudo apt-get install python-webpy</kbd></code></pre>

If you are running Fedora, RHEL or CentOS (and using the [<abbr title="Extra Packages for Enterprise Linux">EPEL</abbr>](https://fedoraproject.org/wiki/EPEL) repository) you can install `web.py` using `yum` or `up2date`:

<pre><code><kbd class=su>yum install python-webpy</kbd>
<kbd class=su>up2date -i python-webpy</kbd></code></pre>

<style>@import url(http://angelo.gladding.name/assets/webpy-redesign.css);</style>