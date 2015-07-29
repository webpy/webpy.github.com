---
layout: default
title: deploying web.py with nginx, uwsgi service and linux
---

# deploying web.py with nginx, uwsgi service and linux

It is possible to deploy web.py with nginx using a uWSGI 2.0.11 or later. Note that earlier versions available in the repository may not work! uWSGI is available via python's pip installer. Nginx natively supports uWSGI since 0.8.40.

Create the folders: 

	/var/srv/www/mon/logs
	/var/srv/www/mon/public_html/static
	/var/srv/www/mon/app

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

Enable the site:

    sudo ln -s /etc/nginx/sites-available/mon /etc/nginx/sites-enabled/mon

Create file: /etc/uwsgi/apps-available/mon.xml

	<uwsgi>
		<plugin>python</plugin>
		<socket>/run/uwsgi/app/mon/mon.socket</socket>
		<pythonpath>/var/srv/www/mon/app/</pythonpath>
		<app mountpoint="/">

		    <script>mon</script>

		</app>
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

Enable the app:

	sudo ln -s /etc/uwsgi/apps-available/mon.xml /etc/uwsgi/apps-enabled/mon.xml

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

Restart nginx and uwsgi. This works on many linux systems:

	sudo service nginx stop
	sudo service uwsgi stop
	sudo service nginx start
	sudo service uwsgi start

Open web browser and view:
	
	http://localhost/

Helpful links:<br />
[ nginx website](http://nginx.net/ )<br />
[ wiki page on Nginx support for uWSGI](http://uwsgi-docs.readthedocs.org/en/latest/Nginx.html )

