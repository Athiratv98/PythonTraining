#create a function that returns if the number is even or odd

def EvenOrOdd(number):
    if(number%2==0):
        return " is Even"
    else:
        return " is Odd"

print("Hello User!please enter input")
user_input=int(input())
#print("User your input is ",user_input)
result=EvenOrOdd(user_input)
print(result)