---
layout: default
title: web.query()
---

# web.query()

used to send a SQL statement to the database.


        # store everything in the sql statement
        clean_query = str(
            'UPDATE ' + clean_update + 
            ' SET ' + clean_column + " = '" + clean_value.encode(output_charset) + 
            "' WHERE " + clean_where
        )
        # execute
        web.query(clean_query)