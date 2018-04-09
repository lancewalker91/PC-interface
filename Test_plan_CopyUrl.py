# -*- coding:utf-8 -*-
'''
Updated on Mar 29 2018

@update by: LT
'''

import unittest
from Provide import Configuration, Confirm
from Provide.post_params import Post_Params


class Test_plan_CopyUrl(unittest.TestCase):
    '''测试复制当前直播url接口'''

    def setUp(self):
        print('test start')
        self.url = Configuration.HostUrl + "/interface/plan/copyUrl"
        self.v = Configuration.version

    def tearDown(self):
        print('test end')
        pass

    def test_plan_copyurl(self):
        """获取当前直播url"""
        self.params = {"planId":Configuration.Plan_Id}
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        s.close()
        self.assertEqual(0, returnObj['code'], "返回态码错误")
        self.assertEqual("success", returnObj['message'])
        self.assertEqual('http://test.gn100.com',returnObj['result']['url'])

if __name__ == '__main__':
    unittest.main()