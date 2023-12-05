#!/usr/bin/env python
# coding: utf-8

# # 1 Hello world

# In[8]:


# printing my first message
print("Hello world!")


# In[9]:


"Hello world!"


# In[10]:


# printing my name
print("Teerut Panalikul")


# # 2 Data Types

# In[11]:


type(1)


# In[12]:


type(2.4)


# In[13]:


1 + 3


# In[15]:


4 - 1 


# In[16]:


type(True)


# In[17]:


type(False)


# In[18]:


type("Hello World")


# In[20]:


"Hello World".upper()
"Hello World".lower()
"Hello World".title()


# In[21]:


print("Hello World".upper())
print("Hello World".lower())
print("Hello World".title())


# In[1]:


"Hello World".count('l')


# In[2]:


"Hello World".replace('o', 'u')


# # 3 Variables

# In[3]:


message_1 = "I'm learning Python"


# In[4]:


message_1


# In[5]:


message_2 = "and it's fun!"


# In[6]:


message_2


# In[7]:


message_1 + message_2


# In[9]:


massage = message_1 + ' ' + message_2
massage


# In[11]:


f'{message_1} test {message_2}'


# # 4 List

# In[16]:


countries = ['United States', 'India', 'China', 'Brazil']


# In[18]:


countries


# In[17]:


countries[0]


# In[19]:


print(countries[0])
print(countries[1])
print(countries[2])
print(countries[3])


# In[20]:


countries[-1]


# In[21]:


countries[-4]


# In[ ]:


# slicing
list_name[start:stop]


# In[23]:


countries[0:3]


# In[24]:


countries[0:1]


# In[25]:


countries[1:]


# In[26]:


countries[:2]


# ## 4.0.1 Adding element to a list

# In[28]:


countries


# In[30]:


countries.append('canada')


# In[31]:


countries


# In[32]:


countries.insert(0, 'Spain')


# In[33]:


countries


# In[35]:


countries_2 = ['UK', 'Germany', 'Austria']


# In[36]:


countries + countries_2


# In[37]:


nested_list = [countries, countries_2]


# In[38]:


nested_list


# ## 4.0.2 Removing an elements

# In[39]:


countries.remove('United States')


# In[40]:


countries


# In[41]:


countries.pop(-1)


# In[42]:


countries


# In[43]:


del countries[0]


# In[44]:


countries


# In[45]:


del countries[3]


# In[46]:


countries


# ## 4.0.3 Sorting a list

# In[47]:


numbers = [4, 3, 10, 7, 1, 2]


# In[49]:


numbers.sort()


# In[50]:


numbers


# In[51]:


numbers = [4, 3, 10, 7, 1, 2]
numbers.sort(reverse=True)
numbers


# ## 4.0.4 Update an Element

# In[53]:


numbers[0] = 1000
numbers


# ## 4.0.5 Copying a list

# In[54]:


countries = ['United States', 'India', 'China', 'Brazil']
countries[:]


# In[ ]:


countries = ['United States', 'India', 'China', 'Brazil']
countries[:]


# In[55]:


countries = ['United States', 'India', 'China', 'Brazil']
new_list = countries[:]


# In[56]:


new_list


# In[57]:


new_list_2 = countries.copy()


# In[58]:


new_list_2


# # 5 Dictionary

# In[59]:


my_dict = {'key1':'value1', 'key2':'value2'}


# my_data = {'name':'Frank', 'age':26}

# In[60]:


my_data = {'name':'Frank', 'age':26}


# In[61]:


my_data


# my_data.keys()

# In[62]:


my_data.keys()


# In[63]:


my_data.values()


# In[64]:


my_data.items()


# In[65]:


my_data['height'] = 1.7


# In[66]:


my_data


# In[79]:


my_data.update({'height':1.95})


# In[80]:


my_data


# ## 5.0.1 Copy a dictionary

# In[70]:


new_dict = my_data.copy()


# In[74]:


new_dict


# In[77]:


new_dict_2 = my_data


# In[81]:


new_dict_2


# ## 5.0.2 Remove element

# In[82]:


my_data.pop('name')


# In[83]:


my_data


# In[84]:


del my_data['age']


# In[85]:


my_data


# In[86]:


my_data.clear()


# In[87]:


my_data


# # 6 If Statement

# In[92]:


age = 30

if age >= 18:
    print("You're an adult!")
else:
    print("You're a kid")


# 

# 

# 

# In[96]:


age = 12

if age >= 18:
    print("You're an adult!")
elif age >= 13:
    print("You're a teenager")
else:
    print("You're a kid")


# # 7 For loop

# for<variable> in<list>:
#     code

# In[98]:


countries


# In[102]:


for country in countries:
    print (country)


# In[103]:


for i, country in enumerate(countries):
    print(i)
    print(country)


# In[108]:


my_data = {'name':'Frank', 'age':26}
my_data


# In[109]:


for key, value in my_data.items():
    print(key)
    print(value)


# # 8 Function

# def function(<params>):
#     <code>
#     return<data>

# In[3]:


def sum_values(a, b):
    x = a + b
    return x


# In[4]:


sum_values(1, 3)


# ## 8.1 Built-in Function

# In[5]:


countries = ['United States', 'India', 'China', 'Brazil']


# In[6]:


len(countries)


# In[8]:


max([10, 63, 81, 1, 99])


# In[9]:


min([10, 63, 81, 1, 99])


# In[10]:


type(countries)


# In[12]:


for i in range(1, 10, 2):
    print(i)


# # 9 Module

# In[ ]:


import


# ## 9.1 OS Module 

# In[14]:


import os


# In[15]:


os.getcwd()


# In[16]:


os.listdir()


# In[17]:


os.makedirs("New Folder")


# In[18]:


os.listdir()


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





# In[ ]:





# In[ ]:





# In[ ]:




