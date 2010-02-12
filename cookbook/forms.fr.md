---
layout: default
title: Comment utiliser les formulaires
---

# Comment utiliser les formulaires

Autre langages: [english](/../forms) | ...

## Problème:

Comment utiliser les formulaires ?

## Solution: 

Le module `web.form`  fournit un support pour créer, valider et interpréter les formulaires.
Ce module contient une classe `Form` et des classes pour diverses entrées de type `Textbox`, `Password`, etc...


Chaque entrée peut prendre une liste de validateurs comme arguments qui sont validées par rapport à l'entrée lorsque `form.validates ()` est appelée.

La classe `Form` peut aussi prendre le mot-clé supplémentaire `validators` en arguments pour valider le formulaire en utilisant la saisie complète.

Voici un exemple de formulaire d'enregistrement d'un nouvel utilisateur.

    import web
    from web import form

    render = web.template.render('templates') # your templates

    vpass = form.regexp(r".{3,20}$", 'must be between 3 and 20 characters')
    vemail = form.regexp(r".*@.*", "must be a valid email address")

    register_form = form.Form(
        form.Textbox("username", description="Username"),
        form.Textbox("email", vemail, description="E-Mail"),
        form.Password("password", vpass, description="Password"),
        form.Password("password2", description="Repeat password"),
        form.Button("submit", type="submit", description="Register"),
        validators = [
            form.Validator("Passwords did't match", lambda i: i.password == i.password2)]

    )

    class register:
        def GET(self):
            # do $:f.render() in the template
            f = register_form()
            return render.register(f)

        def POST(self):
            f = register_form()
            if not f.validates():
                return render.register(f)
            else:
                # do whatever is required for registration

Et le gabarit doit ressembler à ca:

    $def with(form)

    <h1>Register</h1>
    <form method="POST">
        $:form.render()
    </form>