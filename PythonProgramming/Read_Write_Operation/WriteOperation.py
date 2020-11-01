with open("write.txt","w") as data:
    print("Checking file is closed or not",data.closed)
    data.write("New data added tesrt")
    # value=data.read()
    # print(data.mode)
    # print(value)

print("\nAgain Checking file is closed or not",data.closed)