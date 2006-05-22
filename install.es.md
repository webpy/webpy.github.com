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



#### lighttpd



#### Apache



### mod_python