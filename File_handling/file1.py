import json

with open("example.txt", "r") as file:
    content = file.read()
    print(content)

#Read line by line
with open("example.txt", "r") as file:
    for line in file:
        content = file.read()
        print(content.strip()) # strip() removes the new line characters

#OverWritting
with open("example.txt", "w") as file:
    file.write('''--------------------------------------------------"\n
"The term '..' is not recognized as a name of a 
cmdlet, function, script file, or executable program.
Check the spelling of the name, or if a path was included, 
verify that the path is correct and try again."\n
"---------------------------------------------------''')

#Without overwrite
# with open("example.txt", "a") as file:
#     file.write("i am good")

#For writing binary files 
# with open("example.bin", "wb") as file:
#     file.write("i am good")

#For reading binary files 
with open("example.bin", "rb") as file:
    content = file.read()
    print(content)

#need to move the cursor to read from beginning. w+ is used for reading and writing
with open('example.txt', 'w+') as txt:
    txt.write("Hello, sir, how are you")

    content1 = txt.read()
    print("content1 : "+content1)

    txt.seek(0) # moving the cursor

    content2 = txt.read()
    print("content2 : "+content2)

'''json.load function deserializes (decodes) a JSON file into a Python object 
(commonly a dictionary or a list). It takes a file-like object (file pointer) as an argument. '''
with open('./data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(data)
    print(type(data))

'''The json.dump() function serializes (encodes) a Python object into JSON format and writes it directly to a file.
 It takes the Python object and a file-like object (file pointer) as arguments. '''

# data = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }
# # Write the dictionary to a JSON file
# with open('./data.json', 'w') as f:
#     json.dump(data, f, indent=4) # Using 'indent' for human-readable formatting

