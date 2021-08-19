from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from functools import reduce
import random

key = random.randbytes(16)
iv = random.randbytes(16)

cipher = AES.new(key, AES.MODE_CBC, iv)
decipher = AES.new(key, AES.MODE_CBC, iv)


def first(inp):
    prepend = b"comment1=cooking%20MCs;userdata="
    append = b";comment2=%20like%20a%20pound%20of%20bacon"
    return cipher.encrypt(
        pad(
            (prepend + inp.replace(b";", b'";"').replace(b"=", b'"="') + append),
            16,
        )
    )


def second(ct):
    a = decipher.decrypt(ct)
    if b";admin=true;" in a:
        return True
    else:
        return False


if __name__ == "__main__":
    ct = first(b" admin true ")

    # we want to find b";admin=true;" in ct
    # and as ; and = are quoted out in the first function, we'll have to use someother character and perform bitflipping
    # therefore we input " admin true " and xor previous ct block bits to convert spaces to ; and =

    blocks = [ct[i : i + 16] for i in range(0, len(ct) - 16 + 1, 16)]
    #[b'comment1=cooking', b'%20MCs;userdata=', b'?admin?true?;com', b'ment2=%20like%20', b'a%20pound%20of%2', b'0bacon\n\n\n\n\n\n\n\n\n\n']
    exploit_block = list(blocks[1])
    exploit_block[0] ^= 27
    exploit_block[6] ^= 29
    exploit_block[11] ^= 27

    blocks[1] = bytes(exploit_block)
    print(second(b"".join(blocks)))
