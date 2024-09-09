#!/usr/bin/python3

#A program to find whether given year is leap year or not

y = int(input("Enter year: "))

if y%4 == 0:
    if y%100==0:
        if y%400==0:
            print(y," is leap year")
        else:
            print(y," is not leap year")
    else:
        print(y," is leap year")
else:
    print(y," is leap year")

