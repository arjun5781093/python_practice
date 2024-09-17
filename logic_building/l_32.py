#A program to count number of letters, spaces, and numbers of given input string

s = input("Input a string: ")
le_c = 0 #Letter count
nu_c = 0 #Digits count
sp_c = 0 #Space count

for ch in s:
    if ch.isalpha():
        le_c += 1
    elif ch.isdigit():
        nu_c += 1
    elif ch == " ":
        sp_c += 1
        
print(f'Letter Count: {le_c}\nNumbers Count: {nu_c}\nSpaces Count: {sp_c}')
