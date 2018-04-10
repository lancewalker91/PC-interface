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

class Test_redPacket_getRedPacketReceiveList(unittest.TestCase):
    '''测试小红包记录列表接口/redPacket/getRedPacketReceiveList '''

    def setUp(self):
        print('test start')
        self.url = Configuration.HostUrl + "/interface/redPacket/getRedPacketReceiveList"
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

    def test_redPacket_getRedPacketList1(self):
        '''获取小红包记录(id:855)详情与数据库是否一致'''
        self.params = {
            "redPacketId": 855
        }
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        s.close()
        self.assertEqual(0, returnObj['code'], "返回态码错误")
        self.assertEqual("success", returnObj['message'])
        sql = "SELECT fk_user,VALUE FROM t_red_packet_receive WHERE  fk_red_packet = 855"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        #print(result)
        flag = False
        for i in returnObj['result']['data']:
            for k in result:
                if int(i['fk_user'])==k['fk_user'] and int(i['value']) == k['VALUE']:
                    #print('trudasda')
                    flag = True
        self.assertTrue(flag)

    def test_redPacket_getRedPacketList2(self):
        '''获取小红包记录(id:856)详情与数据库是否一致'''
        self.params = {
            "redPacketId": 856
        }
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        s.close()
        self.assertEqual(0, returnObj['code'], "返回态码错误")
        self.assertEqual("success", returnObj['message'])
        sql = "SELECT fk_user,VALUE FROM t_red_packet_receive WHERE  fk_red_packet = 856"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        #print(result)
        flag = False
        for i in returnObj['result']['data']:
            for k in result:
                if int(i['fk_user']) == k['fk_user'] and int(i['value']) == k['VALUE']:
                    #print('trudasda')
                    flag = True
        self.assertTrue(flag)

if __name__ == '__main__':
    unittest.main()