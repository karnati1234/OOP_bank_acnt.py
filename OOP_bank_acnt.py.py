#!/usr/bin/env python
# coding: utf-8

# In[29]:


class Account():
    
    def __init__(self,owner, balance = 0):
        
        self.owner = owner
        self.balance = balance
        
    def deposit(self,dep_amt):
        
        self.balance = self.balance + dep_amt
        print(f" Added {dep_amt} to the balance")
        
    def withdraw(self,wt_amt):
        
        if self.balance >= wt_amt:
            self.balance = self.balance - wt_amt
            print("Withdrawal accepted")
            
        else:
            print("Sorry insufficient balance!")
            
    def __str__(self):
        return f"owner: {self.owner} \n balance: {self.balance}"


# In[30]:


a = Account("Ram",200)


# In[31]:


a.owner


# In[32]:


a.balance


# In[33]:


print(a)


# In[34]:


a.deposit(100)


# In[35]:


a.balance


# In[36]:


print(a)


# In[37]:


a.withdraw(100)


# In[ ]:




