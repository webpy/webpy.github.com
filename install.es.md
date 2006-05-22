---
layout: default
title: install/es
---

# install/es

Para instalar web.py, descargar de:
    
    http://webpy.org/web.py

en el directorio donde se encuentra sus aplicaciones. También puedes hacer accesible las aplicaciones al directorio de Python site-packages. Para ver donde se encuentra, ejecute:

python -c "import sys; print[x for x in sys.path if x.endswith('site-packages')][-1]"