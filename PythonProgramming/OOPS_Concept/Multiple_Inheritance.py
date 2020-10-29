class classA:

    def love1(self):
        print("Method from class A")

    def welcome(self):
        print("I am from class A")

class classB():

    def love2(self):
        print("Method from class B")

    def welcome(self):
        print("I am from class B")

# Below two classes are example of MRO(Method Resolution Order)

class classC(classB,classA):

    def love3(self):
        print("Method from class c")

obj = classC()
obj.love1()
obj.love2()
obj.love3()
obj.welcome()
print(classC.mro())

class classD(classA,classB):

    def love4(self):
        print("Method from class c")

obj=classD()
obj.welcome()
print(classD.mro())