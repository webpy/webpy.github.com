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
* [Comment utiliser web.background](/background). (traduction demandée)
* [Personnaliser le message NotFound](/custom_notfound/fr). 
* [Comment streamer de gros fichiers](/streaming_large_files/fr). 
* [Contrôler les evènements sur le serveur intégré par défaut](/logging/fr). 
* [Configurer le support SSL dans le serveur intégré](/ssl/fr).
* [Run-time language switch](/runtime-language-switch). (traduction demandée)

##Sessions et état des utilisateurs:
* [Travailler avec les sessions](/sessions/fr). 
* [Utiliser session avec reloader](/session_with_reloader/fr). 
* [Utiliser session dans un gabarit](/session_in_template). (traduction demandée)
* [Travailler avec les cookies](/cookies). (traduction demandée)
* [Authentification des utilisateurs](/userauth). (traduction demandée)
* [Authentification des utilisateurs avec base de données Postgresql](/userauthpgsql). (traduction demandée)
* [Session avec des sous-apps](/sessions_with_subapp). (en cours)


##Utils:
* [Envoi de Mail](/sendmail). (traduction demandée)
* [Envoi de Mail en utilisant Gmail](/sendmail_using_gmail). (traduction demandée)
* [Webservice en utilisant soaplib + WSDL](/webservice). (traduction demandée)

##Modèles de mise en forme, gabarits de mise en page:
* [Templetor: le système de gabarits de web.py](/docs/0.3/templetor.fr )
* [Utiliser des gabarits sur le site](/layout_template). (traduction demandée)
* [Alterner un style](/alternating_style). (traduction demandée) 
* [Importer des fonctions dans les gabarits](/template_import). (traduction demandée)
* [i18n support dans les fichiers gabarits](/i18n_support_in_template_file ). (traduction demandée)
* [Utiliser le moteur de gabarit Mako dans webpy](/template_mako). (traduction demandée)
* [Utiliser le moteur de gabarit Cheetah dans webpy](/template_cheetah). (traduction demandée)
* [Utiliser le moteur de gabarit  Jinja2 dans webpy](/template_jinja). (traduction demandée)
* [Comment utiliser les gabarits sur Google App Engine](/templates_on_gae). (traduction demandée)

##Essais:
* [Tester avec Paste et Nose](/testing_with_paste_and_nose). (traduction demandée)
* [RESTful doctesting using an application's request method](/restful_doctesting_using_request). (traduction demandée)

##Entrées utilisateurs:
* [Uploader un fichier](/fileupload). (traduction demandée)
* [Stocker un fichier uploadé](/storeupload). (traduction demandée)
* [Comment limiter la taille des fichiers uploadés](/limiting_upload_size). (traduction demandée)
* [Accéder aux entrées utilisateurs par le biais de web.input](/input). (traduction demandée)
* [Comment utiliser les formulaires](/forms). (traduction demandée)
* [Rendu individuel des champs de formulaires](/form_fields). (traduction demandée)

##Base de données:
* [Multiples bases de données](/multidbs). (traduction demandée)
* [Select: Récupérer les entrées d'une base de données](/select). (traduction demandée)
* [Update: Mettre à jour les entrées d'une base de données](/update). (traduction demandée)
* [Delete: Supprimer les entrées d'une base de données](/delete). (traduction demandée)
* [Insert: Ajouter des entrées à une base de donnée](/insert).  (traduction demandée)
* [Query: Base de données - Requêtes avancées](/query). (traduction demandée)
* [Query: How to use database transactions](/transactions). (traduction demandée)
* [Comment utiliser sqlalchemy](/sqlalchemy). (traduction demandée)
* [Intégrer SQLite UDF (user-defined-functions) à la couche de base de données webpy](/sqlite-udf). (traduction demandée)
* [Utiliser un dictionnaire comme clause where](/where_dict). (traduction demandée)


##Déploiement:
* [Déploiement Fastcgi au travers lighttpd](/fastcgi-lighttpd). (traduction demandée)
* [Déploiement Fastcgi au travers Apache](/fastcgi-apache).  (traduction demandée)
* [Déploiement CGI au travers Apache](/cgi-apache). (traduction demandée)
* Déploiement mod_python au travers Apache (requis)
* [Déploiement mod_wsgi au travers Apache](/mod_wsgi-apache ). (traduction demandée)
* [Déploiement mod_wsgi au travers Nginx](/mod_wsgi-nginx ). (traduction demandée)
* [Déploiement Fastcgi au travers Nginx](/fastcgi-nginx). (traduction demandée)

##Sous-domaines:
* Sous-domaines et comment accéder au nom utilisateur (requis)