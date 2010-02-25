---
layout: default
title: Authentification des utilisateurs
---

# Authentification des utilisateurs

Autres langages : [english](/../userauth) | ...



##Problème

Vous souhaitez mettre en place un système pour authentifier les utilisateurs.


##Solution

Un système d'authentification des utilisateurs est constitué de plusieurs éléments. L'ajout d'utilisateurs, la connexion des utilisateurs, leurs déconnexion, et vérifier s'ils sont déjà enregistrés. Cela nécessite aussi une base de données. Dans cet exemple nous allons utiliser MD5 et SQLite.

##
    import hashlib
    import web    

    def POST(self):
        i = web.input()

        authdb = sqlite3.connect('users.db')
        pwdhash = hashlib.md5(i.password).hexdigest()
        check = authdb.execute('select * from users where username=? and password=?', (i.username, pwdhash))
        if check: 
            session.loggedin = True
            session.username = i.username
            raise web.seeother('/results')   
        else: return render.base("Ces données de connexion ne fonctionnent pas.")   

##Notes

N'utilisez pas ce code sur un site réel. Il n'est là que pour illustrer.