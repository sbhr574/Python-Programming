val1=(1,'java',67.45,True)
print(type(val1))
print(val1)
print(val1.index('java'))
print(val1[3])
# Negative indexing is present
print(val1[-1])
print('*************************************')

val2=(1,'java',67.45,True,1,1,1,'Python','Roy',2,2,2)
print(val2.count(1)) # o/p=5 because in python "True" boolean is returning value 1
print(val2.count(2))
print('*************************************')
# Slicing
val3=(1,'java',67.45,True,1,1,1,'Python','Roy',2,2,2)
print(val3[0:4])

# Immutable example
#val3[0]="Subhajit" # this is not possible because its immutable will throw an error
#print(val3)

