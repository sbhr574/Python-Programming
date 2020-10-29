class name:

    def __init__(self):
        print("Hello Python")

x=name()

print("***************************")

class cons:
    def __init__(self,val1,val2):
        self.fname=val1
        self.lname=val2
        print("Hello "+self.fname+" "+self.lname)

    def sum(self,x,y):
        self.v1=x
        self.v2=y

        return self.v1+self.v2


y=cons("Subhajit","Roy")
print(y.sum(98,100))