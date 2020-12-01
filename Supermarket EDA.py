#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import calmap


# In[2]:


df = pd.read_csv(r"C:\Users\User\Downloads\supermarket_sales.csv")


# In[3]:


df.head()


# In[4]:


df.columns


# In[7]:


df.dtypes


# In[6]:


df["Date"] = pd.to_datetime(df["Date"])


# In[8]:


df.set_index("Date", inplace = True)


# In[9]:


df.head()


# In[11]:


df.describe()


# # Univariate Analysis

# In[18]:


sns.distplot(df["Rating"])
plt.axvline(x = np.mean(df["Rating"]), c = "red", ls ="--", label = "mean")
plt.axvline(x = np.percentile(df["Rating"], 25), c = "green", ls ="--", label = "25-75 percentile")
plt.axvline(x = np.percentile(df["Rating"], 75), c = "green", ls ="--")
plt.legend()


# In[21]:


df.hist(figsize=(16,10))


# In[22]:


sns.countplot(df["Branch"])


# # Bivariate Analysis

# In[23]:


sns.scatterplot(df['Rating'], df['gross income'])


# In[24]:


sns.boxplot(x = df["Branch"], y = df["gross income"])


# In[25]:


sns.boxplot(x = df["Gender"], y = df["gross income"])


# In[34]:


fig, ax1 = plt.subplots()
x = df.index
ax1.set_xticklabels(x, rotation=60)
sns.lineplot(x = df.groupby(df.index).mean().index, 
             y = df.groupby(df.index).mean()["gross income"])  


# # Handling Missing Values and Repeated Rows

# In[35]:


df.drop_duplicates(inplace = True)


# In[37]:


df.isna().sum()


# In[43]:


sns.heatmap(df.isnull(), cbar = False)


# In[40]:


df.fillna(df.mean(),inplace = True)


# In[42]:


df.fillna(df.mode().iloc[0], inplace = True)


# In[ ]:





# In[ ]:




