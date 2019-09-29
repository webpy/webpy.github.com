---
layout: default
title: db.select 查询
---

# 使用 `db.select` 执行简单 SQL 查询

## 问题

怎样执行数据库查询？

## 解决方案

在 web.py 0.3x 和 0.40 版本, 建立数据库大致如下:

```
db = web.database(dbn="postgres", host="localhost", port=5432, db="mytable", user="db_user", pw="db_password")
```

成功建立数据库连接后, 可以这样执行查询数据库:

```
# Select all entries from table `mytable`
results = db.select("mytable")
```

`db.select` 支持以下几个关键字参数:

* vars
* what
* where
* order
* group
* limit
* offset
* _test

### vars

`vars` 是一个 dict，保存 SQL 查询语句里需要用到的变量，在实际构造 SQL 语句时会被用于替换 `WHERE` 语句里以 `$` 开头的变量。如:

```
myvars = dict(name="Bob")

# `name=$name` 将被替换为 `name="Bob"`
results = db.select("mytable", vars=myvars, where="name = $name")
```

### what

`what` 指明要查询的 SQL 字段名。如果省略则默认查询所有字段（即 `SELECT * FROM ...`)。

```
# 实际执行的 SQL 语句： SELECT id, name FROM mytable
results = db.select("mytable", what="id, name")
```

### where

`where` 用于指定 SQL 语句里的查询条件, 如:

```
# 实际执行的 SQL 语句： SELECT id FROM mytable WHERE id > 100
results = db.select("mytable", what=id, where="id > 100")
```

### order

`order` 指明查询结果要以何种方式排序。

```
# 实际执行的 SQL 语句： SELECT * FROM mytable ORDER BY post_date DESC
results = db.select("mytable", order="post_date DESC")
```

### group

`group` 指明以何种方式对查询结果分组统计：

```
# 实际执行的 SQL 语句： SELECT * FROM mytable GROUP BY color
results = db.select("mytable", group="color")    
```

### limit

`limit` 指明返回多少条结果：
 
```
# 实际执行的 SQL 语句： SELECT * FROM mytable LIMIT 10
results = db.select("mytable", limit=10) 
```

### offset

`offset` 指明偏移量，即从第几行开始查询：

```
# 实际执行的 SQL 语句： SELECT * FROM mytable OFFSET 10
results = db.select("mytable", offset=10) 
```

### _test

设置 `_test=True` 时，`db.select` 只是构造 SQL 语句，并不实际执行：

```
# `results` 是一个 string：<sql: 'SELECT * FROM mytable OFFSET 10'>
results = db.select("mytable", offset=10, _test=True) 
```
