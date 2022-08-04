---
layout: default
title: "Templator: le système de gabarits de web.py"
---

# Templator: le système de gabarits de web.py

Autre langues : [English](/docs/0.3/templetor) | ...

## Sommaire

* [Introduction](#introduction)
* [Utiliser un modèle de gabarit](#using)
* [Syntaxe](#syntax)
	* [Substitution d'expression](#expressionsubstitution)
	* [Attribution](#attribut)
	* [Filtrage](#filtrering)
	* [Suppression d'un retour à la ligne](#newlinesuppression)
	* [Caractère d'échappement '$'](#escaping)
	* [Commentaires](#comments)
	* [Structures de contrôle](#controlstructure)
* [Autres déclarations](#otherstatements)
	* [$def : définir une nouvelle fonction de gabarit](#def)
	* [$code : écrire du code python dans le gabarit](#code)
	* [$var : définir des propriétés additionnelles dans les résultats du gabarit](#var)
* [Objets internes et variables globales](#builtins)
* [Sécurité](#security)
* [Mise à jour depuis le gabarit web.py 0.2](#upgrading)

<h1 id="introduction">Introduction</h1>

Le langage de gabarit de web.py, appelé 'Templator', est conçu pour apporter la puissance de python aux modèles de gabarits.
Au lieu d'inventer une nouvelle syntaxe pour les gabarits, il réutilise la syntaxe de python.
Si vous connaissez le langage de programmation python, vous serez à l'aise. 

Templator limite intentionnellement l'accès aux variables dans un gabarit. Un utilisateur a accès aux variables passées dans le modèle de gabarit ainsi qu'à certaines fonctions Python intégrées. Cela permet aux utilisateurs maladroits d'écrire des gabarits, sans vous soucier de causer des dommage au système en cours d'exécution. Vous pouvez, bien sûr, augmenter les variables globales disponibles, c'est ce que nous verrons plus tard.

Voici un gabarit tout simple:

    $def with (name)
    Hello $name!

La première ligne indique que le gabarit est défini avec un argument appelé 'name'.
`$name` dans la seconde ligne sera remplacé par la valeur de name lorsque le template sera rendu.

<h1 id="using">Utiliser un modèle de gabarit</h1>

La façon la plus imple d'utiliser le rendu de gabarits est celle-ci :

    render = web.template.render('templates')
    print render.hello('world')
   
La fonction 'render' prend comme argument le repertoire 'templates'. 'render.hello(..)' appelle le gabarit 'hello.html' avec les arguments donnés. En fait, il cherche les fichiers correspondants 'hello.*' dans le repertoire 'template' et sélectionne le premier fichier correspondant.

Vous pouvez également créer des modèles à partir d'un fichier en utilisant 'frender'.

    hello = web.template.frender('templates/hello.html')
    print hello('world')
    
Ou encore à partir d'une chaîne de caractères:

    template = "$def with (name)\nHello $name"
    hello = web.template.Template(template)
    print hello('world')

<h1 id="syntax">Syntaxe</h1>

<h2 id="expressionsubstitution">Substitution d'expression</h2>

Le caractère spécial '$' est utilisé pour spécifier des expressions python. Les expressions peuvent être jointent dans '()' ou '{}' pour un regroupement explicite.

    Look, a $string. 
    Hark, an ${arbitrary + expression}. 
    Gawk, a $dictionary[key].function('argument'). 
    Cool, a $(limit)ing.

<h2 id="attribut">Attribution</h2>

Vous aurez parfois besoin de définir de nouvelles variables et de réattribuer certaines d'entre elles.
    
    $ bug = get_bug(id)
    <h1>$bug.title</h1>
    <div>
        $bug.description
    <div>
     
Notez l'espace après '$' dans l'attribution. Il est requis pour différencier l'attribution à la substitution d'expression.

<h2 id="filtrering">Filtrage </h2>

Par defaut, Templator utilise le filtre 'web.websafe' pour encoder le HTML.

    >>> render.hello("1 < 2")
    "Hello 1 &lt; 2"

Pour désactiver le filtre, utilisez ':' après '$'. Par exemple:

    Ce qui suit ne sera pas remplacé par une chaîne HTML ("&" par "&amp;" par exemple).
    $:form.render()

<h2 id="newlinesuppression">Suppression d'un retour à la ligne</h2>

Un retour à la ligne peut-être supprimé en ajoutant l'anti-slash '\' à la fin de la ligne.

    Si vou ajoutez un anti-slash \ 
    à la fin de la ligne \ 
    (comme ceci) \ 
    alors il n'y aura pas de retour à la ligne.
    
<h2 id="escaping">Caractère d'échappement '$'</h2>

Utilisez `$$` pour avoir `$` (signe dollars) à l'affichage.

    Can you lend me $$50?
    
<h2 id="comments">Commentaires</h2>

'$#' est utilisé comme indicateur de commentaires. Tout ce qui commence par '$#' jusqu'à la fin de la ligne sera ignoré.

    $# Ceci est un commentaire
    Hello $name.title()! $# Affiche le nom comme titre

<h2 id="controlstructure">Structures de contrôles</h2>

Le système de gabarit accepte les instructions `for`, `while`, `if`, `elif` et `else`.
Tout comme en Python, le corps de la déclaration est indenté.

    $for i in range(10): 
        I like $i

    $for i in range(10): I like $i
        
    $while a:
        hello $a.pop()

    $if times > max: 
        Stop! In the name of love. 
    $else: 
        Keep on, you can do it.

La boucle fixe un certain nombre de variables disponibles dans la boucle:

    loop.index: iteration de la boucle (1-indexé)
    loop.index0: iteration de la boucle (0-indexé)
    loop.first: Vrai si c'est la première itération
    loop.last: Vrai si c'est la dernière itération
    loop.odd: Vrai si une itération impaire
    loop.even: Vrai si une itération paire
    loop.parity: "impair" ou "paire" selon ce qui est vrai
    loop.parent: la boucle ci-dessus est une boucle imbriquée
    
Parfois, celles-ci peuvent être très pratique.

    <table>
    $for c in ["a", "b", "c", "d"]:
        <tr class="$loop.parity">
            <td>$loop.index</td>
            <td>$c</td>
        </tr>
    </table>
    
<h2 id="otherstatements">Autres déclarations</h2>

<h3 id="def">$def</h3>

Vous pouvez définir une nouvelle fonction de gabarit en utilisant `$def`. les arguments-clés sont aussi supportés.

    $def say_hello(name='world'):
        Hello $name!
    
    $say_hello('web.py')
    $say_hello()

Autre exemple
        
    $def tr(values):
        <tr>
        $for v in values:
            <td>$v</td>
        </tr>

    $def table(rows):
        <table>
        $for row in rows:
            $:row
        </table>
    
    $ data = [['a', 'b', 'c'], [1, 2, 3], [2, 4, 6], [3, 6, 9] ]
    $:table([tr(d) for d in data])
    
<h3 id="code">$code</h3>

Du code python arbitraire peut être écrit en utilisant le bloc '$code'.

    $code:
        x = "you can write any python code here"
        y = x.title()
        z = len(x + y)
        
        def limit(s, width=10):
            """limits a string to the given width"""
            if len(s) >= width:
                return s[:width] + "..."
            else:
                return s
                
    Puis nous revenons dans le code du gabarit.
    Les variables définies dans le bloc '$code' peuvent être utilisées ici.
    Par exemple, $limit(x)
  
<h3 id="var">$var</h3>

Le bloc '$var' peut être utilisé pour définir des propriétés additionnelles dans les résultats du gabarit.

    $def with (title, body)
    
    $var title: $title
    $var content_type: text/html
    
    <div id="body">
    $body
    </div>
    
Les résultat du modèle ci-dessus peuvent être utilisés comme suit:

    >>> out = render.page('hello', 'hello world')
    >>> out.title
    u'hello'
    >>> out.content_type
    u'text/html'
    >>> str(out)
    '\n\n<div>\nhello world\n</div>\n'

<h1 id="builtins">Objets internes et variables globales</h1>

Comme toutes fonctions python, le gabarit peut également accèder aux objets internes avec ses arguments et ses variables locales.
Quelques fonctions internes communes telles que 'range', 'max', 'min', etc... et les valeurs booléennes 'True' et 'False' sont accessibles à tous les gabarits.

Outre les fonctions intégrées, les globales spécifique d'application peuvent être spécifiées pour les rendre accessibles à tous les gabarits. [NOTE TRADUCTEUR : A préciser]

Les variables globales peuvent être spécifiées comme arguments à `web.template.render`.

    import web
    import markdown
    
    globals = {'markdown': markdown.markdown}
    render = web.template.render('templates', globals=globals)

Les objets internes qui sont exposés dans les gabarits peuvent aussi être contrôlées. [NOTE TRADUCTEUR: la traduction de Builtins et Globals est à vérifier]

    # disable all builtins
    render = web.template.render('templates', builtins={})

<h1 id="security">Securité</h1>

L'un des objectifs de conception de Templetor est de permettre à des utilisateurs non épprouvés d'écrire des gabarits.

Pour rendre l'exécution du gabarit sûre, ce qui suit n'est pas autorisé dans les templates.

* Les déclarations telles que `import`, `exec` etc.
* Accéder aux attributs qui commencent par `_`
* Des fonctions internes telles que `open`, `getattr`, `setattr` etc.

`SecurityException` est déclenchée si votre modèle utilise l'une de celles-ci.

<h1 id="upgrading">Mise à jour depuis le gabarit web.py 0.2</h1>

La nouvelle implémentation est totalement compatible avec la mise en œuvre plus haut. Cependant, certains cas pourraient ne pas fonctionner pour les raisons suivantes:

* Le rendu du gabarit est toujours stocké comme un objet `TemplateResult`, toutefois, le convertir en 'unicode' ou 'str' donne le résultat sous forme de chaîne unicode.

* La réassignation d'une valeur globale ne fonctionnera pas. Ce qui suit ne fonctionnera pas si x est une globale.
    
        $ x = x + 1
    
Ce qui suit est toujours supporté, mais peu recommandé.

* Utiliser `\$` pour l'échappement. Utilisez plutôt '$$'.
* Modifier `web.template.Template.globals`. Passez plutôt les globales à `web.template.render` en argument à la place.