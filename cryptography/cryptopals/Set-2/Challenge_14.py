import random
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.number import long_to_bytes

key = b"YELLOW SUBMARINE"
AES.block_size = 16

prepend_length = random.randint(1, 21)
prepend_str = random.randbytes(prepend_length)


def enc(pt):
    pt = prepend_str + pt + base64.b64decode(        "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK")
    global key
    return AES.new(key, AES.MODE_ECB).encrypt(pad(pt, 16))


if __name__ == '__main__':
    # len of random string + flag
    input_ = b"A"
    len_last = len(enc(input_))

    for i in range(2, 17):
        len_ = len(enc(input_*i))
        if len_ - len_last == 16:
            len_ran_flag = len_ - len(input_*i) - 16
            break

    for i in range(32, 49):
        if enc(b"A"*i)[16:32] == enc(b"A"*i)[32:48]:
            len_rand = 48 - i
            break
        elif enc(b"A"*i)[32:48] == enc(b"A"*i)[48:64]:
            len_rand = 64 - i
            break

    len_flag = len_ran_flag - len_rand

    fixed_len = 16 - len_rand % 16
    unknown_bytes = b""

    for i in range(1, len_flag+1):
        input_len = fixed_len + 16 - i % 16
        temp_enc = enc(b"A"*input_len)[16*(i//16+1):16*(i//16+2)]
        for j in range(256):
            if enc(b"A"*input_len+unknown_bytes+long_to_bytes(j))[16*(i//16+1):16*(i//16+2)] == temp_enc:
                unknown_bytes += long_to_bytes(j)
                break

    print(unknown_bytes)
