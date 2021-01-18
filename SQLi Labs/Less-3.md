Hello guys,

This is the write-up for Less-3 'GET - Error based - Single quotes with twist'.

So getting started,

using a single quote and comment after the numeric parameter for id
``` ?id = 1' -- -```,
an error is returned.
``` You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' at line 1 ```

so the input after id is not going into a simple ``` WHERE id = '<input>';```

