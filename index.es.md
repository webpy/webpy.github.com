---
layout: default
title: ¡Bienvenido a web.py!
---

Other langages : [Inglés](/index.html) | [Francés](/index.fr.html) | ...

## Acerca de web.py

**web.py** es un framework para desarrollo web sobre Python que es simple y potente. web.py se encuentra en el dominio público: puedes usarlo para cualquier propósito sin restricción alguna.

<div style="float: right; margin: 1em">
<pre>
import web

urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hola, ' + name + '!'

if __name__ == "__main__":
    app.run()
</pre>
<em>Una aplicación web.py completa.</em>
</div>

## Para comenzar

Para instalar la última versión de web.py, corra en un terminal:

    pip install web.py

La última versión `0.40` soporta tanto Python 2.7 como Python >= 3.5.

Si prefiere descargar la última versión de desarrollo de git:
    
    git clone git://github.com/webpy/webpy.git
    ln -s `pwd`/webpy/web .

## Quién utiliza web.py?

web.py fue publicado originalmente cuando Aaron Swartz trabajaba en [reddit.com][20], donde el sitio lo utilizó para crecer hasta convertirse en uno de los 1000 primeros sitios de acuerdo a Alexa, sirviendo millones de páginas diariamente. "Es el framework anti-framework. web.py no se interpone en tu camino," explicó el fundador Steve Huffman. (El sitio fue reescrito usando otras herramientas después de su adquisición por Condé Nast.)

   [20]: http://reddit.com/

### Algunos testimonios de usuarios:

* "En el ecosistema de los frameworks web, alguno debe ocupar el nicho de 'pequeño, ligero y rápido': web.py hace eso."*  
<span class="cite">&nbsp;&nbsp;&mdash;&nbsp; Lloyd Dalton, [colr.org](http://colr.org)</span>

* "Hemos terminado de reescribir nuestro servidor en apenas unos días con la ayuda de web.py y tuvo todo lo que esperábamos."*  
<span class="cite">&nbsp;&nbsp;&mdash;&nbsp; Sam Hsiung, [YouOS][25]</span>

   [25]: http://www.youos.com/

* "[Web.py inspiró] el web framework que usamos en FriendFeed [y] el framework para aplicaciones web que se entrega con App Engine..."*  
<span class="cite">&nbsp;&nbsp;&mdash;&nbsp; [Brett Taylor](http://backchannel.org/blog/google-app-engine), co-fundador de FriendFeed y líder técnico original en Google App Engine</span>

* "Django te permite escribir aplicaciones web en Django. TurboGears te permite escribir aplicaciones web en TurboGears. Web.py te permite escribir aplicaciones web en Python."*  
<span class="cite">&nbsp;&nbsp;&mdash;&nbsp; Alice Atlas</span>

* "Guido* [van Rossum, creador de Python]*, probablemente encuentres que web.py es el que mejor se ajusta a tu estilo. ... Si no te gusta, no puedo imaginarme cual de la otra docena de frameworks existentes te __puede__ gustar."*   
<span class="cite">&nbsp;&nbsp;&mdash;&nbsp; Phillip J. Eby, creador de Python Web Server Gateway Interface (WSGI) [#][30]</span>

   [30]: http://www.artima.com/forums/flat.jsp?forum=106&thread=146149&start=30&msRange=15
