---
layout: default
title: Application processors
---

# Application processors

Autres langues : [english](/../app_processors) | ...

les Application processors permettent au programmeur d'executer du code commun avant que chaque requête soit traitée. Ceci est utile pour les schémas d'authentification ou pour organiser l'état des utilisateurs à chaque requête. Des processors multiples peuvent être ajoutés par application, et ils seront executés dans l'ordre ou ils ont été ajoutés. Le plus basique processor ressemble à ça:


    def proc(handle):
        # faire tout ce dont vous avez besoin ici
        web.ctx.user = web.cookies(user=None).user
        # renvoi le traitement executé
        return handle()
    
    app = web.application(urls, globals())
    # Ajouter le processor
    app.add_processor(proc)

Le "handle" de l'application processor se réfère au code qui sera envoyé à l'URL correspondante (ou chaque processor successif). Cela vous permet d'utiliser "try" et "except", de cette façon:

        def proc(handle):
            try:
                ret = handle()
            except:
                log_error('Uh oh')
            return ret


Voici un exemple de base sur la façon dont un système d'authentification est créé en utilisant les applications processors. Ce n'est pas sécurisé pour une utilisation réelle; Cela ne vise qu'à démontrer comment les application processors pouvent vérifier quelque chose avant que chaque URL ne soit traitée.


## Exemple
    """ Application processors dans web.py """
    import web
    
    urls = (
        '/', 'Index',
        '/login', 'Login',
        '/logout', 'Logout',
    )
    
    class Index:
    
        def GET(self):
            return '<html>Hello %s <a href="/logout">Logout</a></html>' \
                % web.ctx.username
    
    
    class Login:
        
        def GET(self):
            return """
            <html>
            <form action="" method="post">
                <input type="text" name="username">
                <input type="submit" value="Login">
            </form>
            </html>
            """
    
        def POST(self):
            # only set cookie if user login succeeds
            name = web.input(username=None).username
            if name:
                web.setcookie('username', name)
            raise web.seeother('/')
    
    
    class Logout:
        
        def GET(self):
            web.setcookie('username', '', expires=-1)
            raise web.seeother('/login')
        
    
    
    app = web.application(urls, globals())
    
    # Authentification Processor
    def auth_app_processor(handle):
        path = web.ctx.path
        web.ctx.username = name = web.cookies(username=None).username
        if not name and path != '/login':
            raise web.seeother('/login')
        return handle()
    
    app.add_processor(auth_app_processor)
    
    
    if __name__ == '__main__':
        app.run()