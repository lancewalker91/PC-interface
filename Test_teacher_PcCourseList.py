#-*- coding:utf-8 -*-
'''
Updated on Mar 29 2018

@update by: LT
'''

import unittest
from Provide import Configuration,Confirm
import os,re
from pymysql import cursors
import pymysql
from Provide.post_params import Post_Params

class Test_TeacherCourseList(unittest.TestCase):
    """测试教师课程列表接口/teacher/PcCourseList"""
    def setUp(self):
        print('test start')
        self.url = Configuration.HostUrl +"/interface/teacher/PcCourseList"
        self.v =Configuration.version
    def tearDown(self):
        print('test end')
    def create_SqlConnect(self):
        db_url = {"host":Configuration.db_host,"user":"michael","passwd":"michael","db":"db_course","charset":"utf8","cursorclass":cursors.DictCursor}
        connect = pymysql.connect(**db_url)
        connect.autocommit(True)    
        return connect
    
    #教师课程表--全部
    def test_1GetTeacherCourse_all(self):
        """班主任下的课程--默认排序 """
        self.params = {
            "keywords": "",#keywords不传为全搜
            "length": 40,
            "page": 1,
            "sort": 1000,#1000 默认 2000 学生最多 3000 最新建课 4000 进行中(暂时没有)
            "status": 0,#1 未开课  2 进行中  3 已完结
            "teacherId":Configuration.teacherId,
            "type": 0,#课程类型,0全部,1直播课,2录播课,3线下课
            "userType": 1#1 讲师 2 助教
        }
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        s.close()
        self.assertEqual(returnObj['code'],0)
        self.assertEqual(returnObj['message'],"success")
        ActualFirstCourseOfList = returnObj['result']['list']['data'][0]
        CourseProperty = ['courseId','courseName','courseImg','classList','subname','courseType','userTotal']
        text = "数据结构不匹配 Expect keys:{};response keys:{}".format(CourseProperty,ActualFirstCourseOfList.keys())
        self.assertTrue(Confirm.VerifyDataStucture(CourseProperty,ActualFirstCourseOfList.keys()),text)
        conn = self.create_SqlConnect()
        cursor = conn.cursor()
        sql = "SELECT COUNT(c.`pk_course`) AS num,c.`type` FROM t_course_teacher AS t JOIN t_course AS c ON t.`fk_course`=c.`pk_course` WHERE t.`fk_user_teacher`={} AND t.`is_teacher` =1 AND t.`status` = 1 GROUP BY c.`type`".format(Configuration.teacherId)
        cursor.execute(sql)
        rows = cursor.fetchall()
        livingNum,recordNum,underNum = 0,0,0
        for row in rows:
            if row['type'] == 1:
                livingNum = row['num']
            elif row['type'] ==2:
                recordNum = row['num']
            else:
                underNum = row['num']
        total = livingNum + recordNum + underNum
        #print(total)
        #验证课程数量           
        self.assertEqual(total,returnObj['result']['nums']['total'])
        self.assertEqual(livingNum,returnObj['result']['nums']['livingNum'])
        self.assertEqual(recordNum,returnObj['result']['nums']['recordNum'])
        self.assertEqual(underNum,returnObj['result']['nums']['underNum'])
        
        #验证课程名称
        CourseSql = "SELECT c.`pk_course`,c.`title` FROM `t_course_teacher` AS t JOIN t_course AS c ON t.`fk_course`=c.`pk_course` WHERE  t.fk_user_teacher={} AND t.`is_teacher` =1 AND t.`status` = 1".format(Configuration.teacherId)
        cursor.execute(CourseSql)
        rows = cursor.fetchall()
        num = 0 
        for courseObj in returnObj['result']['list']['data']:
            for row in rows:
                if courseObj['courseId']==row['pk_course'] and courseObj['courseName'] == row['title']:
                    num += 1
                    break
        #print(num) #取决length长度
        cursor.close()
        conn.close()        
        self.assertTrue(len(rows),num)

        #教师课程表--多班级课程
        Flag = False
        for CourseObj in returnObj['result']['list']['data']:
            if CourseObj['courseId'] == 39 and CourseObj['courseName'] == "艺术学甄选":
                ClassList = [
                    {'classId': '39', 'className': '1班', 'sectionNum': 0, 'sectionName': '第0章'},
                    {'classId': '185', 'className': '2班', 'sectionNum': 1, 'sectionName': '第1课时'}
                ]
                if ClassList == CourseObj['classList']:
                    Flag = True
                    break
        self.assertTrue(Flag, "没有返回多班级课程")

        
                   
