#!/usr/bin/python3

x=int(input("Input the value of x: "))
n=int(input("Input number of terms: "))

s=0
ft=1 #First term
i=1
#mf=x/i #Multiplying Factor
val=ft

while i<=n:
    s+=val
    val=val*(x/i)
    i+=1
   # print("Multiplying factor: ",mf)

print("Sum of the series: ",s)
