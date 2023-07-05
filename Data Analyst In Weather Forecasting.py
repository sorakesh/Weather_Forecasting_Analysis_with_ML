#!/usr/bin/env python
# coding: utf-8

# In[96]:


import pandas as pd
import numpy as np


# In[97]:


df=pd.read_csv("Weather_Data.csv")


# In[98]:


df.head()


# In[99]:


df.shape


# In[100]:


df.index


# In[101]:


df.dtypes


# In[102]:


df['Weather'].unique()


# In[103]:


df.nunique()


# In[104]:


df['Weather'].value_counts()


# In[105]:


df.info()


# In[106]:


##Find out all the Null Values in the data.
df.isnull().sum()


# In[107]:


##  Find all the unique 'Wind Speed' values in the data.
df['Wind Speed_km/h'].unique()


# In[108]:


## Find the number of times when the 'Weather is exactly Clear'.

df.groupby('Weather').get_group('Clear')


# In[109]:


##Find the number of times when the 'Wind Speed was exactly 4 km/h'.

df[df['Wind S
      peed_km/h'] ==4]


# In[110]:


## Rename the column name 'Weather' of the dataframe to 'Weather Condition'.
df.rename(columns= {'Weather': 'Weather Condution'} , inplace =True)
df


# In[111]:


## What is the mean 'Visibility' ?
df['Visibility_km'].mean()


# In[112]:


##What is the Standard Deviation of 'Pressure'  in this data?

df.Press_kPa.std()


# In[113]:


##Find all instances when 'Snow' was recorded.

df.head(3)


# In[114]:


df[df['Weather Condution']== 'Snow'] 


# In[115]:


## Find all instances when 'Wind Speed is above 24' and 'Visibility is 25'.
df[(df['Wind Speed_km/h'] > 24) & (df['Visibility_km']==25)]


# In[116]:


##//Find all instances when :
#A. 'Weather is Clear' and 'Relative Humidity is greater than 50'
#or
#B. 'Visibility is above 40'//##**
df.head(2)


# In[117]:


df[(df['Weather Condution']== 'Clear') & (df['Rel Hum_%']> 50) | (df['Visibility_km']>40)]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




