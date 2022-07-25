---
layout: default
title: sqlalchemy
---

# sqlalchemy

## Problem

How to use sqlalchemy with web.py

## Solution

create a load hook and use sqlalchemy's [scoped session] (http://docs.sqlalchemy.org/en/rel_0_8/orm/session.html#using-thread-local-scope-with-web-applications)


    import string
    import random
    import web

    from sqlalchemy.exc import OperationalError
    from sqlalchemy.orm import scoped_session, sessionmaker
    from models import *

    urls = (
        "/", "add",
        "/view", "view"
    )

    Session = scoped_session(sessionmaker(bind=engine))

    def load_sqla(handler):
        web.ctx.orm = Session()

        try:
            return handler()
        except OperationalError:
            web.ctx.orm.rollback()
            Session.remove()
            raise
        except:
            web.ctx.orm.commit()
            Session.remove()
            raise
        finally:
            web.ctx.orm.commit()
            Session.remove()

    app = web.application(urls, locals())
    app.add_processor(load_sqla)


    class add:
        def GET(self):
            web.header('Content-type', 'text/html')
            fname = "".join(random.choice(string.letters) for i in range(4))
            lname = "".join(random.choice(string.letters) for i in range(7))
            u = User(name=fname
                    ,fullname=fname + ' ' + lname
                    ,password =542)
            web.ctx.orm.add(u)
            return "added:" + web.websafe(str(u)) \
                                + "<br/>" \
                                + '<a href="/view">view all</a>'

    class view:
        def GET(self):
            web.header('Content-type', 'text/plain')
            return "\n".join(map(str, web.ctx.orm.query(User).all()))


    if __name__ == "__main__":
        app.run()


### models.py

    from sqlalchemy import create_engine
    from sqlalchemy import Column, Integer, String

    engine = create_engine('sqlite:///mydatabase.db', echo=True)

    from sqlalchemy.ext.declarative import declarative_base

    Base = declarative_base()
    class User(Base):
        __tablename__ = 'users'

        id = Column(Integer, primary_key=True)
        name = Column(String)
        fullname = Column(String)
        password = Column(String)

        def __init__(self, name, fullname, password):
            self.name = name
            self.fullname = fullname
            self.password = password

        def __repr__(self):
           return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)


    users_table = User.__table__
    metadata = Base.metadata


    if __name__ == "__main__":
        metadata.create_all(engine)



before running the application. run `python models.py` to setup the sqlite database.
