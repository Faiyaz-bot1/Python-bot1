#!/usr/bin/env python
# coding: utf-8

# In[ ]:


continuation with list datatype:


# In[ ]:





# In[ ]:


slicing of list datatype 
for implementation with list data type:


# In[ ]:





# In[4]:


my_students = ['ravi','irfan','gaurav','deepak','akshay','kalyani','rahul','kiran']
print(my_students)


# In[2]:


type(my_students)


# In[ ]:


get_ipython().set_next_input("req: to access 'gurav' name? index num");get_ipython().run_line_magic('pinfo', 'num')


# In[3]:


print(my_students[2])


# In[ ]:


general syntax of slicing:
    
startvalue:stopvalue:stepcount***(based on indexes)
        
lastvalue is always exclusive(it will not be displayed or printed on the screen or output)


# In[5]:


print(my_students[0:1])


# In[6]:


print(my_students[0:2]) #single group slice


# In[7]:


print(my_students[2:4]) #2nd slice....last value


# In[8]:


print(my_students[4:6])


# In[9]:


print(my_students[6:8])


# In[ ]:





# In[ ]:


req:to print number between 1-20 and i have to store them in a list:


# In[ ]:





# In[13]:


numbers = list(range(1,21))...#last value is always exclusive

print(numbers)


# In[ ]:





# In[ ]:


req: i want to print even number from 1-30 by using a list.


# In[ ]:


if a number is divisible by 2,that is condsidered as even number. 


# In[ ]:





# In[16]:


even_numbers = list(range(2,31,2))
print(even_numbers)


# In[ ]:





# In[ ]:


req: i want to print odd number from 1-31 by using a list


# In[ ]:


if a number is not divisible by 2,that us considered as odd number


# In[ ]:





# In[29]:


odd_numbers = list(range(3,31,2))
print(odd_numbers)


# In[ ]:





# In[ ]:


organising the list:


# In[30]:


print(my_students)


# In[ ]:





# In[ ]:


req:i have to arrange the above list in an alphabetical order(A-Z)

two possible ways:
    
temporary sorting(sorted)

permanent sorting(sort)


# In[ ]:





# In[31]:


print(sorted(my_students)) #A-Z


# In[32]:


print(my_students)


# In[ ]:





# In[ ]:


as you can see it was a temporary sorting.


# In[ ]:





# In[34]:


my_students.sort()

print(my_students)


# In[ ]:





# In[35]:


print(my_students)


# In[ ]:


now you can observe the sorting is done permanenty to your list.


# In[ ]:




