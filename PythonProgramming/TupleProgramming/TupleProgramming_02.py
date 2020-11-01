val3=(1,'java',67.45,True,1,1,1,'Python','Roy',2,2,2)
print(type(val3))
print(val3)
# Converting tuple to list
l1 = list(val3)
print(type(l1))
print(l1)
# Converting tuple to Set
s1 = set(val3)
print(type(s1))
print(s1)
print("********************************************")

t1=('Subhajit')
print(t1)
print(len(t1))

t2=('Subhajit',)
print(t2)
print(len(t2))
print("********************************************")
# We can have list of tuples

list1 = [(10,23,34),('si',23,'ger'),(78,56.4,556)]
print(list1[1])
print(list1[2][2])
print("********************# Tuple creation with tuple constructor************************")

tup = tuple(['Java','Python','DB','Jango'])
print(type(tup))
print(tup[2])
print("****************# tuple unpacking Important topic****************************")
tup1 = tuple(['Java','Python','DB','Jango'])
x,y,z,d=tup1 # Make sure exact number of variables need to use during tuple unpacking
print(y)
print(x)
print(z)
print(d)
