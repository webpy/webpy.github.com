---
layout: default
title: 导入函数到模板中
---

# 导入函数到模板中

### 问题

如何导入函数到模板中？

### 方案

在编写模板时，你不可避免地需要编写一些仅与显示逻辑相关的函数。web.py使您
可以使用 `$code` 块直接在模板中编写大型代码块，包括定义函数(如果您不知道
什么是 `$code` 块，请阅读 [模板的教程](/docs/0.3/templetor)  )。
例如，以下代码块会将状态代码从数字转换为人类可读的状态信息：

```
def status(c):
    st = {}
    st[0] = 'Not Started'
    st[1] = 'In Progress'
    st[2] = 'Finished'
    return st[c]
```

当您进行更多的web.py开发时，您将在模板中的各种地方编写更多此类函数。这会使
模板凌乱，并且违反DRY（Don't Repeat Yourself，不要重复自己）原则。


自然地，您可能需要编写一个模块，叫做 `displayLogic.py` ，并将该模块导入每个
需要这些函数的模板中。不幸的是，出于安全原因，`import` 在模板已被禁用。不过，
通过全局命名空间向模板中导入所需的函数，解决此问题很容易：

```
#
# in your app.py:
#
def status(c):
    st = {}
    st[0] = 'Not Started'
    st[1] = 'In Progress'
    st[2] = 'Finished'
    return st[c]

# Import function `status` to global namespace with same name.
render = web.template.render('templates', globals={'status': status})

#
# in the template file:
#
$def with(mystatus)
...
<div>Status: $status(mystatus)</div>
```

你可以向 `globals` 字典导入多于一个变量名。此技巧
还用于[在template中使用session](session_in_template.zh-cn) 。
