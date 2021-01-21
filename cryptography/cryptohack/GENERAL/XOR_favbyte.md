
This is the writeup for Favourite byte task in GENERAL/XOR from cryptohack.org

a hexstring ```73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d``` was given and we were told 

that the key was only one byte.

As the first character of the flag format is 'c', I tried XORing the first byte with the decimal value of 'c'
and the key was returned as ```0x10```

so XORing the ciphertext with the key, the flag was found.

python code:
```
from pwn import xor
from Crypto.Util.number import bytes_to_long


cipher_hex = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
cipher_byte = bytes.fromhex(cipher_hex)


key= cipher_byte[0] ^ ord('c')

for i in cipher_byte:
    print(chr(bytes_to_long(xor(i, key))), end='')
print()
```
