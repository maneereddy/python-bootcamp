#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector


# In[5]:


import xlrd
import pandas as pd


# In[2]:


mydata = mysql.connector.connect(host="localhost",user="root",passwd="8639488740",database="testdb")


# In[4]:


mydb = mydata.cursor()
mydb.execute("create table stu(stdid int primary key,name varchar(30),section char(10))")


# In[27]:


loc = ("C:\\Users\\Admin\\Documents\\students.xlsx")
l =list()


# In[50]:



a = xlrd.open_workbook(loc)
sheet = a.sheet_by_index(0)
sheet.cell_value(0,0)
for i in range(1,5):
    #print(sheet.row_values(i))
    l.append(tuple(sheet.row_values(i)))
#print(l)

# q = "insert into stu(stdid,name,section)values(%s,%s,%s)"
# l = [("6","manee","D")]
# mydb.execute(q,l)
# mydata.commit()
# mydata.close()    


# In[53]:


q = "insert into stu(stdid,name,section)values(%s,%s,%s)"
# mydb.executemany(q,l)
# mydata.commit()
mydata.close()    


# In[58]:





# In[ ]:




