#A program to print daywise calendar, given first day of the month and number of days in month
day=input("Enter first day of the month: ")
n=int(input("Enter number of days in month: "))
days_of_week = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

code = days_of_week.index(day)
#print(code)
#First line
print("Su Mo Tu We Th Fr Sa")
print('   '*code,end="")
for i in range(1,(7-code)+1):
    print(i,end="  ")

print()
#From second line
count=0
for j in range((7-code)+1,n+1):
    if count == 7:
        print()
        count=0
    if j >9:
        print(j,end=" ")
    else:
        print(j,end="  ")
    count+=1
