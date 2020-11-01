with open("write.txt","a") as data:
    data.write("\n")
    data.write("Welcome")
    data.write("\t")
    data.write("here ")


print("\nAgain Checking file is closed or not",data.closed)