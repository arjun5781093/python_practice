#!/usr/bin/python3

u = int(input("Enter number of units: "))

if u <=100:
    cost = 0
elif u <= 200:
    cost = (u-100)*5
else:
    cost = 500+(u-200)*10

print("Cost is ",cost)
