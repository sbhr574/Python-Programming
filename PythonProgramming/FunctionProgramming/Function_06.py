def func1(**kwargs):
    print(type(kwargs))
    print(kwargs)
    print(kwargs['name'])

func1(name='Subhajit',age=34,address='Kaliyaganj')

print('*********************************************')

def func2(*args,**kwargs):
    print(args)
    print(kwargs)

func2(10,20,30,name='Roy',roll=78)

print('*********************************************')

def func3(new_name,*args,**kwargs):
    print(new_name)
    print(args)
    print(kwargs)

func3(10,20,30,name='Roy',roll=78)