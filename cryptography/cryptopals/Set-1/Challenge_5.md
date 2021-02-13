This is a writeup for Challenge 5 from Set-I from cryptopals.com


Python code:
```
from pwn import xor
from binascii import hexlify
stanza = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''

key = b"ICE"
i = bytearray(stanza, 'utf-8')
cipher_byte = xor(i, key)
print(hexlify(cipher_byte).decode('utf-8'))
```

ouput:
```0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f```
