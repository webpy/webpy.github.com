---
layout: default
title: Sending mail using gmail
---

# Sending mail using gmail

Other languages: [français](/../cookbook/sendmail_using_gmail/fr) | ...

##Problem: 

How to send mail using gmail.

##Solution:

Often it is tedious to setup and maintain a mail server. If you have a
gmail accout, you can use gmail as SMTP server to send mail. To do
that we need to specify username and password of gmail account in
`web.config`.

    web.config.smtp_server = 'smtp.gmail.com'
    web.config.smtp_port = 587
    web.config.smtp_username = 'cookbook@gmail.com'
    web.config.smtp_password = 'secret'
    web.config.smtp_starttls = True

Once this configuration is set, `web.sendmail` can be used to send
mail using the gmail account. Gmail signs all these mails.

    web.sendmail('cookbook@gmail.com', 'user@example.com', 'subject', 'message')

Read [GMail: Configuring other mail clients][1] for more details.

[1]: http://mail.google.com/support/bin/answer.py?hl=en&answer=13287