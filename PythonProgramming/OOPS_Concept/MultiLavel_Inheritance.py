class classA:
    print("From class A")

    def love(self):
        print("Method from class A")

class classB(classA): # classB extending classA
    print("From class B")

    def love(self): # love method overloading here from class A
        print("Method from class B")

class classC(classB): # classC extending classA
    print("From class C")

    def love(self): # love method overloading here from class B
        print("Method from class c")

obj = classC()
obj.love()