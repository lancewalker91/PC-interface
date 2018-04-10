#-*- coding:utf-8 -*-
'''
Updated on Apr 09 2018

@update by: LT
'''
import unittest
from Provide import Configuration
import pymysql
import pymysql.cursors
from Provide.post_params import Post_Params

class Test_redPacket_getPlanPoint(unittest.TestCase):
    '''测试获取积分接口/redPacket/getPlanPoint'''
    def setUp(self):
        print('test start')
        self.url = Configuration.HostUrl + "/interface/redPacket/getPlanPoint"
        self.v = Configuration.version
        db_url = {"host": Configuration.db_host, "user": Configuration.db_user, "passwd": Configuration.db_password, "db": "db_course",
                  "charset": "utf8", "cursorclass": pymysql.cursors.DictCursor}
        self.connect = pymysql.connect(**db_url)
        self.connect.autocommit(True)
        self.cursor = self.connect.cursor()

    def tearDown(self):
        print('test end')
        self.cursor.close()
        self.connect.close()
        pass

    def test_redPacket_getPlanPoint(self):
        '''测试获取接口获取积分与数据库是否一致'''
        self.params = {
            "planId": 6899
        }

        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        s.close()
        self.assertEqual(0, returnObj['code'], "返回态码错误")
        self.assertEqual("success", returnObj['message'])
        sql1 = "SELECT POINT FROM t_course_plan WHERE pk_plan = {}".format(Configuration.Plan_Id)
        self.cursor.execute(sql1)
        result = self.cursor.fetchone()
        #print(result)
        self.assertEqual(returnObj['result']['point'],str(result['POINT']))
        #更新积分为1000分
        sql2 = "UPDATE t_course_plan SET POINT = 1000 WHERE pk_plan = {}".format(Configuration.Plan_Id)
        self.cursor.execute(sql2)

if __name__ == "__main__":
    unittest.main()