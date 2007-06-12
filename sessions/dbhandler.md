---
layout: default
title: DBHandler for Sessions
---

# DBHandler for Sessions

# DBHandler


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
 * DBHandler will need an extra table in the db
 * this is still a "prototype" -> changes reserved :)

[Sessions specs](/sessions)