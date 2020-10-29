# List indexing and slicing

list1=[10,20,30,40]
print(list1[2])
print(list1[-1])

list1=[10,20,30,40,40,40,40]
print(list1)
print(list1.count(40))
print(list1.count(10))
print(list1.count(44))
print(list1[1:])
print(list1[1:4])

list1[0]=888
print(list1)
list1[3]="roy"
print(list1)

list1.append("test")
print(list1)
list1.append(90909)
print(list1)

print(list1.insert(0,333))
print(list1)

print("*********************************************")
list12 = [10,20,30,40,50]
list21 = ['Roy','gsh','jsuis']
list_copy = list21.copy()
print(list_copy)
list21.append(list12)
print(list21)
