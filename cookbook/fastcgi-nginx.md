---
layout: default
title: Webpy + Nginx with FastCGI
---

# Webpy + Nginx with FastCGI

This cookbook entry explains how to run web.py on Nginx with Fastcgi.

### Requirements

* Nginx 0.8.\* or 0.7.\* (with fastcgi and rewrite module).
* Webpy 0.32
* Spawn-fcgi 1.6.2
* Flup

Older versions may work, but aren't tested.

### Resources

* [Nginx wiki](http://wiki.nginx.org/NginxInstall)
* [Spawn-fcgi](http://redmine.lighttpd.net/projects/spawn-fcgi/news)
* [Flup](http://trac.saddi.com/flup)

### Notes

* You may replace `index.py` with your own file name.
* `/path/to/www` Is the path to the directory where your webpy application is located.
* `/path/to/www/index.py` is the full path to your python file.
* Do not run anything until you are at *Run*.

## Nginx configuration

	location / {
            fastcgi_param REQUEST_METHOD $request_method;
            fastcgi_param QUERY_STRING $query_string;
            fastcgi_param CONTENT_TYPE $content_type;
            fastcgi_param CONTENT_LENGTH $content_length;
            fastcgi_param GATEWAY_INTERFACE CGI/1.1;
            fastcgi_param SERVER_SOFTWARE nginx/$nginx_version;
            fastcgi_param REMOTE_ADDR $remote_addr;
            fastcgi_param REMOTE_PORT $remote_port;
            fastcgi_param SERVER_ADDR $server_addr;
            fastcgi_param SERVER_PORT $server_port;
            fastcgi_param SERVER_NAME $server_name;
            fastcgi_param SERVER_PROTOCOL $server_protocol;
            fastcgi_param SCRIPT_FILENAME $fastcgi_script_name;
            fastcgi_param PATH_INFO $fastcgi_script_name;
            fastcgi_pass 127.0.0.1:9002;
	}

To serve static files add this:

        location /static/ {
            root /path/to/www;
            if (-f $request_filename) {
               rewrite ^/static/(.*)$  /static/$1 break;
            }
        }

__Note:__ the address and port may be different.

## Spawn-fcgi

You can start a process with:

	spawn-fcgi -d /path/to/www -f /path/to/www/index.py -a 127.0.0.1 -p 9002

### Start and shutdown script

Start:

	#!/bin/sh
	spawn-fcgi -d /path/to/www -f /path/to/www/index.py -a 127.0.0.1 -p 9002

Shutdown:

	#!/bin/sh
	kill `pgrep -f "python /path/to/www/index.py"`

__Note:__ You're free to choose which address, port, directory and filename to use, but be sure to adjust the Nginx configuration.

## Hello world!

Save the following code in your www directory and call the file index.py (or whatever you like).
The following line is required: `web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)`.

	#!/usr/bin/env python
	# -*- coding: utf-8 -*-

	import web

	urls = ("/.*", "hello")
	app = web.application(urls, globals())

	class hello:
		def GET(self):
			return 'Hello, world!'

	if __name__ == "__main__":
		web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
		app.run()

Note: make your file executable by doing `chmod +x index.py`. You'll get errors if it isn't executable.

## Run

1. Start a process with `spawn-fcgi`.
2. Start Nginx.

To check if it runs do `ps aux | grep index.py` or simply visit the page in your browser.

To reload your configuration:

	/path/to/nginx/sbin/nginx -s reload

And to stop:

	/path/to/nginx/sbin/nginx -s stop


## NOTES

### problem child exited with 2

solution:  insert `#!/usr/bin/env python` into header of main.py 
    
### problem spawn-fcgi child exited with 126

solution: `chmod +x main.py`


