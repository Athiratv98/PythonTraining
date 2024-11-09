
while True:
    num1=int(input("Enter your first number: "))
    num2=int(input("Enter your second number: "))
    print("\n1.Addition\n2.Subtraction\n3.Multiplication4.\n4.Division\n5.Exit\nEnter your choice")
    choice=input()
    if(choice=='1'):
        result=num1+num2
        print("Addition: ",result)
    elif(choice=='2'):
        result=num1-num2
        print("Subtraction: ",result)
    elif(choice=='3'):
        result=num1*num2
        print("Multiplication: ",result)
    elif(choice=='4'):
        result=num1/num2
        print("Division: ",result)
    elif(choice=='5'):
        break
    else:
        print("invalid choice")

