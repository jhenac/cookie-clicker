The Cookie Analysis


Introduction

It took me a week to finalize my code due in part to my wanting to find the optimal code out there. 
I learned about threading, scheduler, and applied strip, split, and time module in the process.

```
end = time.time() + 300
while time.time() < end:
    cookie.click()
    if round(time.time(), 0) % 5 == 0:
```

In this particular lines of code, the ```time.time()``` inside the while loop and for loop DOES NOT work
if placed inside a variable illustrated below:

```
current = time.time()
end = time.time() + 300
while current < end:
    cookie.click()
    if round(current), 0) % 5 == 0:
```

Note also that ```time.time()``` has to be rounded off to produce the desired result.

Another thing to note is that once it is able to purchase an upgrade, it will not purchase additional 
upgrade but instead will loop back to the beginning of the code.


Results

The objective was to find the optimal time breaks for the purchase of upgrades to produce higher 
cookies/per second given the limited 5-minute timeframe.

1. At 5-second interval, I was able to purchase 10 factories, 24 grandmas, and 30 cursors. By the end
of the code, my cookie looked like a pie. With the equipment, I was able to produce 70 cookies/second
and 675 remaining cookies.

2. At 10-second interval, I was able to purchase 5 mines, 16 factories, and 9 grandmas and produced 
126.6 cookies/second higher than #1 and with remaining 978 cookies 
by the end of the code.

3. At 15-second interval, I was able to purchase 6 mines, and 15 factories. Remaining unutilized cookies
are quite high at 1,141 cookies and cookies/second is lower than #2 at 120 cookies/second.

4. At 20-second interval, I was able to purchase 8 mines, and 7 factories and an even lower  
result at 108 cookies/second. 



Conclusion

A 10-second interval was the most ideal producing a result of 126.6 cookies/second compared to the
other interval tests. A higher time given for the build up of cookies does not guarantee a higher 
cookies/second result. However, since the cookie clicker is efficient, it can build up enough money
to buy higher priced upgrades.