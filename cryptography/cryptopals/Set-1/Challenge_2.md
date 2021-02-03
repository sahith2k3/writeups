This is a writeup for Challenge 2 from Set-I from cryptopals.com

I used the xor function in pwn module in python.

```
from pwn import xor
a = bytes.fromhex("1c0111001f010100061a024b53535009181c")
b = bytes.fromhex("686974207468652062756c6c277320657965")
print(xor(a,b).hex())
```

and on execution
```
746865206b696420646f6e277420706c6179
```
was returned.
