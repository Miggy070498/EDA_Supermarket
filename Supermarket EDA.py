import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import calmap


df = pd.read_csv(r"C:\Users\User\Downloads\supermarket_sales.csv") #imports dataset

# Observation and statistical analysis of dataset
df.head()
df.columns
df.dtypes
df["Date"] = pd.to_datetime(df["Date"]) #Converts string to datetime data type
df.set_index("Date", inplace = True) #Date column becomes index column
df.head()
df.describe()

#Univariate Analysis
sns.distplot(df["Rating"])
plt.axvline(x = np.mean(df["Rating"]), c = "red", ls ="--", label = "mean")
plt.axvline(x = np.percentile(df["Rating"], 25), c = "green", ls ="--", label = "25-75 percentile")
plt.axvline(x = np.percentile(df["Rating"], 75), c = "green", ls ="--")
plt.legend()
df.hist(figsize=(16,10))
sns.countplot(df["Branch"])

# Bivariate Analysis
sns.scatterplot(df['Rating'], df['gross income'])
sns.boxplot(x = df["Branch"], y = df["gross income"])
sns.boxplot(x = df["Gender"], y = df["gross income"])

fig, ax1 = plt.subplots()
x = df.index
ax1.set_xticklabels(x, rotation=60)
sns.lineplot(x = df.groupby(df.index).mean().index, 
             y = df.groupby(df.index).mean()["gross income"])  

# Handling Missing Values and Repeated Rows
df.drop_duplicates(inplace = True)
df.isna().sum()
sns.heatmap(df.isnull(), cbar = False)
df.fillna(df.mean(),inplace = True)
df.fillna(df.mode().iloc[0], inplace = True)
