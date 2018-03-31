#-*- coding:utf-8 -*-
'''
Updated on Mar 29 2018

@update by: LT
'''
import unittest
from Provide import Configuration
from Provide.post_params import Post_Params

class Test(unittest.TestCase):
    '''测试学生分组接口详情/group/ClassStudents'''

    def setUp(self):
        print('test start')
        self.url = Configuration.HostUrl + "/interface/group/ClassStudents"
        self.v = Configuration.version

    def tearDown(self):
        print('test end')
        
    
    def test_getGroupStudent1_notInGroup(self):
        '''获取所有学生分组列表详情'''
        self.params = {"classId":Configuration.class_id}
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        self.assertEqual(returnObj['result'][1]['name'],'何涛')
        self.assertEqual(0, returnObj['code'], '返回验证码错误')
        self.assertEqual('success', returnObj['message'])
        s.close()


    def test_getGroupStudent2_withnotClassId(self):
        '''不传入ClassID'''
        self.params = {}
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        self.assertEqual(returnObj['errMsg'], '请求key验证失败')
        self.assertEqual(1002, returnObj['code'], '返回验证码错误')
        self.assertEqual('access key valid failed', returnObj['message'])
        s.close()

    def test_getGroupStudent3_withNotExistClassID(self):
        '''传入不存在的ClassId'''
        self.params = {"classId": -1,}
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        self.assertEqual(returnObj['errMsg'], '获取数据失败')
        self.assertEqual(3002, returnObj['code'], '返回验证码错误')
        self.assertEqual('get data failed', returnObj['message'])
        s.close()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()