#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Find the Factorial of a Number


# In[1]:


a=int(input('Enter the number:'))
fact=1

for i in range(1,a+1): 
    fact=i*fact
print('Factorial of %d is %d' %(a,fact))

