#-*- coding:utf-8 -*-
'''
Updated on Mar 29 2018

@update by: LT
'''
import unittest
from Provide import Confirm,Configuration
import pymysql
from pymysql import cursors
from Provide.post_params import Post_Params

class Test_CoursePlanOfTeacher(unittest.TestCase):
    '''测试课程排课列表详情/teacher/plans'''
    def setUp(self):
        print('test start')
        self.url = Configuration.HostUrl +"/interface/teacher/plans"
        self.v = Configuration.version
    def tearDown(self):
        print('test end')


    def test_1getCoursePlans_onlyTeacherId(self):
        '''只传入班主任Id'''
        self.params = {
                 "classId":Configuration.class_id,
                "teacherId":Configuration.teacherId,
                "courseId":Configuration.course_id
            }
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        s.close()
        self.assertEqual(0, returnObj['code'], "返回态码错误")
        self.assertEqual("success", returnObj['message'])
        #验证返回值排课数据结构
        ExpectKeys = ['planId','sectionDesc','sectionName','teacherId','teacherName','adminId','adminName','courseType','startTime','status','totalTime']
        self.assertTrue(Confirm.VerifyDataStucture(ExpectKeys, returnObj['result']['data'][0].keys()), "返回排课对象属性字段值不对")
        OnePlanInfo = {
            'planId': 6440,
            'sectionDesc': '1',
            'sectionName': '第1课时',
            'teacherId': 42,
            'teacherName': '李涛',
            'adminId': 42,
            'adminName': '李涛',
            'courseType': 1,
            'startTime': '2017-12-01 11:00:00',
            'status': 3,
            'totalTime': 240
            }
        
        self.assertTrue(Confirm.VerifyDictEqual(OnePlanInfo,returnObj['result']['data'][0]),"排课信息不匹配  预期:{},返回值:{}".format(OnePlanInfo,returnObj['result']['data'][0]))
        
    def test_2getCoursePlansWithlessTeacherId(self):
        '''不传入班主任Id,只传讲师id'''
        self.params = {
                 "classId":Configuration.class_id,
                "lecturerId":Configuration.teacherId,
                "courseId":Configuration.course_id
            }
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        s.close()
        self.assertEqual(0, returnObj['code'], "返回态码错误")
        self.assertEqual("success", returnObj['message'])
        self.assertIsNotNone(returnObj['result']['data'],"返回排课列表为空")
    
    def test_3getCoursePlanWithAllTeacher(self):
        '''传入班主任Id,讲师Id'''
        
        self.params = {
                "classId":Configuration.class_id,
                "lecturerId":Configuration.teacherId,
                "courseId":Configuration.course_id,
                "teacherId":0,
            }
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        s.close()
        self.assertEqual(0, returnObj['code'], "返回态码错误")
        self.assertEqual("success", returnObj['message'])
        self.assertIsNotNone(returnObj['result']['data'], "返回排课列表为空")

                
    def test_4getCoursePlansWithErrorClassIdOrCourseId(self):
        '''传入错误的classid'''
        self.params = {
                 "classId":-1,
                "lecturerId":Configuration.teacherId,
                "courseId":Configuration.course_id,
                "teacherId":0,
            }
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        s.close()
        self.assertEqual(3002, returnObj['code'], "返回态码错误")
        self.assertEqual("get data failed", returnObj['message'])
        self.assertEqual(returnObj['errMsg'], "获取数据失败")
        
    def test_5getCoursePlanWithErrorTeacherId(self):
        '''传入错误的courseid'''
        self.params = {
            "classId":Configuration.class_id,
            "lecturerId": Configuration.teacherId,
            "courseId": -1,
            "teacherId": 0,
            }
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        s.close()
        self.assertEqual(3002, returnObj['code'], "返回态码错误")
        self.assertEqual("get data failed", returnObj['message'])
        self.assertEqual(returnObj['errMsg'], "获取数据失败")

        
    def test_6getCoursePlan_WithOnlyMandatoryArgument(self):
        '''只传入courseid 和classid--(必传参数）'''
        self.params = {
                 "classId":Configuration.class_id,
                "courseId":Configuration.course_id
            }
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        s.close()
        self.assertEqual(0, returnObj['code'], "返回态码错误")
        self.assertEqual("success", returnObj['message'])
        self.assertIsNotNone(returnObj['result']['data'], "返回排课列表为空")
        
if __name__ == "__main__":
    unittest.main()