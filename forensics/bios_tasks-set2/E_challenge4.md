Hello guys,

This is a writeup for E_challenge4.jpg from tasks set 2.

Using Exiftool a comment was found...
```
Comment: Njk2ZTYzNzQ2NjdiNzkzMDc1NWY2NzMwNzQ1ZjM3NjgzMzVmNjY2YzM0Njc3ZA==
```

Using Python3,

```
>>> import base64
>>> base64.b64decode('Njk2ZTYzNzQ2NjdiNzkzMDc1NWY2NzMwNzQ1ZjM3NjgzMzVmNjY2YzM0Njc3ZA==')
b'696e6374667b7930755f6730745f3768335f666c34677d'
>>> bytes.fromhex('696e6374667b7930755f6730745f3768335f666c34677d')
b'inctf{y0u_g0t_7h3_fl4g}'
```

Therefore flag is found.
