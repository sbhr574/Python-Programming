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

class classC(classA,classB):

    def love3(self):
        print("Method from class c")

class classD(classC):

    def love4(self):
        print("Method from class c")

obj=classD()
obj.welcome()
obj.love4()
print(classD.mro())