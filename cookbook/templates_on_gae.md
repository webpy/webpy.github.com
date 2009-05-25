---
layout: default
title: How to use templates on Google App Engine
---

# How to use templates on Google App Engine

## Problem

How to use templates on Google App Engine

## Solution

web.py templetor compiles the templates to python source, which requires accessing parser module of python standard library. Unfortunately that module is blocked in GAE for security reasons. 

To overcome that situation, web.py supports compiling the templates to python code so that the compiled sources can be used on GAE instead of the original templates. web.py makes sure that no code changes are required to use templates in this way.

To compile all templates in a template dir (has to be redone each time a template has changed):

    $ python web/template.py --compile templates

This compiles all templates in templates/ dir recursively and creates `__init__.py` with all the templates in that dir. On GAE, `web.template.render` is re-written to treat `templates/` as python module. 

