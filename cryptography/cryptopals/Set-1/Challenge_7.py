This is a writeup for Challenge 7 from Set-I from cryptopals.com




Python code:
```
from Crypto.Cipher import AES
from base64 import b64decode

key = b"YELLOW SUBMARINE"

cipherfile = b64decode((open("7.txt", "r").read()))
plaintext = AES.new(key, AES.MODE_ECB).decrypt(bytes(cipherfile))

print(plaintext.decode("utf-8"))
```

output:
```
