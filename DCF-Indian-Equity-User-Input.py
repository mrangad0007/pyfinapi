#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import numpy as np
import pandas as pd


company1=input()
company=company1.upper()
demo = '986ab3c482c959336e8b3a36d28672ee'
IS = requests.get(
    f'https://financialmodelingprep.com/api/v3/income-statement/{company}?apikey={demo}').json()
count = 0
# get revenue growth to estimate future sales
revenue_g = []
for item in IS:
    if count < 6:
        # print(item)
        revenue_g.append(item['revenue'])
        count = count + 1
revenue_g = (revenue_g[0] - revenue_g[1]) / revenue_g[0]
#revenue_g=0.25
print('The revenue growth is ')
print(revenue_g)
