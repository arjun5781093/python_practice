#!/usr/bin/python3

#Accept 20 numbers from user and display total of only even numbers. 

total=0
i=1
while i<=20:
    print("Enter a number",i)
    num=int(input())
    if num%2==0:
        total+=num
    i+=1
print("Sum of only even numbers: ",total)
