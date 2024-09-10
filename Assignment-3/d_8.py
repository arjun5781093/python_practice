#!/usr/bin/python3

n=int(input("Enter number: "))

b_e=bin(n)
c_0 = 0
c_1=0
i=2

while i<len(b_e):
    if b_e[i] == '0':
        c_0 +=1
    else:
        c_1 +=1
    i+=1
print("Number of 0's: ",c_0)
print("Number of 1's: ",c_1)
