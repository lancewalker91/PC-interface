#-*- coding:utf-8 -*-
'''
Updated on Mar 29 2018

@update by: LT
'''
import unittest
from Provide import Configuration
import pymysql
import pymysql.cursors
import os
from Provide.post_params import Post_Params

class Test_Announcement(unittest.TestCase):
    '''测试发布公告接口/announcement/Announcement'''
    
    @classmethod
    def setUpClass(cls):
        print('test class start')
        db_url = {"host":Configuration.db_host,"user":"michael","passwd":"michael","db":"db_course","charset":"utf8","cursorclass":pymysql.cursors.DictCursor}
        cls.connect = pymysql.connect(**db_url)
        cls.connect.autocommit(True)
        cls.cursor = cls.connect.cursor()
    
    def setUp(self):
        print('test case start')
        self.url = Configuration.HostUrl +"/interface/announcement/Announcement"
        self.v = Configuration.version

    def tearDown(self):
        print('test case end')
        
    def test_Announcement_Add(self):
        """测试发布公告"""

        content = "大家好，很高兴见到大家，我是LT老师！"
        self.params = {
                     "status": "1",      
                     "fkPlan": Configuration.Plan_Id,
                     "content": content
                }
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        self.assertEqual(0,returnObj['code'] ,"返回态码错误")
        self.assertEqual("success", returnObj['message'])
        #数据库验证公告已插入
        sql = "SELECT fk_plan,content FROM `t_announcement` WHERE fk_plan={} and status=1".format(Configuration.Plan_Id)
        cursor = self.cursor
        cursor.execute(sql)
        result = cursor.fetchone()
        self.assertEqual(content,result['content'],"课堂公告未插入")
        s.close()

    def test_Announcement_Update(self):
        '''测试修改公告'''
        content = "大家好，下面开始上课了！"
        self.params = {
                     "status": "1",      
                     "fkPlan": Configuration.Plan_Id,
                     "content": content
                }

        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        self.assertEqual(0,returnObj['code'] ,"返回状态码错误")
        self.assertEqual("success", returnObj['message'])
        #数据库验证公告已更新
        sql = "SELECT fk_plan,content FROM `t_announcement` WHERE fk_plan={} and status=1".format(Configuration.Plan_Id)
        cursor = self.cursor
        cursor.execute(sql)
        result = cursor.fetchone()
        self.assertEqual(content, result['content'], "课堂公告未修改")
        s.close()
         
    def test_Announcement_Update_SameContent(self):
        '''测试修改公告，不更新文本'''
        sql = "select fk_plan,content from t_announcement where fk_plan={} and status=1".format(Configuration.Plan_Id)
        cursor = self.cursor
        cursor.execute(sql)
        result = cursor.fetchone()
        content = result['content']
        self.params = {
                     "status": "1",      
                     "fkPlan": Configuration.Plan_Id,
                     "content": content
                }
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        self.assertEqual(0,returnObj['code'])
        self.assertEqual("success",returnObj['message'])
        s.close()
    
    def test_DeleteAnnouncement(self):
        '''测试删除公告'''
        self.params = {
                     "status": "2",      
                     "fkPlan": Configuration.Plan_Id
                }
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        self.assertEqual(0, returnObj['code'], "返回状态码错误")
        self.assertEqual("success", returnObj['message'])
        sql = "select fk_plan,content from `t_announcement` where fk_plan={} and status=-1".format(Configuration.Plan_Id)
        cursor = self.cursor
        cursor.execute(sql)
        result = cursor.fetchone()
        self.assertIsNotNone(result,'数据库不存在已删除的公告')
        s.close()
     
    def test_DeleteAnnouncement_whichIsDeleted(self):
        '''测试删除无公告'''
        self.params = {
                     "status": "2",      
                     "fkPlan": Configuration.Plan_Id
                }
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        self.assertEqual(1,returnObj['code'],'返回状态码不正确')
        self.assertEqual("failure",returnObj['message'])
        s.close()
    
    @classmethod
    def tearDownClass(cls):
        cls.cursor.close()
        cls.connect.close()
        print('test class end')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()