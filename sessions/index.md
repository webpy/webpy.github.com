---
layout: default
title: Sessions (GSoC)
---

# Sessions (GSoC)

The main session object will always be created as webpy starts. However the user/developer will choose it's usage. If needed the user will call start() method and there by inicializing handlers, variables from db-config like variables. The session will be implemented as storage object. Session identification will mostly rely on client cookies (optionally also on client IP address). All data will be stored/retrieved through handler object (DB-, file-, cookie?- based) as pickled ASCII strings. Save/commit & destroy methods will be created. The user will have the option to set various option including expiration timeout, handler, session id generator (a default will be provided).


# Prototype

    # some modules that I expect to use
    
    import time
    
    import pickle # the default ASCII "pickling"
    import sha # Python2.5 hashlib
    
    # settings
    web.config.session_parameters = {
        session_timeout : 600,
        session_id_seed : 'web.py',
        regenerate_id : True, # boolean, on every request regenerate id and set again cookie
        generator : False, # if False, use default generator

        ignore_change_ip : True, # boolean, if the pair ( id, ip ) doesn't match the db, then fail/raise exception/...
        ignore_session_expiration : False,

        handler : DBHandler(),

        handler_parameters : { file_dir : '/tmp' } # optional handler settings
    }

    
    class Session( Storage ):
            '''main session object
                    main instance variables
                            _generator - reference to user-supplied "unique random number generator" or just to default session generator function
                            _handler
                            _id
                            _data - internal Storage object'''
    
            def __init__( self ):
                    pass
    
            # public methods
            def start( self ):
                    '''starts the session, regenerates id, sets cookies
                            calls _identity, _verify, _generator function'''
                    pass
    
            def get_id( self ):
                    '''returns current session id'''
                    pass
    
            def cleanup( self ):
                    '''cleans expired sessions'''
                    pass

            def save( self ):
                    '''save session data'''
                    pass

            def destroy( self ):
                    '''removes session (including cookies)'''
                    pass            

            # private methods
            def _generate_id( self ):
                    '''implicit session id generator
                            "hashes" ip, time, seed, microtime (?), ...'''
                    pass
    
            def _identify( self ):
                    '''identifies session id (through cookies)'''
                    pass
    
            def _verify( self ):
                    '''verifies with retreived data from handler object'''
                    pass
    
            def _store( self ):
                    '''stores session data (wrapper around handler object)'''
                    pass
    
            def _retreive( self ):
                    '''retreive session data (wrapper around handler object)'''
                    pass
    
            def _remove( self ):
                    '''removes session data (wrapper around handler object)'''
                    pass
    # class
    
    class Handler:
            '''abstract handler class'''
            def __init__( self ):
                    pass
    
            def store( self, ip, id, data ):
                    '''takes
                            ip - client ip, probably number
                            id - string
                            data - dictionary'''
                    pass
    
            def retreive( self, id ):
                    '''return ( id, ip, data ) or maybe dictionary'''
                    pass
    
            def remove( self, id ):
                    pass
    # class
    
    def DBHandler( Handler ):
            def __init__( self ):
                    pass
    
            def clean( self, timeout ):
                    '''removes all expired sessions'''
                    pass
    # class
    
    def FileHandler( Handler ):
            def __init__( self ):
                    '''takes dir where to create session files'''
                    pass
    # class

# Notes
 * data will be stored in Session object member variable _data and passed as "pickled" (ASCII protocol) variables to Handler object
 * session id will be just a hash of some variables ([semi]random) and a seed
 * Session object will use web.ctx.session_parameters
 * DBHandler will need an extra table in the db
 * this is still a "prototype" -> changes reserved :)
 * [DBHandler specs](/sessions/dbhandler)


## Schedule
 * May 28 - June 9 (1st & 2nd week): getting familiar with SVN/Bazaar, internals of web.py, flup and jonpy's sessions; creating a DDL for storing sessions
 * June 10 - June 17 (3rd): creating DBHandler class
 * June 18 - July 8 (4th - 6th): creating Session class's identify/verify methods
 * July 9 - mid-term evulation deadline
 * July 10 - August 19 (7th - ...): finishing the Session class
 * August 20 - final evaluation deadline

## Tasks

### Administrative
 * Bazaar/SVN
 * blog

### DBHandler
 * create table DDL
 * write store(), retrieve(), remove()
 * test (& some docs)

### Session
 * write default session id generator(s)
 * write & test session cookie creation, identification, verification
 * write & test session id regeneration (mainly cookies & session identification)
 * write start()
 * write save()
 * write destroy(), cleanup()
 * test & docs


