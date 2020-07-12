#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Python Program to Solve Quadratic Equation


# In[2]:


a=int(input('Enter the value of a:'))
b=int(input('Enter the value of b:'))
c=int(input('Enter the value of c:'))
x=int(b**2-4*a*c)
z=x**0.5
p=-b+z
y=(p/(2*a))
print('Quadratic equation:',y)

