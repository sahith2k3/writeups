from Crypto.Cipher import AES
from Crypto.Util import long_to_bytes

AES.block_size = 16

def xor(msg, key): return b''.join(
    [bytes([byte ^ key[i % len(key)]]) for i, byte in enumerate(msg)])

def pkcs7_pad(text, size):
    pad_size = size - len(text)
    return text + long_to_bytes(pad_size) * pad_size


def pkcs7_unpad(text):
    pad_size = text[-1]

    if not isinstance(pad_size, int):
        return text
    else:
        if pad_size >= len(text):
            return text

    pkcs = True
    for i in text[-pad_size:]:
        if i != pad_size:
            pkcs = False
            break

    if pkcs:
        return text[:-pad_size]
    else:
        return text


def cbc_encrypt(pt, key, iv):
    ct = b""
    for i in range(0, len(pt), AES.block_size):
        pt_block = pkcs7_pad(pt[i:i+AES.block_size], AES.block_size)
        pt_iv_xor = xor(pt_block, iv)
        ct_block = AES.new(key, AES.MODE_ECB).encrypt(pt_iv_xor)
        ct += ct_block
        iv = ct_block
    return ct
