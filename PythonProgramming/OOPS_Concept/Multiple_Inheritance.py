class classA:

    def love1(self):
        print("Method from class A")

    def welcome(self):
        print("I am from class A")

class classB():

    def love2(self):
        print("Method from class B")

    def welcome(self): # welcome method overriding from classA
        print("I am from class B")

    def calling_welcome_FromclassA(self):
        classA.welcome(self);
        print("I am from calling welcome From classA")

# Below two classes are example of MRO(Method Resolution Order)

class classC(classB,classA): # classB and classA mro order

    def love3(self):
        print("Method from class c")

obj = classC()
obj.love1()
obj.love2()
obj.love3()
obj.welcome()
obj.calling_welcome_FromclassA()
print(classC.mro())

class classD(classA,classB): # classA and classB mro order

    def love4(self):
        print("Method from class c")

obj=classD()
obj.welcome()
print(classD.mro())