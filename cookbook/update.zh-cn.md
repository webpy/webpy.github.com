---
layout: default
title: db.upate 数据更新
---

# db.upate 数据更新

### 问题

向数据库中更新数据。

### 解决方案

    import web
    
    db = web.database(dbn='postgres', db='mydata', user='dbuser', pw='')
    db.update('mytable', where="id = 10", value1 = "foo")

在 [查询](/cookbook/select/zh-cn) 中有更多关于可用参数的信息。


该更新操作会返回更新的影响行数。