#!/usr/bin/env python
# coding: utf-8

# In[125]:


import csv
from datetime import datetime, timedelta


# In[126]:


import pyodbc


# In[127]:


conn = pyodbc.connect('DSN=kubrick.sql;UID=DE14;PWD=password')


# In[128]:


cur = conn.cursor()


# In[129]:


#q = 'SELECT * FROM connor.shark'
q = 'INSERT INTO connor.shark(attack_date, case_number, country, activity, age, gender, isfatal) values (?, ?, ?, ?, ?, ?, ?)'
#p =['2019-10-28', 'c0ck9', 'UK', 'Celebrating', 24, 'M', 0]


# In[130]:


try: 
    cur.execute(q,p)
    conn.commit()
except:
    conn.rollback()


# In[131]:


shark = r'C:\data\november\GSAF5.csv'


# In[132]:


attack_dates = []
case_number = []
country = []
activity = []
age = []
gender = []
isfatal = []
with open(shark, encoding = 'UTF-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        attack_dates.append(row['Date'])
        case_number.append(row['Case Number'])
        country.append(row['Country'])
        activity.append(row['Activity'])
        age.append(row['Age'])
        gender.append(row['Sex '])
        isfatal.append(row['Fatal (Y/N)'])


# In[133]:


data = zip(attack_dates, case_number, country, activity, age, gender, isfatal)


# In[134]:


for d in data:
    try:
        cur.execute(q,d)
        conn.commit()
    except:
        conn.rollback()


# In[ ]:





# In[ ]:




