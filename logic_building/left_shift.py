import math

#Left shifting the integer
#I/p: 2341 O/p: 3412
n=int(input("Enter a number: "))

if n > 9:
    c = math.ceil(math.log(n,10)) #Number of digits
    
    n = (n%(10**(c-1)))*10 + (n//(10**(c-1)))

print(n)
