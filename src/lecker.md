---
layout: default
title: lec.ker - a simple del.icio.us clone
---

# lec.ker - a simple del.icio.us clone

_by Valentin Wüstholz_

### database (MySQL):

    CREATE TABLE  `lecker`.`bookmarks` (
      `id` int(10) unsigned NOT NULL auto_increment,
      `url` text NOT NULL,
      `created` timestamp NOT NULL default CURRENT_TIMESTAMP,
      `tags` text NOT NULL,
      `title` text NOT NULL,
      PRIMARY KEY  (`id`),
      UNIQUE KEY `id` (`id`)
    );

### source code:

    todo-list/
      lecker.py
      templates/
        view.html
        edit.html
        delete.html
        search.html

### `lecker.py`

        import web

        urls = (
            '/', 'view',
            '/add', 'add',
            '/delete', 'delete',
            '/edit/([0-9]*)', 'edit',
            '/search/(\S*)', 'search'        )

        class view:
            def GET(self):
                bookmarks = list(web.select("bookmarks", order="created desc"))
                for b in bookmarks:
                    b.tags = b.tags.split()
                web.render('view.html')

        class add:
            def POST(self):
                i = web.input()
                web.debug(type(i.tags))
                n = web.insert('bookmarks', title=i.title, url=i.url, tags=i.tags)
                web.seeother('./#t'+str(n))

        class delete:
            def GET(self):
                bookmarks = web.select("bookmarks", order="title")
                web.render('delete.html')
            def POST(self):
                i = web.input()
                web.debug(i)
                for item in i:
                    web.delete('bookmarks', 'id = '+item)
                web.seeother('./#')

        class edit:
            def GET(self, id):
                try:
                    bookmark = web.select("bookmarks", where="id = "+id)[0]
                    web.render('edit.html')
                except IndexError:
                    print "This bookmark doesn't exist."            def POST(self, id):
                i = web.input()
                web.update('bookmarks', 'id = '+id, title=i.title, url=i.url, tags=i.tags)
                web.seeother('../')

        class search:
            def GET(self, tag):
                bookmarks = []
                bs = list(web.select("bookmarks", order="created desc"))
                for b in bs:
                    b.tags = b.tags.split()
                    if tag in b.tags:
                        bookmarks.append(b)
                empty = (len(bookmarks) == 0)
                web.render('search.html')
            def POST(self, tag):
                i = web.input()
                tags = i.tags.split()
                bookmarks = []
                bs = list(web.select("bookmarks", order="created desc"))
                for b in bs:
                    b.tags = b.tags.split()
                    if every(lambda t: t in b.tags, tags):
                        bookmarks.append(b)
                empty = (len(bookmarks) == 0)
                web.render('search.html')

        def every(f, lst):
            for x in lst:
                if not f(x):
                    return False
            return True

        web.internalerror = web.debugerror
        web.db_parameters = dict(dbn='mysql', user='root', pw='', db='lecker')
        if __name__ == '__main__': web.run(urls, web.reloader)

### `view.html`

        <p><center><h1>lec.ker</h1></center></p>        
        <p>        <hr/>        </p>        
        <center>        <form name="search" method="post" action="search/#">        <p>        <p>        <input type="text" name="tags" size="50" />        </p>        <input type="submit" value="Search" />        </p>        </form>        </center>        
        <p>        <hr/>        </p>        
        <table border="0" width="100%">        #for bookmark in $bookmarks
             <colgroup>               <col width="50%">               <col width="35%">               <col width="15%">             </colgroup>             <tr>             <form name="del$bookmark.id" method="post" action="delete">             <td>               <a href="$bookmark.url"> $bookmark.title </a>             </td>             <td>             #for tag in $bookmark.tags
                  <a href="/search/$tag"> $tag </a> |
             #end for
             </td>             <td align="right">             <a href="edit/$bookmark.id">(edit)</a>             <input type="hidden" name="$bookmark.id" value="1" />             <a href="#" onclick=document.del${bookmark.id}.submit()>(delete)</a>             </td>             </form>             </tr>        #end for
        </table>        
        <p>        <hr/>        </p>        
        <form name="add" method="post" action="add">        <table border="0" width="100%">        <p>        <tr>          <td>            Title:
          </td>          <td>            <input type="text" name="title" size="100" />          </td>        </tr>        <tr>          <td>            Url:
          </td>          <td>            <input type="text" name="url" size="100" />          </td>        </tr>        <tr>          <td>            Tags:
          </td>          <td>            <input type="text" name="tags" size="100" />          </td>        </tr>        </p>        </table>        <p>        <input type="submit" value="Add" />        </p>        </form>        
        <a href="delete">Delete Bookmarks</a>
### `edit.html`

        <p><center><h1>lec.ker</h1></center></p>        
        <p><h2>Edit Bookmark:</h2></p>        
        <form method="post" action="">        <p>        <p>        Title:<input type="text" name="title" value="$bookmark.title" size="100" />        </p>        Url:<input type="text" name="url" value="$bookmark.url" size="100" />        </p>        Tags:<input type="text" name="tags" value="$bookmark.tags" size="100" />        </p>        <input type="submit" value="Edit" />        </p>        </form>        
        <p>        <hr/>        </p>        
        <a href="../">Back</a>
### `delete.html`

        <p><center><h1>lec.ker</h1></center></p>        
        <form name = "bookmarks" method="post" action="delete">          <p><h2>Delete Bookmarks:</h2></p>        
          <p>           #for bookmark in $bookmarks
                <input type="checkbox" name="$bookmark.id" value="1"> <a href="$bookmark.url"> $bookmark.title </a><br>           #end for
          </p>          <p><input type="submit" value="Delete" />          </p>        </form>        
        <p>        <hr/>        </p>        
        <a href="../">Back</a>
### `search.html`

        <p><center><h1>lec.ker</h1></center></p>        
        <table border="0" width="100%">        #for bookmark in $bookmarks
             <colgroup>               <col width="50%">               <col width="35%">               <col width="15%">             </colgroup>             <tr>             <form name="del$bookmark.id" method="post" action="../delete">             <td>               <a href="$bookmark.url"> $bookmark.title </a>             </td>             <td>             #for tag in $bookmark.tags
                  <a href="../search/$tag"> $tag </a> |
             #end for
             </td>             <td align="right">             <a href="../edit/$bookmark.id">(edit)</a>             <input type="hidden" name="$bookmark.id" value="1" />             <a href="#" onclick=document.del${bookmark.id}.submit()>(delete)</a>             </form>             </td>             </form>             </tr>        #end for
        </table>        #if $empty
             No Bookmarks were found.
        #end if
        </p>        
        <p>        <hr/>        </p>        
        <a href="../">Back</a>