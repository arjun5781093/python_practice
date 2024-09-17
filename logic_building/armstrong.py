import math

#A program that takes a positive number and output whether it is armstrong number or not

n = int(input("Enter number: "))

temp = n
count = math.ceil(math.log(n,10)) #Number of digits of number

total = 0
while temp > 0:
    total += (temp%10)**count
    temp = temp//10

print("Armstrong number" if total == n else "Not Armstrong number" )
