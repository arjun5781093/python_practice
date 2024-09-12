#!/usr/bin/python3

l=list(map(int,input("Enter list of numbers: ").split()))
unique=[]

Method-1
for i in range(len(l)):
    if l[i] not in unique:
        unique.append(l[i])


#Method-2 
#unique = list(set(l))
print("Unique elements from the list are: ",unique)
