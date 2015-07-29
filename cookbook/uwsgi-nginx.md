---
layout: default
title: deploying web.py with nginx, uwsgi service and linux
---

# deploying web.py with nginx, uwsgi service and linux

It is possible to deploy web.py with nginx using a uWSGI 2.0.11 or later. Note that earlier versions available in the repository (such as 1.9.17) may not work! uWSGI is available via python's pip installer. Nginx natively supports uWSGI since 0.8.40. The following is for python 2.7.

	sudo apt-get install python-pip nginx python-webpy python-dev libpcre3-dev
	sudo apt-get remove uwsgi uwsgi-core
	sudo pip install uwsgi

Create the folders and set ownership: 

	sudo mkdir -p /var/srv/www/mon/logs
	sudo mkdir -p /var/srv/www/mon/public_html/static
	sudo mkdir -p /var/srv/www/mon/app
	sudo chown www-data:www-data -R /var/srv/www/mon

Add a file: /etc/nginx/sites-available/mon

	server {
		    listen          80;
		    server_name     $hostname;
		    access_log /var/srv/www/mon/logs/access.log;
		    error_log /var/srv/www/mon/logs/error.log;

		    location / {
		        uwsgi_pass      unix:///run/uwsgi/app/mon/mon.socket;
		        include         uwsgi_params;
		        uwsgi_param     UWSGI_SCHEME $scheme;
		        uwsgi_param     SERVER_SOFTWARE    nginx/$nginx_version;

		    }

		    location /static {
		        root   /var/srv/www/mon/public_html/;
		        index  index.html index.htm;
		    }

	}

Enable the site and disable the default nginx website:

    sudo ln -s /etc/nginx/sites-available/mon /etc/nginx/sites-enabled/mon
	sudo rm /etc/nginx/sites-enabled/default

Create file: /var/srv/www/mon/app/mon.xml

	<uwsgi>
		<plugin>python</plugin>
		<socket>/run/uwsgi/app/mon/mon.socket</socket>
		<pythonpath>/var/srv/www/mon/app/</pythonpath>
		<module>mon</module>
		<master/>
		<processes>4</processes>
		<harakiri>60</harakiri>
		<reload-mercy>8</reload-mercy>
		<cpu-affinity>1</cpu-affinity>
		<stats>/tmp/stats.socket</stats>
		<max-requests>2000</max-requests>
		<limit-as>512</limit-as>
		<reload-on-as>256</reload-on-as>
		<reload-on-rss>192</reload-on-rss>
		<no-orphans/>
		<vacuum/>
	</uwsgi>

Create file: /var/srv/www/mon/app/mon.py

	import os
	import sys

	sys.path.append('/var/srv/www/mon/app')

	os.environ['PYTHON_EGG_CACHE'] = '/var/srv/www/mon/.python-egg'

	def application(environ, start_response):
		status = '200 OK'
		output = 'Hello World!'

		response_headers = [('Content-type', 'text/plain'),
		                ('Content-Length', str(len(output)))]
		start_response(status, response_headers)

		return [output]

If upstart is available, create file: /etc/init/mon.conf

	description "mon uwsgi"
	author "TSC"

	start on runlevel [2345]
	stop on runlevel [016]

	env DIR=/run/uwsgi/app/mon
	env USER=www-data
	env GROUP=www-data
	env PERMS=0755

	pre-start script
	  mkdir -p $DIR              || true
	  chmod $PERMS $DIR       || true
	  chown $USER:$GROUP $DIR || true
	end script

	exec sudo -u www-data uwsgi /var/srv/www/mon/app/mon.xml

Restart nginx and start the new mon service. These commands on many linux systems:

	sudo service nginx stop
	sudo service mon start
	sudo service nginx start

Open web browser and view:
	
	http://localhost/

Errors are variously logged in:

	/var/log/nginx/error.log
	/var/srv/www/mon/logs/error.log
	/var/log/upstart/mon.log
	
Helpful links:<br />
[ nginx website](http://nginx.net/ )<br />
[ wiki page on Nginx support for uWSGI](http://uwsgi-docs.readthedocs.org/en/latest/Nginx.html )

