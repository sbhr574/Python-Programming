# ShortHand Opeartion for if else

print("Welcome")
if 1>10:print("Yes")
print("Thanks")

marks=93
print("Yes from if A+") if marks>=90 else print("from else A")

# Nasted If-else

Salary = input("Please Enter your salary :: ")
print(type(Salary))
sal=int(Salary)
print(type(sal))
#sal = 1900
if sal>50000:
    print("Eligible for Car loan")
    if sal>80000:
        print("Eligible for Home loan")
        if sal>100000:
            print("Premium Customer")
else:
    print("Sorry")

