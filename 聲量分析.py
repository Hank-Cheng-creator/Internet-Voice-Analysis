#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']

colrogroup = ['#427f8f','#4a8fa1','#559db0','#66a7b8','#77b1c0','#89bbc8','#9ac5d0','#bdd9e0','#cee3e8','#e0edf0']
#藍色漸層

colrogroup2 = ['#cd0003','#e60003','#ff0004','#ff1a1d','#ff3436','#ff4d4f','#ff6768','#ff8181','#ff9a9b','#ffb4b4']
#紅色漸層

movie = ['成為王的男人','皇后的品格','赤月青日','神的測驗','死之詠讚','加油吧威基基','皮諾丘','魔女寶鑑','男朋友','來自星星的你']

KoreaDrama = pd.read_csv('KoreaDrama_re.csv', engine='python', error_bad_lines=False)

#Parser engine to use. The C engine is faster while the python engine is currently more feature-complete

#欄位太多的行（例如，帶有太多逗號的csv行）會引發異常，並且不會返回任何DataFrame。
#如果error_bad_lines為False，則這些「壞行」將從返回的DataFrame中刪除。

thearticle = KoreaDrama['標題'] + KoreaDrama['內容']


# In[5]:


KoreaDrama


# In[6]:


total_movie = []

for mov in movie:
    count = 0
    for art in thearticle:
        if mov in str(art):
            count = count +1
    total_movie.append(count)


# In[2]:


total_movie


# In[ ]:


plt.bar(movie, total_movie, color=colrogroup2)
plt.xticks(fontsize=15,rotation=90)
plt.xlabel('韓劇名稱', fontsize=15)
plt.ylabel('聲量', fontsize=15)
plt.title('韓劇聲量分析', fontsize=20)
plt.show() 

