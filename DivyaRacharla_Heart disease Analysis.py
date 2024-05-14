#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().system('pip install matplotlib')
get_ipython().system('pip install seaborn --upgrade')



# In[4]:


data=pd.read_csv('Heart Disease data.csv')


# In[5]:


data.head()


# In[6]:


data.tail()


# In[8]:


data.shape


# In[9]:


data.describe()


# In[11]:


data.isnull().sum()


# In[14]:


data_dup=data.duplicated().any()
print(data_dup)


# In[15]:


data=data.drop_duplicates()


# In[16]:


data.shape


# In[17]:


data.describe()


# In[30]:


plt.figure(figsize=(13,5))
sns.heatmap(data.corr(),annot=True)
plt.show()


# In[35]:


data.columns


# In[41]:


tc=data['target'].value_counts()
tc.name='target'
print(tc)


# In[46]:


unique_targets = data['target'].unique()
print(unique_targets)


# In[49]:


import seaborn as sns
import matplotlib.pyplot as plt

# Assuming 'target' is the column name in your DataFrame
sns.histplot(data['target'])
 
plt.show()


# In[51]:


data['sex'].value_counts()


# In[56]:


sns.histplot(data['sex'])
plt.xticks([0,1],['Female','Male'])
plt.show()


# In[60]:


sns.histplot(x='sex',hue="target",data=data)
plt.xticks([0,1],['Female','Male'])
plt.legend(labels=['No Disease','Disease'])
plt.show()


# In[63]:


sns.distplot(data['age'],bins=20)
plt.show()


# In[68]:


sns.histplot(data['cp'])
plt.Xticks=([0,1,2,3],["TA","ATA","NAP","Asym"])
plt.show()


# In[71]:


sns.histplot(x='cp',hue="target",data=data)

plt.legend(labels=['No Disease','Disease'])
plt.show()


# In[72]:


sns.histplot(x='fbs',hue="target",data=data)

plt.legend(labels=['No Disease','Disease'])
plt.show()


# In[73]:


data['trestbps'].hist()


# In[76]:


g=sns.FacetGrid(data,hue="sex",aspect=4)
g.map(sns.kdeplot,'trestbps',fill=True)
plt.legend(labels=['Male','Female'])
plt.show()


# In[77]:


data['chol'].hist()


# In[82]:


cat_val=[]
cont_val=[]
for column in data.columns:
    if data[column].nunique() <=10:
       cat_val.append(column)
    else:
       cont_val.append(column)
    


# In[83]:


cat_val


# In[84]:


cont_val


# In[86]:


data.hist(cont_val,figsize=(14,6))
plt.tight_layout()
plt.show()


# In[87]:


plt.savefig('example_plot.png')


# In[ ]:




