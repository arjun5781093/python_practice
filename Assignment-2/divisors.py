#!/usr/bin/python3

#A program to print all divisors for a number
import math


l=[] #Divisors of given number
n=int(input("Input a number to know it's divisors: "))

for i in range(1,math.floor(math.sqrt(n))+1):
    if(n%i==0):
        l.append(i)
        if(n//i != i):
            l.append(n//i)
print("Divisors of {} are".format(n),*l)
