#write a function that returns the string after removing vowels

def RemoveVowels(s):
    vowels=['a','e','i','o','u']
    stringwithoutvowels=''
    for i in s:
        if i not in vowels:
            stringwithoutvowels+=i
    return stringwithoutvowels
print(RemoveVowels("ghssAdHaqello"))