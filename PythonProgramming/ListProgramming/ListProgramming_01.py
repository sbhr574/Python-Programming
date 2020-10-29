list1 = [10,20,30]
print(type(list1))
list2 = [10,'roy',34,True]
print(list2)
print(len(list2))

list3 = list1+list2
print(list3)
print(len(list3))

#extend Operation
list4 = [10,20,30,40]
list5 = ["Subhajit","Roy"]
list4.extend(list5)
print(list4)
list6 = "Subhajit"
list4.extend(list6)
#list6 is string when extending with list4 its actully appending characters by characters.The reason is string is iterable
print(list4)