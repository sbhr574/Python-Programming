try:
    read_op=open("file.txt")
    data=read_op.read()
    print(data) # File Read operation
    print(read_op.name) #To check file name
    print(read_op.mode) #To check in which mode it is
    print(read_op.closed) #To check file is closed or not
    read_op.close() # Closing the file
    print(read_op.closed)
except:
    print("Some problem is there")