#!/usr/bin/python3

s1=input("Enter string-1: ")
s2=input("Enter string-2: ")

res = s2[:2] + s1[2:] + " " + s1[:2] + s2[2:]

print(res)
