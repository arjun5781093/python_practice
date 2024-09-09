#!/usr/bin/python3

#A program to find whether given number is prime or not using while-else

num=int(input("Enter a number: "))

i=2
while i<num:
    if num%i==0:
        print("Not a prime number")
        break
    i+=1
else:
    print("Prime number")
