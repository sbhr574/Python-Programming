myset={10,20,30,40}
print(myset)

# Duplicate value not allowing
myset4 = {12,23,45,67,67,58,34}
print(myset4)

myset.add(222)
print(myset)
myset.pop() # For list pop operation is removing last index, but for set removing from random place
print(myset)
myset.remove(30)
print(myset)
myset.discard(899) #Difference between remove and discard is if value is not present in set will not
# throw any exception for discard but remove will throw error
print(myset)
print(len(myset))
myset1 = {12,23,34,55,'Subhajit',90}
print(myset1)
myset2 = myset1.copy()
myset1.clear()
print(myset1)
print(myset2)