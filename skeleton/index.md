---
layout: default
title: skeleton
---

# skeleton

Here's the skeleton of a typical web.py app (as of 0.2):

## code.py

    import web
    import view, config
    from view import render

    urls = (
        '/', 'index'    )

    class index:
        def GET(self):
            print render.base(view.listing())

    if __name__ == "__main__":
        web.run(urls, globals(), *config.middleware)

## config.py

    import web
    web.config.db_parameters = dict(dbn='postgres', db='appname', user='username', pw='')
    web.webapi.internalerror = web.debugerror
    middleware = [web.reloader]
    cache = False

## db.py

    import web

    def listing(**k):
        return web.select('items', **k)

## view.py

    import web
    import db
    import config

    render = web.template.render('templates/', cache=config.cache)

    def listing(**k):
        l = db.listing(**k)
        return render.listing(l)
    
    web.template.Template.globals.update(dict(
      datestr = web.datestr,
      render = render
    ))

## sql/tables.sql

    CREATE TABLE items (
        id serial primary key,
        author_id int references users,
        body text,
        created timestamp default (current_timestamp at time zone 'utc')
    );

## templates/base.html

    $def with (page, title=None)
    <html><head>        <title>my site\
    $if title: : $title\
    </title>    </head><body>    <h1><a href="/">my site</a></h1>
    $:page
    
    </body></html>
## templates/listing.html

    $def with (items)

    $for item in items:
        $:render.item(item)

## templates/item.html

    $def with (item)
    
    <p>$item.body</p>    
    <p class="details">created $datestr(item.created)</p>