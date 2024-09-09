#!/usr/bin/python3

'''Accept 10 integers from user  and 
print their average value on the screen'''

i=1
mus=0
while i<=10:
    print("Enter number",i,": ",end="")
    num=int(input())
    i+=1
    mus+=num
print("Average: ",mus/10)
