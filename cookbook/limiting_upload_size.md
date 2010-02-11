---
layout: default
title: How to put a limit on upload size
---

# How to put a limit on upload size

Other languages: [français](/../cookbook/limiting_upload_size/fr) | ...

## Problem

How to put a limit on upload size

## Solution

web.py uses `cgi` module to parse user inputs and the `cgi` module has a provision to limit max size of input.

The following code limits the size of input data to 10MB.

    import cgi

    # Maximum input we will accept when REQUEST_METHOD is POST
    # 0 ==> unlimited input
    cgi.maxlen = 10 * 1024 * 1024 # 10MB

Please note that this limits the size of POST data, not file uploaded. However they will be almost same if there is no other input.

The `cgi` module raises `ValueError` when the input size is more than `cgi.maxlen`. It can be caught to display required error message.

    class upload:
        def POST(self):
            try:
                i = web.input(file={})
            except ValueError:
                return "File too large"