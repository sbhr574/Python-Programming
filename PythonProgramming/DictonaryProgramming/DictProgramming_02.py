emp = {'QA':['Subhajit',"Ashok","Pranab"],'Dev':'Niraj','DevOps':'kumar'}
print(len(emp))
print(emp.keys())
print(emp.values())
#key and value pair both
print(emp.items())
print('**********************')
del emp['QA']
print(emp)
emp.clear()
print(emp)
del emp


#emp.pop('Dev')
#print(emp)
#print(emp.get('QA'))
#emp.get('QA').remove('Pranab')
#print(emp)