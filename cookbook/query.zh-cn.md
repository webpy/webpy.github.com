---
layout: default
title: 使用 db.query 执行较为复杂的数据库查询
---

# 使用 `db.query` 执行较为复杂的数据库查询

## 问题

您要执行的 SQL 语句如：高级的联接或计数。

## 方案

webpy 没有尝试在数据库之上建立一层模型，而是以尽可能简单的方式查询数据库，
做复杂的查询也很容易。例如：

```
import web

db = web.database(dbn='postgres', db='mydata', user='dbuser', pw='')

# Query number of entries in `users` table
results = db.query("SELECT COUNT(*) AS total_users FROM users")

# Print the result
print(results[0].total_users)
```

或者是，使用一个JOIN示例:

```
results = db.query("SELECT * FROM entries JOIN users WHERE entries.author_id = users.id")
```

为了防止 SQL 注入攻击，`db.query` 也支持 [db.select](select.zh-cn) 一节介绍的 `vars` 参数:

```
results = db.query("SELECT * FROM users WHERE id=$id", vars={'id':10})
```

这将避免用户输入，如果你信任这个 `id` 变量。
