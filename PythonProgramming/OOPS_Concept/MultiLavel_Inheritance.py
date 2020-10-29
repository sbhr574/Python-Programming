class classA:
    print("From class A")

    def love(self):
        print("Method from class A")

class classB(classA):
    print("From class B")

    def love(self):
        print("Method from class B")

class classC(classB):
    print("From class C")

    def love(self):
        print("Method from class c")

obj = classC()
obj.love()