# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 23:23:16 2018

@author: zengla
"""

import psycopg2
import pandas as pd

conn = psycopg2.connect(database="d3l8u727fkdhuh",
                        user="uskhmdlztebice",
                        password="5714697bd569731729daa365947918c513374d064055ec40fd3644ed56963f0f",
                        host="ec2-107-20-237-78.compute-1.amazonaws.com",
                        port="5432")
cursor = conn.cursor()

p = pd.read_csv('comment.csv',encoding='big5')

#cursor.execute("CREATE TABLE COMMENT (No INTEGER,Cid INTEGER REFERENCES COURSE(Cid),Tid INTEGER REFERENCES TEACHER(Tid),Rate INTEGER, Cnotice VARCHAR(2000), Remark VARCHAR(2000),Quizmethod VARCHAR(2000),PRIMARY KEY (No));")
#cursor.execute('DROP TABLE COMMENT')


for i,(cid,tid,rate,cnotice,quizmethod,remark) in enumerate(zip(p['cid'],p['tid'],p['rate'],p['cnotice'],p['quizmethod'],p['remark']),1):
    print (i,cid,tid,rate,cnotice,quizmethod,remark)
    cursor.execute("INSERT INTO COMMENT (No,Cid,Tid,Rate,Cnotice,Quizmethod,Remark) VALUES  ('"+str(i)+"','"+str(cid)+"','"+str(tid)+"','"+str(rate)+"','"+str(cnotice)+"','"+str(quizmethod)+"','"+str(remark)+"')")

conn.commit()
