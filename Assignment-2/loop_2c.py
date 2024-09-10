#!/usr/bin/python3

#A program to display the pattern

n=int(input("Enter a number: "))

ch='10'
ch_t=n-1 #Number of times character need to be printed
sp=0 #Number of spaces to be printed

for line in range(1,n+1):
    print(" "*sp,ch*ch_t,"1",sep="")
    sp+=1
    ch_t-=1
