#Get the maximum key in the given dictionary

dict1={3:'helo',1:4,8:54,67:53,78:23,24:'hello'}
maximum=-2
for key in dict1:
    if key>maximum:
        maximum=key
print("key: ",maximum,"and the value is ",dict1[maximum])

    #OR
print(dict1.keys())
print(type(dict1.keys()))
print(max(dict1.keys()))