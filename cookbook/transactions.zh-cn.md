---
layout: default
title: How to use database transactions
---

# How to use database transactions

### Problem

How to use database transactions


### Solution

The database object has a method `transaction` which starts a new transaction and returns the transaction object. The transaction object can be used to commit or rollback that transaction.

    import web

    db = web.database(dbn="postgres", db="webpy", user="foo", pw="")
    t = db.transaction()
    try:
        db.insert('person', name='foo')
        db.insert('person', name='bar')
    except:
        t.rollback()
        raise
    else:
        t.commit()

With python 2.5+, transaction can be used as with statement also.  

    from __future__ import with_statement
    
    db = web.databse(dbn="postgres", db="webpy", user="foo", pw="")
     
    with db.transaction():
        db.insert('person', name='foo')
        db.insert('person', name='bar')
        

It is also possible to have nested transactions.

    def post(title, body, tags):
        t = db.transaction()
        try:
            post_id = db.insert('post', title=title, body=body)
            add_tags(post_id, tags)
        except:
            t.rollback()
        else:
            t.commit()

    def add_tags(post_id, tags):
        t = db.transaction()
        try:
            for tag in tags:
                db.insert('tag', post_id=post_id, tag=tag)
        except:
            t.rollback()
        else:
            t.commit()


Nested transactions are ignored for sqlite as they are not supported.