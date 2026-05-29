import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset

df = pd.read_csv("Bank_Churn.csv")

print("Dataset Loaded Successfully")
print(df.head())

# Remove unwanted columns

df = df.drop(["CustomerId", "Surname"], axis=1)

# Churn Rate

churn_rate = round(df["Exited"].mean() * 100, 2)

print(f"\nOverall Churn Rate: {churn_rate}%")

# Customer Churn Distribution

plt.figure(figsize=(6,4))
sns.countplot(data=df, x="Exited")
plt.title("Customer Churn Distribution")
plt.show()

# Gender vs Churn

plt.figure(figsize=(6,4))
sns.countplot(data=df, x="Gender", hue="Exited")
plt.title("Gender vs Churn")
plt.show()

# Geography vs Churn

plt.figure(figsize=(6,4))
sns.countplot(data=df, x="Geography", hue="Exited")
plt.title("Geography vs Churn")
plt.show()

# Age Distribution

plt.figure(figsize=(8,5))
sns.histplot(data=df, x="Age", hue="Exited", kde=True)
plt.title("Age Distribution by Churn")
plt.show()

# Balance vs Churn

plt.figure(figsize=(6,4))
sns.boxplot(data=df, x="Exited", y="Balance")
plt.title("Balance vs Churn")
plt.show()

# Active Member Analysis

plt.figure(figsize=(6,4))
sns.countplot(data=df, x="IsActiveMember", hue="Exited")
plt.title("Active Member vs Churn")
plt.show()

# Correlation Heatmap

plt.figure(figsize=(10,6))

corr = df[[
"CreditScore",
"Age",
"Tenure",
"Balance",
"NumOfProducts",
"EstimatedSalary",
"Exited"
]].corr()

sns.heatmap(corr, annot=True, cmap="coolwarm")

plt.title("Correlation Heatmap")
plt.show()

print("\nAnalysis Completed Successfully")
