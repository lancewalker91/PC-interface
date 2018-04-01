#-*- coding:utf-8 -*-
'''
Updated on Mar 29 2018

@update by: LT
'''
import unittest
from Provide import Configuration
from Provide.TestProvide import *
import time
import requests
import json

class Test_login(unittest.TestCase):
    '''测试登录接口/login'''
    def setUp(self):
        print('test start')
        currenttime = int(time.time())
        self.params = {}
        self.params['u'] = 'p'
        self.params['v'] = Configuration.version
        self.params['time'] = currenttime
        self.s = requests.session()

    def tearDown(self):
        self.s.close()
        print('test end')

    def test_1login(self):
        '''测试正确账号密码登录'''
        self.params['params'] = {
            "name": Configuration.mobile,
            "password": Configuration.password,
            "streamInfo": "yes"
        }
        self.params['key'] = generateKey(self.params['time'],self.params['params'])
        loginUrl = Configuration.HostUrl + "/interface/login"
        print("Url: {} \nParameter:{}".format(loginUrl,
                                              json.dumps(self.params, separators=(',', ':'), ensure_ascii=False)))
        response = self.s.post(loginUrl, data=json.dumps(self.params, separators=(',', ':')))
        response.encoding = "utf-8"
        returnObj = json.loads(response.text)
        print(returnObj)
        self.assertEqual(returnObj['result']['real_name'], '李涛')
        self.assertEqual(0, returnObj['code'], '返回验证码错误')
        self.assertEqual('success', returnObj['message'])

    def test_2login(self):
        '''测试正确账号错误密码登录'''
        self.params['params'] = {
            "name": Configuration.mobile,
            "password": 110243,
            "streamInfo": "yes"
        }
        self.params['key'] = generateKey(self.params['time'], self.params['params'])
        loginUrl = Configuration.HostUrl + "/interface/login"
        print("Url: {} \nParameter:{}".format(loginUrl,
                                              json.dumps(self.params, separators=(',', ':'), ensure_ascii=False)))
        response = self.s.post(loginUrl, data=json.dumps(self.params, separators=(',', ':')))
        response.encoding = "utf-8"
        returnObj = json.loads(response.text)
        print(returnObj)
        self.assertEqual(returnObj['errMsg'], '密码错误，请重新输入')
        self.assertEqual(1038, returnObj['code'], '返回验证码错误')
        self.assertEqual('Wrong password, please enter again', returnObj['message'])

    def test_3login(self):
        '''测试正错误账号，正确密码'''
        self.params['params'] = {
            "name": 18671595783,
            "password": Configuration.password,
            "streamInfo": "yes"
        }
        self.params['key'] = generateKey(self.params['time'], self.params['params'])
        loginUrl = Configuration.HostUrl + "/interface/login"
        print("Url: {} \nParameter:{}".format(loginUrl,
                                              json.dumps(self.params, separators=(',', ':'), ensure_ascii=False)))
        response = self.s.post(loginUrl, data=json.dumps(self.params, separators=(',', ':')))
        response.encoding = "utf-8"
        returnObj = json.loads(response.text)
        print(returnObj)
        self.assertEqual(returnObj['errMsg'], '密码错误，请重新输入')
        self.assertEqual(1038, returnObj['code'], '返回验证码错误')
        self.assertEqual('Wrong password, please enter again', returnObj['message'])

    def test_4login(self):
        '''测试账号密码都为空'''
        self.params['params'] = {
            "name": "",
            "password": "",
            "streamInfo": "yes"
        }
        self.params['key'] = generateKey(self.params['time'], self.params['params'])
        loginUrl = Configuration.HostUrl + "/interface/login"
        print("Url: {} \nParameter:{}".format(loginUrl,
                                              json.dumps(self.params, separators=(',', ':'), ensure_ascii=False)))
        response = self.s.post(loginUrl, data=json.dumps(self.params, separators=(',', ':')))
        response.encoding = "utf-8"
        returnObj = json.loads(response.text)
        print(returnObj)
        self.assertEqual(returnObj['errMsg'], '请求参数为空')
        self.assertEqual(1000, returnObj['code'], '返回验证码错误')
        self.assertEqual('request param empty', returnObj['message'])


if __name__ == '__main__':
    unittest.main()

