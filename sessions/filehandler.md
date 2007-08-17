---
layout: default
title: FileHandler for Sessions
---

# FileHandler for Sessions

# Specification

## Summary
The FileHandler will provide Handler-interface to file storage. It will store pickled data, session id & client's IP address in specified directory as files. Also retreiving & removing requested data by id will be implemented. On request the FileHandler will perform a generall clean up -> delete old session files.

## Implementation details

FileHandler is a derivate of Handler.

### Public methods
 * store() -
 * retreive() -
 * remove() -
 * clean() -

### Private methods
 * _session_file() - it will store the session data (& pickle them before that); if the argument _old_id is set, it will look for an already storaged session data, it will create locks on both old & new session files, it will try to 
 * _lock_file() -
 * _acquire_lock() -
 * _release_lock() -

### Requirements
FileHandler will need a storage directory (web.config.handler_parameters.file_dir) on the filesystem with write (& read) permission.

[Sessions specs](/sessions)