#!/usr/bin/python3

#A program to find whether two lists are cirucularly identical or not

l1=list(map(int,input("Enter list-1: ").split()))
l2=list(map(int,input("Enter list-2: ").split()))
'''l1=[1,2,3,4]
l2=[2,1,3,4]'''

#Edge cases
if len(l1) != len(l2):
    print("False")
elif l1==l2 and l1!=[]:
    print("True")
elif l1==l2==[]:
    print("True")
else:
    j=l2.index(l1[0])
    i=0
    while i < len(l1):
        if l1[i] != l2[j]:
            print("False")
            break
        else:
            i += 1
            j = (j+1)%len(l2)
    else:
        print("True")


def find_index(ele,li):
#Return list of indices of occurences of element in list
#O(n),O(n)
    l = []
    for i,num in enumerate(li):
        if ele == num:
            l.append(i)
    return l

'''
ind_l = find_index(l1[0],l2)
print(ind_l)
if ind_l:
    for ind in ind_l:
        i=0
        j=ind
        while i<len(l1) and  l1[i] == l2[j]:
            i+=1
            j = (j+1)%len(l2)
        if i > len(l1):
            print("True")
            break
        else:
            print("False")
            break
else:
    print("False")
'''
