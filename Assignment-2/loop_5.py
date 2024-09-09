#!/usr/bin/python3

#A program to calculate the count and sum of all digits

num=int(input("Enter a number: "))
count=0 #Count of digits
s_d=0 #Sum of digits

while num>0:
    count+=1
    s_d+=num%10
    num//=10
print("Count of digits: ", count)
print("Sum of digits: ",s_d)
