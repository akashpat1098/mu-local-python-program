import pandas  as pd
import os 
import numpy as np
def getfilePath(fileName):
    currentDir=os.getcwd()
    fullPath=os.path.join(currentDir,fileName)
    return fullPath
df=pd.read_csv(getfilePath("police.csv"))

print(df.head())

print(df.shape)

print(df.info())

df['stop_date']=pd.to_datetime(df['stop_date'])
df['stop_date']=pd.to_datetime(df['stop_date'],format="%H:%M").dt.time
print(df.info)

print(df.isnull().sum())

df.drop(['county_name'],axis=1,inplace=True)
print(df.describe())

print(df['search_type'].value_counts())

print(df['driver_gender'].isnull().sum())

df['driver_gender'].fillna(df['driver_gender'].mode(),inplace=True)
print(df['driver_gender'].isnull().sum())

print(df.sample(7))

print(df['driver_gender'].nunique())

print(df.columns)

print(df.nsmallest(4,"driver_age"))

print(df.nlargest(4,"driver_age"))

print(df.groupby('driver_race').agg(np.mean))

print(df.groupby('driver_race').get_group('Asian'))

print(df.groupby('driver_race').driver_age.describe())

print(df.loc[:5,['driver_age','violation']])

print(df.loc[(df.driver_age < 16) & (df.violation == 'Speeding')])

print(df.iloc[:5,:5])
print(df[['stop_date','driver_age','driver_race','violation','stop_outcome']].sort_values(by='driver_age'))

print(df.query('45 < driver_age < 50').head())

print(df.query('driver_age == 17 and driver_gender == "F"'))

print(df.set_index('stop_date').head(4))

print(df.duplicated().sum())

df.drop_duplicates(inplace=True)
print(df.duplicated().sum())

newdf=pd.get_dummies(df.driver_race,prefix="driver_race_").iloc[:,0:]
print(newdf.head())

numerical_df=df.select_dtypes(include=[np.number])
print(numerical_df.head())

categorical_df=df.select_dtypes(include='object')
print(categorical_df.head())

comb_df =pd.concat([numerical_df,categorical_df],axis=1)
print(comb_df.head(4))

def currentAge(dob):
    return (2021 - dob)
df['driver_current_age']=df['driver_age_raw'].apply(currentAge)
print(df['driver_current_age'].head())

df['driver_age_qcut_bins']=pd.qcut(df["driver_age"],q=5)
print(df['driver_age_qcut_bins'].value_counts())

df['driver_age_qcut_bins']=pd.cut(df["driver_age"],bins=3,labels=["1-21","22-60","61-100"])
print(df['driver_age_qcut_bins'].value_counts())

comb_df.to_csv("output.csv",index=False)



