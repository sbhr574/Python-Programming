# Below library will show how to close a file automatically

with open("file.txt") as data:
    print("Checking file is closed or not",data.closed)
    value=data.read()
    print(value)

print("\nAgain Checking file is closed or not",data.closed)