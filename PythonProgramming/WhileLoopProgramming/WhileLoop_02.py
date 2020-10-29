num=2

while num<6:
    print(num)
    num=num+1
    if num==5:
        break
else:
    print("Num is not valid")

print("*************************************************")

val = 3
while val<9:
    val=val+1
    if val==6:
        print("Python")
        continue
    print(val)
else:
    print("Num is not valid")
print("*************************************************")

x=5
while x<10:
    print("pal")
    pass
    break

print("*************************************************")

feedback=""

while feedback not in ["1","2","3","4"]:
    feedback = input("Please enter feedback:: ")
    print("Thank You !!!")