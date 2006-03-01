---
layout: default
title: Symonds.net
---

# Symonds.net

I was able to get web.py running without too much trouble on my hosting service [Symonds.net](http://symonds.net/). I created a personal status page with it, which can be viewed [here](http://deepak.jois.name). The source code for the page is also included.

## Getting it up

web.py can be run on Symonds.net using FastCGI.

Note that the Python installation on Symonds.net did not have the following modules installed, so I had to install it inside my local folder.  

* Cheetah
* [flup](http://www.saddi.com/software/flup/)

**TODO** : include precise instructions like on the [TextDrive](/TextDrive) page
 
After that, include the following in your `.htaccess` file :

     Options FollowSymLinks ExecCGI
     
     <Files *py>     SetHandler cgi-script
     Addhandler cgi-script py
     </Files>
You might also want to include some URL redirection directives.

