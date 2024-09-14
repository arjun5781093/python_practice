#!/usr/bin/python3

'''Method-1
#Time Complexity: O(klogk), k-no.of digits-log(n,base=10)
#Space Complexity: O(k)

n=int(input("Enter a number: "))
count=0 #Number of digits
l=[] #list of digits
num=0

#getting digits
while n > 0:
    count+=1
    l.append(n%10)
    n=n//10

#Sorting the list of digits in descending order
l.sort(reverse=True)

#Making number from the list of digits
i=count-1
for each in l:
    num = num*10 + each
    i-=1
print(num)'''

#Method-2: using hash table concept
hash = [0]*10
n=int(input("Enter number: "))

while n > 0:
    hash[n%10] +=1
    n=n//10

j=9
num=0
while j >= 0:
    while hash[j]:
        num = num*10 + j
        hash[j]-=1
    j-=1
print(num)
