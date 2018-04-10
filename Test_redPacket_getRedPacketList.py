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

class Test_redPacket_getRedPacketList(unittest.TestCase):
    '''测试大红包记录接口/redPacket/getRedPacketList '''

    def setUp(self):
        print('test start')
        self.url = Configuration.HostUrl + "/interface/redPacket/getRedPacketList"
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

    def test_redPacket_getRedPacketList(self):
        '''获取大红包记录详情与数据库是否一致'''
        self.params = {
            "objectId":6899, #红包范围对应Id 1:排课Id,2:用户Id,3:课程Id（必传）
            "objectType":1, #红包范围 1:排课，2：个人，3：课程（必传）
            "uId":42 #上课老师Id（必传）
        }
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        s.close()
        self.assertEqual(0, returnObj['code'], "返回态码错误")
        self.assertEqual("success", returnObj['message'])
        for i in returnObj['result']['data']:
            sql = "SELECT VALUE FROM t_red_packet WHERE pk_red_packet = {}".format(i['pk_red_packet'])
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            #print(result)
            self.assertEqual(result['VALUE'],int(i['value']))

if __name__ == '__main__':
    unittest.main()