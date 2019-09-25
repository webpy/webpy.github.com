---
layout: default
title: 如何流传输大文件
---

# 如何流传输大文件

## 问题

如何流传输大文件？

## 方案

要流传输大文件，需要添加传输译码(Transfer-Encoding)区块头，这样才能一边下载一边显示。否则，浏览器将缓冲所有数据直到下载完毕才显示。

如果这样写：直接修改基础字符串(例中就是j)，然后用 yield 返回－－是没有效果的。如果要使用 yield，就要向对所有内容使用 yield。因为这个函式此时是一个生成器。(注：具体细节请查看 yield 文档，在此不做过多论述。)

例子

```
# Simple streaming server demonstration
# Uses time.sleep to emulate a large file read
import web
import time

urls = (
    "/",    "count_holder",
    "/(.*)",  "count_down",
)

app = web.application(urls, globals())

class count_down:
    def GET(self,count):
        # These headers make it work in browsers
        web.header('Content-type','text/html')

        # 再次提醒，只有使用 web.py 自带的 http server 的时候才需要添加
        # `Transfer-Encoding: chunked` 这个 http header。web.py 自带的
        # http server 不应该在生产环境中使用，请使用 Apache/Nginx 等
        # web 服务器。
        web.header('Transfer-Encoding','chunked')

        yield '<h2>Prepare for Launch!</h2>'
        j = '<li>Liftoff in %s...</li>'
        yield '<ul>'
        count = int(count)
        for i in range(count,0,-1):
            out = j % i
            time.sleep(1)
            yield out
        yield '</ul>'
        time.sleep(1)
        yield '<h1>Lift off</h1>'

class count_holder:
    def GET(self):
        web.header('Content-type','text/html')
        web.header('Transfer-Encoding','chunked')
        boxes = 4
        delay = 3
        countdown = 10
        for i in range(boxes):
            output = '<iframe src="/%d" width="200" height="500"></iframe>' % (countdown - i)
            yield output
            time.sleep(delay)

if __name__ == "__main__":
    app.run()
```
