# 📊 Bank Customer Churn Analysis

A Data Analytics project focused on analyzing customer churn in the banking sector using Python. The project applies Exploratory Data Analysis (EDA) techniques to identify customer characteristics and behavioral patterns associated with churn, helping businesses improve customer retention strategies.

---

## 📌 Project Objective

The objective of this project is to analyze bank customer data and identify the key factors influencing customer churn. Through data cleaning, visualization, and statistical analysis, the project provides actionable insights into customer behavior and attrition trends.

---

## 📁 Dataset Information

**Dataset:** Bank_Churn.csv

The dataset contains customer demographic, financial, and account-related information.

### Features

* CustomerId
* Surname
* CreditScore
* Geography
* Gender
* Age
* Tenure
* Balance
* NumOfProducts
* HasCrCard
* IsActiveMember
* EstimatedSalary
* Exited (Target Variable)

**Target Variable:**

* Exited = 1 → Customer Churned
* Exited = 0 → Customer Retained

---

## 🛠 Tools & Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

---

## 🔍 Project Workflow

### 1. Data Loading & Understanding

* Imported dataset using Pandas
* Reviewed dataset structure and dimensions
* Examined data types and summary statistics

### 2. Data Cleaning

* Removed unnecessary columns:

  * CustomerId
  * Surname
* Checked for missing values
* Prepared dataset for analysis

### 3. Exploratory Data Analysis (EDA)

#### Customer Churn Overview

* Overall churn distribution
* Churn rate calculation

#### Demographic Analysis

* Churn by Gender
* Churn by Geography
* Churn by Age Groups

#### Customer Behavior Analysis

* Active Member vs Churn
* Number of Products vs Churn

#### Financial Analysis

* Credit Score vs Churn
* Balance vs Churn
* Estimated Salary vs Churn

### 4. Correlation Analysis

* Generated correlation heatmap
* Examined relationships between numerical variables and churn

---

## 📈 Visualizations Included

* Customer Churn Distribution
* Churn Rate by Geography
* Churn Rate by Age Group
* Gender vs Churn
* Products vs Churn
* Active Member vs Churn
* Credit Score Analysis
* Balance Analysis
* Correlation Heatmap

---

## 🎯 Key Insights

* Customers aged 41 years and above showed higher churn tendencies.
* Customer churn varied significantly across different geographic regions.
* Inactive customers were more likely to leave the bank.
* Customers with specific product ownership patterns showed increased churn risk.
* Account balance demonstrated a stronger relationship with churn than salary.
* Credit score showed only a moderate impact on customer attrition.

---

## ✅ Business Impact

The analysis helps identify high-risk customer segments and supports data-driven customer retention strategies. These insights can help banks:

* Improve customer engagement
* Reduce churn rates
* Develop targeted retention campaigns
* Enhance customer lifetime value

---

## 📂 Project Structure

Bank-Customer-Churn-Analysis/

├── Bank_Churn.csv

├── customer_churn_analysis.py

├── README.md

└── Visualizations/

---

## 🚀 Future Enhancements

* Build machine learning models for churn prediction
* Implement customer segmentation techniques
* Develop an interactive Power BI dashboard
* Perform advanced statistical analysis

---

## 👩‍💻 Author

**Rutuja Kundangar**

Data Analyst | Business Analyst

Skills: SQL, Power BI, Excel, Python, Tableau

LinkedIn: [www.linkedin.com/in/rutujavk08](http://www.linkedin.com/in/rutujavk08)

GitHub: [github.com/RutujaK08]

---

## 📄 License

This project is intended for educational and portfolio purposes.
