# add two number 
# 1. maybe two list is different length 
# 2. maybe there is a carry

def XchgList(ls1,ls2):
    if(len(ls1)>len(ls2)):
        pass
    else:
        ls1,ls2=ls2,ls1

def AppendListWith0(length,ls):
    if(len(ls)>length):
        print("the length is two long")
    elif(len(ls)<length):
        for i in range(0,length-len(ls)):
            ls.append(0)
    else:
        pass

        
def AddTwoNumber(ls1,ls2):
    ls3 = []
    k = 0
    XchgList(ls1,ls2)
    AppendListWith0(len(ls1)+1,ls1)
    AppendListWith0(len(ls1)+1,ls2)
    for i in range(0,len(ls1)):
        w = k
        j = ls1[i]+ls2[i]+w
        if(int(j/10) == 1):
            j = j%10
            k = 1
        else:
            k = 0
        ls3.append(j)
    if (ls3[-1] == 0):
        ls3.pop()
    else:
        pass 
    return ls3

ls1 = [9,9,9,9,9]
ls2 = [1]

print(AddTwoNumber(ls1,ls2))

        

    

