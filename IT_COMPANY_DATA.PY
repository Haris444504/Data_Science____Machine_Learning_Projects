import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import random 

path  = pd.read_csv(r"C:\Users\Haris_hp\Downloads\IT_Company_Workers_Corrupted.csv")
data = pd.DataFrame(path)

print(data.describe())

print(data.head(10))

marks =  (data["Experience_Years"].between(0,1)) | (data["Performance_Score"].between(0,1.0)) | (data["Projects"].between(0,1)) 
fill_Salary = data["Salary"].isna() & marks
data.loc[fill_Salary,"Salary"] = np.random.uniform(40005,60733,size= fill_Salary.sum())
    
imarks =  (data["Experience_Years"].between(1.5,5)) | (data["Performance_Score"].between(1.1,1.97)) | (data["Projects"].between(2,4)) 
fill_Salary = data["Salary"].isna() & marks
data.loc[fill_Salary,"Salary"] = np.random.uniform(60734,80733,size= fill_Salary.sum())
    
marks =   (data["Experience_Years"].between(6,10)) | (data["Performance_Score"].between(1.98,2.98)) | (data["Projects"].between(5,7)) 
fill_Salary = data["Salary"].isna() & marks
data.loc[fill_Salary,"Salary"] = np.random.uniform(80734,123814,size= fill_Salary.sum())
    

marks =   (data["Experience_Years"].between(11,15)) | (data["Performance_Score"].between(2.99,4.03)) | (data["Projects"].between(8,11)) 
fill_Salary = data["Salary"].isna() & marks
data.loc[fill_Salary,"Salary"] = np.random.uniform(123815,164709,size= fill_Salary.sum())

marks =   (data["Experience_Years"].between(16,19)) | (data["Performance_Score"].between(4.04,5.0)) | (data["Projects"].between(12,14)) 
fill_Salary = data["Salary"].isna() & marks
data.loc[fill_Salary,"Salary"] = np.random.uniform(164710,210000,size= fill_Salary.sum())


print("------------------------------------Performnace here---------------------------------------")
marks =  (data["Experience_Years"].between(0,1)) | (data["Salary"].between(40005,60733)) | (data["Projects"].between(0,1)) 
fill_PS = data["Performance_Score"].isna() & marks
data.loc[fill_PS,"Performance_Score"] = np.random.uniform(0,1.0,size= fill_PS.sum())

marks =  (data["Experience_Years"].between(2,5)) | (data["Salary"].between(60734,80733)) | (data["Projects"].between(2,4)) 
fill_PS = data["Performance_Score"].isna() & marks
data.loc[fill_PS,"Salary"] = np.random.uniform(1.1,1.97,size= fill_PS.sum())

marks =  (data["Experience_Years"].between(6,10)) | (data["Salary"].between(80734,123814)) | (data["Projects"].between(5,7)) 
fill_PS = data["Performance_Score"].isna() & marks
data.loc[fill_PS,"Performance_Score"] = np.random.uniform(1.98,2.98,size= fill_PS.sum())

marks =  (data["Experience_Years"].between(11,15)) | (data["Salary"].between(123815,164709)) | (data["Projects"].between(8,11)) 
fill_PS = data["Performance_Score"].isna() & marks
data.loc[fill_PS,"Performance_Score"] = np.random.uniform(2.99,4.03,size= fill_PS.sum())

marks =  (data["Experience_Years"].between(16,19)) | (data["Salary"].between(164710,210000)) | (data["Projects"].between(12,14)) 
fill_PS = data["Performance_Score"].isna() & marks
data.loc[fill_PS,"Performance_Score"] = np.random.uniform(4.04,5.0,size= fill_PS.sum())


#print("------------------------------------Experience here---------------------------------------")

marks =  (data["Performance_Score"].between(0,1.0)) | (data["Salary"].between(40005,60733)) | (data["Projects"].between(0,1)) 
fill_EY = data["Experience_Years"].isna() & marks
data.loc[fill_EY,"Experience_Years"] = 0

marks =  (data["Performance_Score"].between(1.1,1.98)) | (data["Salary"].between(60734,80733)) | (data["Projects"].between(2,4)) 
fill_EY = data["Experience_Years"].isna() & marks
data.loc[fill_EY,"Experience_Years"] = np.random.uniform(1,5,size= fill_EY.sum())

