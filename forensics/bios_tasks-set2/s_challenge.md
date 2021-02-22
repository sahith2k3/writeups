Hello guys,

This is a writeup for s_challenge4.png from task

Using exiftool..
```
Warning                         : [minor] Text chunk(s) found after PNG IDAT (may be ignored by some readers)
Datecreate                      : 2019-03-15T12:55:21+05:00
Datemodify                      : 2019-03-15T12:55:20+05:00
Comment                         : 5a6d78685a33746f4e474e724d334a7a587a52794d31387a646a4e796558646f4d33497a66513d3d
```

a comment in hex was found.

Using python3,

```
>>> bytes.fromhex('5a6d78685a33746f4e474e724d334a7a587a52794d31387a646a4e796558646f4d33497a66513d3d')
b'ZmxhZ3toNGNrM3JzXzRyM18zdjNyeXdoM3IzfQ=='
>>> import base64
>>> base64.b64decode('ZmxhZ3toNGNrM3JzXzRyM18zdjNyeXdoM3IzfQ==')
b'flag{h4ck3rs_4r3_3v3rywh3r3}'
```

the flag is found.
