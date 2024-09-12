#!/usr/bin/python3

'''Write a Python function that takes two lists and
 returns True if they have at least one common member.'''

#Time Complexity: O(n^2)
#Space Complexity: O(1)

def check_same(l1,l2):
    for num in l1:
        if num in l2:
            return True
    return False

n1=int(input("Enter length of list-1: "))
l1=[]
for i in range(n1):
    l1.append(int(input("Enter a number to list-1: ")))
n2=int(input("Enter length of list-2: "))
l2=[]
for i in range(n2):
    l2.append(int(input("Enter a number to list-2: ")))
'''
l1=list(map(int,input("Enter list-1: ").split()))
l2=list(map(int,input("Enter list-2: ").split()))'''
print(check_same(l1,l2))
