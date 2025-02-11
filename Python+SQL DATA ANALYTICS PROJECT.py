#!/usr/bin/env python
# coding: utf-8

# In[45]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[46]:


df = pd.read_csv("C://Users//home//Downloads//archive (3)//orders.csv")
df.head()


# In[47]:


df.shape


# In[48]:


df.describe()


# In[ ]:


#checking the unique values in shipmode column and replacing null with none


# In[49]:


df['Ship Mode'].unique()


# In[30]:


#Handling null values


# In[50]:


df = pd.read_csv("C://Users//home//Downloads//archive (3)//orders.csv", na_values=['Not Available','unknown'])


# In[51]:


df['Ship Mode'].unique()


# In[ ]:


#rename the column names


# In[52]:


df.columns=df.columns.str.lower()


# In[53]:


df.columns=df.columns.str.replace(' ','_')


# In[54]:


df.head()


# In[55]:


df['discount']=df['list_price']*df['discount_percent']*.01
df['sale_price']=df['list_price']-df['discount']
df['profit']=df['sale_price']-df['cost_price']


# In[56]:


df.head()


# In[57]:


df.drop(['cost_price','list_price','discount_percent'],axis=1,inplace = True)


# In[58]:


df.isnull().any()


# In[59]:


df.info()


# In[60]:


df['order_date']=pd.to_datetime(df['order_date'],format ="%Y-%m-%d")


# In[61]:


df.info()


# In[62]:


df.head()


# In[ ]:


#Load the data into sql server


# In[63]:


import sqlalchemy as sal
engine = sal.create_engine('mssql://DESKTOP-4QG8FDD\MSSQLSERVER_1/LEARN?driver=ODBC+DRIVER+17+FOR+SQL+SERVER')
conn=engine.connect()


# In[65]:


df.to_sql('df_orders',con=conn,index = False,if_exists ='append')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




