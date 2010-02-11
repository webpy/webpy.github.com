---
layout: default
title: CGI deployment on Apache
---

# CGI deployment on Apache

Here are the simple steps needed to create and run an web.py application.

* Install web.py and flups

* Create the application as documented

        if __name__ == "__main__":
            web.application(urls, globals()).run()

For our example, let it be named `app.py`, located in `/www/app` and we need it accessible as `http://server/app/app.py`.

* Configure Apache (version 2.2 in this example)

        ScriptAlias /app "/www/app/"
        <Directory "/www/app/">
                Options +ExecCGI +FollowSymLinks
                Order allow,deny
                Allow from all
        </Directory>

That's it. Your application is accessible via `http://server/app/app.py/`. Additional URLs handled by the application are added to the end of the URL, for examples `http://server/app/app.py/myurl`.

* .htaccess configuration 

              Options +ExecCGI
              AddHandler cgi-script .py
              DirectoryIndex index.py
              <IfModule mod_rewrite.c>
                  RewriteEngine on
                  RewriteBase /
                  RewriteCond %{REQUEST_FILENAME} !-f
                  RewriteCond %{REQUEST_FILENAME} !-d
                  RewriteCond %{REQUEST_URI} !^/favicon.ico$
                  RewriteCond %{REQUEST_URI} !^(/.*)+index.py/
                  RewriteRule ^(.*)$ index.py/$1 [PT]
              </IfModule>

Here it is assumed that your application is called index.py. The above htaccess checks if some static file/directory exists failing which it routes the data to your index.py. Change the Rewrite Base to a sub-directory if needed.

#Hiding the script name using mod_rewrite (tested with webpy 0.33)

(warning: this section written by someone new to webpy; it works, but may not follow prescribed practices)

If you want your app accessible as `http://server/app/` and not `http://server/app/app.py/` (i.e. `http://server/app/articles/` and not `http://server/app/app.py/articles`) then you need to tweak mod_rewrite a bit. Here's an example of the relevant bit in a .htaccess file (placed in `/www/app` or wherever `app.py` is):

    RewriteEngine on
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteRule ^(.*)$ app.py/$1 [L]

It's cruder than the rewrite rules presented above. The first rule states that if a file exists it should be served by the webserver (ideally you'd want something more secure than that, like only certain file types, or only static/). The second line says in any request of form `.../app.py/blah` we should run `app.py` and give it `blah`.

So now if you go to `http://server/app/` you'll hit `app.py`'s handler for `'/'`. If you go to `http://server/app/articles`, the handler for `'/articles'`, etc.

Are we done? Well, that's what I thought. There's still one problem: webpy doesn't know how things were rewritten on the way *in*, so it doesn't know how to rewrite them on the way *out*.

For instance, one can normally use `web.url()` to compose urls such that the right content is found. Want `static/style.css`? Call `web.url('/static/style.css') and you'll get ... `/app/app.py/static/style.css` ... not what we wanted. That doesn't exist. Problem.

If you don't use `web.url()`, it can still bite you because *webpy* does. Say `raise web.seeother('/')` and you'll end up at `http://server/app/app.py/`, which defeats the purpose of hiding it using mod_rewrite.

How to fix that prefix on the way out then? That's stored in `web.ctx.homepath`. Unfortunately, efforts to modify that didn't work for me. Some old forum post said it comes from the environment variable `SCRIPT_NAME` but that didn't work either. It turns out `REAL_SCRIPT_NAME` works though, so we can add the following to our `app.py`, before initialising webpy:

    import os

    home = '/app'
    os.environ["SCRIPT_NAME"] = home
    os.environ["REAL_SCRIPT_NAME"] = home

    #and calling web.application or whatever goes here or after

This seems to work. Running `raise web.seeother('/')` gets us to `http://server/app/` like we wanted.