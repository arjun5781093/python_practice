#!/usr/bin/python3

date=int(input("Enter date: ")[:2])%7
f_day=input("Enter first day of the month: ")
f_day=f_day.title()

days_of_week = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

fd_n=days_of_week.index(f_day) #Code of first days of the month
res = (fd_n + date-1)%7

print(days_of_week[res])
