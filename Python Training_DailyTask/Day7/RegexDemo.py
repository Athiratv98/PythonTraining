import re
pattern='^a...s'
test_string='abyss'
result=re.match(pattern,test_string)
if(result):
    print("It's a match")
else:
    print("No match")