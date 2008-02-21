---
layout: default
title: web.ctx.get()
---

# web.ctx.get()

Returns the HTTP username passed in the request headers, or 'None' if none.

    return web.ctx.get('environ',{}).get('REMOTE_USER', None)