#for x in range(0,20):
#    print(x)

#for x in range(20):
#    print(x)

evenList = []
oddList = []

for val in range(20):
    if val%2 == 0:
        evenList.append(val)
    else:
        oddList.append(val)
print(evenList)
print(oddList)

print("*************************************************")
#Nested For loop
l1=['Subhajt','Mou','Das']
l2=['Java','Python',"C"]
l3=['Aus',"Ind","Ban"]

for a in l1:
    for b in l2:
        for c in l3:
            print(a + " "+b+" "+ c )

