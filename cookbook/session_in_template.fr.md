---
layout: default
title: Utiliser session dans les gabarits
---

# Utiliser session dans les gabarits

Autre langages: [english](/../session_in_template) | ...


##Problème: 

Vous souhaitez utiliser session dans votre gabarit (par exemple pour obtenir session.username et l'afficher)

##Solution:

Dans le code de votre application:

    render = web.template.render('templates', globals={'context': session})

Dans le gabarit:

    <span>Vous êtes connecté en tant que:  <b>$context.username</b></span>

Vous pouvez littéralement utiliser n'importe quel nom de variables python valides, comme les _context_ utilisés ci-dessus. *I would prefer just use 'session' in real applications.*

[Note traducteur: la dernière phrase n'a pas été comprise]