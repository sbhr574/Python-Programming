def func1(*args):
    print(args)
    print(args[2]) # tuples working on index beased

func1('Python','Java','C','JS')

def sum_of_num(*args):
    print("Sum of all number :: ",sum(args))

def max_num(*args):
    print(max(args))

def min_num(*args):
    print(min(args))

sum_of_num(10,34,50)
max_num(98,67,88,79.5,4)
min_num(3,4,5,3,1,56)