#获取教师课程--分页，下一页
    def test_2TeacherCoursePaging(self):
        '''班主任下课程--翻页'''
        self.params = {
            "keywords": "",  # keywords不传为全搜
            "length": 20,
            "page": 2,
            "sort": 1000,#1000 默认 2000 学生最多 3000 最新建课 4000 进行中(暂时没有)
            "status": 0,  # 1 未开课  2 进行中  3 已完结
            "teacherId": Configuration.teacherId,
            "type": 0,  # 课程类型,0全部,1直播课,2录播课,3线下课
            "userType": 1  # 1 讲师 2 助教
        }
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        s.close()
        self.assertEqual(returnObj['code'], 0)
        self.assertEqual(returnObj['message'], "success")

        CourseList = returnObj['result']['list']['data']
        self.assertEqual(2,returnObj['result']['list']['page'],"没有翻页")
        self.assertEqual(2,returnObj['result']['list']['totalPage'])
        self.assertIsNotNone(CourseList,"翻页后没有数据")   
    
    #通过关键字搜索课程
    def test_3SearchCourseByKeyword(self):
        '''班主任下课程--关键词搜索'''
        keywords = "双师测试"
        self.params = {
            "keywords": keywords,  # keywords不传为全搜
            "length": 20,
            "page": 1,
            "sort": 1000,#1000 默认 2000 学生最多 3000 最新建课 4000 进行中(暂时没有)
            "status": 0,  # 1 未开课  2 进行中  3 已完结
            "teacherId": Configuration.teacherId,
            "type": 0,  # 课程类型,0全部,1直播课,2录播课,3线下课
            "userType": 1  # 1 讲师 2 助教
        }
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        s.close()
        self.assertEqual(returnObj['code'], 0)
        self.assertEqual(returnObj['message'], "success")
        courseObjs = returnObj['result']['list']['data']
        self.assertIsNotNone(courseObjs,"关键词搜索无返回结果")      
    
    #教师课程表--按学生最多排序
    def test_4TeacherCourseSortByStudent(self):
        '''班主任下课程--学生最多排序'''
        self.params = {
            "keywords": "",  # keywords不传为全搜
            "length": 20,
            "page": 1,
            "sort": 2000,  # 1000 默认 2000 学生最多 3000 最新建课 4000 进行中(暂时没有)
            "status": 0,  # 1 未开课  2 进行中  3 已完结
            "teacherId": Configuration.teacherId,
            "type": 0,  # 课程类型,0全部,1直播课,2录播课,3线下课
            "userType": 1  # 1 讲师 2 助教
        }
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        s.close()
        self.assertEqual(returnObj['code'], 0)
        self.assertEqual(returnObj['message'], "success")
        CourseList = returnObj['result']['list']['data']
        self.assertGreaterEqual(int(CourseList[0]['userTotal']),int(CourseList[1]['userTotal']))
        self.assertGreaterEqual(int(CourseList[-2]['userTotal']),int(CourseList[-1]['userTotal']),"未按学生人数倒序排序")

    
    # 按课程类型筛选---直播课
    def test_5TeacherCourseOfLiving(self):
        '''班主任下课程--直播课类型筛选'''
        self.params = {
            "keywords": "",  # keywords不传为全搜
            "length": 20,
            "page": 1,
            "sort": 1000,  # 1000 默认 2000 学生最多 3000 最新建课 4000 进行中(暂时没有)
            "status": 0,  # 1 未开课  2 进行中  3 已完结
            "teacherId": Configuration.teacherId,
            "type": 1,  # 课程类型,0全部,1直播课,2录播课,3线下课
            "userType": 1  # 1 讲师 2 助教
        }
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        s.close()
        self.assertEqual(returnObj['code'], 0)
        self.assertEqual(returnObj['message'], "success")
        courseList= returnObj['result']['list']['data']
        #判断返回的课程都是直播课
        result = True
        for course in courseList:
            if int(course['courseType']) != 1:
                result =False
                break
        self.assertTrue(result, "返回的课程包含非直播课")

if __name__ == "__main__":
    unittest.main()