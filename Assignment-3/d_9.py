#!/usr/bin/python3

print("Which input needs to be converted to integer: ")
print("1.Binary","2.Octal","3.Hexadecimal",sep="\n")
ch=int(input("Enter your choice: "))


if ch == 1:
    s=input("Enter Binary string: ")
    print("Integer Equivalent: ",int(s,base=2))

elif ch == 2:
    s=input("Enter Octal string: ")
    print("Integer Equivalent: ",int(s,base=8))

elif ch == 3:
    s=input("Enter Hexadecimal string: ")
    print("Integer Equivalent: ",int(s,base=16))
