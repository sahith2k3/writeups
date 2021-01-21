
this is the writeup for BASE64 task in GENERAL/ENCODING from cryptohack.org

I simply imported the base64 module to use b64encode() method to convert bytes to base64


python code:
```
import base64

ciphert_byte = bytes.fromhex("72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf")

plaint = base64.b64encode(ciphert_byte)

print(plaint)
```