marks =  (data["Performance_Score"].between(0,1.0)) | (data["Salary"].between(80734,123814)) | (data["Projects"].between(5,7)) 
fill_EY = data["Experience_Years"].isna() & marks
data.loc[fill_EY,"Experience_Years"] = np.random.uniform(6,10,size= fill_EY.sum())

marks =  (data["Performance_Score"].between(0,1.0)) | (data["Salary"].between(123815,164709)) | (data["Projects"].between(8,11)) 
fill_EY = data["Experience_Years"].isna() & marks
data.loc[fill_EY,"Experience_Years"] = np.random.uniform(11,15,size= fill_EY.sum())

marks =  (data["Performance_Score"].between(0,1.0)) | (data["Salary"].between(164710,210000)) | (data["Projects"].between(12,14)) 
fill_EY = data["Experience_Years"].isna() & marks
data.loc[fill_EY,"Experience_Years"] = np.random.uniform(16,19,size= fill_EY.sum())


# print("------------------------------------Projects here---------------------------------------")

marks =  (data["Performance_Score"].between(0,1.0)) | (data["Salary"].between(40005,60733)) | (data["Experience_Years"].between(0,1)) 
fill_P = data["Projects"].isna() & marks
data.loc[fill_P,"Projects"] = np.random.uniform(0,1,size= fill_P.sum())

marks =  (data["Performance_Score"].between(1.1,1.98)) | (data["Salary"].between(60734,80733)) | (data["Experience_Years"].between(2,5)) 
fill_P = data["Projects"].isna() & marks
data.loc[fill_P,"Projects"] = np.random.uniform(2,4,size= fill_P.sum())

marks =  (data["Performance_Score"].between(0,1.0)) | (data["Salary"].between(80734,123814)) | (data["Experience_Years"].between(6,10)) 
fill_P = data["Projects"].isna() & marks
data.loc[fill_P,"Projects"] = np.random.uniform(5,7,size= fill_P.sum())

marks =  (data["Performance_Score"].between(0,1.0)) | (data["Salary"].between(123815,164709)) | (data["Experience_Years"].between(11,15)) 
fill_P = data["Projects"].isna() & marks
data.loc[fill_P,"Projects"] = np.random.uniform(8,11,size= fill_P.sum())


marks =  (data["Performance_Score"].between(0,1.0)) | (data["Salary"].between(164710,210000)) | (data["Experience_Years"].between(16,19)) 
fill_P = data["Projects"].isna() & marks
data.loc[fill_P,"Projects"] = np.random.uniform(12,14,size= fill_P.sum())


data = data.replace([np.inf,-np.inf],np.nan) 
# print(data.head(10))

condition = [
    (data["Experience_Years"].between(0,4) & data["Performance_Score"].between(0,2)),
    (data["Experience_Years"].between(5,10) & data["Performance_Score"].between(3,3.9)),
    (data["Experience_Years"].between(11,19) & data["Performance_Score"].between(4,5)),
]

choice = ["Low Rank" , "Average Rank" , "High Rank"]

data["Rank"] = np.select(condition,choice,default="Average Rank")

print(data.head(10))

top_ranked = data.nlargest(5,"Experience_Years")
top_Salary = data.nlargest(5,"Salary")
top_Performance = data.nlargest(5,"Performance_Score")
top_Project = data.nlargest(5,"Projects")

print("Top Rank : \n",top_ranked)
print("Top Salary : \n",top_Salary)
print("Top Performance Score : \n",top_Performance)
print("Top Project Number : \n",top_Project)


# plt.plot(data["Experience_Years"],data["Projects"])
# plt.xlabel("--------Experience Years---------")
# plt.ylabel("--------Projects---------")
# plt.title("Data of IT Company")
# fig = plt.figure()
# axis1 = fig.add_axes([0.1,0.1,0.8,0.8])
# axis1.plot(data["Performance_Score"],data["Projects"])
# axis2 = fig.add_axes([0.2,0.2,0.7,0.7])
# axis2.plot(data["Performance_Score"],data["Projects"])
# sns.pairplot(data,hue="Age")
sns.displot(data['Salary'],kde=True,color="blue",bins=100)
sns.jointplot(x=data["Salary"],y=data['Experience_Years'],data=data,kind='reg')
plt.show()
data.to_excel(r"C:\Users\Haris_hp\Documents\IT_COMPANY_DATA.xlsx",index=False)