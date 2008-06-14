---
layout: default
title: Sending mail
---

# Sending mail

### Problem

How to send mails from web.py

### Solution

`web.sendmail` function can be used to send mail from web.py. 

    web.sendmail('cookbook@webpy.org', 'user@example.com', 'subject', 'message')

If any mail server is specified in `web.config` it uses that to send the mail or it uses the traditional sendmail from `/usr/lib/sendmail`. 

    web.config.smtp_server = 'mail.mydomain.com'

To send a mail to multiple recipients, a list can be passed for `to_address`.

    web.sendmail('cookbook@webpy.org', ['user1@example.com', 'user2@example.com'], 'subject', 'message')

Optinal cc and bcc keyword arguments can be passed to `web.sendmail` to add Cc and Bcc recipients.
Values of cc and bcc can be list as well.

    web.sendmail('cookbook@webpy.org', 'user@example.com', 'subject', 'message', cc='user1@example.com', bcc='user2@example.com')

Addition headers can be passed to `web.sendmail` via `headers` tuple.

    web.sendmail('cookbook@webpy.org', 'user@example.com', 'subject', 'message',
            cc='user1@example.com', bcc='user2@example.com',
            headers=({'User-Agent': 'webpy.sendmail', 'X-Mailer': 'webpy.sendmail',})
            )