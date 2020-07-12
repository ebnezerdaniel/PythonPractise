#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Python Program to Calculate the Area of a Triangle


# In[3]:


u=int(input('height:'))
i=int(input('base:'))
o=(u*i)/2
print('Area of Triangle:',o)


# In[ ]:





# In[4]:


#Python Program to Calculate the Area of a Triangle with three sides


# In[5]:


a=int(input('side 1:'))
b=int(input('side 2:'))
c=int(input('side 3:'))
s=(a+b+c)/2
p=s*(s-a)*(s-b)*(s-c)**0.5
print('Area of triangle:',p)

