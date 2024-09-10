#!/usr/bin/python3

#A program to find gcd of two numbers

#Time Complexity: O(min(m,n))
#Space Complexity: O(1)

#Method-1
n1=int(input("Enter number-1: "))
n2=int(input("Enter number-2: "))
gcd=1
i=min(n1,n2)

while i>1:
    if n1%i == n2%i == 0:
        gcd=i
        break
    i+=1
print("GCD of two numbers is: ",gcd)


'''#Method-2: Eucledian Algorithm
n1=int(input("Enter number-1: "))
n2=int(input("Enter number-2: "))

while n1>0 and n2>0:
    if n1>n2:
        n1=n1%n2
    if n2>n1:
        n2=n2%n1
if n1==0:
    print("GCD of two numbers is {}".format(n1,n2,n2))

if n2==0:
    print("GCD of two numbers is {}".format(n1,n2,n1))
'''
