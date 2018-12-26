# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 15:55:43 2018

@author: YURU
"""

import psycopg2
import pandas as pd

conn = psycopg2.connect(database="d3l8u727fkdhuh",
                        user="uskhmdlztebice",
                        password="5714697bd569731729daa365947918c513374d064055ec40fd3644ed56963f0f",
                        host="ec2-107-20-237-78.compute-1.amazonaws.com",
                        port="5432")
cursor = conn.cursor()

p = pd.read_csv('107course.csv')

#cursor.execute("CREATE TABLE TEACH (Tid INTEGER  REFERENCES TEACHER (Tid), Cid INTEGER REFERENCES COURSE (Cid), PRIMARY KEY(Tid,Cid), Credit INTEGER, Cls_name VARCHAR(100), Score VARCHAR(3000), Popularity INTEGER, Note VARCHAR(200) );")
#cursor.execute('DROP TABLE TEACH')
'''
Tid,Cid,Credit,Cls_name,Score,Popularity,Note
tid+cid+credit+cls+score+popu+note
'''

for tid,cid,credit,cls,score,popu,note in zip(p['tid'],p['cid'],p['credit'],p['cls_name'],p['score'],p['populartiy'],p['note']):
    if score == '-1':
        score='nan'
    score = str(score).replace("'",'o').replace('\r','').replace('\t\t\t','').replace('\t',' ')
    note = str(note).replace('\r','')
    print (tid,cid,credit,cls,score,popu,note)
    cursor.execute("INSERT INTO TEACH (Tid,Cid,Credit,Cls_name,Score,Popularity,Note) VALUES ('"+str(tid)+"','"+str(cid)+"','"+str(int(credit))+"','"+str(cls)+"','"+str(score)+"','"+str(int(popu*100))+"','"+str(note)+"')")

conn.commit()
