#!/usr/bin/python3

#Time Complexity: O(n)
#space Complexity: O(1)

l=[1,1,1,1,1,2,4,45,70,20,13]
n=len(l)

mi1=l[0] #first minimum
ma1=float('-inf') #First maximum
for num in l:
    if num < mi1:
        mi1=num
    if ma1 < num:
        ma1=num

mi2=float('inf') #Second minimum
ma2=float('-inf') #Second maximum
for num in l:
    if mi1 < num and mi2 > num:
        mi2=num
    if ma1 > num and ma2 < num:
        ma2=num

if mi2 != float('inf'):
    print("Second smallest element is",mi2)
else:
    print("No second smallest element")

if ma2 != float('-inf'):
    print("Second largest element is",ma2)
else:
    print("No second largest element")
