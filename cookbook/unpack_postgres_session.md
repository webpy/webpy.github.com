---
layout: default
title: Exploit sessions stored in a postgresql database.
---

# Exploit sessions stored in a postgresql database.

##Problem:

When using session and storing some ids or any kind of stuff referencing a database, you'll do a lot of queries like this one:
"select foo, bar from foobar_table where id=%s and id_foor=%s" % (session.id, session.id_foo)

That's not a real problem, but if your session is stored in a postgresql database, this is wierd to take these fields in your database to unpack them in web.py and then re-use them in your queries. 

At the other end, this is also weird to take data in your database to bring them in web.py and then repack them in your database.

A cleaner approach would be to access directly these informations in postgresql to read and/or write them.


##Solution:

To apply this recipe, you'll need to use postgresql DBStore for your sessions. 
You'll also need to install the plpythonu in your database.
Web.py installed as a system python library is also needed, session objects are defined in web.utils and pickle asks for these classes to work.

First, take a quick look to postgresql storage of sessions with some obvious code: :

##
    db = web.database(dbn='postgres', db='db_name', user='db_user', pw='db_pw')
    
    store = web.session.DBStore(db, 'sessions')
    
    session = web.session.Session(app, store, initializer={'uid': 0,
                                                  'username': '',
                                                  'current_page': 'index',
                                                  'user_role': 'invited'
                                                  })
##

You'll also need a table to handle this, here's a reminder:

##
    CREATE TABLE sessions
                (
                 session_id CHARACTER(40) PRIMARY KEY,
                 atime TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
                 data TEXT
                );
##

With that, you should be able to have working sessions stored in postgresql.
When a client connects to web.py, sessions are automatically started and stored in the sessions table. A quick look into it will show something like this:

    session_id        |atime                      | data
    8982d61dblabla... |2010-08-04 15:13:34.889288 | KGRwMQpTJ3VzZblablabla...

The session_id is quite obvious to understand, atime is the timestamp of last access and data is a base64 packed version of the pickled session instance.

With a plpythonu function, we are able to unpack these informations and use them. Here's an example of function:

    We need this to make a function return a set of fields instead of a single value, execute once:
    create type read_session_type as (uid integer, current_page varchar(20), user_role varchar(20));

    create function unpack_this_session(session_id varchar(128)) returns read_session_type as
    $$
    import base64, pickle, sys
    sys.argv=[] # pickle needs sys.argv... workaround !
    data = plpy.execute("select data from sessions where session_id='%s'" % (session_id))[0]['data']

    pickled = base64.decodestring(data)
    session_instance = pickle.loads(pickled)

    uid = session_instance['uid']
    current_page = session_instance['current_page']
    user_role = session_instance['user_role']

    return (uid, current_page, user_role)
    $$
    language plpythonu;


This function should be as simple as this to use:

    select * from unpack_this_session('8982d61db185462b983242beb7009ad12a716aef')

now, if you didn't already managed to understand what that mean:

    "select * from unpack_this_session('%s') ss \
      inner join users u on u.id=ss.uid \
      inner join user_rules ur on ur.role = ss.user_role" % (session.id)

You also can imagine modifying session information and repack it within a python function, taking informations directly in the database and making them accessible in web.py session object without any code in your web.py classes.

Exciting, isn't it ?

Technically, as it uses the primary key indexes to match the session_id, seeking data should not be a problem, but postgresql won't be able to use indexes with unpacked data as it comes from a procedure. 

But, we can easily consider using general functions which unpack every session at once, making all of them readable in a view. The temptation is huge, but this is overkill because you shouldn't have to use every sessions data for one client handling only one session, and, more important, this would be an awful CPU and Memory killer. Don't do it ! 

If you think of doing a lot of these operations, consider using triggers to unpack these fields when they're updated or inserted, this is quite better for database performance, opening the window to indexes and foreign keys... 
Can you imagine the simplicity, and performance, you gain with a session instance raising a database exception when you try to set a value in your sessions that violates a database foreign key, with a synchronous and transactional behavior, and no more SQL to verify them ?

This function is quite obvious, to demonstrate how to access session data, but it doesn't handle any kind of exceptions. So, don't use it as this for production matters, it needs enlightenment to be as stable and functionnal as needed ;)

I didn't managed to test this procedure with exact keywords, so If you encounter problems, feel free to mention it !