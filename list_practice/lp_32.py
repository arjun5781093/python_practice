#!/usr/bin/python3

#Time Complexity: O(nm)
#Space Complexity: O(1)

l1 = [5,7,9,12]
l2=[12,9,7,5]

n1=len(l1)
n2=len(l2)

if n1<=n2:
    for num in l1:
        if num not in l2:
            print("False")
            break
    else:
        print("True")
else:
    for num in l2:
        if num not in l1:
            print("False")
            break
    else:
        print("True")
