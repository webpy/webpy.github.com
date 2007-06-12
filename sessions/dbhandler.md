---
layout: default
title: DBHandler for Sessions
---

# DBHandler for Sessions

# DBHandler

The DBHandler will provide Handler-interface to db storage.
It will store pickled data, session id & client's IP address in db. Also retreiving & removing requested data by id will be implemented. On request the DBHandler will perform a generall clean up -> delete old session rows (cleanup(timeout)).


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

# Notes
 * DBHandler will need an extra table in the db
 * this is still a "prototype" -> changes reserved :)

[Sessions specs](/sessions)