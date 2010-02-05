---
layout: default
title: Librairie Formulaires
---

# Librairie Formulaires

# Sommaire

* <a href="#introduction">Introduction</a>
* <a href="#carac">Caracteristiques des entrées formulaires</a>
* <a href="#listes">Listes déroulantes</a>
* <a href="#parti">Particularités des formulaires</a>
* <a href="#exemple">Exemple</a>

<a name="introduction"></a>
## Introduction

Le module de formulaire de web.py permet de générer des formulaires HTML, de récuperer les entrées des utilisateurs, et les valider avant de les traiter ou les ajouter à une base de donnée.

Le module de formulaire définit 2 classes primaires: la classe Form et la classe Input. 

Les formulaires sont instanciés avec une ou plusieurs entrées, et des validateurs optionnels. Les entrées sont instanciées avec une variable nom, ainsi que des arguments optionnels et des validateurs. 

La classe Input est sous-classée dans les entrées html suivantes (type HTML dans les parenthèses):


* Textbox     - Champ de saisie de texte d'une ligne (input type="text")
* Password   - Champ de saisie de texte d'une ligne qui cache ce qui est entré (input type="password")
* Textarea   - Champ de saisie de texte multiligne (textarea)
* Dropdown - Selection d'un seul élément dans une liste déroulante (select and options)
* Radio         - Boutons radio pour un seul choix (input type="radio")
* Checkbox  - Cases à cocher à plusieurs choix (input type="checkbox")
* Button        - Soumettre le formulaire (button)

Un simple formulaire de connexion pourrait ressembler à ceci:

    login = form.Form(
        form.Textbox('username'),
        form.Password('password'),
        form.Button('Login'),
    )

Ceci définit un simple formulaire. Une fois défini, vous devrez l'appeler à nouveau pour obtenir une instance, et alors vous pourrez appeler la méthode de rendu sur elle, de cette façon:

    f = login()
    print f.render()

Ce qui affichera le code HTML suivant:

    <table>
        <tr><th><label for="username">username</label></th><td><input type="text" id="username" name="username"/><div class="post" style="display: none;"></div></td></tr>
        <tr><th><label for="password">password</label></th><td><input type="password" id="password" name="password"/><div class="post" style="display: none;"></div></td></tr>
        <tr><th><label for="Login"></label></th><td><button id="Login" name="Login">Login</button><div class="post" style="display: none;"></div></td></tr>
    </table>

Ce qui donnera:

<table>
    <tr><th><label for="username">username</label></th><td><input type="text" id="username" name="username"/><div class="post" style="display: none;"></div></td></tr>
    <tr><th><label for="password">password</label></th><td><input type="password" id="password" name="password"/><div class="post" style="display: none;"></div></td></tr>
    <tr><th><label for="Login"></label></th><td><button id="Login" name="Login">Login</button><div class="post" style="display: none;"></div></td></tr>
</table>

<a name="carac"></a>
## Caracteristiques des entrées formulaires
Les entrées formulaires offrent quelques attributs additionnels. Par exemple :


    form.textbox("firstname",
        form.notnull, # Place les validateurs en premier, suivi par des attributs facultatifs
        class_="textEntry", # Donne un nom de classe à la zone de texte - à noter le caractère de soulignement (underscore)
        pre="pre", # Directement devant la zone de texte
        post="post", # Directement après la zone de texte
        description="please enter your name", # Décrit le champ, par défaut le nom du formulaire
        value="bob", # Valeur par défaut
        id="nameid", # Spécifier l'ID
    )

En plus des attributs ci-dessus, tous les attributs HTML peuvent être entré de la même manière. Par exemple:
    
    myform2 = form.Form(
        form.textbox('phonenumber',
            size="12",
            maxlength="12"        )
    )

<a name="listes"></a>
##Listes déroulantes  (Dropdown) 

Les entrées des listes déroulantes permettent une description et une valeur uniques de chaque élément dans la liste déroulante. Pour ce faire, créez la liste déroulante avec les tuples comme ceci:
    
    form.Dropdown('mydrop', [('value1', 'description1'), ('value2', 'description2')])

<a name="introduction"></a>
## Particularités des formulaires
En plus des champs de saisie individuels, form.py permet une complète validation de formulaire qui autorise la comparaison des champs. Les validations sont passées sous forme de liste dans une variable 'validators'. Par exemple :

    signup = form.Form(
        form.Textbox('username'),
        form.Password('password'),
        form.Password('password_again'),
        validators = [form.Validator("Passwords didn't match.", lambda i: i.password == i.password_again)]
    )

Une fois les données du formulaire postées, elles peuvent facilement être mises dans une base de données (si la structure de base de données a des noms compatibles avec votre formulaire webpy). Par exemple:

    def POST(self):
        f = myform()
        if f.validates():
            web.insert('data_table', **f.d)
        # NE FAITES PAS: web.insert('data_table', **web.input()) Car des données malicieuses peuvent être envoyées
        else:
            render.foo(f)

<a name="exemple"></a>
## Exemple

    import web
    from web import form

    render = web.template.render('templates/')

    urls = ('/', 'index')
    app = web.application(urls, globals())

    myform = form.Form( 
        form.Textbox("boe"), 
        form.Textbox("bax", 
            form.notnull,
            form.regexp('\d+', 'Must be a digit'),
            form.Validator('Must be more than 5', lambda x:int(x)>5)),
        form.Textarea('moe'),
        form.Checkbox('curly'), 
        form.Dropdown('french', ['mustard', 'fries', 'wine'])) 

    class index: 
        def GET(self): 
            form = myform()
            # make sure you create a copy of the form by calling it (line above)
            # Otherwise changes will appear globally
            return render.formtest(form)

        def POST(self): 
            form = myform() 
            if not form.validates(): 
                return render.formtest(form)
            else:
                # form.d.boe and form['boe'].value are equivalent ways of
                # extracting the validated arguments from the form.
                return "Grrreat success! boe: %s, bax: %s" % (form.d.boe, form['bax'].value)

    if __name__=="__main__":
        web.internalerror = web.debugerror
        app.run()

Ansi que l'exemple formtest.html (à placer dans le sous-repertoire *templates*): 

    $def with (form)

    <form name="main" method="post"> 
    $if not form.valid: <p class="error">Try again, AmeriCAN:</p>
    $:form.render()
    <input type="submit" />    </form>