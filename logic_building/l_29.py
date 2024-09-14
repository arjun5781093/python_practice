#!/usr/bin/python3

n1 = input("Enter binary number-1: ")
n2 = input("Enter binary number-2: ")

for bit1,bit2 in zip(n1,n2):
    print(bit1,bit2)
