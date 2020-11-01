try:
    read_op=open("file.txt")
    data=read_op.read()
    print(data) # File Read operation
    print(read_op.closed)
except Exception as error:
    print("Some problem is there",error)

finally:
    read_op.close()  # Closing the file
    print(read_op.closed)