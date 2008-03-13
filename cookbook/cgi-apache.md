---
layout: default
title: CGI deployment on Apache
---

# CGI deployment on Apache

Here are the simple steps needed to create and run an web.py application.

* Install web.py and flups

* Create the application as documented

        if __name__ == "__main__":
            web.run(urls, globals())

For our example, let it be named `app.py`, located in `/www/app` and we need it accessible as `http://server/app/app.py`.

* Configure Apache (version 2.2 in this example)

        ScriptAlias /app "/www/app/"
        <Directory "/www/app/">
                Options +ExecCGI +FollowSymLinks
                Order allow,deny
                Allow from all
        </Directory>

That's it. Your application is accessible via `http://server/app/app.py/`. Additional URLs handled by the application are added to the end of the URL, for examples `http://server/app/app.py/myurl`.
