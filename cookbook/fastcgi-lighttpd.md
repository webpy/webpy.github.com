---
layout: default
title: Webpy + LightTTPD with FastCGi
---

# Webpy + LightTTPD with FastCGi

Other languages: [français](/../cookbook/fastcgi-lighttpd/fr) | ...

*If you have problems with this recipe read this [thread](http://www.mail-archive.com/webpy@googlegroups.com/msg02800.html)*

*The following applies on lighttpd version 1.4.18*

##Note:  
* You may replace <code>code.py</code> with your own file name.
* <code>/path-to/webpy-app</code> found below refers to the path to the directory contains your <code>code.py</code>
* <code>/path-to/webpy-app/code.py</code> is the full path to your **python file**

If you are not certain what version you are running simply type: <code>lighttpd -v</code> at your console.

Note: Earlier version of lighttpd may organize the .conf files differently. Yet, the same principles applied on them as well.

###ligghttpd Configuration under Debian GNU/Linux

<pre>
Files and Directories in /etc/lighttpd:
---------------------------------------

lighttpd.conf:
         main configuration file

conf-available/
        This directory contains a series of .conf files. These files contain
        configuration directives necessary to load and run webserver modules.
        If you want to create your own files they names should be
        build as nn-name.conf where "nn" is two digit number (number
        is used to find order for loading files)

conf-enabled/
        To actually enable a module for lighttpd, it is necessary to create a
        symlink in this directory to the .conf file in conf-available/.

Enabling and disabling modules could be done by provided
/usr/sbin/lighty-enable-mod and /usr/sbin/lighty-disable-mod scripts.
</pre>

<strong>
For web py you should enable mod_fastcgi and mod_rewrite, thus run: <code>/usr/sbin/lighty-enable-mod</code> and supply <code>fastcgi</code>  
(mod_rewrite will be enabled within <code>10-fastcgi.conf</code> file as you will see in a moment).

##Below are instructions for the following files:
* <code>/etc/lighttpd/lighttpd.conf</code>
* <code>/etc/lighttpd/conf-available/10-fastcgi.conf</code>
* <code>code.py</code>

###<code>/etc/lighttpd/lighttpd.conf</code>

<pre>
server.modules              = (
            "mod_access",
            "mod_alias",
            "mod_accesslog",
            "mod_compress",
)
server.document-root       = "/path-to/webpy-app"
</pre>

In my case I used postgresql and therefore runs lighttpd as postgres in order to grant permissions to the database, therefore I added the line:

<pre>
server.username = "postgres"
</pre>

###<code>/etc/lighttpd/conf-available/10-fastcgi.conf</code>

<pre>
server.modules   += ( "mod_fastcgi" )
server.modules   += ( "mod_rewrite" )

 fastcgi.server = ( "/code.py" =>
 (( "socket" => "/tmp/fastcgi.socket",
    "bin-path" => "/path-to/webpy-app/code.py",
    "max-procs" => 1,
   "bin-environment" => (
     "REAL_SCRIPT_NAME" => ""
   ),
   "check-local" => "disable"
 ))
 )

 url.rewrite-once = (
   "^/favicon.ico$" => "/static/favicon.ico",
   "^/static/(.*)$" => "/static/$1",
   "^/(.*)$" => "/code.py/$1",
 )
</pre>

###<code>/code.py</code>  
At the top of the file add:

<pre>
#!/usr/bin/env python
</pre>

and don't forget to make it executable (otherwise you will get a "permission denied" error):

<pre>
$ chmod 755 /path-to/webpy-app/code.py
</pre>