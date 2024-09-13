#!/usr/bin/python3

#A program to remove even numbers from the list
l=list(map(int,input("Enter list of numbers: ").split()))

res = [num for num in l if num%2!=0]
print(res)
