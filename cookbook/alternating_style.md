---
layout: default
title: Alternating Style
---

# Alternating Style

Problem: You want to alternate the background color of a list's elements as you dynamically generate it from a passed sequence.

Solution: Give templetor access to the `int` built-in and use modulo to test.

## code.py ##

    web.template.Template.globals['int'] = int


## template.html ##

    <ul>
    $var i: 0
    $for track in tracks:
        $var i: ${int(self.i) + 1}
        <li class="
        $if int(self.i) % 2:
            odd
        $else:
            even
        ">$track.title</li>
    </ul>