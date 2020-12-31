#!/usr/bin/env python
# coding: utf-8

# # Credit Defaults(Analysis)

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 400


# In[2]:


df = pd.read_csv('cleandata_ver1.csv')


# In[3]:


pay_status = ['PAY_1','PAY_2','PAY_3','PAY_4','PAY_5','PAY_6']
df[pay_status].describe()


# In[4]:


df[pay_status[0]].value_counts().sort_index()


# In[5]:


df[pay_status[0]].hist()


# In[6]:


pay1_bins = np.array(range(-2,10))-0.5


# In[7]:


pay1_bins


# In[8]:


df[pay_status[0]].hist(bins=pay1_bins)
plt.xlabel("PAY_1")
plt.ylabel("Number of accounts")


# In[9]:


mpl.rcParams['font.size'] = 4
df[pay_status].hist(bins=pay1_bins, layout=(2,3))


# In[10]:


df.loc[df["PAY_2"]==2,["PAY_2","PAY_3"]].head()


# In[11]:


df.describe()


# In[12]:


amount_status = ['PAY_AMT1','PAY_AMT2','PAY_AMT3','PAY_AMT4','PAY_AMT5','PAY_AMT6']
df[amount_status].describe()


# In[13]:


bill_status = ['BILL_AMT1','BILL_AMT2','BILL_AMT3','BILL_AMT4','BILL_AMT5','BILL_AMT6']
df[bill_status].describe()


# In[14]:


df[bill_status].hist(bins=20, layout=(2,3))


# In[15]:


df[amount_status].hist(layout=(2,3), xrot=30)


# In[16]:


zero_amount_mask = df[amount_status]==0
zero_amount_mask.sum()


# In[17]:


df[amount_status][~zero_amount_mask].apply(np.log10).hist(layout=(2,3))


# In[ ]:




