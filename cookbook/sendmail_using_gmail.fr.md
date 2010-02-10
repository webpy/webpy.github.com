---
layout: default
title: Envoi de mails en utilisant Gmail
---

# Envoi de mails en utilisant Gmail

Autre langages: [english](/../sendmail_using_gmail) | ...


##Problème: 

Comment envoyer un mail en utilisant Gmail ?

##Solution:

Il est souvent fastidieux de configurer et de maintenir un serveur de messagerie. Si vous possédez un compte Gmail, vous pouvez utiliser Gmail comme serveur SMTP pour envoyer des mails. Pour cela, vous aurez besoin de spécifier le nom d'utilisateur et le mot de passe du compte Gmail dans `web.config`.


    web.config.smtp_server = 'smtp.gmail.com'
    web.config.smtp_port = 587
    web.config.smtp_username = 'cookbook@gmail.com'
    web.config.smtp_password = 'secret'
    web.config.smtp_starttls = True


Une fois la configuration définie, `web.sendmail` peut être employé pour envoyer des mails en utilisant le compte Gmail. Gmail signe tous ces mails.

    web.sendmail('cookbook@gmail.com', 'user@example.com', 'subject', 'message')

Veuillez lire [GMail: Configuring other mail clients][1] pour plus de détails.

[1]: http://mail.google.com/support/bin/answer.py?hl=en&answer=13287