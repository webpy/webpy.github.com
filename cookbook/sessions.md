---
layout: default
title: Sessions
---

# Sessions

Other languages: [Français](./sessions.fr) | ...

### Problem

How to use sessions in web.py.

### Solution

*__NOTE: sessions doesn't work in [debug](./tutorial#developing) mode because it interferes with reloading. See [session_with_reloader](session_with_reloader) for more details.__*

The `web.session` module provides session support. Here is a simple application to count using sessions.

```
import web

web.config.debug = False

urls = (
    "/count", "count",
    "/reset", "reset",
)

app = web.application(urls, locals())

# Store session data in folder 'sessions' under the same directory as your app.
session = web.session.Session(app, web.session.DiskStore("sessions"), initializer={"count": 0})

class count:
    def GET(self):
        session.count += 1
        return str(session.count)

class reset:
    def GET(self):
        session.kill()
        return "Reset"

if __name__ == "__main__":
    app.run()
```

Save above code in file `app.py`, start the application:

```
python app.py 8000
```

Test it with `curl` on another console:

```
curl -c cookie.txt http://127.0.0.1/count  # Store cookie in file 'cookie.txt'. It returns `1`.
curl -b cookie.txt http://127.0.0.1/count  # Use existing cookie. It returns `2`.
curl -b cookie.txt http://127.0.0.1/count  # Use existing cookie. It returns `3`.
curl -b cookie.txt http://127.0.0.1/reset  # Use existing cookie. It returns `Reset`.
                                           # Count is set back to the initial value `0`.
```

The session object is loaded with the session data before handling the request and saves the session data after handling the request, if modified. Note in the current (11-22-2008) version of web.py, one must turn off debug to use the development server with sessions.

The optional `initializer` argument to Session specifies the initial session.

You can use `DBStore` instead of `DiskStore` if you prefer to store sessions in database instead of disk. For using DBStore you need to have a table with the following schema.

```
create table sessions (
    session_id char(128) UNIQUE NOT NULL,
    atime timestamp NOT NULL default current_timestamp,
    data text
);
```

And you need to pass `db` object and session table name to the constructor of `DBStore`.

```
db = web.database(dbn='postgres', db='mydatabase', user='myname', pw='')
store = web.session.DBStore(db, 'sessions')
session = web.session.Session(app, store, initializer={'count': 0})
```

Options related to sessions can be modified using the `sessions_parameters` dict in `web.config`. The default values are shown below.

```
web.config.session_parameters['cookie_name'] = 'webpy_session_id'
web.config.session_parameters['cookie_domain'] = None
web.config.session_parameters['cookie_path'] = None
web.config.session_parameters['timeout'] = 86400  # in seconds
web.config.session_parameters['ignore_expiry'] = True
web.config.session_parameters['ignore_change_ip'] = True
web.config.session_parameters['secret_key'] = 'fLjUfxqXtfNoIldA0A0J'
web.config.session_parameters['expired_message'] = 'Session expired'
```

* `cookie_name` - name of the cookie used to store the session id
* `cookie_domain` - domain for the cookie used to store the session id
* `cookie_path` - path of the cookie. Defaults to `None`. You can set it to something like `/`, `/yourapp`.
* `timeout` - number of second of inactivity that is allowed before the session expires
* `ignore_expiry` - if `True`, the session timeout is ignored
* `ignore_change_ip` - if `False`, the session is only valid when it is accessed from the same ip address that created the session
* `secret_key` - [salt](http://en.wikipedia.org/wiki/Salt_%28cryptography%29) used in session id hash generation
* `expired_message` - message displayed when the session expires
