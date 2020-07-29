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
    ...
```

当您进行更多的web.py开发时，您将在模板中的各种地方编写更多此类函数。这会使
模板凌乱，并且违反DRY（Don't Repeat Yourself，不要重复自己）原则。


自然地，您可能需要编写一个模块，例如 `display_logic.py` ，并将该模块导入每个
需要这些函数的模板中。遗憾的是，出于安全原因，模版里禁止使用 `import`。不过，
可以通过将需要的函数导入全局命名空间来解决此问题：

```
#
# 在主程序 app.py 里:
#
def status(c):
    ...

# 将自定义的 `status` 函数导入到全局命名空间 `globals` 字典里，导入后的名字
# 也是 `status`（字典的 key）。
render = web.template.render('templates', globals={'status': status})

#
# 在模版文件里可以调用导入的函数 `status`：
#
$def with(mystatus)
...
<div>Status: $status(mystatus)</div>
```

可以根据需要在 `globals` 字典里导入更多函数。此技巧还用于
[在 template 中使用 session](session_in_template.zh-cn) 。
