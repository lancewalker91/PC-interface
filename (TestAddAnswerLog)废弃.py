#-*- coding:utf-8 -*-
#!/usr/bin/env python3
'''
Created on 2016年10月13日

@author: lsh
'''
from Provide import TestProvide
import Configuration
import requests,time
import json
import unittest
import pymysql 
from pymysql import cursors

class Test_AddAnswerLog(unittest.TestCase):
    '''测试公布答案'''
    def initsqlConnect(self):
        connect_url = {"host":"121.42.232.104","user":"michael", "passwd":"michael", "db":"db_course", "charset":"utf8", "cursorclass":pymysql.cursors.DictCursor}#查询结果字典显示
        connect = pymysql.connect(**connect_url)
        connect.autocommit(True)
        return connect
    
    def setUp(self):
        self.s = requests.session()
        self.url = Configuration.HostUrl +"/interface/plan/addAnswerLog"
        self.timeStamp = int(time.time())
        self.params = {}
        self.params['u'] ='p'
        self.params['v'] = Configuration.v
        self.params['time'] = self.timeStamp
        
        
    def tearDown(self):
        pass
        
    def publishQuestion(self):
        RequestUrl = Configuration.HostUrl +"/interface/plan/getQuestionId"    
        timeStamp = int(time.time())
        params = {}
        params['u'] ='p'
        params['v'] = Configuration.v
        params['time'] = self.timeStamp
        plan_id = Configuration.Plan_Id
        params['params'] = {"answerRight":"B",
                            "phraseId":4,
                            "planId":plan_id
                        }

        params['key']= TestProvide.generateKey(timeStamp,params['params'])
        response = self.s.post(RequestUrl, data=json.dumps(params,separators=(",",":")))
        response.encoding = "utf-8"
        returnObj = json.loads(response.text)
        return returnObj['result']['questId']
    
    '''def test_AddAnswerLog(self):
        '''公布答案，答题情况记录在数据库'''
        QuestionId = self.publishQuestion()
        self.params['params'] = {
                "data": [
                    {
                        "answer": "B",
                        "answerStatus": 1,
                        "planId": 3559,
                        "questId": QuestionId,
                        "userId": 22519
                    },
                    {
                        "answer": "C",
                        "answerStatus": -1,
                        "planId": 3559,
                        "questId": QuestionId,
                        "userId": 22520
                    },
                    {
                        "answer": "D",
                        "answerStatus": -1,
                        "planId": 3559,
                        "questId": QuestionId,
                        "userId": 22521
                    },
                    {
                        "answer": "A",
                        "answerStatus": -1,
                        "planId": 3559,
                        "questId": QuestionId,
                        "userId": 22522
                    }
                ]
            }

        self.params['key']= TestProvide.generateKey(self.timeStamp,self.params['params'])
        
        #提交请求
        print("Url: {} \n Parameter:{}".format(self.url,json.dumps(self.params,separators=(',',':'),ensure_ascii=False)))
        response = self.s.post(self.url,data=json.dumps(self.params,separators=(',',':')))
        response.encoding= "utf-8"
        returnObj = json.loads(response.text) 
        self.assertEqual(1,returnObj['result']['code'])
        self.assertEqual(1,returnObj['result']['dbFlag'])
        time.sleep(8)
        #验证数据库答题记录已更新
        Flag = True
        inputAnswers = self.params['params']['data']
        sql = "SELECT fk_user,answer,answer_status FROM db_stat.`t_course_plan_phrase_log` WHERE fk_plan_phrase={}".format(QuestionId)
        connect = self.initsqlConnect()
        cursor = connect.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        msg = ""
        for row in rows:
            for answer in inputAnswers:
                if row['fk_user'] == answer["userId"]:
                    if type(row['answer'])  is bytes:
                        row['answer'] = row['answer'].decode('utf-8')
                    if row['answer']!=answer["answer"] or row["answer_status"]!= answer["answerStatus"]:
                        Flag = False
                        msg = "not equal node--sql:{};requestPara:{}".format(row,answer)
                        break
        cursor.close()
        connect.close()
        self.assertTrue(Flag, msg)            
    
    def test_AddAnswerlogWithlessParameter(self):
        '''公布答案--缺少PlanId'''
        self.params['params'] = {
                "data": [
                    {
                        "answer": "B",
                        "answerStatus": 1,
                        "questId": 2621,
                        "userId": 22519
                    },
                    {
                        "answer": "C",
                        "answerStatus": -1,
                        "questId": 2621,
                        "userId": 22520
                    }
                ]         
            }
                                      
        self.params['key']= TestProvide.generateKey(self.timeStamp,self.params['params'])
        #提交请求
        print("Url: {} \n Parameter:{}".format(self.url,json.dumps(self.params,separators=(',',':'),ensure_ascii=False)))
        response = self.s.post(self.url,data=json.dumps(self.params,separators=(',',':'),ensure_ascii=False))
        response.encoding= "utf-8"
        returnObj = json.loads(response.text)
        self.assertEqual(1,returnObj['result']['code'])
        self.assertEqual(1,returnObj['result']['dbFlag'])'''

if __name__ == '__main__':
    #unittest.main()
    publishQuestion()