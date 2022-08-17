#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[4]:


data = pd.read_excel(r'C:\Users\Azeez Sharieff\Documents\data files for practice\Book1.xlsx')
data


# In[5]:


data2 = pd.read_csv(r'C:\Users\Azeez Sharieff\Documents\data files for practice\Book1.csv')
data2


# In[18]:


data3 = pd.read_csv(r'C:\Users\Azeez Sharieff\Documents\data files for practice\data3.tsv')
data3


# In[19]:


import os


# In[20]:


os.getcwd()


# In[26]:


data4 = pd.read_csv("student.tsv")
data4


# In[27]:


data5 = pd.read_excel("Book1.xlsx")
data5


# In[ ]:




