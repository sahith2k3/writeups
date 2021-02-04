This is a writeup for Challenge 3 from Set-I from cryptopals.com

I started by taking english [letter frequencies](https://gist.github.com/pozhidaevak/0dca594d6f0de367f232909fe21cdb2f)

so I let the scoring system be equal to the sum of the relative frequencies of english alphabets and reduced the score by 10% for every character in the 

plain text which wasnt a letter or characters in ```',.'?! ' ``` which included a whitespace. so starting a for loop for values between 0, 255 i.e all possible

numbers one byte can be, and added scores and plain text to a dictionary and printed the plaintext with maximum score.


Python code:
```
from pwn import xor
import string


letterFrequency = {'E' : 12.0,'T' : 9.10,'A' : 8.12,'O' : 7.68,'I' : 7.31,'N' : 6.95,'S' : 6.28,'R' : 6.02,'H' : 5.92,
'D' : 4.32,'L' : 3.98,'U' : 2.88,'C' : 2.71,'M' : 2.61,'F' : 2.30,'Y' : 2.11,'W' : 2.09,'G' : 2.03,'P' : 1.82,
'B' : 1.49,'V' : 1.11,'K' : 0.69,'X' : 0.17,'Q' : 0.11,'J' : 0.10,'Z' : 0.07 }


cipher_byte = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")

scores= {}

for i in range(256):
    temp_key = bytes(i)
    temp_plain = xor(cipher_byte, i)
    score = 0
    for j in temp_plain:
        c = chr(j)
        if c in string.ascii_lowercase:
            score += letterFrequency[c.upper()]
        if c in string.ascii_uppercase:
            score += letterFrequency[c] * 0.5
    score /= len(cipher_byte)
    for j in temp_plain:
        if chr(j) not in (string.ascii_letters + ",.'?! "):
            score /= 2
    scores[temp_plain] = score
print(max(scores, key=scores.get))
```

Output:
```b"Cooking MC's like a pound of bacon"```
