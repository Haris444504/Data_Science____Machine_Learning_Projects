import numpy as np 
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler , MinMaxScaler


data_set = pd.read_csv(r"[Enter your path].csv")
print(data_set.describe())
print(data_set.isnull().sum())
# salary cleaning
data_set["monthly_salary"] = pd.to_numeric(data_set["monthly_salary"], errors='coerce')
data_set["monthly_salary"] = data_set["monthly_salary"].fillna(data_set["monthly_salary"].mean())

# AGE FIX (this is what was breaking)
data_set["age"] = pd.to_numeric(data_set["age"], errors='coerce')
data_set["age"] = data_set["age"].fillna(data_set["age"].mean())

# performance rating fix
data_set["performance_rating"] = pd.to_numeric(data_set["performance_rating"], errors='coerce')
data_set["performance_rating"] = data_set["performance_rating"].fillna(data_set["performance_rating"].mean())

# department (categorical)
data_set["department"] = data_set["department"].fillna("Unknown")
data_set["full_name"] = data_set["full_name"].fillna("Unknown")
print(data_set)

print(data_set.isnull().sum())

# cleaning and preprocessing 

data_cleaned = data_set.copy()
data_cleaned.drop_duplicates(inplace=True)
le = LabelEncoder()
data_cleaned["age"] = le.fit_transform(data_cleaned["age"])
data_cleaned["monthly_salary"] = le.fit_transform(data_cleaned["monthly_salary"])
data_cleaned["performance_rating"] = le.fit_transform(data_cleaned["performance_rating"])
data_cleaned["department"] = le.fit_transform(data_cleaned["department"])
data_cleaned["email_address"] = le.fit_transform(data_cleaned["email_address"])
data_cleaned["full_name"] = le.fit_transform(data_cleaned["full_name"])
data_cleaned["hire_date"] = le.fit_transform(data_cleaned["hire_date"])
data_cleaned["office_location"] = le.fit_transform(data_cleaned["office_location"])
# data_cleaned["department"] = pd.get_dummies(data_cleaned["department"])
# data_cleaned["email_address"] = pd.get_dummies(data_cleaned["email_address"])
# data_cleaned["full_name"] = pd.get_dummies(data_cleaned["full_name"])
print(data_cleaned)

scaler = MinMaxScaler()
data_cleaned[["age" , "monthly_salary" , "performance_rating" , "email_address", "full_name", "hire_date", "office_location"]] = scaler.fit_transform(
    data_cleaned[["age" , "monthly_salary" , "performance_rating" , "email_address", "full_name", "hire_date", "office_location"]])

print(data_cleaned)
