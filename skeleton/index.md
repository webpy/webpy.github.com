---
layout: default
title: skeleton
---

# skeleton

Here's the skeleton of a typical web.py app:

## code.py

    import web
    import view, config

    urls = (
        '/', 'index'    )

    class index:
        def GET(self):
            print render.base(view.listing())

    if __name__ == "__main__":
        web.run(urls, *config.middleware)

## config.py

    import web
    web.db_parameters = dict(dbn='postgres', db='appname', user='username', pw='')
    web.internalerror = web.debugerror
    middleware = [web.reloader]

## db.py

    import web

    def listing(**k):
        return web.select('items', **k)

## view.py

    import web, template
    import db

    render = template.render('templates/')

    def listing(**k):
        l = db.listing(**k)
        return render.listing(l)
    
    template.Template.globals.update(dict(
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
    </title>    </head><body>    <h1>my site</h1>
    $page
    
    </body></html>
## templates/listing.html

    $def with (items)

    $for item in items:
        $:render.item(item)

## templates/item.html

    $def with (item)
    
    <p>$item.body</p>    
    <p class="details">created $datestr(item.created)</p>