#!/usr/bin/python3

#Write a Python program to find the list of words that are longer than n
# from a given list of words.

#Time Complexity: O(nm);n:number of words;m-length of each word
#Space Complexity: O(k); k-number of words whose length is greater than the given number

words=input("Enter list of words: ").split()
n=int(input("Enter number: "))

res=[word for word in words if len(word)>n]
print(res)
