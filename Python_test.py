# -*- coding:utf-8 -*-
'''
Updated on Mar 29 2018

@update by: LT
'''

'''import requests
import json

s = requests.session()
response = s.post('http://test.gn100.com/interface/announcement/GetAnnouncement', {"u":"p","v":"1.16.1","time":1523281095,"token":"182451610c5f74e6953ce79b7115ed5e","params":{},"key":"fd2d163e2b03ed1ba80e26f2f4952866"})
response.encoding = "utf-8"
returnObj = json.loads(response.text)
print(returnObj)'''

'''import unittest
from Provide import Configuration
from Provide.post_params import Post_Params


class Test(unittest.TestCase):
    测试学生分组接口详情/group/ClassStudents

    def setUp(self):
        print('test start')
        self.url = Configuration.HostUrl + "/interface/group/ClassStudents"
        self.v = Configuration.version

    def tearDown(self):
        print('test end')



    def test_getGroupStudent2_withnotClassId(self):
        不传入ClassID
        self.params = {}
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        self.assertEqual(returnObj['errMsg'], '请求key验证失败')
        self.assertEqual(1002, returnObj['code'], '返回验证码错误')
        self.assertEqual('access key valid failed', returnObj['message'])
        s.close()



if __name__ == "__main__":
    unittest.main()'''

#-*- coding:utf-8 -*-
'''
Updated on Mar 29 2018

@update by: LT
'''

from Provide import Configuration
import time,requests,json
from Provide import TestProvide

class Post_Params:
    def __init__(self,v,url,params):
        self.v = v
        self.url = url
        self.params = params
        self.s = requests.session()
    def psot_params_returnObj(self):
        s = TestProvide.login(self.s,Configuration.mobile,Configuration.password)
        token = s.cookies.get('token_test')
        params = {}
        timeStamp = int(time.time())
        params['u'] = 'p'
        params['v'] = self.v
        params['time'] = timeStamp
        params['token'] = token
        params['params'] = self.params
        params['key'] = TestProvide.generateKey(timeStamp, params['params'])
        print("Url: {} \nParameter:{}".format(self.url,
                                               json.dumps(params, separators=(',', ':'), ensure_ascii=False)))
        response = self.s.post(self.url,json.dumps(params))
        #response = self.s.post(self.url, data=json.dumps(params, separators=(',', ':')))
        response.encoding = "utf-8"
        #print(response.text)
        returnObj = json.loads(response.text)
        print('result:{}'.format(returnObj))
        #return returnObj,s

url = Configuration.HostUrl + "/interface/group/ClassStudents"
v = Configuration.version
params = {}
Post_Params(v, url, params).psot_params_returnObj()

