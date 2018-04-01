#-*- coding:utf-8 -*-
'''
Updated on Mar 29 2018

@update by: LT
'''


import unittest
from Provide import Configuration
from Provide.post_params import Post_Params

class Test_getAnnounce(unittest.TestCase):
    '''测试获取历史公告接口/announcement/GetAnnouncement'''


    def setUp(self):
        print('test start')
        self.url = Configuration.HostUrl + "/interface/announcement/GetAnnouncement"
        self.v = Configuration.version

    def tearDown(self):
        print('test end')

    def test_getAnnouncement(self):
        '''获取正确的planid公告'''
        self.params = {
                        "fkPlan": Configuration.Plan_Id
                    }
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        self.assertEqual(0,returnObj['code'],'返回状态码不正确')
        self.assertEqual("success",returnObj['message'])
        self.assertIsNotNone(returnObj['result'])
        s.close()
        
    def test_getAnnouncementWithReturnError(self):
        '''传入不正确planid,也能正常返回值'''
        self.params = {
            "fkPlan": -1
        }
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        self.assertEqual(0, returnObj['code'], '返回状态码不正确')
        self.assertEqual("success",returnObj['message'])
        self.assertEqual(0,len(returnObj['result']))
        s.close()

    def test_getAnnouncementWithoutfkplan(self):
        '''不传入fkplan'''

        self.params = {}
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        self.assertEqual(1002, returnObj['code'], '返回状态码不正确')
        self.assertEqual("access key valid failed", returnObj['message'])
        self.assertEqual('请求key验证失败', returnObj['errMsg'])
        s.close()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()