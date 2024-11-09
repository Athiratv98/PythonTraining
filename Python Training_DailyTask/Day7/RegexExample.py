# capture all numbers in test string.not the all
import re
def find_numbers_in_string(test_string):
   pattern=r"\d+"
   result=re.findall(pattern,test_string)
   return result
test_string="H6ello987"
print(find_numbers_in_string(test_string))

