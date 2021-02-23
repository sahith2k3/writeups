Hello guys,

This is a writeup for "Detect AES in ECB mode" frpm Set-I cryptopals.org


Python code:
```
referred to laconicwolf.com


def count_repetitions(ct, block_size):
	chunks = [ct[i:i+block_size] for i in range(0, len(ct), block_size)]
	reps = len(chunks) - len(set(chunks))
	return {'ct': ct, 'reps': reps}


cipher = open("8.txt", "r")
cipher_bytes = [bytes.fromhex(i.strip()) for i in cipher]
chunk_size = 16
repetitions = [count_repetitions(ct, chunk_size) for ct in cipher_bytes]
most_reps = sorted(repetitions, key= lambda x: x['reps'], reverse=True)[0]
print(most_reps)
```

output:
```{'ct': b'\xd8\x80a\x97@\xa8\xa1\x9bx@\xa8\xa3\x1c\x81\n=\x08d\x9a\xf7\r\xc0oO\xd5\xd2\xd6\x9ctL\xd2\x83\xe2\xdd\x05/kd\x1d\xbf\x9d\x11\xb04\x85B\xbbW\x08d\x9a\xf7\r\xc0oO\xd5\xd2\xd6\x9ctL\xd2\x83\x94u\xc9\xdf\xdb\xc1\xd4e\x97\x94\x9d\x9c~\x82\xbfZ\x08d\x9a\xf7\r\xc0oO\xd5\xd2\xd6\x9ctL\xd2\x83\x97\xa9>\xab\x8dj\xec\xd5fH\x91Tx\x9ak\x03\x08d\x9a\xf7\r\xc0oO\xd5\xd2\xd6\x9ctL\xd2\x83\xd4\x03\x18\x0c\x98\xc8\xf6\xdb\x1f*?\x9c@@\xde\xb0\xabQ\xb2\x993\xf2\xc1#\xc5\x83\x86\xb0o\xba\x18j', 'reps': 3}```
