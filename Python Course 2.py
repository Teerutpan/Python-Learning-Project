#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[4]:


# creating an array
data = np.array([[1,4], [2,5], [3,6]])


# In[6]:


# creating a data frame
pd.DataFrame(data)


# In[7]:


df = pd.DataFrame(data, index=['row1','row2','row3'],
             columns=['col1', 'col2'])
             


# In[8]:


# showing the dataframe
df


# In[9]:


# creating an array with shape
data = [[1,4], [2,5], [3,6]]


# In[10]:


# creating a data frame
df = pd.DataFrame(data, index=['row1','row2','row3'],
             columns=['col1', 'col2'])


# In[11]:


# showing the dataframe
df


# In[13]:


# lists used for this emample
states = ['California', 'Texas', 'Florida', 'New York']
population = [39613493, 29730311, 21944577, 19299981]


# In[14]:


# Storing lists within a dictionary
dict_states = {'States':states, 'population': population}


# In[15]:


# Creating the dataframe
df_population = pd.DataFrame(dict_states)


# In[6]:


# Showing the dataframe
df_population


# In[8]:


# reading the csv file
df_exams = pd.read_csv('StudentsPerformance.csv')


# In[24]:


# show first 5 rows in a dataframe
df_exams.head()


# In[25]:


df_exams


# In[28]:


df_exams.tail(10)


# In[27]:


df_exams.head(10)


# In[29]:


df_exams.shape


# In[31]:


pd.set_option('display.max_row',1000)
df_exams


# # Basic Attributes, Methods and Function

# In[32]:


df_exams.index


# In[33]:


df_exams.columns


# In[34]:


df_exams.dtypes


# In[36]:


df_exams.info()


# In[37]:


df_exams.describe()


# In[38]:


len(df_exams)


# In[39]:


max(df_exams.index)


# In[40]:


min(df_exams.index)


# In[41]:


type(df_exams)


# In[42]:


round(df_exams, 2)


# # Select One Column from a Dataframe

# In[44]:


df_exams['gender']


# In[45]:


type(df_exams['gender'])


# In[47]:


df_exams['gender'].index
df_exams['gender'].head()


# In[49]:


df_exams.gender


# In[50]:


df_exams.math score


# In[51]:


df_exams['math score']


# # Selecting two or more columns

# In[52]:


df_exams[['gender', 'math score']]


# In[53]:


type(df_exams[['gender', 'math score']])


# In[54]:


df_exams[['gender', 'writing score','math score','reading score']]


# # Adding a new column 

# In[9]:


# adding new column to dataframe
df_exams['language score'] = 70


# In[10]:


df_exams


# In[11]:


import numpy as np


# In[16]:


language_score = np.arange(0, 1000)


# In[17]:


len(language_score)


# In[18]:


df_exams['language score'] = language_score
df_exams


# In[21]:


int_language_score = np.random.randint(1, 100, size=1000)


# In[23]:


min(int_language_score)


# In[24]:


max(int_language_score)


# In[25]:


df_exams['language score'] = int_language_score
df_exams


# In[26]:


np.random.uniform(1,100, size=100)


# # Operations on Dataframes

# In[27]:


df_exams['math score'].sum()


# In[32]:


df_exams['math score'].count()
df_exams['math score'].mean()
df_exams['math score'].std()
df_exams['math score'].max()
df_exams['math score'].min()


# In[34]:


df_exams.describe()


# In[35]:


df_exams['reading score'] + df_exams['writing score'] + df_exams['language score']


# In[38]:


df_exams['average'] = (df_exams['reading score'] + df_exams['writing score'] + df_exams['language score'])/3


# In[40]:


df_exams.round(2)


# # The value_counts()method

# In[41]:


len(df_exams['gender'])


# In[42]:


df_exams['gender'].count()


# In[43]:


df_exams['gender'].value_counts()


# In[44]:


df_exams['gender'].value_counts(normalize = True)


# In[45]:


df_exams['parental level of education'].value_counts()


# In[47]:


df_exams['parental level of education'].value_counts(normalize = True).round(2)


# # Sort a Dataframe

# In[50]:


df_exams.sort_values('math score')


# In[51]:


df_exams.sort_values('math score', ascending=False)


# In[54]:


df_exams.sort_values(['math score','reading score'], ascending=False)


# In[55]:


df_exams


# In[56]:


df_exams.sort_values(['math score','reading score'], ascending=False, inplace = True)


# In[57]:


df_exams


# In[58]:


df_exams.sort_values('race/ethnicity', ascending = True, key = lambda col:col.str.lower())


# # Pivot()

# In[64]:


df_gdp = pd.read_csv('gdp.csv', encoding='latin-1')


# In[65]:


df_gdp


# In[66]:


df_gdp.pivot(index="year", columns="country", values="gdppc")


# # pivot_table()

# In[68]:


df_sales = pd.read_excel("supermarket_sales.xlsx")
df_sales


# In[69]:


df_sales.pivot_table(index="Gender", aggfunc="sum")


# In[72]:


df_sales.groupby("Gender").sum(numeric_only=True)


# In[74]:


df_sales.pivot_table(index="Gender", values=["Quantity", "Total"], aggfunc="sum")


# In[75]:


df_sales.pivot_table(index = "Gender",
                     columns = "Product line",
                     values = "Total",
                     aggfunc = "sum")


# In[76]:


df_sales.pivot_table(index = "Gender",
                     columns = "Product line",
                     values = "Total")


# In[2]:


df_population_raw = pd.read_csv('population_total.csv')


# In[78]:


df_population_raw


# In[4]:


df_population_raw.dropna(inplace=True)


# In[5]:


df_pivot = df_population_raw.pivot(index = "year",
                                   columns = "country",
                                   values ="population")


# In[6]:


df_pivot = df_pivot[["United States", "India", "China", "Indonesia", "Brazil"]]


# In[11]:


df_pivot


# In[18]:


df_pivot.plot(kind = 'line', xlabel = 'Year',
                             ylabel = 'Population',
                              title ='Population (1955-2022)',
                             figsize = (10, 4))
plt.savefig('my_test.png')
plt.show()


# In[19]:


df_pivot.to_excel('pivot_table.xlsx')


# In[21]:


df_pivot.index


# In[24]:


df_pivot.index.isin([2020])


# In[7]:


df_pivot_20 = df_pivot[df_pivot.index.isin([2020])]


# In[26]:


df_pivot_20


# In[37]:


df_pivot_20.T


# In[8]:


df_pivot_20 = df_pivot_20.T


# In[44]:


df_pivot_20.plot(kind = 'bar', color = 'orange',
                              xlabel = 'Year',
                              ylabel = 'Population',
                               title ='Population (2020)',
                             figsize = (7, 4))


# In[45]:


df_pivot[df_pivot.index.isin([1980, 1990, 2000, 2010, 2020])]


# In[46]:


df_pivot_sample = df_pivot[df_pivot.index.isin([1980, 1990, 2000, 2010, 2020])]


# In[47]:


df_pivot_sample.plot( kind = 'bar',
                    xlabel = 'Year',
                    ylabel = 'Population',
                   figsize = (7, 4))


# In[10]:


# changing column (integer to string)
df_pivot_20.rename(columns = {2020:'2020'}, inplace=True)


# In[11]:


df_pivot_20


# In[14]:


df_pivot_20.plot(kind = 'pie', y ='2020', title = 'Population in 2020(%)' )


# In[15]:


import matplotlib.pyplot as plt


# In[16]:


plt.savefig('my_test.png')


# In[17]:


plt.show()


# In[ ]:





# In[ ]:




