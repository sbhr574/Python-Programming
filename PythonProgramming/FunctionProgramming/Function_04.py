even_num=[]
odd_num=[]
def func1(list1):
    for val in list1:
        result = val%2==0
        if(result):
            even_num.append(val)
#            print(val," Even")
        else:
            odd_num.append(val)
#            print(val," Odd")
    print(even_num)
    print(odd_num)

func1([10,3,45,60,8,9,5,6])