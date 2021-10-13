from Crypto.Util.number import *
from encrypt import e ,dp, n

ct = open("crypto\Re-entry Tasks\Intro\Godf\cipher.txt").read()

ct = bytes_to_long(bytes.fromhex(ct))

for k in range(2,e):
    p = (e*dp-1 +k) //k
    if n%p ==0:
        l=p
        print(l)
        break

p=l
q=n//p
pt = long_to_bytes(pow(ct,inverse(e,(p-1)*(q-1)),n))
print(pt)