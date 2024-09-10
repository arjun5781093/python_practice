#!/usr/bin/python3

#A program to print a pattern


n=int(input("Enter a number: "))
ch=1 #Number of times * needs to be printed
sp=n-1 #Number of times space needs to be printed

for line in range(1,(n//2)+2):
    print(" "*sp,"*"*ch,sep="")
    ch+=2
    sp-=2    

ch=n-2 #Number of times * needs to be printed
sp=2 #Number of times space need to be printed
for line in range((n//2)+2,n+1):
    print(" "*sp,"*"*ch,sep="")
    ch-=2
    sp+=2
