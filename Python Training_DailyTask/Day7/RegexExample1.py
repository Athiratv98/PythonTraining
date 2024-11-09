#find words starting with a specific letter
import re
def findword_starts_with(input_string):
    pattern=r"\bh\w*"
    result=re.findall(pattern,input_string,re.IGNORECASE)
    return result
test_string="H6ello987 hai cometo hht"
print(findword_starts_with(test_string))