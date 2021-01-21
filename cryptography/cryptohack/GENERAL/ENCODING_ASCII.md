
This is the write up for ASCII task in GENERAL/ENCODING from cryptohack.com

I simply used the inbuilt function ```chr``` to convert decimal to ASCII

python code:
```
ciphertext = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

string = ''
for i in ciphertext:
    string += chr(i)

print(string)
```
