import pandas as pd
details=pd.Series([70,80,78,90,99],index=['Athira','Anusree','Fathima','Das','abfr'])

print(details)
pos1=details.iloc[3]
print(pos1)
pos1=details.loc['Anusree']
print(pos1)
print('*************')
student={
    'Athira':60,
    'Anusree':56,
    'Abd':59,
    'rgdg':45

}
details=pd.Series(student)
print(details)
pos1=details.iloc[3]
print(pos1)
pos1=details.loc['Anusree']
print(pos1)
print("________")
print(details[details>58])
