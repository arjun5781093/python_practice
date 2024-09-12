#!/usr/bin/python3

l=['abc','xyz','aba','1221']
count=0

for string in l:
    if len(string)>2 and (string[0] == string[-1]):
        count+=1
print(count)
