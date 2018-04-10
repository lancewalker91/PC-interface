#-*- coding:utf-8 -*-
'''
Updated on Mar 29 2018

@update by: LT
'''
import unittest
from Provide import Configuration
from Provide.post_params import Post_Params

class Test_AssiantTeacherGroups(unittest.TestCase):
    '''获取分组详情接口测试/group/classlist'''
    def setUp(self):
        print('test start')
        self.url = Configuration.HostUrl +"/interface/group/classlist"
        self.v = Configuration.version

    def test_1getGroupList(self):
        '''测试获取分组详情'''
        self.params = {"classId": Configuration.class_id}
        returnObj,s = Post_Params(self.v,self.url,self.params).psot_params_returnObj()
        self.assertEqual(returnObj['result'][2]['groupName'],'第一学神组')
        self.assertEqual(0, returnObj['code'], '返回验证码错误')
        self.assertEqual('success',returnObj['message'])
        s.close()

    def test_2getGroupList_withNotExistClassID(self):
        '''传入不存在classID'''
        self.params = {"classId": -1}
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        self.assertEqual(0, returnObj['code'], '返回验证码错误')
        self.assertEqual('success', returnObj['message'])
        for i in returnObj['result']:
            self.assertNotIn('未分组',i['groupName'])
        s.close()


    def test_3getGroupList_withnotClassId(self):
        '''不传入classID'''
        self.params =  {"classId": ''}
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        self.assertEqual(0, returnObj['code'], '返回验证码错误')
        self.assertEqual('success', returnObj['message'])
        for i in returnObj['result']:
            self.assertNotIn('未分组', i['groupName'])
        s.close()


    def tearDown(self):
        print('test end')
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()