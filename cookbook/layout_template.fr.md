---
layout: default
title: Mise en page selon un gabarit
---

# Mise en page selon un gabarit

Autres langages : [english](/../layout_template) | ...



### Problème


Comment puis-je utiliser un modèle/gabarit de site qui s'affiche dans chaque page? (Dans d'autres frameworks, cela s'appelle l'héritage des templates - template inheritance)

### Solution


Cela peut être fait en utilisant l'attribut de base:

    render = web.template.render('templates/', base='layout')
    

Maintenant si vous faites quelque chose comme `render.foo ()` il cherchera le gabarit `templates/foo.html`, puis l'enveloppera dans le gabarit `templates/layout.html`



Le format de "layout.html" doit être un simple gabarit qui contient une variable. Par exemple:

    $def with (content)
    <html>
    <head>
        <title>Foo</title>
    </head>
    <body>
    $:content
    </body>
    </html>


Si vous ne souhaitez pas utiliser le modèle de base, il suffit de créer un deuxième objet, sans l'attribut "base", ainsi:

    render_plain = web.template.render('templates/')
    
###Astuce: Le titre de page est défini dans d'autres fichiers gabarits qui sont ensuite utilisés par la mise en page (layout.html). Par exemple:

#####templates/index.html
    $var title: This is title.

    <h3>Hello, world</h3>

#####templates/layout.html
    $def with (content)
    <html>
    <head>
        <title>$content.title</title>
    </head>
    <body>
    $:content
    </body>
    </html>


###Astuce: Ajouter des fichiers css dans d'autres fichiers gabarits. Exemple:

####templates/login.html

    $var cssfiles: static/login.css static/login2.css

    hello, world.

####templates/layout.html

    $def with (content)
    <html>
    <head>
        <title>$content.title</title>

        $if content.cssfiles:
            $for f in content.cssfiles.split():
                <link rel="stylesheet" href="$f" type="text/css" media="screen" charset="utf-8"/>

    </head>
    <body>
    $:content
    </body>
    </html>

Le code HTML de sortie ressemble à celui ci-dessous:

    <link rel="stylesheet" href="static/login.css" type="text/css" media="screen" charset="utf-8"/>
    <link rel="stylesheet" href="static/login2.css" type="text/css" media="screen" charset="utf-8"/>