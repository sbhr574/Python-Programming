status = False
langs = ['Java','Python','JS','Csharp']

for val in langs:
    if val=='JS':
        status=True
        print(status)
        break
    else:
        print("Value not found from that list")

if status:
    print("Got the value")
else:
    print("Value Not Found")