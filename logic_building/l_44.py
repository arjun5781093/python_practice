# Program to find number in a list which is repeated exactly 'n' times
#Time Complexity: O(n)
#Space Complexity: O(n)

l = list(map(int,input("Enter list: ").split()))
n = int(input("Enter number: "))

f_c = dict() #Frequency count of each element of list
for num in l:
    f_c[num] = f_c.get(num,0) + 1

for k,v in f_c.items():
    if v == n:
        print(f'{k} repeated exactly {n} time(s)')
        break
else:
    print(f"There is no number which repeated exactly {n} time(s)")
