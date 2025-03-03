class createObj:
    place = "Bengaluru"

    def fun1(self):
        print("From function1 - "+self.place)

    def fun2(self):
        return self.place

test_obj = createObj()
print(test_obj.place)
test_obj.fun1()
print("From function2 - "+test_obj.fun2())


