---
layout: default
title: DBHandler for Sessions
---

# DBHandler for Sessions

# Specification

## Summary
The DBHandler will provide Handler-interface to db storage.
It will store pickled data, session id & client's IP address in db. Also retreiving & removing requested data by id will be implemented. On request the DBHandler will perform a generall clean up -> delete old session rows.

## Implementation details

DBHandler is a derivate of Handler.

### Public methods
 * store() - it will store the session data (& pickle them before that); if the argument _old\_id is set, it will look for an already storaged session data and if they are present overwrite them or else store as new; if there is already stored data (SELECT), it will do an UPDATE on the table, otherwise it will just call INSERT
 * retreive() - it will retreive storaged data unpickled in a Storage object ( id, ip, time, data), if there aren't any for given id, it will return empty Storage object; it will do a SELECT on the storage db-table
 * remove() - it will remove storaged data for given id; it will not do a check to see if there is any stored data under given id, it will only call DELETE
 * clean() - it will remove all session data, which been updated longer then before given timeout (DELETE)

### Requirements
DBHandler will need an extra table in the db (where \<name\> == web.config.handler_parameters.db_table):

      CREATE TABLE <name> (
        id CHAR(129) UNIQUE NOT NULL,
        ip CHAR(16) NOT NULL,
        created int NOT NULL,
        touched int NOT NULL,
        data TEXT
      );

[Sessions specs](/sessions)