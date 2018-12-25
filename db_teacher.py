#coding=utf-8
import psycopg2
import pandas as pd

conn = psycopg2.connect(database="d3l8u727fkdhuh",
                        user="uskhmdlztebice",
                        password="5714697bd569731729daa365947918c513374d064055ec40fd3644ed56963f0f",
                        host="ec2-107-20-237-78.compute-1.amazonaws.com",
                        port="5432")
cursor = conn.cursor()

p = pd.read_csv('teacher.csv')

cursor.execute("CREATE TABLE TEACHER (Tid INTEGER PRIMARY KEY, Tname VARCHAR(50) );")

for r in p['teacher']:
    print (r)
    cursor.execute("INSERT INTO TEACHER (TName) VALUES  ('"+r+"')")

conn.commit()





