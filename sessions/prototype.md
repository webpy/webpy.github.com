---
layout: default
title: Prototype
---

# Prototype

-

    # some modules that are expected to be used
    import time
    
    import pickle # the default ASCII "pickling"
    import sha # Python2.5 hashlib
    
    # settings
    web.config.session_parameters = {
        use_flag : False, # will the session be used? if not then the Session object will not be created
        timeout : 600,
        id_seed : 'web.py',
        regenerate_id : True, # boolean, on every request regenerate id and set again cookie
        generator : False, # if False, use default generator

        ignore_change_ip : True, # boolean, if the pair ( id, ip ) doesn't match the db, then fail/raise exception/...
        ignore_expiration : False,

        handler : DBHandler()
    }

    web.config.handler_parameters = { # optional handler settings
        file_dir : '/tmp',
        db_table : 'session_data' # table name
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
                    '''return ( id, ip, data, time ) or maybe dictionary'''
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
