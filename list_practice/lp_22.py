#!/usr/bin/python3

l=list(map(int,input("Enter list of number: ").split()))
num = int(input("Enter a item for which you want to know index: "))

'''#Method-1
#Time Complexity: O(n)
#Space Complexity: O(1)
print(l.index(num))'''


#Method-2
#Time Complexity: O(n)
#Space Complexity: O(1)
for ind,each in enumerate(l):
    if each == num:
        print("Index: ",ind)
        break
else:
    print("Item not found")

'''#Method-3
#Time Complexity: O(n)
#Space Complexity: O(1)
if num in l:
    print("Index:",l.index(num))
else:
    print("Item not found")
'''
