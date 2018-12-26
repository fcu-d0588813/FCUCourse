# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 14:58:52 2018

@author: YURU
"""

import os
import psycopg2
import random

#連接資料庫
conn = psycopg2.connect(database="d3l8u727fkdhuh",
                        user="uskhmdlztebice",
                        password="5714697bd569731729daa365947918c513374d064055ec40fd3644ed56963f0f",
                        host="ec2-107-20-237-78.compute-1.amazonaws.com",
                        port="5432")
cursor = conn.cursor()

def get(req):
    p = req['queryResult']['parameters']
    msg=''
    #msg = 'Course: ' + p['Course'] + '\nTeacher: ' + p['Teacher'] + '\nAction: ' + p['Action']
    if p['Action'] == '評價':  #老師-課程 or 老師
        if p['Course'] != '':
            #教授名字 課程名稱 評論
            cursor.execute("SELECT round(avg(rate),2) FROM TEACHER,COURSE,COMMENT WHERE tname='"+p['Teacher']+"' AND cname='"+p['Course']+"' AND TEACHER.tid=COMMENT.tid AND COURSE.cid=COMMENT.cid;")
            rate = cursor.fetchall()
            cursor.execute("SELECT remark FROM TEACHER,COURSE,COMMENT WHERE tname='"+p['Teacher']+"' AND cname='"+p['Course']+"' AND TEACHER.tid=COMMENT.tid AND COURSE.cid=COMMENT.cid;")
            remark = cursor.fetchall()
            print(rate,remark)
            msg +='教授:'+ p['Teacher'] +'\n'
            if rate != None:
                if rate[0]!=None:
                    msg +='推薦指數: '+str(rate[0]).strip()+'\n'
                if remark[0]!=None or remark[0]!='nan':
                    r = random.randint(0,len(remark[0]))
                    print('>>',r)
                    msg +=str(remark[0]).strip() +'\n'
                else:
                    msg +='沒有評論'+'\n'                      
            else:
                msg += '沒有資料，請重新輸入'+'\n'
        else:
            #教授名字 推薦指數/評論
            cursor.execute("SELECT round(avg(rate),2) FROM TEACHER,COMMENT WHERE tname='"+p['Teacher']+"' AND TEACHER.tid=COMMENT.tid;")
            co = cursor.fetchone()
            #尋找對應老師ID的course、comment
            #計算平均rate
            if co != None:
                msg +='推薦指數: '+str(co[0]).strip() +'\n'
            else:
                msg += '沒有資料，請重新輸入'+'\n'
           
            
    elif p['Action'] == '課程' and p['Teacher'] != '' and p['Course'] != '':
        #教授名字 課程名稱 課程
        cursor.execute("SELECT score FROM Teacher,Teach,Course WHERE tname='"+p['Teacher']+"' AND cname='"+p['Course']+"' AND Teach.tid=Teacher.tid AND Teach.cid=Course.cid;")
        co = cursor.fetchone()
        if co != None:
            msg += str(co[0]).strip()+'\n'
        else:
            msg += '沒有資料，請重新輸入'
        
            
    elif p['Action'] == '作業考試' and p['Teacher'] != '' and p['Course'] != '':
        #教授名字 課程名稱 作業考試
        cursor.execute("SELECT quizmethod FROM Teacher,Teach,Course WHERE tname='"+p['Teacher']+"' AND cname='"+p['Course']+"' AND Teach.tid=Teacher.tid AND Teach.cid=Course.cid;")
        co = cursor.fetchone()
        if co != None:
            msg += str(co[0]).strip()+'\n'
        else:
            msg += '沒有資料，請重新輸入'+'\n'
    
    elif p['Action'] == '推薦指數' and p['Teacher'] != '' and p['Course'] == '':
        #教授名字 推薦指數
        cursor.execute("SELECT round(avg(rate)) FROM TEACHER,COMMENT WHERE tname='"+p['Teacher']+"' AND TEACHER.tid=COMMENT.tid;")
        co = cursor.fetchone()
        if co != None:
            msg += '推薦指數: '+str(co[0]).strip()+'\n'
        else:
            msg += '沒有資料，請重新輸入'+'\n'

        
    elif p['Action'] == '熱門程度': #老師-課程 or 課程
        if p['Teacher'] != '':
            #教授名字 課程名稱 熱門程度
            cursor.execute("SELECT popularity FROM Teacher,Teach,Course WHERE tname='"+p['Teacher']+"' AND cname='"+p['Course']+"' AND Teach.tid=Teacher.tid AND Teach.cid=Course.cid;")
            hot = cursor.fetchone()
            if hot != None:
                msg += '熱門程度: '+str(hot[0]).strip() +'%\n'
        else:
            #課程名稱 熱門程度
            cursor.execute("SELECT round(avg(popularity)) FROM TEACH,COURSE WHERE cname='"+p['Course']+"' AND TEACH.cid=COURSE.cid;")
            co = cursor.fetchone()
            if co != None:
                msg += '熱門程度: '+str(co[0]).strip()+'\n'
            else:
                msg += '沒有資料，請重新輸入'+'\n'
            
    if msg == '': 
        msg = '請輸入正確課程~'
    
    #rows = cursor.fetchone()
    print(msg.strip())
    return msg.strip()

from flask import Flask, request, make_response, jsonify
app = Flask(__name__)

@app.route("/")
def verify():
    return "FCU Course", 200

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print(req)
    res = {"fulfillmentText": get(req)}
        
    return make_response(jsonify(res))
	
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

conn.close()
    