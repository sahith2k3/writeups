import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.number import long_to_bytes
key = b"YELLOW SUBMARINE"
AES.block_size = 16

def ecb(pt):
    pt += base64.b64decode("Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK")
    global key
    return AES.new(key, AES.MODE_ECB).encrypt(pad(pt, 16))

if __name__ == "__main__":

    # finding length of uknown string
    input_ = b"A"
    len_last = len(ecb(input_))

    for i in range(2, 17):
        len_ = len(ecb(input_*i))
        if len_ - len_last == 16:
            len_unkwown = len_ - len(input_*i) - 16
    #len_unkwown = 128

    # byte-at-a-time-attack
    unknown_bytes = b""

    for i in range(1, len_unkwown+1):
        len_A = 16 - i % 16
        ct = ecb(input_*len_A)[16*(i//16):16*(i//16+1)]
        for j in range(256):
            if ecb(input_*len_A + unknown_bytes + long_to_bytes(j))[16*(i//16):16*(i//16+1)] == ct:
                unknown_bytes += long_to_bytes(j)
                break

    print(unknown_bytes)
