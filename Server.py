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
            rate = cursor.fetchone()
            cursor.execute("SELECT remark FROM TEACHER,COURSE,COMMENT WHERE tname='"+p['Teacher']+"' AND cname='"+p['Course']+"' AND TEACHER.tid=COMMENT.tid AND COURSE.cid=COMMENT.cid;")
            remark = cursor.fetchall()
            print(rate,remark)
            msg +='教授: '+ p['Teacher'] +'\n'
            if rate[0] != None:
                if rate[0]!=None:
                    msg +='推薦指數: '+str(rate[0]).strip()+'\n'
                if remark != [] :
                    r = random.randint(0,len(remark)-1)
                    print('>>',r)
                    msg +=str(remark[r][0]).strip() +'\n'
                else:
                    msg +='沒有評論'+'\n'                      
            else:
                msg += '沒有資料，請重新輸入'+'\n'
        elif p['Teacher'] != '':
            #教授名字 推薦指數/評論
            cursor.execute("SELECT round(avg(rate),2) FROM TEACHER,COMMENT WHERE tname='"+p['Teacher']+"' AND TEACHER.tid=COMMENT.tid;")
            rate = cursor.fetchone()
            print(rate)
            if rate[0] != None:
                msg +='推薦指數: '+str(rate[0]).strip() +'\n'
            else:
                msg += '沒有資料，請重新輸入'+'\n'
        else:
            msg = '欲搜尋 課程評價 需輸入開課老師'
           
    elif p['Action'] == '課程' and p['Teacher'] != '' and p['Course'] != '':
        #教授名字 課程名稱 課程
        cursor.execute("SELECT credit,score FROM Teacher,Teach,Course WHERE tname='"+p['Teacher']+"' AND cname='"+p['Course']+"' AND Teach.tid=Teacher.tid AND Teach.cid=Course.cid;")
        co = cursor.fetchone()
        print(co)
        if co[0] != None:
            msg += '學分數: '+str(co[0]).strip()+'\n'
            msg += '評分方式: \n'+str(co[1]).strip()+'\n'
        else:
            msg = '沒有資料，請重新輸入\n'
        
            
    elif p['Action'] == '作業考試' and p['Teacher'] != '' and p['Course'] != '':
        #教授名字 課程名稱 作業考試
        cursor.execute("SELECT quizmethod FROM Teacher,Comment,Course WHERE tname='"+p['Teacher']+"' AND cname='"+p['Course']+"' AND Comment.tid=Teacher.tid AND Comment.cid=Course.cid;")
        quiz = cursor.fetchall()
        print(quiz)
        if quiz != []:
            r = random.randint(0,len(quiz)-1)
            print('>>',r)
            msg +=str(quiz[r][0]).strip() +'\n'
        else:
            msg = '沒有資料，請重新輸入\n'
    
    elif p['Action'] == '推薦指數' and p['Teacher'] != '':
        #教授名字 推薦指數
        if p['Course'] != '':
             msg = '欲搜尋 老師推薦指數 不需輸入課程名稱'
        cursor.execute("SELECT round(avg(rate),2) FROM TEACHER,COMMENT WHERE tname='"+p['Teacher']+"' AND TEACHER.tid=COMMENT.tid;")
        rate = cursor.fetchone()
        print(rate)
        if rate[0] != None:
            msg += '推薦指數: '+str(rate[0]).strip()+'\n'
        else:
            msg = '沒有資料，請重新輸入\n'

    elif p['Action'] == '熱門程度': #老師-課程 or 課程
        if p['Teacher'] != '':
            #教授名字 課程名稱 熱門程度
            cursor.execute("SELECT popularity FROM Teacher,Teach,Course WHERE tname='"+p['Teacher']+"' AND cname='"+p['Course']+"' AND Teach.tid=Teacher.tid AND Teach.cid=Course.cid;")
            hot = cursor.fetchone()
            print(hot)
            if hot[0] != None:
                msg += '熱門程度: '+str(hot[0]).strip() +'%\n'
        elif p['Course'] != '':
            #課程名稱 熱門程度
            cursor.execute("SELECT round(avg(popularity)) FROM TEACH,COURSE WHERE cname='"+p['Course']+"' AND TEACH.cid=COURSE.cid;")
            po = cursor.fetchone()
            print(po)
            if po[0] != None:
                msg += '熱門程度: '+str(po[0]).strip()+'\n'
            else:
                msg = '沒有資料，請重新輸入\n'
        else:
            msg = '欲搜尋 課程熱門程度 需輸入課程名稱'
            
    if msg == '': 
        msg = '請輸入正確課程名稱哦~'
    
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
    