---
layout: default
title: Using session in template
---

# Using session in template

Other languages: [français](/../cookbook/session_in_template/fr) | ...

##Problem: 

I want to use session in template (e.g. get session.username to display)

##Solution:

In your application code:

    render = web.template.render('templates', globals={'context': session})

In the template:

    <span>You are logged in as <b>$context.username</b></span>

You can literally use any valid python variable names, like the _context_ used above. I would prefer just use 'session' in real applications.