# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 14:31:14 2018

@author: YURU
"""

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

#將課程評論爬下後進行情感分析，透過情感分析做為參考依據之一。

r = requests.get("https://babu7.github.io/")
soup = bs(r.text,"lxml")
table_l = soup.find_all('table')

#儲存標題
table = table_l[0]
t = table.find('tr')
title=[]
for row in t.find_all('th')[1:]:
    title.append(row.text)
title

d = []
for i in range(len(title)):
    d.append([])
d

for table in table_l:
    for row in table.find_all('tr')[1:]:
        for i,r in enumerate(row.find_all('td')):
            d[i].append(str(r.text.strip()).replace('\r\n','，'))
            #print(i,r.text.strip())
            
data = pd.DataFrame()
for i in range(len(title)):
    data[title[i]] = d[i]
data

data.to_csv('dcardScrap.csv',index=False)