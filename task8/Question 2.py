#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np


# In[ ]:


from numpy import *
arr_1= int(input("enter the number of elements you want in the first array: "))
a= zeros(arr_1, dtype=int)
for i in range(len(a)):
    x=int(input("enter the elements: "))
    a[i] = x
arr_2=int(input("enter the number of elements you want in the second array: ")) 
b= zeros(arr_2, dtype=int)
for i in range(len(b)):
    y=int(input("enter the elements: "))
    b[i] = y
print(a)
print(b)
print(np.array_equal(a,b))


# 
