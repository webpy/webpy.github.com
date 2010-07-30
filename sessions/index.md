---
layout: default
title: Session
---

# Session

# Usage
[example](/sessions/example)

[simple example, a counter](/sessions/simpleexample)


# Specification
## Summary
The main session object will be created depending on the configuration. However the user/developer will choose it's usage. If needed the user will call start() method and there by inicializing handlers, variables from db-config like variables. The session will be implemented as storage object. Session identification will mostly rely on client cookies (optionally also on client IP address). All data will be stored/retrieved through handler object (DB-, file-, cookie?- based). Save/commit & destroy methods will be created. The user will have the option to set various settings including expiration timeout, handler, session id generator (a default will be provided).

## Design
The session functionality will rely on a two-layer implementation: Session -> Handler. The Session class will provide identification & verification of the client request while the Handler-like classes will guarante data persistence.

## Implementation details

### Session class
The Session class is a derivate of Storage. It will store as a dict anyhow called variable, but through the Storage interface only variables not named as internal private variables.

#### Private variables
 * _handler - reference to user-choosen Handler
 * _id - current session id
 * \_old\_id - used if the session regenerates id
 * _data - internal Storage object for session data

#### Public methods

 * start() - it will start the session, regenerate id, set cookies, retreive data if the session isn't new; it will call \_identity(), \_verify(), \_generate\_id(), \_retreive()
 * get_id() - it will return current session id
 * cleanup() - it will clean expired sessions depending on the provided interface by choosen Handler object (cookie based will do nothing); it will call Handler.clean() with the user preset timeout
 * save() - it will save session data using the _store()
 * destroy() - it will remove the session (cookies & data); it will call _remove()

#### Private methods

 * _generate\_id() - it will _only_ make a hash of ip, time, seed or it will call user supplied generator
 * _identify() - it will identify the session id (through client cookie                s)
 * _verify() - it will verify the session id with retreived data from handler object i.e. check for expiration, IP change (headers change?)
 * _store() - a simple wrapper around Handler.store(); data will be passed **unpickled**
 * _retreive() - a simple wrapper around Handler.retreive(); data will be awaited **unpickled**
 * _remove() - a simple wrapper around Handler.remove()

#### Main session parameters
web.config.session_parameters - Storage object:

 * cookie_name - name of the cookie which will transfer the session id; default value: 'webpy'
 * cookie_domain - cookie domain for the setcookie() when setting session id cookie; default value: None
 * timeout - number of second after a not-updated session will be considered expired; default value: 600
 * max_age - the maximum age a session can reach; default value: 24 * 60 * 60 (1day)
 * id_seed - a seed-string that will be used in the default Session._generator(); default value: 'web.py'
 * regenerate_id - should the session id be regenerated and set again with a cookie on every request?; default value: True
 * generator - a function to generate _random_ session ids, if False, the implicit generator (Session.\_generate\_id()) will be used; default value: False
 * ignore_change_ip - if the pair ( _id_, _ip_) doesn't match the retreived data from Handler objcet, then fail/raise exception/...; default value: False
 * ignore_expiration - should the session expiration be ignored?; default value: False
 * ignore_old_age - should the session be checked for max_age?; default value: True
 * handler - a Handler-like object to provide persistence for Session class; default value: 'db'

### Handler class
An abstract class which defines a interface to store/retreive/remove session data.

#### Public methods
 * store() - it will store the session data (& pickle them before that); if the argument _old\_id_ is set, it will look for an already storaged session data and if they are present overwrite them or else store as new
 * retreive() - it will retreive storaged data *unpickled* in a Storage object ( _id_, _ip_, _time_, _data_), if there aren't any for given _id_, it will return empty Storage object
 * remove() - it will remove storaged data for given _id_
 * clean() - optional function (may not be available for any Handler implementation [CookieHandler]), it will remove all session data, which been updated longer then before given _timeout_

### Handler parameters
web.config.handler_parameters as Storage object will include additional parameters that are necessary for various Handlers
#### DBHandler
 * db_table - table storing session data; default value: 'session_data'
#### FileHandler
 * file_dir - directory used to store session data; default value: '/tmp'
 * file_prefix - prefix to session data files; default value: 'sess'

### *Handler specs
 * [DBHandler](/sessions/dbhandler)
 * [FileHandler](/sessions/filehandler)
 * [CookieHandler](/sessions/cookiehandler) - **DANGEROUS, UNSECURE, EXPERIMENTAL**


## Notes
 * [Google Summer of Code project](/sessions/gsoc)
 * [installation instructions](/sessions/install)
 * [bazaar](http://bazaar-vcs.org/) branch: http://bazaar.launchpad.net/~karol.tarcak/webpy/webpy.sessions.branch