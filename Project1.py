from statistics import correlation
import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler , minmax_scale
from sklearn.model_selection import train_test_split
from scipy.stats import pearsonr
from scipy.stats import chi2_contingency


data = pd.read_csv(r"C:\Users\Haris_hp\Downloads\insurance.csv")
print(data.head())

# data analysis
print(data.shape)
print(data.head())
print(data.info())
print(data.describe())
print(data.isnull().sum())

print(data.columns)
# for distrubation of numerical columns
numeric_columns = ['age', 'bmi', 'children', 'charges']

# for column in numeric_columns:
#     plt.figure(figsize=(8, 4))
#     sns.histplot(data[column], kde=True,bins = 20)
#     plt.show()

# # for categorical columns we can use countplot
# sns.countplot(x='region', data=data)
# plt.show()
# sns.countplot(x='children', data=data)
# plt.show()
# sns.countplot(x=data['sex'])
# plt.show()
# sns.countplot(x=data['smoker'])
# plt.show()

# for outliers detection we can use boxplot
# for col in numeric_columns:
#     plt.figure(figsize=(6,4))
#     sns.boxplot(x=data[col])
#     plt.show()

# plt.figure(figsize=(10,6))
# # correlation heatmap for numerical columns it is only for numeric values.
# sns.heatmap(data.corr(numeric_only=True) , annot=True , cmap='coolwarm')
# plt.show()

# data clearing and preprocessing

data_cleaned = data.copy()
data_cleaned.drop_duplicates(inplace=True)
print(data_cleaned.shape)
print(data_cleaned.dtypes)
print(data_cleaned.value_counts())

# Save encoders so you can inverse_transform later
le_sex = LabelEncoder()
data_cleaned['sex'] = le_sex.fit_transform(data_cleaned['sex'])

le_smoker = LabelEncoder()
data_cleaned['smoker'] = le_smoker.fit_transform(data_cleaned['smoker'])

# FIX: removed LabelEncoder for region — get_dummies handles it correctly
data_cleaned = pd.get_dummies(data_cleaned, columns=['region'], drop_first=True)
print([c for c in data_cleaned.columns if 'region' in c])
sns.histplot(data['bmi'])
plt.show()
# Feature engineering BEFORE scaling
data_cleaned['bmi_category'] = pd.cut(
    data_cleaned['bmi'],
    bins=[0, 18.5, 24.9, 29.9, 100],
    labels=['Underweight', 'Normal', 'Overweight', 'Obese']
)

data_cleaned = pd.get_dummies(data_cleaned , columns= ['bmi_category'] , drop_first=True)
data_cleaned.astype(int)

# scaling
scaler = StandardScaler()
data_cleaned[numeric_columns] = scaler.fit_transform(data_cleaned[numeric_columns])
print(data_cleaned.head())


# Check what region columns actually exist
region_cols = [c for c in data_cleaned.columns if c.startswith('region_')]
print(region_cols)  # confirm before using

selected_features = [
    'age', 'bmi', 'children', 'sex', 'smoker',
] + region_cols + [
    'bmi_category_Normal', 'bmi_category_Overweight', 'bmi_category_Obese'
]

corr_dict = {
    feature: pearsonr(data_cleaned[feature], data_cleaned['charges'])[0]
    for feature in selected_features
}

correlation_df = pd.DataFrame(
    list(corr_dict.items()),
    columns=['Features', 'Pearson Correlation']
)

correlation_df = correlation_df.sort_values(by='Pearson Correlation', ascending=False)

print(correlation_df)
cat_features = ['sex', 'smoker'] + region_cols + [
    'bmi_category_Normal', 'bmi_category_Overweight', 'bmi_category_Obese'
]

alpha = 0.05  
data_cleaned['charges_bin'] = pd.qcut(data_cleaned['charges'], q=4, labels=False)
chi2_results = {}

for col in cat_features:
    contingency = pd.crosstab(data_cleaned[col], data_cleaned['charges_bin'])
    chi2_stat, p_val, _, _ = chi2_contingency(contingency)

    # FIX: assign the string first, then print it separately
    decision = "Reject NULL (keep Feature)" if p_val < alpha else "Accept NULL (Drop Feature)"
    print(f"{col}: {decision}")

    chi2_results[col] = {
        'chi2_statistics': chi2_stat,
        'p_values': p_val,
        'Decision': decision   # now stores the actual string, not None
    }

# FIX: .T transposes so features are rows, stats are columns
chi2_df = pd.DataFrame(chi2_results).T
chi2_df.index.name = 'Feature'
print(chi2_df)

# FIXED: use dynamic region col instead of hardcoded 'region_2'
print(data_cleaned[['age','sex','bmi','children','smoker','charges', region_cols[0] ,'bmi_category_Obese']])