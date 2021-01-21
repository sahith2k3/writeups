
this is the writeup for Bytes and Big Integers task from GENERAL/ENCODING from cryptohack.org

To solve this task, I used long_to_bytes() method as mentioned in the question. I installed pycryptodome module to import and use this function

python code:
```
from Crypto.Util.number import long_to_bytes
print(long_to_bytes(11515195063862318899931685488813747395775516287289682636499965282714637259206269))
```
