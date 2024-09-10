#!/usr/bin/python3

#A program to display a pattern

n=int(input("Enter a number: "))

for line in range(1,n+1):
    for col in range(1,line+1):
        print(col,end = " ")
    print()
