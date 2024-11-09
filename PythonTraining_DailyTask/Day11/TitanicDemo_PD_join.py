import pandas as pd
df=pd.read_csv(r"C:\Users\Administrator\Desktop\Python Training\Titanic\titanic.csv")
print(df.head())
#print first 4 of the age column

print(df['Age'].head())
#print(df.loc[0:4,'age'])

# create a subset of datafram with only two columns age and sex
print(df[['Age','Sex']].head())

#filter out the people whose age <25 and print the dataframe
#print(df['Age']<25)] -------will give boolean values.
print(df[df['Age']<25])

#print total line in the dataframe
print(len(df.index))
print("-----")
#average age of the data in the dataframe
print(df['Age'].mean())

#print(df['Age'].sum()/len(df.index))#Not accurate

# average fare price of all male passengers whose age is less than 25  
df_name=df[df['Sex']=='male']
print(df_name)
df_age=df_name[df_name['Age']<25]
print(df_age)
print(df_age['Fare'].mean())

#OR

print(df[ (df['Age']<25) & (df['Sex']=='male') ])


#what percentage of the passengers survived in titanic
print("--------")
df_Survived=df[df['Survived']==1]
total_survived=len(df_Survived.index)
total_pass=len(df.index)
print((total_survived/total_pass)*100)