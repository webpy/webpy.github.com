---
layout: default
title: 在template中使用session
---

# 在template中使用session

`问题`: 我想在模板中使用session（比如：读取并显示session.username）

`解决`:

在应用程序中的代码:

    render = web.template.render('templates', globals={'context': session})

在模板中的代码:

    <span>You are logged in as <b>$context.username</b></span>

你可以真正的使用任何符合语法的python变量名，比如上面用的_context_。我更喜欢在应用中直接使用'session'。