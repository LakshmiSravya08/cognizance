#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:



ser = pd.Series(['amrita', 'school', 'of','engineering','chennai','campus'])
new_ser= ser.str.title()  #inbuilt function
print("The original series: ")
print(ser)
print("\nThe new series: ")
print(new_ser)


# In[ ]:




