---
layout: default
title: web.ctx
---

# web.ctx

Autre langages: [english](/../ctx) | ...

Probleme
-------

Vous souhaitez utiliser des variables contextuelles dans votre code comme la page référante ou le navigateur du client.


Solution
--------

C'est possible en utilisant 'web.ctx'. D'abord un peu d'architecture: 'web.ctx' est basée sur la classe 'threadeddict', alias 'ThreadedDict'. Cette classe crée un objet de type dictionnaire qui possède des attributs spécifiques au processus id de thread. C'est élégant dans la mesure ou cela nous permet d'utiliser un objet de type dictionnaire, tandis que beaucoup d'utilisateurs accèdent au système simultanément, et l'objet ne contiendra que les données de la requête HTTP donnée. (aucune données n'est partagée donc l'objet est ["thread-safe"](http://fr.wikipedia.org/wiki/Threadsafe) -- _On dit qu’un programme ou qu'une portion de code est thread-safe s’il fonctionne correctement durant une exécution simultanée par plusieurs threads (processus légers)_.)


'web.ctx' contient des variables pour chaque requête qui comprennent des informations spécifiques pour chaque demande, comme les variables environnement du client. En supposant que vous vouliez déterminer quelle était la page référante d'un utilisateur accédant à une page: 

Exemple
-------

    class example:
        def GET(self):
            referer = web.ctx.env.get('HTTP_REFERER', 'http://google.com')
            raise web.seeother(referer)


Ce code utilise 'web.ctx.env' pour accéder à l'environnement variables 'HTTP_REFERER'. Si il n'y en a pas, ce sera par défaut google.com. Enfin, il redirige l'utilisateur vers la page d'où il vient.


'web.ctx' est aussi très pratique car il peut-être rêglé par un ['loadhook'] (../application_processors/fr). Les données session, par exemple, sont fixées chaque fois qu'une demande est traitée et les données sont stockées dans 'web.ctx'. Depuis que 'web.ctx' est ["thread-safe"](http://fr.wikipedia.org/wiki/Threadsafe), vous pouvez utiliser les données session comme si elles étaient un objet régulier python.


Données que l'on trouve dans 'ctx'
-------------------

### Request ###
*   `environ` alias 'env' &ndash; un dictionnaire contenant les variables environnement standard de [WSGI](http://www.python.org/dev/peps/pep-0333/#environ-variables)
*   `home` &ndash; le chemin de base pour l'application, y compris tout élément «consommée» par les applications extérieures *http://example.org/admin*
*   `homedomain` &ndash; ? (semble être le protocole + l'hôte) *http://example.org*
*   `homepath` &ndash; La partie du chemin requise par l'utilisateur, déduite de l'application courante. C'est à dire homepath + path = le chemin actuellement requis en HTTP par l'utilisateur. Exemple: */admin*

*   `host` &ndash; le nom d'hôte (domaine) et (si ce n'est pas celui par défaut) le port requis par l'utilisateur. Exemple: *example.org*, *example.org:8080*
*   `ip` &ndash; L'adresse ip de l'utilisateur. exemple: *xxx.xxx.xxx.xxx*
*   `method` &ndash; la méthode HTTP utilisée. exemple: *GET*
*   `path` &ndash; Le chemin demandé par l'utilisateur, relatif à l'aaplication en cours. Si vous utilisez des sous-applications, chaque partie de l'url filtrée par l'application externe sera déduite. Par exemple: vous avez une application principale dans code.py, et une sous application appelée 'admin.py'. Dans 'code.py', vous pointez '/admin' vers 'admin.app'. Dans 'admin.py', vous pointez '/stories' sur une classe nommée 'stories'. Au sein de 'stories', 'web.ctx.path' sera '/stories' et pas '/admin/stories'. Exemple: */articles/845*
*   `protocol` &ndash; Le protocole utilisé. Exemple:  *https*
*   `query` &ndash; Une chaîne vide s'il n'y a pas d'argument de requête autre que '?' suivit par la chaine de requête. Exemple *?fourlegs=good&twolegs=bad*
*   `fullpath` alias 'path + query' &ndash; Le chemin demandé inclut les arguments de requête mais n'inclut *pas* 'homepath'. Exemple : */articles/845?fourlegs=good&twolegs=bad*

### Response ###
*   `status` &ndash; Le code statut HTTP (par defaut '200 OK') *401 Unauthorized*
*   `headers` &ndash; Une liste de deux tuples contenant les en-têtes HTTP (headers)
*   `output` &ndash; Une chaîne contenant l'entité de réponse