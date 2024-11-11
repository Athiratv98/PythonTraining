import pandas as pd
df=pd.read_csv(r"titanic.csv")

#1.Compare the average age of passengers who who survived with those who didn't

avg_age_survived=df[df['Survived']==1]["Age"].mean()

avg_age_not_survived=df[df['Survived']==0]["Age"].mean()
print(avg_age_survived,avg_age_not_survived)

# calculate the survival rate by gender

print(df.groupby('Sex')['Survived'].mean())
#Add new cloumnfamily size
df['Family_size']=df['SibSp']+df['Parch']
print(df[['SibSp','Parch','Family_size']].head())

# calculate average survival rate by family size
print("----------")
avg_survival_rate_family=df.groupby('Family_size')['Survived'].mean().reset_index()
print(avg_survival_rate_family)
avg_survival_rate_family.columns=['Family_size','Family_survival_rate']

#merge the family survival rate back into original Dataframe

print("-----")
df=pd.merge(df,avg_survival_rate_family,on='Family_size',how='left')

#display resulting dataframe
print(df)