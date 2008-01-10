---
layout: default
title: web.cookies()
---

# web.cookies()

returns a storage object filled with the cookies available to the current domain.  If you have set a cookie using web.setcookie() but have not specified the domain that you are using for web.cookies(), then it will not show up in this list.

        
        web.setcookie('hc', '1', 3600, 'huntercross.com')
        
        print web.cookies()

