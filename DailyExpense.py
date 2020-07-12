#!/usr/bin/env python
# coding: utf-8

# In[1]:


#daily expenses


# In[31]:


salary = int(input('Enter the salary:'))


# In[4]:


DailyExpenseLimit= int(input('Enter the Daily Expense Limit:'))


# In[21]:


BreakFast= int(input('Enter the expenditure of Breakfast:'))


# In[22]:


Lunch= int(input('Enter the expenditure of lunch:'))


# In[23]:


Dinner= int(input('Enter the expenditure of dinner:'))


# In[24]:


OtherExpenses= int(input('Enter the expenditure of Other Expenses:'))


# In[25]:


TotalExpenditureOfDay=BreakFast+Lunch+Dinner+OtherExpenses
print(str('TotalExpenditureOfDay='),TotalExpenditureOfDay)


# In[32]:


if TotalExpenditureOfDay<DailyExpenseLimit:
     print('You,ve spent=',TotalExpenditureOfDay,','
           'Hurray ! You have not exceeded the daily limit')
elif TotalExpenditureOfDay==DailyExpenseLimit:
     print('You,ve spent=',TotalExpenditureOfDay,','
           'WellDone ! Your expenditure is equal to daily limit')
else:
     print('You,ve spent=',TotalExpenditureOfDay,','
           'Alert ! Your expenditure has been exceeded')       

