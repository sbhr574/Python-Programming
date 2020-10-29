# Without Argument
def func1():
    print('Welcome func1')
    c=10+23
    print(c)
    print('Bye func1')

# Calling the finc1 function
func1()

print('*********************************************')

# With Argument
def func2(num1,num2):
    print('Welcome func2')
    c=num1+num2
    print(c)
    print('Bye func2')
func2(10,20)
print('*********************************************')
# Return operation
def func3(num1,num2):
    result=num1+num2
    return result
print(func3(50,67))
