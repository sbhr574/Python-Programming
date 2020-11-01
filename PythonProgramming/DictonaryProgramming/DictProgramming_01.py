emp = {'QA':'Subhajit','Dev':'Niraj','DevOps':'kumar'}
print(emp)
print(type(emp))
# Two ways we can get the value
print(emp['QA'])
print(emp.get('DevOps'))

# Any Type of value can be putted
emp1 = {'IT':'Avin','Country':'India','Age':45,67:'Number'}
print(emp1)

emp = {'QA':['Subhajit',"Ashok","Pranab"],'Dev':'Niraj','DevOps':'kumar'}
print(emp)
print(emp.get('QA')[1])
emp2 = emp.get('QA')
print(emp2[2])

emp3 = {'QA':'Roy',"Dev":{"Frontend":'Niraj',"Backend":'Vikram'}}
print(emp3.get('Dev').get("Frontend"))
print(emp3['Dev']['Backend'])
# process to add a new entry
emp3['Manager']='susmita'
print(emp3)

emp3['Dev']['GUI'] = 'Manoj'
print(emp3)

# process to update new value on existing key
emp3['Manager'] = 'Roy'
print(emp3)

#Deletion
emp3.pop("QA")
print(emp3)
# popitem is removing last in fast order(LIFO)
emp3.popitem()