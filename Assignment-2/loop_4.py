#!/usr/bin/python3
mus=0
count=0
num=0
prod=1

while (1):
    num=input("Enter a number, press q to quit: ")
    if(num=='q'):
        break
    num=int(num)
    mus+=num
    count+=1
    prod*=num
   
print("Product of all numbers: ",prod)
print("Average: ",mus/count)
