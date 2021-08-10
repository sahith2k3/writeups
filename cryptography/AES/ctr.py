from Crypto.Util.number import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def xor(msg, key): return b''.join(
    [bytes([byte ^ key[i % len(key)]]) for i, byte in enumerate(msg)])


def AES_CTR_encrypt(pt, key, nonce, counter):
    ct = b""
    pt = pad(pt, 16)
    for i in range(0, len(pt), 16):
        nonce_counter = nonce + long_to_bytes(counter + i//16)
        XOR_key = AES.new(key, AES.MODE_ECB).encrypt(nonce_counter)
        ct += xor(pt[i:i+16], XOR_key)
    return ct


def AES_CTR_decrypt(ct, key, nonce, counter):
    pt = b""
    for i in range(0, len(ct), 16):
        nonce_counter = nonce + long_to_bytes(counter + i//16)
        XOR_key = AES.new(key, AES.MODE_ECB).encrypt(nonce_counter)
        pt += xor(ct[i:i+16], XOR_key)
    return unpad(pt, 16)


if __name__ == "__main__":
    nonce = b"FLAGFLAGFLA"
    counter = 452582389000

    key = b"YELLOW SUBMARINE"
    pt = b"crypto{ok_b00m3r}_23445554"

    ct = AES_CTR_encrypt(pt, key, nonce, counter)
    pt = AES_CTR_decrypt(ct, key, nonce, counter)
    print(ct)
    print(pt)
