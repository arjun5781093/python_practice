import math

#Right shifting the integer
#I/p: 1234 O/p: 4231
n=int(input("Enter a number: "))

if n > 9:
    c = math.ceil(math.log(n,10)) #Number of digits

    n = (n%10)*10**(c-1) + n//10

print(n)
