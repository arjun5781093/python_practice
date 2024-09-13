#!/usr/bin/python3
import math

l = [3,5,7,13]
flag=1
for num in l:
    #Checking whether a number is prime or not
    i=2
    while i<=math.sqrt(num):
        if num%i==0:
            print("False")
            flag=0
            break
        i+=1
    
if flag != 0:
    print("True")
