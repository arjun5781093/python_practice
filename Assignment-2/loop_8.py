#!/usr/bin/python3

'''Ask user number of terms to be generated of a series. 
generate numbers for the following series and find its addition 
[9 + 99 + 999 + 9999+……..] '''

n=int(input("Enter number of terms to be generated: "))
i=1
#ser='9'
total = 0

while(i<=n):
    num=(10**i)-1
    total+=num
    print(num)
    i+=1

print("Addition: ",total)
