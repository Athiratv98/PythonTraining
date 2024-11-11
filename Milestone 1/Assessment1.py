import pandas as pd
import re
from collections import Counter
try:
    with open(r"C:\Users\Administrator\Desktop\PythonTraining\Milestone 1\Novel.txt",'r',encoding='utf8') as file:
        noveldata=file.read()
except FileNotFoundError as e:
    print("No such file present")
words_count_by_character=re.findall(r"\b[\w'-]+\b",noveldata)
wordscount=Counter(words_count_by_character)

print(pd.DataFrame(wordscount.items(),columns=["word","count"]))