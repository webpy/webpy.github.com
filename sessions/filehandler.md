---
layout: default
title: FileHandler for Sessions
---

# FileHandler for Sessions

# Specification

## Summary
The FileHandler will provide Handler-interface to file storage. It will store pickled data, session id & client's IP address in specified directory as files. Also retreiving & removing requested data by id will be implemented. On request the FileHandler will perform a generall clean up -> delete old session files.

## Implementation details

FileHandler is a derivate of Handler. All files will be created in the directory  web.config.handler_parameters.file_dir with prefix web.config.handler_parameters.file_prefix.

### Public methods
 * store() - it will store the session data (& pickle them before that); if the argument _old_id is set, it will look for an already storaged session data, it will create locks on both old & new session files, it will try to retreive time of the old session creation; after the pickle data is stored, the lock will be released; it will call \_acquire_lock(), \_release\_lock() and \_session\_file()
 * retreive() - it will retreive storaged data unpickled in a Storage object ( id, ip, time, data), if there aren't any for given id, it will return empty Storage object; all necessary lock procedures will be used; it will call \_acquire\_lock(), \_release\_lock() and \_session\_file()
 * remove() - it will remove storaged data for given id; all necessary lock procedures will be used, it will simply unlink the session file (ignoring if it's not existing); it will call \_acquire\_lock(), \_release\_lock() and \_session\_file()
 * clean() - it will remove all session data, which been updated longer then before given timeout; all necessary lock procedures will be used (however not blocking); it will call \_acquire\_lock() and \_release\_lock()


### Private methods
 * \_session\_file() - it will return the full name of the session storage file
 * \_lock\_file() - it will return the full name of the session storage lock file; ; it will call \_session\_file()
 * \_acquire\_lock() - it will create a lock file; if the lock file is already present, it will check, that the lock file is not older than 60s, in that case the old lock file will be erased; if blocking is set False, it will not wait; it will call \_lock\_file()
 * \_release\_lock() - it will simply unlink the session lock file (ignoring if it's not existing); it will call \_lock\_file()

### Requirements
FileHandler will need a storage directory (web.config.handler_parameters.file_dir) on the filesystem with write (& read) permission.

[Sessions specs](/sessions)