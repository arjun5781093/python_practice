#!/usr/bin/python3

#A program to find whether a number is perfect square or not without using built-in functions
x=int(input("Enter a number: "))

'''Method-1
#Time Complexity: O(n)
#Space Complexity: O(1)
y=1

while(y<=(x//2)):
    if x%y==0:
        #y is a factor of x
        if y*y==x:
            print("{} is a perfect square".format(x))
            break
    y+=1
else:
    print("{} is not a perfect square".format(x))
'''

#Method-2
#Time Complexity: O(1)
#Space Complexity: O(1)
sqr=int(x**0.5)
if sqr*sqr==x:
    print("{} is perfect square".format(x))
else:
    print("{} is not perfect square".format(x))
