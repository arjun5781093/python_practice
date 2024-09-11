#!/usr/bin/python3

#No.of seconds to HH:MM:SS

sec=int(input("Input number of seconds: "))

if sec < 60:
    hh = 0
    mm = 0
    ss = sec
elif 60<=sec<3600:
    hh=0
    mm=sec//60
    ss=sec%60
else:
    hh=sec//3600
    mm=(sec%3600)//60
    ss=(sec%3600)%60

print("{:02}:{:02}:{:02}".format(hh,mm,ss))
