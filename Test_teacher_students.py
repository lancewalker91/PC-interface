#-*- coding:utf-8 -*-
'''
Updated on Mar 29 2018

@update by: LT
'''
import unittest
from Provide import Configuration,Confirm
from Provide.post_params import Post_Params


class Test_TeacherOfStudents(unittest.TestCase):
    '''测试课程卡片详情--学生列表/teacher/students'''
    def setUp(self):
        print('test start')
        self.url = Configuration.HostUrl +"/interface/teacher/students"
        self.v = Configuration.version

    def tearDown(self):
        print('test end')
        pass
    
    def test_1getStudentList(self):
        """获取学生列表---通过班主任获取teacherID"""
        self.params = {
                "page":1,
                "length":20,
                "classId": Configuration.class_id,
                "courseId": Configuration.course_id,
                "teacherId":Configuration.teacherId,
              }
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        s.close()
        self.assertEqual(0, returnObj['code'], "返回态码错误")
        self.assertEqual("success", returnObj['message'])
        firstObj=returnObj['result']['data'][0]
        keys = ['startTime','address','sex','userName','mobile','userId']
        Result=Confirm.VerifyDataStucture(keys,firstObj.keys())
        self.assertTrue(Result, "学生属性值返回错误")
    
    def test_2getStudentList_withlecturerId(self):
        """获取学生列表---通过讲师获取"""
        self.params = {
                "page":1,
                "length":20,
                "classId": Configuration.class_id,
                "courseId": Configuration.course_id,
                "lecturerId":Configuration.teacherId,
              }
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        s.close()
        self.assertEqual(0, returnObj['code'], "返回态码错误")
        self.assertEqual("success", returnObj['message'])
        self.assertIsNotNone(returnObj['result']['data'],"返回学生列表为空")
         
    def test_3getStudentWithPaging(self):
        '''学生列表翻页'''
        self.params = {
                "page":2,
                "length":20,
                "classId": Configuration.class_id,
                "courseId":Configuration.course_id,
                "lecturerId":Configuration.teacherId,
              }
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        s.close()
        self.assertEqual(0, returnObj['code'], "返回态码错误")
        self.assertEqual("success", returnObj['message'])
        OneUser= {
            'userId': '1001089', 'userName': '18810001026', 'sex': '', 'mobile': '18810001026', 'address': ' ', 'startTime': '2017年12月01日 15:10'
        }

        if returnObj['code']==0:
            self.assertEqual('2',returnObj['result']['page'])
            Students = returnObj['result']['data']
            Result = False
            for studentObj in Students:
                if OneUser['mobile']==studentObj['mobile'] and OneUser['userName']==studentObj['userName']  and OneUser['userId']==studentObj['userId']:
                    Result = True
                    break
            else:
                raise ("接口返回失败")

            self.assertTrue( Result)

    def test_4getStudentWithErrorClassId(self):
        '''获取学生列表传入错误班级ID'''
        self.params = {
                "page":2,
                "length":20,
                "classId": Configuration.class_id,
                "courseId":-1,
                "lecturerId":Configuration.teacherId,
              }
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        s.close()
        self.assertEqual(3002,returnObj['code'])
        self.assertEqual("get data failed",returnObj['message'])
     
    def test_5getStudentWithErrorCourseId(self):
        '''获取学生列表传入错误课程ID'''
        self.params = {
            "page": 2,
            "length": 20,
            "classId": -1,
            "courseId": Configuration.course_id,
            "lecturerId": Configuration.teacherId,
        }
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        s.close()
        self.assertEqual(3002, returnObj['code'])
        self.assertEqual("get data failed", returnObj['message'])

if __name__ == "__main__":
    unittest.main()