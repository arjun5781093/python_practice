#!/usr/bin/python3

total_cl = int(input("Total number of classes held: "))
atten_cl = int(input("Total number of classes attended: "))
per_att = (atten_cl/total_cl)
print("Your attendance percentage is: ",per_att*100)

if(per_att >= 0.75):
    print("You are allowed to sit in exam")
else:
    print("You are not allowed to sit in exam")

