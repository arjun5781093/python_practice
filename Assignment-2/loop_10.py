#!/usr/bin/python3

x=int(input("Input the value of x: "))
n=int(input("Input number of terms: "))

r=-(x**2) #Common ratio

print("The value of the series: ")
val=x
i=1
while i<=n:
    print(val)
    val=val*r
    i+=1

ans=(x*((r**n)-1)/(r-1))
print("Sum of the series: ",ans)
