
try:
    numerator=int(input("Please enter numerator: "))
    demonimator=int(input("Please enter denominator: "))
    result=numerator/demonimator
    print(result)
except ZeroDivisionError as e:
    print("You cant devide by 0")
#except ValueError as e:
    print("please enter correct input")
except Exception as e:
    print("Something else happend.we are looking in to it")
    print(e)
print("completed successfully")

