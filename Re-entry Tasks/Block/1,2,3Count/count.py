import multiprocessing

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from secret import key
from pwn import xor
counter = 0
aes = AES.new(key, AES.MODE_ECB)


def chunk(input_data, size):
    return [input_data[i:i + size] for i in range(0, len(input_data), size)]

def worker_function(block):
    global counter
    key_stream = aes.encrypt(pad(str(counter).encode(), 16))
    result = xor(block, key_stream)
    counter += 1
    return result


def distribute_work(worker, data_list, processes=8):
    pool = multiprocessing.Pool(processes=processes)
    result = pool.map(worker, data_list)
    pool.close()
    return result


def encrypt_parallel(plaintext, workers_number):
    chunks = chunk(pad(plaintext, 16), 16)
    results = distribute_work(worker_function, chunks, workers_number)
    return b"".join(results)

plaintext = """The Song of the Count

You know that I am called the Count
Because I really love to count
I could sit and count all day
Sometimes I get carried away
I count slowly, slowly, slowly getting faster
Once I've started counting it's really hard to stop
Faster, faster. It is so exciting!
I could count forever, count until I drop
1! 2! 3! 4!
1-2-3-4, 1-2-3-4,
1-2, i love couning whatever the ammount haha!
1-2-3-4, heyyayayay heyayayay that's the sound of the count
I count the spiders on the wall...
I count the cobwebs in the hall...
I count the candles on the shelf...
When I'm alone, I count myself!
I count slowly, slowly, slowly getting faster
Once I've started counting it's really hard to stop
Faster, faster. It is so exciting!
I could count forever, count until I drop
1! 2! 3! 4!
1-2-3-4, 1-2-3-4, 1,
2 I love counting whatever the
ammount! 1-2-3-4 heyayayay heayayay 1-2-3-4
That's the song of the Count!
""" 

def main():
    plaintext = b"a"*800
    encrypted = encrypt_parallel(plaintext, 32)
    enc_blocks = chunk(encrypted, 32)
    for i,j in enumerate(enc_blocks):
        print(str(i)+ ": " + j.hex())

if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()
