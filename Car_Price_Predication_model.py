import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data = pd.read_csv(r"C:\Users\Haris_hp\Downloads\ford.csv")
print(data.head())

print(data.describe())

print(data.shape)

print(data.info())

print(data.isnull().sum())

#visualization
sns.histplot(data['price'] , bins = 50 , kde = True)

data.corr(numeric_only = True)
sns.heatmap(data.corr(numeric_only = True) , annot = True)

sns.boxplot(x = 'year' , y = 'price' , data = data)
plt.xticks(rotation = 90)

sns.scatterplot(data = data , x = 'mileage' , y = 'price')

sns.boxplot(x = 'engineSize' , y = 'price' , data = data) 

sns.boxplot(data = data , x = 'transmission' ,y = 'price' )

sns.boxplot(data = data  , x = 'fuelType' , y = 'price') 

sns.boxplot(x = 'model' , y = 'price' , data = data)
plt.xticks(rotation = 90)

sns.boxplot(data = data , x = 'tax' , y = 'price')
plt.xticks(rotation = 90)

sns.histplot(data = data , x = 'mpg' , y = 'price')
plt.xticks(rotation = 90)

x = data.drop(columns = ['price'] , axis = 1)
y = data['price']

# One-hot encoding for categorical variables
x_one_encoded = pd.get_dummies(x, columns=['model', 'transmission', 'fuelType'], drop_first=True)

print(x_one_encoded)
print(data.columns)

x_one_encoded = x_one_encoded.astype(int)
print(x_one_encoded)

#Data analysis
x = data.drop(columns=['price'], axis=1)


columns = ['model', 'transmission', 'fuelType']
for col in columns:
    x[col] = x[col].astype(str).str.strip()

xlabel = x.copy()
label_encoders = {}

for col in columns:
    le = LabelEncoder()
    xlabel[col] = le.fit_transform(xlabel[col])
    label_encoders[col] = le

print("Unique models encoded:", xlabel['model'].unique())
xlabel.head()

print(xlabel)

print(xlabel['model'].value_counts())

# scaling

numerical_columns = ['year' , 'mileage' , 'engineSize' , 'tax' , 'mpg']
scaler = StandardScaler()

xlabel[numerical_columns] = scaler.fit_transform(xlabel[numerical_columns])

print(xlabel)

columns_to_scale = ['year', 'model', 'transmission', 'mileage', 'fuelType', 'tax', 'mpg', 'engineSize']
xlabel[columns_to_scale] = scaler.fit_transform(xlabel[columns_to_scale])

x_test , x_train , y_test , y_train = train_test_split(x_one_encoded , y , test_size = 0.2 , random_state = 42)

# Train the model
model = LinearRegression()
model.fit(x_train , y_train)
y_pred = model.predict(x_test)

print(y_pred)

print(y_test)

r2 = r2_score(y_test , y_pred)
print("R-squared:", r2)

n = x_test.shape[0]
p = x_test.shape[1]
adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
print("Adjusted R-squared:", adj_r2)

x_test , x_train , y_test , y_train = train_test_split(xlabel , y , test_size = 0.2 , random_state = 42)

model = LinearRegression()
model.fit(x_train , y_train)
y_pred = model.predict(x_test)

print(y_pred)

print(y_test)

r2 = r2_score(y_test , y_pred)
print("R-squared:", r2)

n = x_test.shape[0]
p = x_test.shape[1]
adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
print("Adjusted R-squared:", adj_r2)