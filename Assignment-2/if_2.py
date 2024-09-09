#!/usr/bin/python3


amt=int(input("Enter amount: "))

if amt >= 2000:
    print("#2000 note: ",amt//2000)
    amt = amt % 2000
if amt >= 500:
    print("#500 note: ",amt//500)
    amt=amt%500
if amt >= 100:
    print("#100 note: ",amt//100)
    amt=amt%100
if amt>=50:
    print("#50 note: ",amt//50)
    amt%=50
if amt>=10:
    print("#10 note: ",amt//10)
    amt%=10
if amt>=5:
    print("#5 coin: ",amt//5)
    amt%=5
if amt>=2:
    print("#2 coin: ",amt//2)
    amt%=2
if amt>= 1:
    print("#1 coin: ",amt)
