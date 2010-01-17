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

<style>
body {
  background-color: #fff;
  color: #000;
  font: 300 16px/1.5 "Helvetica Neue", Helvetica, Arial, sans-serif; }
h1 {
  font-size: 2em;
  margin: .5em; }
h2 {
  font-size: 1.75em;
  margin: .571428571em; }
h3 {
  font-size: 1.5em;
  margin: .6666em; }
h4 {
  font-size: 1.25em;
  margin: .8em; }
h1, h2, h3, h4, h5, h6 {
  color: #000;
  margin-left: 0;
  margin-right: 0; }
#header .logo a {
  font-size: 4em;
  font-weight: 900;
  padding: .25em; }
#header .logo a:after {
  content: 'web.py'; }
#header .logo a img {
  display: none; }
#header .blurb {
  font-size: 1.25em;
  float: right;
  left: 0;
  padding: 1em;
  position: relative; }
#location {
  background-color: #bbb; }
#location a:first-child {
  text-transform: capitalize; }
#main {
  color: #000; }
pre {
  background-color: #ddd;
  border: 0;
  color: #222;
  padding: 1em 2em; }
pre code {
  font-family: "Andale Mono", Courier; }
pre code kbd:before {
  content: '$ '; }
pre code kbd.su:before {
  content: '# '; }
</style>