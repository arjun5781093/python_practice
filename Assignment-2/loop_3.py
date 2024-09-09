#!/usr/bin/python3

#A program to find gcd of two numbers

#Time Complexity: O(max(m,n))
#Space Complexity: O(1)

m=int(input("Enter number-1: "))
n=int(input("Enter number-2: "))
gcd=1
i=2

while i <= max(m,n):
    if m%i == n%i == 0:
        gcd=i
    i+=1
print("GDC of two numbers is: ",gcd)
