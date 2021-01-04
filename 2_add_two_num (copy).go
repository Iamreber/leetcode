def AddTwoNumber(list1,list2):
    list1.reverse()
    list2.reverse()
    list1.append(0)
    list2.append(0)
    list3 = []
    a = len(list1)
    b = 0
    for i in range(0,a):
        c = list1[i]+list2[i]+b
        b = list1[i]+list2[i]+b
        b = b%10
        list3.append(b)
        b = int(c/10)
    if(list3[a-1]==0):
        list3.pop()
    else:
        pass
    return (list3.reverse())

list1 = [1,2,3,4]
list2 = [1,2,3,4]

print(AddTwoNumber(list1,list2))

