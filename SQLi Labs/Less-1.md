Hello guys.
This is the first time im doing something related to SQL injection. I have basic knowledge about sql syntax and functions...

This is the write up for Less-1 - " GET-Error Based- Single Quotes - String"


started with a [URL].../Less-1/ page, which instructed me to input the ID as parameter with numeric value.

So I start with adding ```?id=1``` after the URL and got 

Your Login name:Dumb
Your Password:Dumb

in the page.

and using different numbers after 2, I got different Login names and passwords.
So I realized this is ?id=x , is going into an sql command like
```SELECT * WHERE id = x;```

As the name of the Lesson suggests I start with a single quote Error
