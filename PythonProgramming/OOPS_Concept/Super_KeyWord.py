# Example 1
class rik:
    def roy(self):
        print("Rik khub valo.")

    def bye(self):
        print("bye from rik")

class rai(rik):
    def roy(self):
        super().roy()
        super().bye()
        super(rai, self).bye()
        print("rai khub valo.")

obj = rai()
obj.roy()

# Example 2
class test:
    def __init__(self,name):
        print("from cons "+name)

    def m1(self):
        print("from test")

class test1(test):
    def __init__(self):
        super().__init__('test class')
    def m2(self):
        print("from test1")

xy = test1()
xy.m2()