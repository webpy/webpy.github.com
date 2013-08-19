---
layout: default
title: install/es
---

# install/es

## Instalación

Para instalar web.py, descargar de:
    
    http://webpy.org/web.py

en el directorio donde se encuentra sus aplicaciones. También puedes hacer accesible las aplicaciones al directorio de Python site-packages. Para ver donde se encuentra, ejecute:

    python -c "import sys; print[x for x in sys.path if x.endswith('site-packages')][-1]"
## Producción

El servidor web que inicias cuando ejecutas un programa en web.py, es algo muy agradable y placentero, pero si deseas sitios más populares, es interesante tener montado algo un poco más serio.

### FastCGI

Lighttpd con soporte FastCGI lo más recomendable para montar web.py en un sitio en producción. Sitios como [reddit.com][3] soportan millones de peticiones y está funcionando con Lighttpd + FastCGI.

   [3]: http://reddit.com/

Al inicio de su code.py añade:

    #!/usr/bin/env python

Y ejecute chmod +x code.py


#### lighttpd

Su configuración lighttpd puede ser parecida a:

     server.modules = ("mod_fastcgi", "mod_rewrite")
     server.document-root = "/path/to/root/"     fastcgi.server = ( "/code.py" =>     (( "socket" => "/tmp/fastcgi.socket",
        "bin-path" => "/path/to/root/code.py",
        "max-procs" => 1
     ))
     )
    
     url.rewrite-once = (
       "^/favicon.ico$" => "/static/favicon.ico",
       "^/static/(.*)$" => "/static/$1",
       "^/(.*)$" => "/code.py/$1",
     )
    

#### Apache

Si deseas utilizar FastCGI con Apache en lugar de otra opción, tienes que instalar mod_fastcgi y usar .htaccess así: 

    <Files code.py>    SetHandler fastcgi-script
    </Files>
Desafortunadamente, con Apache no pasa como con lighttpd, y tenemos que decirle de forma explícita que interactuamos con el servidor FastCGI, así que tenemos que añadir este código para decirle a web.py que usamos el servidor FastCGI:

    web.runwsgi = web.runfcgi


### mod_python
mod_python se desempeña tan bien como FastCGI, pero no es tan fácil de configurar.

Para Python 2.5 haz esto:

    cd /usr/lib/python2.5/wsgiref
    # o en windows: cd /python2.5/lib/wsgiref
    wget -O modpython_gateway.py http://svn.aminus.net/misc/modpython_gateway.py
    # o descarga el archivo de la direccion usando tu navegador

Para Python <2.5 haz esto:

    cd /usr/lib/python2.4/site-packages
    # o en windows: cd /python2.4/lib/site-packages
    svn co svn://svn.eby-sarna.com/svnroot/wsgiref/wsgiref
    cd wsgiref
    wget -O modpython_gateway.py http://svn.aminus.net/misc/modpython_gateway.py
    # o descarga el archivo de la direccion usando tu navegador


Renombra el archivo `code.py` a algo como `codep.py` y agrega:
    
    app = web.application(urls, globals())
    main = app.wsgifunc()

En tu `.htaccess`, agrega:
    
    
    AddHandler python-program .py
    PythonHandler wsgiref.modpython_gateway::handler
    PythonOption wsgi.application codep::main
    

Tambien querras agregar a `RewriteRule` apuntando a `/` to `/codep.py/`

Asegurate de visitar `/codep.py/` con el extra `/` al final. De lo contrario, veras un error como `A server error occurred. Please contact the administrator.`

<a name="apachemodwsgi"></a>
#### .. with mod_wsgi

mod\_wsgi es un nuevo modulo de Apache el cual [usualmente es mejor en desempeño a mod_python](http://code.google.com/p/modwsgi/wiki/PerformanceEstimates) for hosting WSGI applications, and is very easy to set up. <div style="text-indent:-90000px;">[Watch Live Sports Online](http://www.sportspiks.com)[Watch tv episodes online](http://purehunting.blogspot.com)[Watch movies Online](http://www.overheadmovies.com)[Watch Resident Evil Afterlife (2010) Online](http://www.overheadmovies.com/action/resident-evil-afterlife-2010)</div>

Al final del archivo `code.py`, agrega:

    app = web.application(urls, globals(), autoreload=False)
    application = app.wsgifunc()

mod\_wsgi ofrece [muchas maneras](http://code.google.com/p/modwsgi/wiki/ConfigurationDirectives) de exponer la aplicación WSGI en la estructura jerarquica de Apache, pero una forma sencilla será de agregar lo siguiente a tu .htaccess:

    <Files code.py>
        SetHandler wsgi-script
        Options ExecCGI FollowSymLinks
    </Files>

Si obtienes un "ImportError: No module named web" in your apache error.log file, you could try setting the absolute path in code.py before importing web:

    import sys, os
    abspath = os.path.dirname(__file__)
    sys.path.append(abspath)
    os.chdir(abspath)
    import web

Also, you might want to read the "Application Working Directory" section from [Common problems with WSGI application](http://code.google.com/p/modwsgi/wiki/ApplicationIssues).

It should then be accessible at `http://example.com/code.py/` as usual.



<a name="apachemodrewrite"></a>
#### mod_rewrite Reglas para Apache

Si quieres que web.py sea accesible a 'http://example.com' en vez de 'http://example.com/code.py/' agrega la sigueinte regla al archivo `.htaccess`:

    <IfModule mod_rewrite.c>      
      RewriteEngine on
      RewriteBase /
      RewriteCond %{REQUEST_URI} !^/icons
      RewriteCond %{REQUEST_URI} !^/favicon.ico$
      RewriteCond %{REQUEST_URI} !^(/.*)+code.py/
      RewriteRule ^(.*)$ code.py/$1 [PT]
    </IfModule>
Si el archivo `code.py` esta en el subfolder `myapp/`, ajusta el archivo RewriteBase a `RewriteBase /myapp/`. Si tienes los archivos estaticos como los CSS y las imagenes para pasar, duplica la linea con los iconos para cada ruta  que quieras agregar.
