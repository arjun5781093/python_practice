l1=list(map(int,input("Enter list-1: ").split()))
l2=list(map(int,input("Enter list-2: ").split()))

def find_index(ele,li):
#Return list of indices of occurences of element in list
#O(n),O(n)
    l = []
    for i,num in enumerate(li):
        if ele == num:
            l.append(i)
    return l

if len(l1) != len(l2):
    print("False")
elif l1==l2 and l1!=[]:
    print("True")
elif l1==l2==[]:
    print("True")
else:
    ind_l = find_index(l1[0],l2)
    for each in ind_l:
        j=each
        i=0
        while i < len(l1):
            if l1[i] != l2[j]:
                break
            else:
                i += 1
                j = (j+1)%len(l2)
        else:
            print("True")
            break
    else:
        print("False")
