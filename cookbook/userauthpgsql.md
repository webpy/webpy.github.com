---
layout: default
title: User Authentication with PostgreSQL database
---

# User Authentication with PostgreSQL database

##Problem
You want a system to authenticate users, with a postgresql database.

##Solution
A user authentication system could have a lot of functions. For this example, we're only going to manage the authentication process, throught a postgresql database.

##Needed
I use mako templates, and pg. So, you have to import all of that:
	import web
	from web.contrib.template import render_mako
	import pg

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
There will be 2 states during the login/logout session. "Login" is for the login page, and "Reset" for the logout page.

##
	urls = (
	 	'/login', 'login',
		'/reset', 'reset',
		 )



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
			if privilege==0:
				render = render_mako(
					directories=['templates/reader'],
					input_encoding='utf-8',
					output_encoding='utf-8',
					)
			elif privilege==1:
				render = render_mako(
					directories=['templates/user'],
					input_encoding='utf-8',
					output_encoding='utf-8',
					)
			elif privilege==2:
				render = render_mako(
					directories=['templates/admin'],
					input_encoding='utf-8',
					output_encoding='utf-8',
					)
		else:
			render = render_mako(
				directories=['templates/communs'],
				input_encoding='utf-8',
				output_encoding='utf-8',
				)
		return render
	
## 5th: Login and Reset Python Classes
Now, let's have fun. If you are already logged, you are redirecting to the login_double.html template file, Else, to the login.html.

##
	class login:
		def GET(self):
			if logged():
				render = create_render(session.privilege)
				return "%s" % (
					render.login_double()				)
			else:
				render = create_render(session.privilege)
				return "%s" % (
					render.login()
					)

Ok, ok. Now, for the POST(). According to the .html file, we recover the variables posted in the form (see the login.html), and we compare it to the example_users.user row. If the login/pass is ok, redirect to the login_ok.html. If not, redirect to the login_error.html.

##	
		def POST(self):
			user, passwd = web.input().user, web.input().passwd
			ident = db.query("select * from example_users where user = '%s'" % (user)).getresult()
			try:
				if passwd==ident[0][2]:
					session.login=1
					session.privilege=ident[0][4]
					render = create_render(session.privilege)
					return "%s" % (
							render.login_ok()
							)
				else:
					session.login=0
					session.privilege=0
					render = create_render(session.privilege)
					return "%s" % (
						render.login_error()
						)
			except:
				session.login=0
				session.privilege=0
				render = create_render(session.privilege)
				return "%s" % (
					render.login_error()
					)

For the reset function, we just kill the session, and redirect to the logout.html template file.
##
	class reset:
		def GET(self):
			session.login=0
			session.kill()
			render = create_render(session.privilege)
			return "%s" % (
				render.logout()
			 	)

## 6th: HTML templates help
Well, I think that nobody will need this, but, I prefer to give all the informations. The most important is the login.html.

##
	<FORM action=/login method=POST>
		<table id="login">
			<tr>
				<td>User: </td>
				<td><input type=text name='user'></td>
			</tr>
			<tr>
				<td>Password: </td>
				<td><input type="password" name=passwd></td>
			</tr>
			<tr>
				<td></td>
				<td><input type=submit value=LOGIN></td>
			</tr>
</table>
	</form>

## 7th: Wowowow