#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


# CONSIDER THE GIVEN ARRAY

n = np.array([10,11,12,13,14])
print(" The Original array is:")
print(n)
k = 5
new_num = np.zeros(len(n) + (len(n)-1)*(k))
new_num[::k+1] = n
print("The new array is:")
print(new_num)


# In[ ]:




