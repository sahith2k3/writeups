Hello guys,

This is the writeup for Loops task from tasks set 2.

The task is the make to sh programs which print the following patterns

```
Pattern 1: 
    #
   ##
  ###
 ####
#####

Pattern 2:
        #
       ###
      #####
     #######
    #########
   ###########
  #############
```
  
Shellscript codes:
------------------
Pattern 1:
```
#!/bin/sh

a=1
while [ "$a" -le 5 ]
do 
        b=`expr 5 - $a`
        while [ "$b" -ge 1 ]
        do 
                echo -n " "
                b=`expr $b - 1`
        done
        b="$a"
        while [ "$b" -ge 1 ]
        do
                echo -n "#"
                b=`expr $b - 1`
        done
        echo
        a=`expr $a + 1`
done
```

Pattern 2:
```
#!/bin/sh
a=1
while [ "$a" -le 7 ]
do
        b=`expr 7 - $a`
        while [ $b -gt 0 ]
        do
                echo -n " "
                b=`expr $b - 1`
        done
        b=`expr $a + $a - 1`
        while [ $b -gt 0 ]
        do
                echo -n "#"
                b=`expr $b - 1`
        done
        echo
        a=`expr $a + 1`
done
```
