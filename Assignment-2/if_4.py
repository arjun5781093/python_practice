#!/usr/bin/python3

marks=int(input("Enter your marks: "))

if marks >80:
    g="A"
elif 60<marks<=80:
    g="B"
elif 50<marks<=60:
    g="C"
elif 45<marks<=50:
    g="D"
elif 25<marks<=45:
    g="E"
else:
    g="F"

print("Grade: ",g)
