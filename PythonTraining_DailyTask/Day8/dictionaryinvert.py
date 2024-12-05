dict1={'a':4,'b':5,'c':2}
print(dict1)
new_data={}
for key, value in dict1.items():
    new_data[value] = key
    print(f"Key: {key}, value: {value}")
#for key, value in new_data.items():
       
    # print(key)
#     value=dict1[key]
#     new_data[value] = key
# print(new_data[value])