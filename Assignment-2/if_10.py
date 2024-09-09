#!/usr/bin/python3

'''a program to accept the price of a bike and 
display the road tax and insurance to be paid 
according to the following criteri, 
also display total amount to be paid.'''

cp=int(input("Enter cost price of bike: "))

if cp<=50_000:
    tax = 0.05*cp
    ins = 0.05*cp
elif 50_000<cp<1_00_000:
    tax = 0.1*cp
    ins = 0.08*cp
else:
    tax=0.15*cp
    ins=0.2*cp

total=cp+tax+ins

print("Total amount to be paid: ",total)
