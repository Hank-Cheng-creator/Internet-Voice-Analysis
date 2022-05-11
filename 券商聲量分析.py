#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests
from bs4 import BeautifulSoup

title=[]
url = 'https://www.ptt.cc/bbs/Foreign_Inv/index.html'

for times in range(10):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    articles = soup.select('.title a')
    paging = soup.select('.btn-group.btn-group-paging a')
    next_url = "https://www.ptt.cc" + paging[1]['href']
    url = next_url
    
    for each_title in articles:
        print(each_title.text, "https://www.ptt.cc" +each_title['href'])


# In[9]:


import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']

colrogroup = ['#427f8f','#4a8fa1','#559db0','#66a7b8','#77b1c0','#89bbc8','#9ac5d0','#bdd9e0','#cee3e8','#e0edf0']
#藍色漸層

colrogroup2 = ['#cd0003','#e60003','#ff0004','#ff1a1d','#ff3436','#ff4d4f','#ff6768','#ff8181','#ff9a9b','#ffb4b4']
#紅色漸層

security_brand = ['TD','SCHWAB','IB','複委託','FT']

brand_count = []

for name in security_brand:
    count = 0
    for mentioned in title:
        if name in str(mentioned):
            count = count +1
    brand_count.append(count)
    
brand_count


# In[3]:


plt.bar(security_brand, brand_count, color=colrogroup)
plt.xticks(fontsize=15, rotation=90)

for index, data in enumerate(brand_count):
    plt.text(x=index, y=data, s=data, verticalalignment="top", horizontalalignment="center")
    

plt.xlabel('券商品牌', fontsize=15)
plt.ylabel('聲量', fontsize=15)
plt.title('券商品牌聲量分析', fontsize=20)
plt.show()


# In[ ]:




