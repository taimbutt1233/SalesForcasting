#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


# In[6]:


data=pd.read_csv('export.csv')


# In[7]:


data.head(5)


# In[8]:


data.columns


# In[10]:


X = data.drop(columns=['Item_Outlet_Sales'], axis=1)
y = data['Item_Outlet_Sales']


# In[19]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10,shuffle=False)


# In[20]:


model = LinearRegression()

model.fit(X_train, y_train)
print(
    model.score(X_train, y_train),
    model.score(X_test, y_test)
)


# In[28]:


data['prediction']= model.predict(X)


# In[30]:


data[['prediction','Item_Outlet_Sales']]


# In[21]:


model_ = DecisionTreeClassifier()


# In[22]:


model_.fit(X_train,y_train)


# In[24]:


import pickle


# In[31]:


pickle.dump(model, open('model.pkl','wb'))


# In[ ]:




