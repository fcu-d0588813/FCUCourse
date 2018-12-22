# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 19:34:59 2018

@author: YURU
"""

import pandas as pd

data = pd.read_csv('106course.csv')
teacher = pd.read_csv('teacher.csv')
teacher = set(list(teacher['teacher']))

d = pd.DataFrame(data,columns=['sub_name','scr_period','tpa_score'])

t = []
for s in d['scr_period']:
    ts = s.split(' ')[-1].split(',')
    for i,tt in enumerate(ts):
        if tt not in teacher:
            print(ts.pop(i))
    print(ts)
    t.append(ts)  
t

d['teacher']=t

data['teacher']=t

data.to_csv('106course.csv',index=False)