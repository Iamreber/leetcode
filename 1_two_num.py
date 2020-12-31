array = [1,34,45,61,3,45,6,5,8,9]
a = range(0,len(array) - 1)
dic = dict(zip(array, a))

def two_num():
    tar = int(input("please input a interger\n"))
    for num in array:
        another = tar - num
        for i in a:
            if(another == array[i]):
                return dic[num], dic[another]
            else:
                pass

print(two_num())

