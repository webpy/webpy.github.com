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