---
layout: default
title: Reading raw data from post
---

# Reading raw data from post

Other languages: [français](/../cookbook/postbasic/fr) | ...

## Introduction

Sometimes, the client sends a lot of data by the POST method. In webpy, you can handle it like this.


## Code

    class RequestHandler():
        def POST():
            data = web.data() # you can get data use this method