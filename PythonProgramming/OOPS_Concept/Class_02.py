class man:

    def age(self):
        print("That person age is 28")

    def place(self):
        print("He is from kaliyaganj")

    def sum(self,num1,num2):
        print(num1+num2)

# man_Obj = man()
# man_Obj.sum(12,80)

# We can create multiple object and assign values in those objects

man_Obj1 = man()
man_Obj1.name='Abir'
man_Obj1.roll="AB12"
man_Obj1.country='India'
man_Obj1.city='Bangalore'

man_Obj2 = man()
man_Obj2.name='Gho'
man_Obj2.roll="Gh12"
man_Obj2.country='Nepal'
man_Obj2.city='Thimpu'

print(man_Obj1.name)
print(man_Obj2.name)