#Create a program to read csv file which contain large text of some novel.
# Get the frequencies of all words in the file and Show the output in dataframe
import pandas as pd
import re
from collections import Counter
#opening the file
try:
    with open(r"C:\Users\Administrator\Desktop\PythonTraining\Milestone 1\Novel.csv",'r',encoding='utf8') as file:
        noveldata=file.read()
except FileNotFoundError as e:
    print("No such file present")
#find the words from the novel
words_count_by_character=re.findall(r"\b[\w'-]+\b",noveldata)
#finding the frequencies of words in the file
wordscount=Counter(words_count_by_character)
#printing in Dataframe
df=pd.DataFrame(wordscount.items(),columns=["word","count"])
print(df)