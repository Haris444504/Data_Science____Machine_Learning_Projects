# 📊 Data Analytics & Machine Learning Projects

> A collection of end-to-end data analysis and machine learning projects built with Python — covering healthcare, e-commerce, automotive, and insurance domains.

---

## 🗂️ Table of Contents

- [Project 1 — E-commerce Data Analysis](#-project-1--e-commerce-data-analysis)
- [Project 2 — Patient Data Analysis](#-project-2--patient-data-analysis)
- [Project 3 — Heart Disease Prediction](#-project-3--heart-disease-prediction)
- [Project 4 — Car Price Prediction](#-project-4--car-price-prediction)
- [Project 5 — Insurance Charges Prediction](#-project-5--insurance-charges-prediction)
- [How to Run](#️-how-to-run)
- [Folder Structure](#-folder-structure)
- [Skills Demonstrated](#-skills-demonstrated)
- [Author](#-author)

---

## 📦 Project 1 — E-commerce Data Analysis
**File:** `Ecommerce_data_by_google.py`

Analyzes a large e-commerce dataset to extract actionable business intelligence around sales, customers, and logistics.

**Business Insights:**
- Total revenue and Average Order Value (AOV)
- Most popular product categories
- Top revenue-generating cities
- Age group and payment method trends
- Delivery performance — on-time vs. late

**Key Steps:**
- Removed duplicates and handled missing values
- Engineered `Total_Spend` feature
- Extracted `Year`, `Month`, `Day` from order dates

**Visualizations:**

| Chart | Purpose |
|-------|---------|
| 📊 Bar Chart | Sales per Product Category |
| 🥧 Pie Chart | Payment Method Distribution |
| 📈 Histogram | Age Distribution & Monthly Trends |
| 🔥 Heatmap | Correlation — Age, Quantity, Spend |
| 📦 Boxplot | Spending Distribution by Gender |

**Libraries:** `pandas` `numpy` `matplotlib` `seaborn` `scipy`

---

## 🏥 Project 2 — Patient Data Analysis
**File:** `Patient_data.py`

Healthcare analytics pipeline to understand patient visit trends, consultation revenue, and doctor performance.

**Business Insights:**
- Total consultation revenue
- Most visited department
- Most common patient age group
- Top performing doctor by patient count
- No-show (missed appointment) percentage

**Key Steps:**
- Converted appointment dates to datetime format
- Removed duplicate patient records
- Added time-based columns: `Year`, `Month`, `Day`

**Visualizations:**

| Chart | Purpose |
|-------|---------|
| 📊 Bar Chart | Patients per Department |
| 🥧 Pie Chart | Payment Method Distribution |
| 🔥 Heatmap | Correlation — Age, Fees, Visits |
| 📦 Boxplot | Fee Distribution by Department |

**Libraries:** `pandas` `numpy` `matplotlib` `seaborn` `scipy`

---

## ❤️ Project 3 — Heart Disease Prediction
**File:** `Heart_Disease_Prediction.py`

End-to-end supervised ML pipeline to classify whether a patient has heart disease based on clinical features.

**ML Pipeline:**

```
Raw Data → EDA → Visualization → Encoding → Scaling → Model Training → Evaluation
```

**Steps Covered:**
- **EDA** — Feature distributions, class balance, outlier detection
- **Visualization** — Correlation heatmap, feature distributions by target class
- **Encoding** — Label Encoding / One-Hot Encoding for categorical features
- **Scaling** — StandardScaler / MinMaxScaler for numerical features
- **Supervised Learning** — Logistic Regression, Decision Tree, Random Forest, SVM
- **Evaluation** — Accuracy, Precision, Recall, F1-Score, Confusion Matrix, ROC-AUC

**Libraries:** `pandas` `numpy` `matplotlib` `seaborn` `scikit-learn`

---

## 🚗 Project 4 — Car Price Prediction
**File:** `Car_Price_Prediction.py`

Regression-based machine learning pipeline to predict the selling price of used cars based on features like brand, year, mileage, and fuel type.

**ML Pipeline:**

```
Raw Data → EDA → Visualization → Encoding → Scaling → Model Training → Evaluation
```

**Steps Covered:**
- **EDA** — Price distribution, feature relationships, outlier analysis
- **Visualization** — Price trends by brand, year, and fuel type
- **Encoding** — Handling categorical features (fuel type, transmission, seller type)
- **Scaling** — Normalizing numerical features
- **Supervised Learning** — Linear Regression, Random Forest Regressor, Gradient Boosting
- **Evaluation** — MAE, MSE, RMSE, R² Score

**Libraries:** `pandas` `numpy` `matplotlib` `seaborn` `scikit-learn`

---

## 🏦 Project 5 — Insurance Charges Prediction
**File:** `Insurance_Charges_Prediction.py`

Regression pipeline to predict medical insurance charges based on demographic and lifestyle features such as age, BMI, smoking status, and region.

**ML Pipeline:**

```
Raw Data → EDA → Visualization → Encoding → Scaling → Model Training → Evaluation
```

**Steps Covered:**
- **EDA** — Charge distribution, skewness analysis, feature correlations
- **Visualization** — Impact of smoking, BMI, and age on insurance charges
- **Encoding** — Encoding region, sex, and smoker status
- **Scaling** — Feature normalization for regression models
- **Supervised Learning** — Linear Regression, Ridge, Lasso, Random Forest Regressor
- **Evaluation** — MAE, MSE, RMSE, R² Score

**Libraries:** `pandas` `numpy` `matplotlib` `seaborn` `scikit-learn`

---

## ⚙️ How to Run

**Step 1 — Install all dependencies:**
```bash
pip install pandas numpy matplotlib seaborn scipy scikit-learn
```

**Step 2 — Run any project script:**
```bash
python Ecommerce_data_by_google.py
python Patient_data.py
python Heart_Disease_Prediction.py
python Car_Price_Prediction.py
python Insurance_Charges_Prediction.py
```

---

## 🧩 Folder Structure

```
📁 Data-Analytics-ML-Projects/
│
├── Ecommerce_data_by_google.py
├── Patient_data.py
├── Heart_Disease_Prediction.py
├── Car_Price_Prediction.py
├── Insurance_Charges_Prediction.py
│
├── README.md
│
└── datasets/
    ├── ecommerce_dataset.csv
    ├── healthcare_dataset.csv
    ├── heart_disease_dataset.csv
    ├── car_price_dataset.csv
    └── insurance_dataset.csv
```

---

## 📊 Skills Demonstrated

| Area | Topics |
|------|--------|
| **Data Wrangling** | Cleaning, deduplication, missing value handling, feature engineering |
| **EDA** | Statistical summaries, distribution analysis, outlier detection |
| **Visualization** | Bar, pie, histogram, heatmap, boxplot, ROC curves |
| **Preprocessing** | Label encoding, one-hot encoding, StandardScaler, MinMaxScaler |
| **Machine Learning** | Classification, Regression, Ensemble methods |
| **Model Evaluation** | Accuracy, F1, ROC-AUC, MAE, RMSE, R² Score |
| **Business Insights** | Revenue analysis, customer segmentation, risk prediction |

---

## 👨‍💻 Author

**Haris Saddique**  
Data Analytics | Machine Learning Enthusiast

[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?logo=github)](https://github.com/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://linkedin.com/)
