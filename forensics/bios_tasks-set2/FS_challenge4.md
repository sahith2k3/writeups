Hello guys,

This is a writeup for FS_challenge4.png from tasks set 2.

When we try to open the png image, it doesnt open with a "File Format error" 

opening this image with ghex, we can identify that magic number is incorrect.

It is ```90 50 4e 47 0d 0a 1a 0a``` instead of ```89 50 4e 47 0d 0a 1a 0a```.

So correcting it and opening it again, the image whas the flag.

The flag is ```inctf{7h4nk5_for_h3lp1ng_m3}```
