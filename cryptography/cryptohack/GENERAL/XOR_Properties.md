
This is the writeup for XOR PROPERTIES task in GENERAL/XOR from cryptohack.org

given:
```
KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf
```

analyzing basic properties of xor like ```A ^ A = 0``` and ```A ^ 0 = A```,

i tried to get the flag by by doing the following operations on the last hex string ( FLAG ^ KEY1 ....):
```
let FLAG ^ KEY1 ^ KEY3 ^ KEY2 = X
X ^ KEY1 ^ KEY2 ^ KEY3 = FLAG

```
as KEY1 was already given and we also know KEY2 ^ KEY3, we can directly XORing ``` X, first and third equations ``` to get the FLAG

python code:
```
KEY1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
KEY2xorKEY3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")

a = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")
FLAG = xor(KEY1,KEY2xorKEY3,a)

print(FLAG)
```
