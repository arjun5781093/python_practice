#!/usr/bin/python3

#Take a number from user and print total of all odd numbers till that number.

'''Time Complexity: O(1)
   Space Complexity: O(1)'''

n=int(input("Enter a number: "))
if(n%2==0):
    print((n//2)**2)
else:
    print(((n//2)+1)**2)

