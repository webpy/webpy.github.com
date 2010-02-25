---
layout: default
title: user authentication
---

# user authentication

#I'm still working on this page, please no body else edit

Other languages : [français](/userauth/fr) | ...

##Problem
You want a system to authenticate users.

##Solution
A user authentication system is made up of a few parts. Adding users, logging users in, logging users out and checking if users are logged in. It also requires a database. For this example we'll be using MD5 and SQLite.

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
        else: return render.base("Those login details don't work.")   

##Notes
Do not use this code on real site - this is only for illustration.