This is a writeup for Challenge 4 from Set-I from cryptopals.com

I used the scoring system from [Challenge 3](https://github.com/sahith2k3/writeups/blob/main/cryptography/cryptopals/Set-1/Challenge_3.md)
and saved the line and their scores in a dictionary adn finally printed the line with the maximum score.

Python code
```
from pwn import xor
import string

text = open("4.txt", "r").read()

letterFrequency = {'E' : 12.0,'T' : 9.10,'A' : 8.12,'O' : 7.68,'I' : 7.31,'N' : 6.95,'S' : 6.28,'R' : 6.02,'H' : 5.92,
'D' : 4.32,'L' : 3.98,'U' : 2.88,'C' : 2.71,'M' : 2.61,'F' : 2.30,'Y' : 2.11,'W' : 2.09,'G' : 2.03,'P' : 1.82,
'B' : 1.49,'V' : 1.11,'K' : 0.69,'X' : 0.17,'Q' : 0.11,'J' : 0.10,'Z' : 0.07 }

text = text.split('\n')

def chall3(cipher_byte):
    scores = {}

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
    return max(scores, key=scores.get), scores[max(scores, key=scores.get)]

line_scores = {}

for line in text:
    line = bytes.fromhex(line)
    plain_line, score = chall3(line)
    line_scores[plain_line] = score

print(max(line_scores, key=line_scores.get))
```
