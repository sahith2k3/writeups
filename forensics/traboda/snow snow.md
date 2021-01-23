This is a write-up for the task 'Snow Snow'

Task:
```
"Ravi thinks there is something suspicious between these lines of this file. Can you help him find out what is suspicious?

Flag Format: flag{some_l33t_string}"
```
and a text file called 'THISISIT.txt' was given.


opening thi file..

```
I see you standing among them all    	 	  	      	 	  
  	       	      	   	   	    	  	     	     	       
Standing so strong ,proud and tall      	   	     	       	    
  	      	     	 	  	   	  	     	      	      
The world looks at you, but does not see       	   	    	      	      
   	   	    	  	     	     	 	    	    
Everything you sacrifice to keep us free	  	       	       	 
     	       	       	      	      	   	       	     	       	       
I'm here to say, to let you know    	      		     	 	 
	  		 	     	    	   	       	  
That you are loved, even if it doesn't show

You fight for our hopes,dreams,and liberty

You fight for our freedom

A hero to be

We want you to know, your never alone

For we are waiting, for you to come home

But the hardest thing for a person to be is you

A soldier, fighting to keep us free.

```

I could select whitespaces in the first nine lines, which was odd. So starting my attempt by assuming it is Whitespace Steganography,

I used this linux command ``` $ stegsnow -C THISISIT.txt```

``` 
ntio{eP1B35x4K3_aB3O0_q5_K00t}
``` was printed in the terminal.
as the flag format was given as ``` flag{some_l33t_string} ```

I used caesar cipher from dcode.fr to get the decrypt the flag which was
``` flag{wH1T35p4C3_sT3G0_i5_C00l} ```
