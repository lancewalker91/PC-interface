# -*- coding:utf-8 -*-
'''
Updated on Mar 29 2018

@update by: LT
'''

import unittest
from Provide import Configuration
from Provide.post_params import Post_Params

class Test_main_qrauthorize(unittest.TestCase):
    '''测试app扫码授权登录接口/main/qrauthorize '''

    def setUp(self):
        print('test start')
        self.url = Configuration.HostUrl + "/interface/main/qrauthorize"
        self.v = Configuration.version

    def tearDown(self):
        print('test end')
        pass
    def test_main_qrauthorize1(self):
        '''同意李涛登录'''
        self.params = {
            "qruuid": "6edb8125638f3c4", "type": 1, "uid": "42"
        }
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        s.close()
        self.assertEqual(0, returnObj['code'], "返回态码错误")
        self.assertEqual("success", returnObj['message'])
        self.assertEqual(returnObj['errMsg'], '操作成功')

    def test_main_qrauthorize2(self):
        '''拒绝李涛登录'''
        self.params = {
            "qruuid": "6edb8125638f3c4", "type": 2, "uid": "42"
        }
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        s.close()
        self.assertEqual(0, returnObj['code'], "返回态码错误")
        self.assertEqual("success", returnObj['message'])
        self.assertEqual(returnObj['errMsg'], '操作成功')

    def test_main_qrauthorize3(self):
        '''同意litao登录'''
        self.params = {
            "qruuid": "4325620a1eeb455", "type": 1, "uid": "42"
        }
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        s.close()
        self.assertEqual(0, returnObj['code'], "返回态码错误")
        self.assertEqual("success", returnObj['message'])
        self.assertEqual(returnObj['errMsg'], '操作成功')

    def test_main_qrauthorize4(self):
        '''拒绝litao登录'''
        self.params = {
            "qruuid": "4325620a1eeb455", "type": 1, "uid": "42"
        }
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        s.close()
        self.assertEqual(0, returnObj['code'], "返回态码错误")
        self.assertEqual("success", returnObj['message'])
        self.assertEqual(returnObj['errMsg'], '操作成功')

if __name__ == '__main__':
    unittest.main()

