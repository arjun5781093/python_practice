#!/usr/bin/python3

l=[1,2,3,4,5]

print("Sum of all numbers in list: ",sum(l))

prod=1
for num in l:
    prod*=num
print("Product of all numbers in list: ",prod)

print("Largest of all numbers in list: ",max(l))

print("Smallest of all numbers in list: ",min(l))
