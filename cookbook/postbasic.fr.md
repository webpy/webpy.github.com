---
layout: default
title: Lire les données brutes d un post
---

# Lire les données brutes d un post

Autres langages: [English](/../postbasic) | ...

## Probleme:

Parfois, le client envoie de nombreuses données par la péthode post. Dans webpy, vous pouvez les traiter de cette façon:

## Solution:

    class RequestHandler(object):
        def POST(self):
            data = web.data() # Vous pouvez obtenir les données en utilisant cette méthode
