#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
from urllib.request import urlopen
from bs4 import BeautifulSoup


# In[2]:


data = pd.read_csv("Oregon Hwy 26 Crash Data for 2019 - Crashes on Hwy 26 during 2019.csv")


# In[9]:


CrashesDF = data[data['Record Type'] == 1]
VehiclesDF = data[data['Record Type'] == 2]
ParticipantsDF = data[data['Record Type'] == 3]


# In[10]:


CrashesDF = CrashesDF.dropna(axis=1,how='all')
VehiclesDF = VehiclesDF.dropna(axis=1,how='all')
ParticipantsDF = ParticipantsDF.dropna(axis=1,how='all')


# In[31]:


#existence assertion test - crash id check
count = 0
for x in CrashesDF['Crash ID']:
    if not isinstance(x, int):
        print("ERROR: Missing Crash ID")
        count += 1
for x in VehiclesDF['Crash ID']:
    if not isinstance(x, int):
        print("ERROR: Missing Crash ID")
        count += 1        
for x in ParticipantsDF['Crash ID']:
    if not isinstance(x, int):
        print("ERROR: Missing Crash ID")
        count += 1
print("EXISTENCE ASSERTION TEST - CRASH ID CHECK, COMPLETED: {count} errors were found".format(count = count))

#existence assertion test - county id check
count = 0
for x in CrashesDF['County Code']:
    if not isinstance(x, float):
        print("ERROR: Missing County ID")
        count += 1
    
print("EXISTENCE ASSERTION TEST - COUNTY CODE CHECK, COMPLETED: {count} errors were found".format(count = count))


# In[27]:


CrashesDF


# In[28]:


VehiclesDF


# In[29]:


ParticipantsDF


# In[ ]:




