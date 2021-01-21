
This is the writeup for XOR STARTER task from GENERAL/XOR from cryptohack.org

I used the inbuilt ```ord()``` and ```chr()``` methods to change ASCII to decimal and vice-versa.

Then I XORed between the decimal value and 13 as given in the task.

python code:
```
string = "label"
new_string = ""
for i in string:
    new_string += chr(ord(i)^13)

print(new_string)
```
*** WHEN "label" was XORed with 13, "aloha" was returned, which is the Havaiian word for Hi .... and bye :)
