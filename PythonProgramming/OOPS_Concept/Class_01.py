class Person:

    def age(self):
        print("That person age is 28")

def place():
    print("He is from kaliyaganj")

person_Object=Person()
person_Object.age()
# Other way to call the method
Person.age(person_Object)
place()
print(person_Object)
print(person_Object.age)