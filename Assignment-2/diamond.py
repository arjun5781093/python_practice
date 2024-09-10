#!/usr/bin/python3

#A program to print diamond pattern

n=5
sp=n//2
st=1

for line in range(1,n//2+2):
    print(" "*sp,end="")
    print("*"*st)
   # print()
    sp-=1
    st+=2

sp=1
st=n//2+1
for line in range(n//2+2,n+1):
    print(" "*sp,"*"*st,sep="")
    sp+=1
    st-=2
