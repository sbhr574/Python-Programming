class A:
    def __init__(self):
        print("Constructor from Class A")

class B(A):
    def __init__(self):
        super().__init__()
        print("Constructor from Class B")

class C(B):
    def __init__(self):
        super().__init__()
        print("Constructor from Class C")

obj1 = C()

obj2 = B()

