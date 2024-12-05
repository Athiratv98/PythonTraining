#write a for loop to print user names multiple times
#take users names and limit from user
def Namescountprint(names,count):
    '''this function print the number of times the name need to print'''
    for i in range(count):
        print(names)
        print(i)
        
print("Please enter the username")
username=input()
print("The number of times name need to print")
limit=int(input())
Namescountprint(username,limit)