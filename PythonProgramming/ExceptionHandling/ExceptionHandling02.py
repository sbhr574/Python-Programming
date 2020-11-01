try:
    num1=int(input("Enter some value:: "))
    num2=int(input("Enter some value again:: "))
    result = num1/num2
    print("Result is ",result)
except TypeError as error:
    print("Problem with type error",error)
except ZeroDivisionError as error:
    print("Do not enter zero",error)
except ValueError as error:
    print("Enter valid entry",error)

finally:
    print("This block will execute always.No matter its get fail or pass.")
