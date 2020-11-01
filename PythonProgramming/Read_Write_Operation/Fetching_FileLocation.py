import os

file = os.getcwd()
print(file)
print(os.path.dirname(file))

# with open(os.path.dirname(file)+"\\readme.txt") as data:
#     print("Checking file is closed or not",data.closed)
#     value=data.read()
#     print(value)
#
# print("\nAgain Checking file is closed or not",data.closed)