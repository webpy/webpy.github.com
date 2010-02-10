---
layout: default
title: FAQ
---

# FAQ

Autres langages : [español](/faq/es) | [russian ???????](/faq/ru) |[ Japan 日本語](/faq/ja) | [chinese 简体中文](/faq/zh-cn) | [english](/faq) | ...


Des exemples de code pour de nombreuses questions communes peuvent être trouvées dans la section [cookbook](/cookbook/fr).
    
99. **Pourquoi les urls ne sont qu'une longue liste?**

    Si elles étaient de type dictionnaire, elles ne seraient pas classées. Si c'etait une liste tuples, ce serait plus long à taper.

99. **Comment puis-je servir des fichiers statiques comme les JavaScripts ou des images de type PNG ou JPG avec le serveur web.py?**

    Créez un repertoire ( ou dossier) appelé 'static' au même emplacement que le script qui fait tourner le server web.py (par défaut code.py). Puis placez les fichiers statiques (scripts javascripts, css, images) que vous voulez servir dans ce dossier 'static'. Par exemple, l'URL 'http://localhost/static/logo.png' enverra l'image './static/logo.png' au client.

99. **Où puis-je trouver de l'aide supplémentaire??**

    Les Groupes Google proposent le [groupe web.py ](http://groups.google.com/group/webpy) qui est très utile.

99. **Comment afficher un débugage dans la console**

	web.debug("Je serai affiché dans la console et NON dans le corps de la page web.")

99. **Je suis tombé sur un bug dans web.py. Ou puis-je l'annonçer?**

	Allez sur le site [webpy launchpad](https://launchpad.net/webpy), connectez-vous (ou enregistrez-vous) et cliquez sur "report a bug".

99. **Qu'est-ce que ce fameux 'ctx' que je vois dans les exemples ?**

	'ctx' est une classe qui permet d'utiliser des variables contextuelles dans votre code, comme par exemple, la page  référante, le navigateur du client... voir [web.ctx](/cookbook/ctx/fr)