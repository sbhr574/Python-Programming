# the factorial of a given number
# def fact(x):
#     print(x)
#     if x == 0:
#         return 1
#     return x * fact(x - 1)
#
# x=int(input())
# print(fact(x))

#
# num = input("Please enter a number :: ")
# num = int(num)
# d=dict()
# for i in range(1,num+1):
#     d[i]=i+i
#
# print(d)

# Question:
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98

values=input("Enter a list of values :: ")
l=values.split(",")
print(type(l))
t=tuple(l)
print(l)
print(t)