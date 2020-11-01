try:
    content=open("C:\\Users\\Subhajit\\PycharmProjects\\Python-Programming\\readme.txt","r")
    print(content.read())
    print("Read is done.")
except:
    print("Facing some problem.")


try:
    content=open("C:\\Users\\Subhajit\\PycharmProjects\\Python-Programming\\readme1.txt","r")
    print(content.read())
    print("Read is done.")
except FileNotFoundError as error:
    print("Facing some problem.", error)

print("Execution is done.")