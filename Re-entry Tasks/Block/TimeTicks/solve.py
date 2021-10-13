import time
from base64 import b64decode
from hashlib import md5
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import string

ct = open("crypto\Re-entry Tasks\Block\TimeTicks\encrypted", "r").read()
ct = b64decode(ct)

i = 1586383840
end = i - 2600000 #3days
printable = [i.encode() for i in string.printable]

while True:
    if i == end:
        print("three days")
        exit()
    key = md5(str(i).encode()).digest()
    pt = AES.new(key, AES.MODE_ECB).decrypt(ct)
    i -= 1
    try:
        pt = unpad(pt, 16)
        # if all(i in pt for i in [b"{", b"}", b"_"]):
        #     print(pt)
        if b"bi0s{" in pt:
            print(pt, i)
            break
    except:
        continue
    continue

#flag = bi0s{s0met1m3n3s_y0u_n33d_t0_bru73}