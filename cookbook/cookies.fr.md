---
layout: default
title: Travailler avec les cookies
---

# Travailler avec les cookies

Autre langages: [english](/../cookies) | ...

##Problème:

Comment déposer et récupérer les cookies d'un utilisateur qui navigue sur le site?

##Solution:

Web.py permet d'une façon très simple d'utiliser les méthodes de dépot/récupération de cookies (setting/getting).

###Déposer des cookies
####Vue d'ensemble
    setcookie(name, value, expires="", domain=None, secure=False): 
       
* *name* `(string)` - Le véritable nom du cookie, tel qu'il est stocké par le navigateur, et retourné vers le serveur.
* *value* `(string)` - La valeur que vous voulez stocker sous ce nom.
* *expires* `(int)` - Optionnel. C'est le temps en secondes jusqu'à ce que le navigateur voit le cookie expirer. *Note: ce doit être un entier, pas une chaîne*
* *domain* `(string)` - Le nom de domaine pour lequel le cookie est valide. Par défaut, réglé sur le site d'accueil, cela vous permet de définir le domaine, plutôt que simplement un hôte(tel que `.webpy.org`).
* *secure* `(bool)`- Si vrai, exige que le cookie soit envoyé via HTTPS.

####Exemple

`web.setcookie()` peut être utilisé pour déposer un cookie à un utilisateur, comme ceci:

    class CookieSet:
        def GET(self):
            i = web.input(age='25')
            web.setcookie('age', i.age, 3600)
            return "Age set in your cookie"


L'appel de la classe ci-dessus avec GET déposera un cookie nommé "age" ayant pour valeur par défaut "25" (cette valeur par défaut provient en fait de web.input et non de la fonction setcookie), et qui expirera dans une heure (3600 secondes).


Le troisième (et optionnel) argument de `web.setcookie()`, "expires", vous permet de définir quand vous voulez que votre cookie expire. Tout nombre négatif expirera le cookie immédiatement. Un nombre positif est le nombre de secondes durant lequel le cookie va durer (3600 se traduirait en une heure de durée du cookie). Laisser cet argument vide a pour conséquence, d'expirer le cookie session quand le navigateur s'arrête. Pour créer un cookie permanent, mettez à jour le temps d'expiration du cookie à intervalles réguliers (exemple : quand un utilisateur s'est connecté)


###Récuperer des cookies
####Vue d'ensemble

Il existe de nombreuses méthodes pour retrouver des cookies, en fonction de la réaction souhaitée à un cookie manquant.

#####Méthode 1 (Renvoi None si le cookie n'est pas trouvé):
    web.cookies().get(cookieName)  
        #cookieName est le nom du cookie présenté par le navigateur
#####Méthode  2 (Lève une exception AttributeError si le cookie n'est pas trouvé):
    foo = web.cookies()
    foo.cookieName
#####Méthode  3 (Evite la levée d'exception en attribuant une valeur par défaut au cookie qui n'a pas été trouvé):
    foo = web.cookies(cookieName=defaultValue)
    foo.cookieName   # renvoi la valeur (qui pourrait être par défaut)
        #cookieName est le nom du cookie présenté par le navigateur

####Exemple


`web.cookies()` peut être utilisé pour accéder à un cookie déjà défini. Si un cookie est créé en utilisant le code `web.setcookie()` plus haut, il peut être retrouvé de cette façon:

    class CookieGet:
        def GET(self):
            c = web.cookies(age="25")
            return "Your age is: " + c.age

L'exemple définit une valeur par défaut pour le cookie si il n'existe pas. La raison de fixer une valeur par défaut est que si il y a une tentative de consultation du cookie, mais qu'il n'existe pas, `web.cookies()` lève une exception.

Parfois, vous voudrez savoir concrètement si quelque chose n'existe pas, auquel cas, vous pourrez utiliser quelque chose comme ce qui suit:

    class CookieGet:
        def GET(self):
            try: 
                 return "Votre age : " + web.cookies().age
            except:
                 # Faites ce que vous avez besoin ici
                 return "Le cookie n'existe pas."

Ce code tente d'utiliser le cookie présenté par le navigateur, mais ne lui donne pas une valeur par défaut. Si le cookie n'existe pas, une exception est levée, et la clause `except` est executée, donnant au serveur la possibilité de gérer l'absence de cookie.

ou

    class CookieGet:
        def GET(self):
            age=web.cookies().get(age)
            if age:
                return "Votre age est: %s" % age
            else:
                return "Le cookie n'existe pas."