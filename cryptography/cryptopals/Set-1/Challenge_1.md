
This is a writeup for Challenge 1 from Set-I from cryptopals.com

I simply proceeded by converting the hex string to bytes and then encoding it to base64 with b64encode() method from base64 module.


python code:
```
import base64

hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
string_inbytes = bytes.fromhex(hex_string)

print(base64.b64encode(string_inbytes))
```
