class cons:
    state_name = "West Bengal"
    vill = "KALIYAGANJ"  # class attribute

    def __init__(self, vill, post):
        self.vill = vill  # obj attribute > class attribute
        self.post = post
        print("Village name : " + self.vill + " " + self.post)

    def fun01(self):
        print("From function01 - "+self.vill)


cons_obj1 = cons("kaliyaganj", "Birth")
print(cons_obj1.vill)  # will print obj attribute. Because obj attribute gets higher priority then class attribute
cons_obj1.fun01()
cons_obj2 = cons("Kodathi", "Job")


