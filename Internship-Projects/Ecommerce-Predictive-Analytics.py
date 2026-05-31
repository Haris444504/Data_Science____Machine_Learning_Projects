import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
try:
    import sheryanalysis as sh
except ModuleNotFoundError:
    sh = None
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
data = pd.read_excel(r"C:\Users\Haris_hp\Downloads\Dataset for Data Analytics.xlsx")
# Display the first few rows of the dataset
# print(data.head())

# print(data.describe())
# print(data.shape)
# print(data.columns)
# Check for missing values
# print(data.isnull().sum())
# print(data['CouponCode'])

if sh is not None:
    print(sh.analyze(data))
else:
    print("Optional module 'sheryanalysis' not installed; skipping optional analysis.")

data["CouponCode"] = data["CouponCode"].fillna("No Coupon")

# Remove duplicates
data.drop_duplicates(inplace=True)
data.drop("Date", axis=1, inplace=True)

# Correlation analysis
numeric_data = data.select_dtypes(include=[np.number])
correlation_matrix = numeric_data.corr()
plt.figure(figsize=(10, 8))
# sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
# plt.title("correclation matrix")
# plt.show()

# 🧱 Columns: ['OrderID', 'Date', 'CustomerID', 'Product', 'Quantity',
# 'UnitPrice', 'ShippingAddress', 'PaymentMethod', 'OrderStatus', 'TrackingNumber',
# 'ItemsInCart', 'CouponCode', 'ReferralSource', 'TotalPrice']

# 🧼 Columns with nulls: ['CouponCode']

# 🔠 Categorical Columns: ['Product', 'Quantity', 'PaymentMethod', 
# 'OrderStatus', 'ItemsInCart', 'CouponCode', 'ReferralSource']

# 🔢 Numerical Columns: ['UnitPrice', 'TotalPrice']


categorical_columns = [
    "Product",
    "Quantity",
    "PaymentMethod",
    "OrderStatus",
    "ItemsInCart",
    "CouponCode",
    "ReferralSource",
]
# for col in categorical_columns:
#     plt.figure(figsize=(10, 5))
#     sns.boxplot(x=col, y="TotalPrice", data=data)
#     plt.title(f"Box Plot of {col}")
#     plt.xticks(rotation=45)
#     plt.show()

# numerical_columns = ["UnitPrice", "TotalPrice"]
# for col in numerical_columns:
#     plt.figure(figsize=(10, 5))
#     sns.scatterplot(data=data, x=col, y="TotalPrice")
#     plt.title(f"Scatter Plot of {col} vs TotalPrice")
#     plt.show()

# one-hot encoding
data = pd.get_dummies(
    data,
    columns=["Product", "PaymentMethod", "OrderStatus", "CouponCode", "ReferralSource"],
    drop_first=True,
    dtype=int, 
)

# --- FIXING DATA LEAKAGE & UNWANTED COLUMNS ---
# TotalPrice is the target. 
# OrderID, CustomerID, TrackingNumber, and ShippingAddress are unique identifiers (useless for ML).
# UnitPrice and Quantity must be dropped because they directly calculate TotalPrice.
columns_to_drop = [
    "TotalPrice", 
    "OrderID", 
    "CustomerID", 
    "TrackingNumber", 
    "ShippingAddress", 
    "UnitPrice", 
    "Quantity"
]

columns_to_drop = ["TotalPrice", "OrderID", "CustomerID", "ShippingAddress", "TrackingNumber"]
columns_to_drop = [col for col in columns_to_drop if col in data.columns]

X = data.drop(columns_to_drop, axis=1)
y = data["TotalPrice"]
#  modeling
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"R-squared Score: {r2}")

