# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 19:34:59 2018

@author: YURU
"""

import pandas as pd

deptId = {"GE":'通識中心', #通識中心
          "CE":'工學院', #工學院
          "CB":'商學院', #商學院
          "CS":'理學院', #理學院
          "CH":'人社學院', #人社學院
          "CI":'資電學院', #資電學院
          "CD":'建設學院', #建設學院
          "CF":'金融學院', #金融學院
          "NM":'國際科技與管理學院', #國際科技與管理學院
          "AS":'建築專業學院', #建築專業學院
          "PC":'學分學程', #學分學程
          "XA":'外語文', #外語文
          "XC":'通識核心課', #通識核心課
          "XD":'體育選項課', #體育選項課
          "XE":'綜合班', #綜合班
          "XF":'統籌科目', #統籌科目
          "XH":'軍訓', #軍訓
         }

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


dcard = pd.read_csv('dcardScrap.csv')

t=[]
c=[]
for d in dcard['teacher_course']:
    dd = d.split(' ')[-2:]
    t.append(dd[0])
    c.append(dd[1])
    
dcard['teacher']=t
dcard['course']=c

dcard.to_csv('dcardScrap.csv',index=False)

course = pd.DataFrame(data,columns=['department','cname','score','cls_name','credit','note'])
po = list(data['acptcnt']/data['precnt'])
for i,p in enumerate(po):
    if p>1:
        po[i]=1
course['populariy'] = po
#quizmethod : 考試方式 ($-dcard)
course.to_csv('CourseInDB.csv',index=False)

comment = pd.DataFrame(dcard,columns=['rate','cnotice','remark'])
comment['rate'] = [r[0] for r in comment['rate']]

comment.to_csv('CommentInDB.csv',index=False)

sub = pd.read_csv('sub_name.csv')
sub = sub['1']
dept=[]
for s in sub:
    d = data[data['cname'].str.lower() == s.lower()]['department']
    d = d[d.duplicated()==False]
    if len(d[d.str.contains('X')])>0:
        d = list(d[d.str.contains('X')])[0]
    else:
        d = list(d)[0]
    dept.append(deptId[d])


