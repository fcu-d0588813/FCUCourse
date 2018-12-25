import psycopg2


# Update connection string information obtained from the portal
conn = psycopg2.connect(database="d3l8u727fkdhuh",
                        user="uskhmdlztebice",
                        password="5714697bd569731729daa365947918c513374d064055ec40fd3644ed56963f0f",
                        host="ec2-107-20-237-78.compute-1.amazonaws.com",
                        port="5432")
cursor = conn.cursor()
cursor.execute("CREATE TABLE COURSE (Cid INTEGER PRIMARY KEY, Department VARCHAR(50), Cname VARCHAR(50) );")
cursor.execute("CREATE TABLE TEACHER (Tid INTEGER PRIMARY KEY, Tname VARCHAR(50) );")
cursor.execute("CREATE TABLE TEACH (Tid INTEGER  REFERENCES TEACHER (Tid), Cid INTEGER REFERENCES COURSE (Cid), PRIMARY KEY(Tid,Cid),Score INTEGER, Quizmethod VARCHAR(150), Popularity INTEGER, Cls_name VARCHAR(50), Credit INTEGER, Note VARCHAR(150) );")
cursor.execute("CREATE TABLE COMMENT (Tid INTEGER  REFERENCES TEACHER (Tid), Cid INTEGER REFERENCES COURSE (Cid), PRIMARY KEY(Tid,Cid), CNotice VARCHAR(150), Remark VARCHAR(150), Rate INTEGER );")

conn.commit()





