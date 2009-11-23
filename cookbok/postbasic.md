---
layout: default
title: Reading raw data from post
---

# Reading raw data from post

## Introduction

Sometimes, the client send a lot of data by post method. In webpy, you can handle it like this.


## Code

    class RequestHandler():
        def POST():
            data = web.data() # you can get data use this method