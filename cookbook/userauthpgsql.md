---
layout: default
title: User Authentication with PostgreSQL database
---

# User Authentication with PostgreSQL database

##Problem
- You want a system to authenticate users, with a postgresql database.

##Solution
- A user authentication system could have a lot of functions. For this example, we're only going to manage the authentication process, through a postgresql database.

##Needed
- The only one we need is web.py:

	import web

## 1st: The database
First of all, we need a table for the users. This scheme is very simple, but is enough for a lot of projects.

##
	CREATE TABLE example_users
	(
	  id serial NOT NULL,
	  user character varying(80) NOT NULL,
	  pass character varying(80) NOT NULL,
	  email character varying(100) NOT NULL,
	  privilege integer NOT NULL DEFAULT 0,
	  CONSTRAINT utilisateur_pkey PRIMARY KEY (id)
	)

## 2nd: the urls
There will be 2 states during the login/logout session:

- "Login" is for the login page

- "Reset" for the logout page.

*sessions doesn't work in [debug](/tutorial3.en#developing) mode because it interfere with reloading. see [session_with_reloader](session_with_reloader) for more details.*

##
	web.config.debug = False
	
	urls = (
	  '/login', 'Login',
	  '/reset', 'Reset',
	)
	app = web.application(urls, locals())
	db = web.database(dbn='postgres', db='YOURDB', user='USERNAME', pw='PASSWORD')
	
	store = web.session.DiskStore('sessions')
	session = web.session.Session(app, store,
	                              initializer={'login': 0, 'privilege': 0})


## 3rd: Logged or not logged ?
To manage the access for people who are logged or not, it's very easy. Just define the logged expression like this, and use it for your login/reset classes:

##
	def logged():
		if session.login==1:
			return True
		else:
			return False

## 4th: Easy Privleges Management
I manage my users, in 4 categories: admin+user+reader (logged), and visitors (not logged). The directory template is choosing according to the privilege specified in the table example_users.

##
	def create_render(privilege):
	    if logged():
	        if privilege == 0:
	            render = web.template.render('templates/reader')
	        elif privilege == 1:
	            render = web.template.render('templates/user')
	        elif privilege == 2:
	            render = web.template.render('templates/admin')
	        else:
	            render = web.template.render('templates/communs')
	    else:
	        render = web.template.render('templates/communs')
	    return render

	
## 5th: Login and Reset Python Classes
Now, let's have fun:
- If you are already logged, you are redirecting to the login_double.html template file
- Else, to the login.html.

##
	class Login:
	
	    def GET(self):
	        if logged():
	            render = create_render(session.privilege)
	            return '%s' % render.login_double()
	        else:
	            render = create_render(session.privilege)
	            return '%s' % render.login()

- Ok, ok. Now, for the POST(). According to the .html file, we recover the variables posted in the form (see the login.html), and we compare it to the example_users.user row.
- If the login/pass is ok, redirect to the login_ok.html.
- If not, redirect to the login_error.html.

##	
	    def POST(self):
	        name, passwd = web.input().name, web.input().passwd
	        ident = db.select('example_users', where='name=$name', vars=locals())[0]
	        try:
	            if passwd == ident['pass']:
	                session.login = 1
	                session.privilege = ident['privilege']
	                render = create_render(session.privilege)
	                return render.login_ok()
	            else:
	                session.login = 0
	                session.privilege = 0
	                render = create_render(session.privilege)
	                return render.login_error()
	        except:
	            session.login = 0
	            session.privilege = 0
	            render = create_render(session.privilege)
	            return render.login_error()


For the reset function, we just kill the session, and redirect to the logout.html template file.
##
	class Reset:
	
	    def GET(self):
	        session.login = 0
	        session.kill()
	        render = create_render(session.privilege)
	        return render.logout()


## 6th: HTML templates help
Well, I think that nobody will need this, but, I prefer to give all the informations. The most important is the login.html.

##
	<form action="/login" method="POST">
		<table id="login">
			<tr>
				<td>User: </td>
				<td><input type="text" name="user"></td>
			</tr>
			<tr>
				<td>Password: </td>
				<td><input type="password" name="passwd"></td>
			</tr>
			<tr>
				<td></td>
				<td><input type="submit" value="LOGIN"></td>
			</tr>
		</table>
	</form>

## 7th: Some problems or questions ?
- Mail: you can contact me at guillaume(at)process-evolution(dot)fr
- IRC: #webpy on irc.freenode.net (pseudo: Ephedrax)
- Translations: I'm french, and my english is bad...you can edit my work
- Revision: Vayn <vayn at vayn dot de>