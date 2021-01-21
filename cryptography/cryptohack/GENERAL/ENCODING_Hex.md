
this is the writeup for HEX task from GENERAL/ENCODING from cryptohack.org

I used fromhex() attribut of bytes to decode the hex string to bytes

python code
```
cipher = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
byte1 = bytes.fromhex(cipher)

print(byte1)
```
