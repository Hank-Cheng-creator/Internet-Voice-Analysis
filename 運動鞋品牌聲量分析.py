#!/usr/bin/env python
# coding: utf-8

# In[6]:


paging


# In[7]:


paging[1]


# In[8]:


paging[1]['href']


# In[9]:


import requests
from bs4 import BeautifulSoup

title=[]
url = 'https://pttbuy.cc/shoes/'

for page in range(1, 10):
    
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    data = soup.select('a')
    paging = soup.select('.brdbtn')
    last_url = paging[1]['href']
    url = last_url
    
    for item in data:
        title.append(item.text)
        print(item.text)


# In[24]:


import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']

colrogroup = ['#427f8f','#4a8fa1','#559db0','#66a7b8','#77b1c0','#89bbc8','#9ac5d0','#bdd9e0','#cee3e8','#e0edf0']
#藍色漸層

colrogroup2 = ['#cd0003','#e60003','#ff0004','#ff1a1d','#ff3436','#ff4d4f','#ff6768','#ff8181','#ff9a9b','#ffb4b4']
#紅色漸層

shoes_brand = ['nike','adidas','balance','puma','acisc',
'converse','reebok','mizuno','kappa','fila', 'underarmour', 'vans', 'diadora']

brand_count = []

for name in shoes_brand:
    count = 0
    for mentioned in title:
        if name in str(mentioned):
            count = count +1
    brand_count.append(count)
    
brand_count


# In[23]:


plt.bar(shoes_brand, brand_count, color=colrogroup)
plt.xticks(fontsize=15, rotation=90)

for index, data in enumerate(brand_count):
    plt.text(x=index, y=data, s=data, verticalalignment="top", horizontalalignment="center")
    

plt.xlabel('運動鞋品牌', fontsize=15)
plt.ylabel('聲量', fontsize=15)
plt.title('運動鞋品牌聲量分析', fontsize=20)
plt.show()


# In[19]:


for index, data in enumerate(brand_count):
    print(index, data)


# In[15]:


L= ['a','b','c']
for i in enumerate(L):
    print(i)

