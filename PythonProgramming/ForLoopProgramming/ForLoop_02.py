set1={10,20,30.0,'baby',30,True}

for val in set1:
    print(val)

print("*************************************************")

mydict = {1:"Subhajit",2:"Roy"}
for val in mydict:
    print(val)

for val1 in mydict.items():
    print(val1)

for a,b in mydict.items():
    print(a)
    print(b)

#Only Printing the Values
for c in mydict.values():
    print(c)
