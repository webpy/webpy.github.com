---
layout: default
title: Web.py Cookbook
---

# Web.py Cookbook

Autres langages : [japan 日本語](/ja) | [chinese 简体中文](/zh-cn) | [english](/../cookbook) | ...

Documentation de type Cookbook pour web.py 0.3. Veuillez noter que certaines de ces fonctions ne sont pas disponibles dans les versions précedentes. 
La version actuelle 0.3 est la branche développement.

#Mise en forme

1. En termes de mise en forme, essayez d'utiliser un format de type cookbook... Comme ceci:
    
    ###Probleme: Vous voulez accéder aux données de la base ...
     
    ###Solution: Utilisez ce code ...

1. Notez que les urls n'ont pas besoin de "web" dans leur structures -- juste "/cookbook/select" , et pas "/cookbook/web.select".  

1. Cette documentation est finalement pour la version 0.3, donc veuillez ajouter du code qui ne fonctionne qu'avec cette version.

-------------------------------------------------

##Basique:
* [Hello World](/helloworld/fr). 
* [Servir des fichiers statiques](/staticfiles/fr).  
* [Comprendre la gestion des URLs](/url_handling/fr).  
* [Seeother et Redirect](/redirect+seeother/fr).  
* [Utiliser les sous-applications](/subapp/fr).  
* [Servir du XML](/xmlfiles/fr).   
* [Lire les données brutes d'un post](/postbasic/fr). 


##Avancé
* [web.ctx](/ctx/fr). 
* [Application processors, charger et décharger des hooks](/application_processors/fr). 
* [Comment utiliser web.background](/background). - traduction demandée, voir [Todo](/docs/0.3.fr/todo)
* [Personnaliser le message NotFound](/custom_notfound/fr). 
* [Comment streamer de gros fichiers](/streaming_large_files/fr). 
* [Contrôler les evènements sur le serveur intégré par défaut](/logging/fr). 
* [Configurer le support SSL dans le serveur intégré](/ssl/fr).
* [Run-time language switch](/runtime-language-switch). - traduction demandée, voir [Todo](/docs/0.3.fr/todo)

##Sessions et état des utilisateurs:
* [Travailler avec les sessions](/sessions/fr). 
* [Utiliser session avec reloader](/session_with_reloader/fr). 
* [Utiliser session dans les gabarits](/session_in_template/fr). 
* [Travailler avec les cookies](/cookies/fr). 
* [Authentification des utilisateurs](/userauth/fr). 
* [Authentification des utilisateurs avec base de données Postgresql](/userauthpgsql). - traduction demandée, voir [Todo](/docs/0.3.fr/todo)
* [Utiliser les sessions avec les sous-applications](/sessions_with_subapp/fr). 


##Utils:
* [Envoi de Mail](/sendmail). - traduction demandée, voir [Todo](/docs/0.3.fr/todo)
* [Envoi de Mail en utilisant Gmail](/sendmail_using_gmail/fr). 
* [Webservice en utilisant soaplib + WSDL](/webservice). - traduction demandée, voir [Todo](/docs/0.3.fr/todo)

##Modèles de mise en forme, gabarits de mise en page:
* [Templetor: le système de gabarits de web.py](/docs/0.3/templetor.fr )
* [Mise en page selon un gabarit](/layout_template/fr). 
* [Alterner un style](/alternating_style). - traduction demandée, voir [Todo](/docs/0.3.fr/todo)
* [Importer des fonctions dans les gabarits](/template_import). - traduction demandée, voir [Todo](/docs/0.3.fr/todo)
* [i18n support dans les fichiers gabarits](/i18n_support_in_template_file ). - traduction demandée, voir [Todo](/docs/0.3.fr/todo)
* [Utiliser le moteur de gabarit Mako dans webpy](/template_mako). - traduction demandée, voir [Todo](/docs/0.3.fr/todo)
* [Utiliser le moteur de gabarit Cheetah dans webpy](/template_cheetah). - traduction demandée, voir [Todo](/docs/0.3.fr/todo)
* [Utiliser le moteur de gabarit  Jinja2 dans webpy](/template_jinja). - traduction demandée, voir [Todo](/docs/0.3.fr/todo)
* [Comment utiliser les gabarits sur Google App Engine](/templates_on_gae). - traduction demandée, voir [Todo](/docs/0.3.fr/todo))

##Essais:
* [Tester avec Paste et Nose](/testing_with_paste_and_nose). - traduction demandée, voir [Todo](/docs/0.3.fr/todo)
* [RESTful doctesting using an application's request method](/restful_doctesting_using_request). - traduction demandée, voir [Todo](/docs/0.3.fr/todo)

##Entrées utilisateurs:
* [Uploader un fichier](/fileupload/fr). 
* [Stocker un fichier uploadé](/storeupload/fr). 
* [Comment limiter la taille des fichiers uploadés](/limiting_upload_size/fr). 
* [Accéder aux entrées utilisateurs par le biais de web.input](/input/fr). 
* [Comment utiliser les formulaires](/forms/fr). 
* [Rendu individuel des champs de formulaires](/form_fields). - traduction demandée, voir [Todo](/docs/0.3.fr/todo)

##Base de données:
* [Multiples bases de données](/multidbs). - traduction demandée, voir [Todo](/docs/0.3.fr/todo)
* [Select: Récupérer les entrées d'une base de données](/select). - traduction demandée, voir [Todo](/docs/0.3.fr/todo)
* [Update: Mettre à jour les entrées d'une base de données](/update). - traduction demandée, voir [Todo](/docs/0.3.fr/todo)
* [Delete: Supprimer les entrées d'une base de données](/delete). - traduction demandée, voir [Todo](/docs/0.3.fr/todo)
* [Insert: Ajouter des entrées à une base de donnée](/insert).  - traduction demandée, voir [Todo](/docs/0.3.fr/todo)
* [Query: Base de données - Requêtes avancées](/query). - traduction demandée, voir [Todo](/docs/0.3.fr/todo)
* [Query: How to use database transactions](/transactions). - traduction demandée, voir [Todo](/docs/0.3.fr/todo)
* [Comment utiliser sqlalchemy](/sqlalchemy). - traduction demandée, voir [Todo](/docs/0.3.fr/todo)
* [Intégrer SQLite UDF (user-defined-functions) à la couche de base de données webpy](/sqlite-udf). - traduction demandée, voir [Todo](/docs/0.3.fr/todo)
* [Utiliser un dictionnaire comme clause where](/where_dict). - traduction demandée, voir [Todo](/docs/0.3.fr/todo)


##Déploiement:
* [Déploiement Fastcgi au travers lighttpd](/fastcgi-lighttpd/fr). 
* [Déploiement Fastcgi au travers Apache](/fastcgi-apache).  - traduction demandée, voir [Todo](/docs/0.3.fr/todo)
* [Déploiement CGI au travers Apache](/cgi-apache). - traduction demandée, voir [Todo](/docs/0.3.fr/todo)
* Déploiement mod_python au travers Apache (requis)
* [Déploiement mod_wsgi au travers Apache](/mod_wsgi-apache ). - traduction demandée, voir [Todo](/docs/0.3.fr/todo)
* [Déploiement mod_wsgi au travers Nginx](/mod_wsgi-nginx ). - traduction demandée, voir [Todo](/docs/0.3.fr/todo)
* [Déploiement Fastcgi au travers Nginx](/fastcgi-nginx). - traduction demandée, voir [Todo](/docs/0.3.fr/todo)

##Sous-domaines:
* Sous-domaines et comment accéder au nom utilisateur (requis)