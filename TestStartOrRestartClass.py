#-*- coding:utf-8 -*-
'''
Updated on Mar 29 2018

@update by: LT
'''

import unittest
from Provide import TestProvide,Confirm,DB
from Provide import Configuration
from Provide.post_params import Post_Params

class Test_startClass(unittest.TestCase):
    '''测试直播上课/下课接口(只能上课的时候测试，无法模拟发送websocket）'''

    def setUp(self):
        print('test start')
        self.url = Configuration.HostUrl +"/interface/plan/StartPlay"
        self.v = Configuration.version

    def test_1startClassNormal(self):
        '''测试直播课堂--开始上课'''
        self.params = {
                        "planId" : Configuration.Plan_Id
                    }
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        s.close()
        self.assertEqual(2003,returnObj['code'],"返回值状态码错误")
        #self.assertEqual("success", returnObj['message'])

        #从数据表t_course_plan验证排课状态
        connect = DB.Generate_DB_Connect()
        cursor = connect.cursor()
        sql = "SELECT status FROM `t_course_plan` WHERE pk_plan={}".format(Configuration.Plan_Id)
        result = DB.fetchone_fromDB(cursor, sql)
        self.assertEqual(3,result['status'],"开始上课后，排课状态不是直播中")
    
    def test_2getPlayStream(self):
        '''测试获取音视频流信息'''
        self.url = Configuration.HostUrl + "/interface/play/stream"
        self.params ={
                         "planId":Configuration.Plan_Id
                            }

        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        s.close()
        self.assertEqual(1011, returnObj['code'], "返回值状态吗错误")
        #self.assertEqual("success", returnObj['message'])
        #self.assertEqual('rtmp://121.42.232.97:1936/chat', returnObj['result']['url'])
        
        
    def test_3restartClassNormal(self):
        '''测试直播课堂--重新上课'''
        self.params = {
                        "planId" : Configuration.Plan_Id,
                        "cleanFile": "Yes"
                    }
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        s.close()
        self.assertEqual(2003,returnObj['code'],"返回值状态码错误")
        #self.assertEqual("success", returnObj['message'])

        #从数据表t_course_plan验证排课状态
        connect = DB.Generate_DB_Connect()
        cursor = connect.cursor()
        sql = "SELECT status FROM `t_course_plan` WHERE pk_plan={}".format(Configuration.Plan_Id)
        result = DB.fetchone_fromDB(cursor, sql)
        connect.close()
        self.assertEqual(3,result['status'],"开始上课后，排课状态不是直播中")
        
    def test_4stopClassNormal(self):
        '''测试直播课堂教师下课'''
        self.url = Configuration.HostUrl +"/interface/plan/ClosePlay"
        self.params = {
                        "planId" : Configuration.Plan_Id,
                        "uid":Configuration.teacherId
                    }
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        s.close()
        self.assertEqual(0, returnObj['code'], "返回值状态吗错误")
        self.assertEqual("success", returnObj['message'])
        
        #从数据表表验证plan的status状态值是否变为3
        connect = DB.Generate_DB_Connect()
        cursor = connect.cursor()
        sql = "SELECT status FROM `t_course_plan` WHERE pk_plan={}".format(Configuration.Plan_Id)
        result = DB.fetchone_fromDB(cursor, sql)
        connect.close()
        self.assertEqual(3,result['status'],"开始上课后下课，排课状态不是下课中")

    
    def tearDown(self):
        print('test end')

    
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

    