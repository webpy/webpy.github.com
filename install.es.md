---
layout: default
title: Guía de instalación
---

# Guía de instalación

Otros idiomas : [english](/install) | [Japan 日本語 ](/install.ja) | [chinese 简体中文 ](/install.zh-cn) | [italiano](/install.it) | [français](/install.fr) | [Serbo-Croatian](http://science.webhostinggeeks.com/webpy-vodic-za-instalaciju)

## Índice

* <a href="#install">Instalación</a>
* <a href="#dev">Desarrollo</a>
* <a href="#prod">Producción</a>
    * <a href="#nginx">Nginx</a>
    * <a href="#lighttpd">LightTPD</a>
        * <a href="#lighttpdfastcgi">.. con FastCGI</a>
    * <a href="#apache">Apache</a>
        * <a href="#apachecgi">.. con CGI</a>
        * <a href="#apachecgihtaccess"> .. con CGI usando .htaccess</a>
        * <a href="#apachefastcgi">.. con FastCGI</a>
        * <a href="#apachescgi">.. con SCGI</a>
        * <a href="#apachemodpython">.. con mod_python</a>
        * <a href="#apachemodwsgi">.. con mod_wsgi</a>
        * <a href="#apachemodrewrite">.. con mod_rewrite</a>

<a name="install"></a>
## Instalación

Para instalar web.py para Python 2.7 o Python >= 3.4, descargue:

    https://github.com/webpy/webpy/archive/0.40.tar.gz

o bien obtenga la última versión de desarrollo:

    https://github.com/webpy/webpy/tarball/master

extraiga y copie el directorio _web_ en el directorio donde desee que su aplicación se encuentre. Si desea hacerlo accesible a todas las aplicaciones, corra:

    python setup.py install

Nota: en algunos sistemas tipo UNIX es posible que necesite `sudo` para obtener los privilegios del usuario root:

    sudo python setup.py install

Vea [Configuración recomendada](/recommended_setup).

Otra opción es utilizar [Easy Install](http://peak.telecommunity.com/DevCenter/EasyInstall). Una vez que Easy Install está correctamente configurado corra:

    easy_install web.py

O [PIP](http://packages.python.org/distribute/)

    pip install web.py==0.40

<a name="dev"></a>
## Desarrollo

web.py trae incluido un servidor web. Puede aprender a escribir una aplicación siguiendo el [tutorial](http://webpy.org/tutorial). Cuando tenga su aplicación escrita, coloque su código en `code.py` e inicie el servidor así:

     python code.py

Abra su navegador web y vaya a [http://localhost:8080/](http://localhost:8080/) para visualizar la página. Para especificar otro puerto, use `python code.py 1234`.

<a name="prod"></a>
## Producción

El servidor web que se inicia cuando se corre un programa en web.py está bien,
pero para sitios web populares necesitará algo un poco más serio. web.py
implementa [WSGI](http://www.python.org/dev/peps/pep-0333/) y corre con todo
lo que sea compatible con este. WSGI es una API (Application Program Interface, Interfaz de Programación de Aplicaciones) común entre los servidores web
y las aplicaciones, análogo a la interfaz Servlet de Java. Para correr web.py con
CGI, FastCGI o SCGI necesitará instalar
[flup](https://www.saddi.com/software/flup/)
([descargue aquí](https://pypi.org/project/flup/#history)), que brinda las interfaces WSGI
para dichas APIs.

Para todas las variantes CGI, adicione esto al inicio de su archivo `code.py`:

    #!/usr/bin/env python

Y corra `chmod +x code.py` para hacerlo ejecutable.

### Nginx

* [Despliegue con Nginx del servicio uWSGI sobre Linux](http://webpy.org/cookbook/uwsgi-nginx)
* [Despliegue de mod_wsgi mediante Nginx](http://webpy.org/cookbook/mod_wsgi-nginx)
* [Despliegue de Fastcgi mediante Nginx](http://webpy.org/cookbook/fastcgi-nginx)

<a name="lighttpd"></a>
### Lighttpd

<a name="lighttpdfastcgi"></a>

#### .. con FastCGI

FastCGI con lighttpd es la manera sugerida para usar web.py en producción. [reddit.com][3] maneja millones de hits con esta configuración.

   [3]: http://reddit.com/

Su configuración de lighttpd puede ser algo así:

     server.modules = ("mod_fastcgi", "mod_rewrite")
     server.document-root = "/path/to/root/"
     fastcgi.server = ( "/code.py" =>
     (( "socket" => "/tmp/fastcgi.socket",
        "bin-path" => "/path/to/root/code.py",
        "max-procs" => 1
     ))
     )

     url.rewrite-once = (
       "^/favicon.ico$" => "/static/favicon.ico",
       "^/static/(.*)$" => "/static/$1",
       "^/(.*)$" => "/code.py/$1"
     )

Con algunas versiones de lighttpd, es importante asegurarse que la propiedad "check-local" de la entrada fastcgi.server esté puesta en "false", especialmente si su `code.py` se encuentra fuera de la raiz de los documentos.

Si usted obtiene un mensaje de error que dice que es imposible importar flup, instálelo tecleando "easy_install flup" en la línea de comandos.

A partir de la revisión 145, es necesario fijar una variable bin-environment en la configuración de fastcgi si su código usa redirecciones. Si cuando su código redirecciona a http://dominio.com/ en la barra de direcciones usted ve http://dominio.com/code.py/, usted debe configurar esta variable de entorno. Esto provocará que la configuración anterior de fastcgi.server luzca de la manera siguiente:

    fastcgi.server = ( "/code.py" =>
    ((
       "socket" => "/tmp/fastcgi.socket",
       "bin-path" => "/path/to/root/code.py",
       "max-procs" => 1,
       "bin-environment" => (
         "REAL_SCRIPT_NAME" => ""
       ),
       "check-local" => "disable"
    ))
    )

<a name="apache"></a>
### Apache

<a name="apachecgi"></a>
#### .. con CGI


Adicione lo siguiente en `httpd.conf` o `apache2.conf`.

    Alias /foo/static/ /camino/a/static
    ScriptAlias /foo/ /camino/a/code.py

<a name="apachecgihtaccess"></a>
#### .. con CGI usando .htaccess

CGI es fácil de configurar, pero no es adecuado para sitios que requieren alto rendimiento.
Adicione esto a su `.htaccess`:

    Options +ExecCGI
    AddHandler cgi-script .py

y apunte su navegador a `http://ejemplo.com/code.py/`. No olvide el último slash; de omitirlo recibirá un mensaje `not found` (no encontrado) (debido a que en la lista de `urls` ninguna se corresponde con este caso). Para hacer que funcione sin tener que teclear `code.py`, habilite las reglas mod_rewrite (ver más abajo).

Nota: Por la manera en que `web.py` está implementado, rompe el módulo `cgitb` puesto que captura `stdout`. Una manera de resolver este problema es usando esto:

    import cgitb; cgitb.enable()
    import sys

    # ... import web etc aquí...

    def cgidebugerror():
        _wrappedstdout = sys.stdout

        sys.stdout = web._oldstdout
        cgitb.handler()

        sys.stdout = _wrappedstdout

    web.internalerror = cgidebugerror


<a name="apachefastcgi"></a>
#### .. con FastCGI

FastCGI es sencillo de configurar y funciona tan bien como mod_python.

Adicione esto a su `.htaccess`:

    <Files code.py>
    SetHandler fastcgi-script
    </Files>

Desafortunadamente, a diferencia de lighttpd, Apache no deja pistas de que quiere utilizar su script web.py script para actuar como servidor FastCGI, por tanto hay que llamar explícitamente a web.py. Adicione esto a `code.py` antes de la línea `if __name__ == "__main__":`:

    web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)

y apunte su navegador a `http://ejemplo.com/code.py/`. No olvide el slash del final, pues sino obtendrá un mensaje `not found` (porque en la lista de `urls` definidas no se corresponde con ninguna). Para hacer que funcione sin tener que teclear `code.py`, habilite las reglas de mod_rewrite (ver más abajo).

[Walter tiene consejos adicionales](http://lemurware.blogspot.com/2006/05/webpy-apache-configuration-and-you.html).


<a name="apachescgi"></a>
#### .. con SCGI
https://www.mems-exchange.org/software/scgi/
Descargue el código fuente de  `mod_scgi` aquí: http://www.mems-exchange.org/software/files/mod_scgi/
Usuario de Apache en Windows:
edite su httpd.conf:

    LoadModule scgi_module Modules/mod_scgi.so
    SCGIMount / 127.0.0.1:8080

reinicie apache y luego corra su code.py con el comando siguiente:

    python code.py 127.0.0.1:8080 scgi

abra su navegador, visite 127.0.0.1.
Funciona!


<a name="apachemodpython"></a>
#### .. con mod_python

mod_python funciona tan bien como FastCGI, pero no es tan sencillo de configurar.

Para Python 2.5 haga lo siguiente:

    cd /usr/lib/python2.5/wsgiref
    # o en windows: cd /python2.5/lib/wsgiref
    wget -O modpython_gateway.py http://svn.aminus.net/misc/modpython_gateway.py
    # u obtenga el fichero de esa dirección utilizando su navegador

Para Python <2.5 haga lo siguiente:

    cd /usr/lib/python2.4/site-packages
    # o en windows: cd /python2.4/lib/site-packages
    svn co svn://svn.eby-sarna.com/svnroot/wsgiref/wsgiref
    cd wsgiref
    wget -O modpython_gateway.py http://svn.aminus.net/misc/modpython_gateway.py
    # u obtenga el fichero de esa dirección utilizando su navegador


Renombre su `code.py` a algo así como `codep.py` y adicione:

    app = web.application(urls, globals())
    main = app.wsgifunc()

En su `.htaccess`, adicione:

    AddHandler python-program .py
    PythonHandler wsgiref.modpython_gateway::handler
    PythonOption wsgi.application codep::main

Probablemente desee añadir una regla de reescritura (`RewriteRule`) apuntando `/` a `/codep.py/`

Asegúrese de visitar `/codep.py/` con el `/` al final. De otra forma, verá un mensaje de error como `A server error occurred. Please contact the administrator.`

<a name="apachemodwsgi"></a>
#### .. con mod_wsgi

mod\_wsgi es un nuevo módulo de Apache que  [típicamente mejora el rendimiento respecto a mod_python](http://code.google.com/p/modwsgi/wiki/PerformanceEstimates) a la hora de alojar aplicaciones WSGI, y que además es muy fácil de configurar.</div>

Al final de su `code.py`, adicione:

    app = web.application(urls, globals(), autoreload=False)
    application = app.wsgifunc()

mod\_wsgi ofrece [muchas maneras posibles](http://code.google.com/p/modwsgi/wiki/ConfigurationDirectives) para exponer una aplicación WSGI en la jerarquía de URL de Apache. Una manera muy simple sería adicionar lo siguiente en su .htaccess:

    <Files code.py>
        SetHandler wsgi-script
        Options ExecCGI FollowSymLinks
    </Files>

Si obtiene un "ImportError: No module named web" en el archivo error.log de Apache, puede intentar fijar el camino absoluto in code.py antes de importar el módulo web:

    import sys, os
    abspath = os.path.dirname(__file__)
    sys.path.append(abspath)
    os.chdir(abspath)
    import web

También, puede que desee leer la sección "Directorio de trabajo de la aplicación" en [Problemas comunes con aplicaciones WSGI](http://code.google.com/p/modwsgi/wiki/ApplicationIssues).

El sitio debe estar accesible en `http://ejemplo.com/code.py/` como es habitual.

<a name="apachemodrewrite"></a>
#### Reglas mod_rewrite para Apache

Si desea que web.py sea accesible en 'http://ejemplo.com' en vez de en 'http://ejemplo.com/code.py/', adicione las reglas siguientes en su archivo .htaccess:

    <IfModule mod_rewrite.c>
      RewriteEngine on
      RewriteBase /
      RewriteCond %{REQUEST_URI} !^/icons
      RewriteCond %{REQUEST_URI} !^/favicon.ico$
      RewriteCond %{REQUEST_URI} !^(/.*)+code.py/
      RewriteRule ^(.*)$ code.py/$1 [PT]
    </IfModule>

Si el archivo `code.py` se encuentra en el subdirectorio `myapp/`, ajuste el camino RewriteBase a `RewriteBase /myapp/`. Si tiene archivos estáticos como CSS e imágenes que deben pasar a través de web.py, duplique la línea con los íconos para cada camino que desee permitir.
