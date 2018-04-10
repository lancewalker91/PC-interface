# -*- coding:utf-8 -*-
'''
Updated on Mar 29 2018

@update by: LT
'''

import unittest
from Provide import Configuration
from Provide.post_params import Post_Params
import pymysql
import pymysql.cursors

class Test_redPacket_addRedPacket(unittest.TestCase):
    '''测试老师发送红包接口/redPacket/addRedPacket &撤销红包接口/redPacket/cancelRedPacket'''

    def setUp(self):
        print('test start')
        self.url = Configuration.HostUrl + "/interface/redPacket/addRedPacket"
        self.v = Configuration.version
        db_url = {"host": Configuration.db_host, "user": Configuration.db_user, "passwd": Configuration.db_password,
                  "db": "db_user",
                  "charset": "utf8", "cursorclass": pymysql.cursors.DictCursor}
        self.connect = pymysql.connect(**db_url)
        self.connect.autocommit(True)
        self.cursor = self.connect.cursor()

    def tearDown(self):
        print('test end')
        self.cursor.close()
        self.connect.close()
        pass

    def test_redPacket_addRedPacket1(self):
        '''发送红包1个积分100分,然后撤销红包'''
        self.params = {
            "number":1,"objectId":6899,"objectType":1,"type":1,"uId":42,"value":100
        }
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        s.close()
        self.assertEqual(0, returnObj['code'], "返回态码错误")
        self.assertEqual("success", returnObj['message'])
        sql = "SELECT VALUE FROM t_red_packet WHERE  pk_red_packet = {}".format(returnObj['result']['redPacketId'])
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        #print(result)
        self.assertEqual(result['VALUE'],100)

        '''撤回已经发送的红包'''
        self.url = Configuration.HostUrl + "/interface/redPacket/cancelRedPacket"
        self.params = {
             "objectId": 6899, "objectType": 1, "redPacketId": returnObj['result']['redPacketId'], "type": 1, "uId": 42
        }
        Obj, t = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        t.close()
        self.assertEqual(0, Obj['code'], "返回态码错误")
        self.assertEqual("success", Obj['message'])
        sql = "SELECT STATUS FROM t_red_packet WHERE  pk_red_packet = {}".format(returnObj['result']['redPacketId'])
        self.cursor.execute(sql)
        resource = self.cursor.fetchone()
        self.assertEqual(resource['STATUS'],Obj['result'])


    def test_redPacket_addRedPacket2(self):
        '''发送红包100个积分100分，然后撤销红包'''
        self.params = {
            "number":100,"objectId":6899,"objectType":1,"type":1,"uId":42,"value":100
        }
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        s.close()
        self.assertEqual(0, returnObj['code'], "返回态码错误")
        self.assertEqual("success", returnObj['message'])
        sql = "SELECT VALUE FROM t_red_packet WHERE  pk_red_packet = {}".format(returnObj['result']['redPacketId'])
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        #print(result)
        self.assertEqual(result['VALUE'],100)

        '''撤回已经发送的红包'''
        self.url = Configuration.HostUrl + "/interface/redPacket/cancelRedPacket"
        self.params = {
            "objectId": 6899, "objectType": 1, "redPacketId": returnObj['result']['redPacketId'], "type": 1, "uId": 42
        }
        Obj, t = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        t.close()
        self.assertEqual(0, Obj['code'], "返回态码错误")
        self.assertEqual("success", Obj['message'])
        sql = "SELECT STATUS FROM t_red_packet WHERE  pk_red_packet = {}".format(returnObj['result']['redPacketId'])
        self.cursor.execute(sql)
        resource = self.cursor.fetchone()
        self.assertEqual(resource['STATUS'], Obj['result'])

    def test_redPacket_addRedPacket3(self):
        '''发送红包101个积分100分'''
        self.params = {
            "number":101,"objectId":6899,"objectType":1,"type":1,"uId":42,"value":100
        }
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        s.close()
        self.assertEqual(2078, returnObj['code'], "返回态码错误")
        self.assertEqual("system error", returnObj['message'])
        self.assertEqual(returnObj['errMsg'],'红包数量大于红包金额')

    def test_redPacket_addRedPacket4(self):
        '''发送红包个数为空积分100分'''
        self.params = {
            "number":'',"objectId":6899,"objectType":1,"type":1,"uId":42,"value":100
        }
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        s.close()
        self.assertEqual(1001, returnObj['code'], "返回态码错误")
        self.assertEqual("missed required param", returnObj['message'])
        self.assertEqual(returnObj['errMsg'],'缺少必传参数')

    def test_redPacket_addRedPacket5(self):
        '''发送红包1个积分数为空'''
        self.params = {
            "number":1,"objectId":6899,"objectType":1,"type":1,"uId":42,"value":''
        }
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        s.close()
        self.assertEqual(1001, returnObj['code'], "返回态码错误")
        self.assertEqual("missed required param", returnObj['message'])
        self.assertEqual(returnObj['errMsg'],'缺少必传参数')

if __name__ == '__main__':
    unittest.main()