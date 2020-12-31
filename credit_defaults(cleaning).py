#!/usr/bin/env python
# coding: utf-8

# # Credit Card Defaults

# In[2]:


import pandas as pd


# In[3]:


df = pd.read_excel("default_of_credit_card_clients__courseware_version_1_21_19.xls")


# In[4]:


df.shape


# In[5]:


df.info()


# In[6]:


df.columns


# In[7]:


df.head()


# In[8]:


df["ID"].nunique()


# In[9]:


id_counts = df["ID"].value_counts()


# In[10]:


id_counts.head()


# In[11]:


id_counts.value_counts()


# In[12]:


import numpy as np


# In[13]:


np.random.seed(seed=24)


# In[14]:


random_int = np.random.randint(low=1,high=5,size=100)


# In[15]:


random_int[:10]


# In[16]:


is_equal_to_3 = random_int==3


# In[17]:


random_int[:10]


# In[18]:


is_equal_to_3[:10]


# In[19]:


sum(is_equal_to_3)


# In[20]:


mask = id_counts == 2


# In[21]:


mask[0:]


# In[22]:


repeated_ids = id_counts.index[mask]


# In[23]:


repeated_ids = list(repeated_ids)


# In[24]:


len(repeated_ids)


# In[25]:


repeated_ids[0:]


# In[26]:


df.loc[df["ID"].isin(repeated_ids[0:]),:].head(313)


# In[27]:


df_zero_matrix = df ==0


# In[28]:


zero_mask = df_zero_matrix.iloc[:,1:].all(axis=1)


# In[29]:


sum(zero_mask)


# In[30]:


clean1 = df.loc[~zero_mask,:].copy()


# In[31]:


clean1.shape


# In[32]:


clean1["ID"].nunique()


# In[33]:


clean1.info()


# In[35]:


clean1["PAY_1"].head(10)


# In[36]:


clean1["PAY_1"].value_counts()


# In[37]:


valid_clean1=clean1["PAY_1"]!="Not available"
valid_clean1[0:]


# In[38]:


sum(valid_clean1)


# In[40]:


clean2=clean1.loc[valid_clean1,:].copy()
clean2.shape


# In[42]:


clean2["PAY_1"]=clean2["PAY_1"].astype("int64")


# In[43]:


clean2[["PAY_1","PAY_2"]].info()


# In[45]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 400


# In[46]:


clean2[["LIMIT_BAL","AGE"]].hist()


# In[47]:


clean2[["LIMIT_BAL","AGE"]].describe()


# In[48]:


clean2["EDUCATION"].value_counts()


# In[49]:


clean2["EDUCATION"].replace(to_replace=[0,5,6],value=4,inplace=True)
clean2["EDUCATION"].value_counts()


# In[50]:


clean2["MARRIAGE"].value_counts()


# In[53]:


clean2["MARRIAGE"].replace(to_replace=0,value=3,inplace=True)
clean2["MARRIAGE"].value_counts()


# In[55]:


clean2.groupby('EDUCATION').agg({'default payment next month':'mean'}).plot.bar(legend=False)
plt.ylabel('Default rate')
plt.xlabel('Education level: ordinal encoding')


# In[56]:


clean2["EDUCATION_CATEGORY"]="none"


# In[58]:


clean2[["EDUCATION", "EDUCATION_CATEGORY"]].head(15)


# In[61]:


edu_mapping = {1:"graduate school", 2:"university", 3:"high school", 4:"others"}


# In[63]:


clean2['EDUCATION_CATEGORY']=clean2['EDUCATION'].map(edu_mapping)
clean2[['EDUCATION', 'EDUCATION_CATEGORY']].head(15)


# In[65]:


ohe_frame = pd.get_dummies(clean2["EDUCATION_CATEGORY"])
ohe_frame.head(15)


# In[66]:


ohe_frame2 = pd.concat([clean2,ohe_frame], axis=1)
ohe_frame2[["EDUCATION_CATEGORY", "graduate school", "high school", "university", "others"]].head(15)


# In[68]:


ohe_frame2.to_csv('cleandata_ver1.csv')


# In[ ]:




