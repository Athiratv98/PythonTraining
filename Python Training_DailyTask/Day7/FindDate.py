import re
# find the date which are in a string in format yyyy mm rdd\b
def find_date(input_string):
    #pattern=r'\b\d{4}[-/]\d{2}[-/]\d{2}\b'
    pattern=r'\b\d{4}-\d{2}-\d{2}|\b\d{4}/\d{2}/\d{2}\b'
    result=re.findall(pattern,input_string)
    return result
input_string='i have work on 2024-04-02 and 2024/05/82'
print(find_date(input_string))