---
layout: default
title: Subdomain application
---

# Subdomain application

Subdomain applications delegate requests based on host. This makes virtual hosting very easy. This works like a [subdir application](/docs/0.3/apps/subdir), only switches to the corresponding application based on host name instead of sub directory.

## Example

     import mainsite 
     import wiki
     import usersite

     mapping = ( 
         "(www\.)?example.com", mainsite.app, 
         "wiki.example.com", wiki.app,
         ".*\.example.com", usersite.app 
     ) 

     app = web.subdomain_application(mapping)

     if __name__ == '__main__':
         app.run()