#!/usr/bin/python3

s = input("Input a string: ")

'''#Method-1(my own method)
#Time Complexity: O(n)
#Space Complexity: O(1)

#String to list
s=list(s)

f_c = s[0] #first character

#Replacing each character
for i,ch in enumerate(s):
    if ch == f_c and i != 0:
        s[i] = '$'

#List to String
s="".join(s)
print(s)'''

#Method-2 without converting to string
#Time Complexity: O(n)
#Space Complexity: O(n)
f_c = s[0]
i = 1
res = f_c

while i < len(s):
    if s[i] == f_c:
        res +='$'
    else:
        res += s[i]    
    i+=1
print(res)


