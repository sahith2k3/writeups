This is the write up for Less-2 - " GET-Error Based- Intiger-based"

In [Less-1](https://github.com/sahith2k3/writeups/blob/main/SQLi%20Labs/Less-1.md) user input is inputted like ```id='user_input'```
and we exploited by typing ```'``` by ourselves and commented the other single quote out.

Here, Integer Based input exists...
more like ``` id = <integer> ``` so we dont need to use a single quote like in [Less-1](https://github.com/sahith2k3/writeups/blob/main/SQLi%20Labs/Less-1.md)

The login dump can simply be retrieved by using
```
UNION SELECT 1, group_concat(username,0x7c,password),3 FROM users 

```
