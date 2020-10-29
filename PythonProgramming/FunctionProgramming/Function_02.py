# Defualt Parameter
def func1(num1,num2=0):
    result=num1+num2
    return result
print(func1(50))

def func2(num1,num2=0,num3=0,num4=0):
    result=num1+num2+num3+num4
    return result
print("Result is :: ",func2(50,12,20))