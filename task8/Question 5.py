#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


#1. adding two numpy arrays
import numpy as np
from numpy import *
arr_1= int(input("enter the number of elements you want in array 1: "))
a= zeros(arr_1, dtype=int)
for i in range(len(a)):
    x=int(input("enter the elements: "))
    a[i] = x
arr_2=int(input("enter the number of elements you want in array 2: ")) 
b= zeros(arr_2, dtype=int)
for i in range(len(b)):
    y=int(input("enter the elements: "))
    b[i] = y
print("\nFirst array: ",a)
print("\nSecond array: ",b)
c=np.add(a,b) # using add function
print("\nSum of the given arrays is: ",c)


# In[ ]:


# 4. array datatype conversion

import numpy as np
from numpy import *
n= int(input("enter the number of elements you want: "))
arr= zeros(n, dtype=int)
for i in range(len(arr)):
    x=int(input("enter the elements: "))
    arr[i] = x
print(arr) 
print(arr.dtype)
arr = arr.astype('float64')
print(arr)
print(arr.dtype)


# In[ ]:




