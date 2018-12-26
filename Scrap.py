# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 13:59:23 2018

@author: YURU
"""

import json
import requests
import pandas as pd
import js2py

deptId = ("GE", #通識中心
          "CE", #工學院
          "CB", #商學院
          "CS", #理學院
          "CH", #人社學院
          "CI", #資電學院
          "CD", #建設學院
          "CF", #金融學院
          "NM", #國際科技與管理學院
          "AS", #建築專業學院
          "PC", #學分學程
          "XA", #外語文
          "XC", #通識核心課
          "XD", #體育選項課
          "XE", #綜合班
          "XF", #統籌科目
          "XH", #軍訓
         )

data=[]
url = "https://coursesearch04.fcu.edu.tw/Service/Search.asmx/GetType1Result"
year=106
for sms in [1,2]:
    for dept in deptId:
        params = {'baseOptions': {'lang': "cht", 'year': year, 'sms': sms},
                  'typeOptions': {'degree': "1", 'deptId': dept, 'unitId': "*", 'classId': "*"}}
        r = requests.post(url, json=params)
        for d in json.loads(json.loads(r.text)['d'])['items']:
            d['year']=year
            d['sms']=sms
            d['deptId']=dept
            d['courseid'] = str(d['year'])+str(d['sms'])+d['cls_id']+d['sub_id']+d['scr_dup']
            print(d)
            data.append(d)
data

title = list(data[0].keys())
title

d = []
for i in range(len(title)):
    d.append([])
d

for dd in data:
    for i,ds in enumerate(dd.values()):
        d[i].append(ds)
d   

df = pd.DataFrame()
for i in range(len(title)):
    df[title[i]] = d[i]
df

'''
http://service120.sds.fcu.edu.tw/W320104/W320104_stu_pre.aspx?courseid=1061CE0711127436001&lang=cht

http://service120.sds.fcu.edu.tw/W320104/action/getdata.aspx/getEvoluationInfo

courseid = year + sms + cls_id + sub_id + scr_dup

'''

#get cookies
r=requests.get('http://service120.sds.fcu.edu.tw/W320104/W320104_stu_pre.aspx?courseid=1061CE0711127436001&lang=cht')
r.cookies

cookie = {'Cookie':'ASP.NET_SessionId='+r.cookies['ASP.NET_SessionId']}
cookie

df.to_csv('106course.csv',encoding='utf-8',index=False)

#js轉py
js2py.translate_file('DES.js', 'DES.py')

from DES import *

course_id=[]
for cid in df['courseid']:
    en = str(encMe(cid))[1:-1]
    print(en)
    course_id.append(en)
course_id

df['course_id'] = course_id
df

r = requests.get('http://service120.sds.fcu.edu.tw/W320104/W320104_stu_pre.aspx?courseid=1061CE0711127436001&lang=cht')
cookie = {'Cookie':'ASP.NET_SessionId='+r.cookies['ASP.NET_SessionId']}
params = {"course_id":"e3e73945c1c6299996bbeff1916a72e8532af778ef114215ac81a6729f51590368e931f1f26b98c3"}
print(cookie)
print(params)
url = 'http://service120.sds.fcu.edu.tw/W320104/action/getdata.aspx/getEvoluationInfo'
r = requests.post(url, json=params, headers=cookie)
json.loads(r.text)['d'][0]

df = pd.read_csv('106course.csv')  
df

tpa_score=[]
url = 'http://service120.sds.fcu.edu.tw/W320104/action/getdata.aspx/getEvoluationInfo'
for i,cid in enumerate(df['course_id']):
    if i%20 == 0:
        r = requests.get('http://service120.sds.fcu.edu.tw/W320104/W320104_stu_pre.aspx?courseid=1061CE0711127436001&lang=cht')
        cookie = {'Cookie':'ASP.NET_SessionId='+r.cookies['ASP.NET_SessionId']}
        print(cookie)
    params = {"course_id":cid}
    print(params)
    for t in range(3):
        print(t)
        try:
            r = requests.post(url, json=params, headers=cookie,timeout=5)
        except:
            print('timeout')
        if r.status_code == 200:
            break
    s = json.loads(r.text)['d']
    if s == '':
        tpa_score.append(-1)
    else:
        s = s[0]['tpa_score_new']
        tpa_score.append(s)
    print(s)
    
df['tpa_score'] = tpa_score

course106 = df[df['tpa_score']!='-1']

course106.to_csv('106course.csv',encoding='utf-8',index=False)
