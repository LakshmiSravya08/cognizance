#!/usr/bin/env python
# coding: utf-8

# In[2]:


from numpy import *
a=array([])
b=int(input('Enter the First Number:'))
c=int(input('Enter the last  Number:'))
for p in range(b,c):
    a=append(a,p)
    for p in range(5):
        a=append(a,0)
a=append(a,c)
print(a)


# In[ ]:




