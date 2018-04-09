# -*- coding:utf-8 -*-
'''
Updated on Mar 29 2018

@update by: LT
'''

import unittest
from Provide import Configuration, Confirm
from Provide.post_params import Post_Params


class Test_user_getqrcode(unittest.TestCase):
    '''测试获取二维码接口'''

    def setUp(self):
        print('test start')
        self.url = Configuration.HostUrl + "/interface/user/getqrcode"
        self.v = Configuration.version

    def tearDown(self):
        print('test end')
        pass

    def test_user_getqrcode1(self):
        """获取李涛的二维码"""
        self.params = {"userId":42}
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        s.close()
        self.assertEqual(0, returnObj['code'], "返回态码错误")
        self.assertEqual("success", returnObj['message'])
        self.assertEqual('http://testf.gn100.com/5,04594ba2cc1521',returnObj['result']['qrurl'])

    def test_user_getqrcode2(self):
        """获取李涛的二维码"""
        self.params = {"userId":44}
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        s.close()
        self.assertEqual(0, returnObj['code'], "返回态码错误")
        self.assertEqual("success", returnObj['message'])
        self.assertEqual('http://testf.gn100.com/1,045951e3485bd1',returnObj['result']['qrurl'])

    def test_user_getqrcode3(self):
        """获取李涛的二维码"""
        self.params = {"userId":2000106}
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        s.close()
        self.assertEqual(0, returnObj['code'], "返回态码错误")
        self.assertEqual("success", returnObj['message'])
        self.assertEqual('http://testf.gn100.com/2,045d331c5157da',returnObj['result']['qrurl'])


if __name__ == '__main__':
    unittest.main()