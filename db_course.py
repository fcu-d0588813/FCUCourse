# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 13:38:37 2018

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

p = pd.read_csv('course.csv')

cursor.execute("CREATE TABLE COURSE (Cid INTEGER PRIMARY KEY, Department VARCHAR(50), Cname VARCHAR(50) );")

for i,(sub,dept) in enumerate(zip(p['sub'],p['dept']),1):
    print (i,sub,dept)
    cursor.execute("INSERT INTO COURSE (Cid,Department,Cname) VALUES  ('"+str(i)+"','"+sub+"','"+dept+"')")

conn.commit()



