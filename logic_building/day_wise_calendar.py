#A program to print daywise calendar, given first day of the month and number of days in month
#Time Complexity: O(31)
#Space Complexity: O(1)
day=input("Enter first day of the month: ")
n=int(input("Enter number of days in month: "))
days_of_week = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

code = days_of_week.index(day)
#First line
print("Su Mo Tu We Th Fr Sa")
print('   '*code,end="") #printing space in the first line
for i in range(1,(7-code)+1):
    print(i,end="  ")

print()
#From second line
count=0
for j in range((7-code)+1,n+1):
    if count == 7: #To print 7 numbers in one line
        print()
        count=0
    if j >9: #if number to be printed is of two digits, print only one space
        print(j,end=" ")
    else: #if number to be printed is of one digit, print two spaces
        print(j,end="  ")
    count+=1
