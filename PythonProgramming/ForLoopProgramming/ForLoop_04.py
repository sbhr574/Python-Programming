tup1=[10,20,30]
tup2=[11,22,33]
tup3=[12,13,14]

list1=[tup1,tup2,tup3]

# for val in list1:
#     print(val[0])
#     print(val[1])
#     print(val[2])

# Another way we can retrieve the data with the help of tuple unpacking
for x,y,z in list1:
    print(x)
    print(y)
    print(z)
