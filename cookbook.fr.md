---
layout: default
title: Web.py Cookbook
---

# Web.py Cookbook

Autres langages : [japan 日本語](/cookbook/ja) | [chinese 简体中文](/cookbook/zh-cn) | [english](/cookbook) | ...

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
* [Hello World](/cookbook/helloworld). (traduction demandée)
* [Servir des fichiers statiques](/cookbook/staticfiles).   (traduction demandée)
* [Comprendre la gestion des URL](/cookbook/url_handling).  (traduction demandée)
* [Seeother et Redirect](/cookbook/redirect+seeother).  (traduction demandée)
* [Utiliser une sous-application](/cookbook/subapp).   (traduction demandée)
* [Servir du XML](/cookbook/xmlfiles).   (traduction demandée)
* [Lire les données brutes d'un post](/cookbook/postbasic).  (traduction demandée)


##Avancé
* [web.ctx](/cookbook/ctx). (traduction demandée)
* [Application processors, loadhooks et unloadhooks](/cookbook/application_processors). (traduction demandée)
* [Comment utiliser web.background](/cookbook/background). (traduction demandée)
* [Personnaliser le message de NotFound](/cookbook/custom_notfound). (traduction demandée)
* [Comment streamer de gros fichiers](/cookbook/streaming_large_files). (traduction demandée)
* [Contrôle sur les enregistrements pour HTTPServer par défaut](/cookbook/logging). (traduction demandée)
* [Support SSL dans serveur intégré cherrypy](/cookbook/ssl). (traduction demandée)
* [Run-time language switch](/cookbook/runtime-language-switch). (traduction demandée)

##Sessions et état des utilisateurs:
* [Travailler avec Session](/cookbook/sessions). (traduction demandée)
* [Utiliser session avec reloader](/cookbook/session_with_reloader). (traduction demandée)
* [Utiliser session dans un gabarit](/cookbook/session_in_template). (traduction demandée)
* [Travailler avec les cookies](/cookbook/cookies). (traduction demandée)
* [Authentification des utilisateurs](/cookbook/userauth). (traduction demandée)
* [Authentification des utilisateurs avec base de données Postgresql](/cookbook/userauthpgsql). (traduction demandée)
* [Session avec des sous-apps](/cookbook/sessions_with_subapp). (traduction demandée)


##Utils:
* [Envoi de Mail](/cookbook/sendmail). (traduction demandée)
* [Envoi de Mail en utilisant Gmail](/cookbook/sendmail_using_gmail). (traduction demandée)
* [Webservice en utilisant soaplib + WSDL](/cookbook/webservice). (traduction demandée)

##Modèles de mise en forme, gabarits de mise en page:
* [Templetor: le système de gabarits de web.py](/docs/0.3/templetor.fr )
* [Utiliser des gabarits sur le site](/cookbook/layout_template). (traduction demandée)
* [Alterner un style](/cookbook/alternating_style). (traduction demandée) 
* [Importer des fonctions dans les gabarits](/cookbook/template_import). (traduction demandée)
* [i18n support dans les fichiers gabarits](/cookbook/i18n_support_in_template_file ). (traduction demandée)
* [Utiliser le moteur de gabarit Mako dans webpy](/cookbook/template_mako). (traduction demandée)
* [Utiliser le moteur de gabarit Cheetah dans webpy](/cookbook/template_cheetah). (traduction demandée)
* [Utiliser le moteur de gabarit  Jinja2 dans webpy](/cookbook/template_jinja). (traduction demandée)
* [Comment utiliser les gabarits sur Google App Engine](/cookbook/templates_on_gae). (traduction demandée)

##Essais:
* [Tester avec Paste et Nose](/cookbook/testing_with_paste_and_nose). (traduction demandée)
* [RESTful doctesting using an application's request method](/cookbook/restful_doctesting_using_request). (traduction demandée)

##Entrées utilisateurs:
* [Uploader un fichier](/cookbook/fileupload). (traduction demandée)
* [Stocker un fichier uploadé](/cookbook/storeupload). (traduction demandée)
* [Comment limiter la taille des fichiers uploadés](/cookbook/limiting_upload_size). (traduction demandée)
* [Accéder aux entrées utilisateurs par le biais de web.input](/cookbook/input). (traduction demandée)
* [Comment utiliser les formulaires](/cookbook/forms). (traduction demandée)
* [Rendu individuel des champs de formulaires](/cookbook/form_fields). (traduction demandée)

##Base de données:
* [Multiples bases de données](/cookbook/multidbs). (traduction demandée)
* [Select: Récupérer les entrées d'une base de données](/cookbook/select). (traduction demandée)
* [Update: Mettre à jour les entrées d'une base de données](/cookbook/update). (traduction demandée)
* [Delete: Supprimer les entrées d'une base de données](/cookbook/delete). (traduction demandée)
* [Insert: Ajouter des entrées à une base de donnée](/cookbook/insert).  (traduction demandée)
* [Query: Base de données - Requêtes avancées](/cookbook/query). (traduction demandée)
* [Query: How to use database transactions](/cookbook/transactions). (traduction demandée)
* [Using sqlalchemy](/cookbook/sqlalchemy). (traduction demandée)
* [Intégrer SQLite UDF (user-defined-functions) à la couche de base de données webpy](/cookbook/sqlite-udf). (traduction demandée)
* [Utiliser un dictionnaire comme clause where](/cookbook/where_dict). (traduction demandée)


##Déploiement:
* [Déploiement Fastcgi au travers lighttpd](/cookbook/fastcgi-lighttpd). (traduction demandée)
* [Déploiement Fastcgi au travers Apache](/cookbook/fastcgi-apache).  (traduction demandée)
* [Déploiement CGI au travers Apache](/cookbook/cgi-apache). (traduction demandée)
* Déploiement mod_python au travers Apache (requis)
* [Déploiement mod_wsgi au travers Apache](/cookbook/mod_wsgi-apache ). (traduction demandée)
* [Déploiement mod_wsgi au travers Nginx](/cookbook/mod_wsgi-nginx ). (traduction demandée)
* [Déploiement Fastcgi au travers Nginx](/cookbook/fastcgi-nginx). (traduction demandée)

##Sous-domaines:
* Sous-domaines et comment accéder au nom utilisateur (requis)