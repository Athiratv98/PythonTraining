def Arithmetic(a,b,oper_type):
    if(oper_type=='add'):
        return a+b
    elif(oper_type=='sub'):
        return a-b
    elif(oper_type=='mul'):
        return a*b

input_code=''

while(input_code!='4'):
   
    print("\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Quit")
    input_code=input("Enter your choice")
    if(input_code=='1'):
        a=int(input("Enter first number"))
        b=int(input("Enter second number"))
        print("a+b: ",Arithmetic(a,b,oper_type='add'))
    elif(input_code=='2'):
        a=int(input("Enter first number"))
        b=int(input("Enter second number"))
        print("a-b: ",Arithmetic(a,b,oper_type='sub'))
    elif(input_code=='3'):
        a=int(input("Enter first number"))
        b=int(input("Enter second number"))
        print("a*b: ",Arithmetic(a,b,oper_type='mul'))