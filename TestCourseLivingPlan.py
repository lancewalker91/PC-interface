#-*- coding:utf-8 -*-
'''
Updated on Mar 29 2018

@update by: LT
'''
import unittest
from Provide import TestProvide,Confirm,Seek
from Provide import Configuration
from datetime import datetime
from Provide.post_params import Post_Params

class Test_courseLivingPlan(unittest.TestCase):
    '''测试获取当月直播列表接口测试/interface/course/PlanList'''

    def setUp(self):
        print('test start')
        self.url = Configuration.HostUrl +"/interface/course/PlanList"
        self.v = Configuration.Plan_Id

    def tearDown(self):
        print('test end')
    
    def test_getLivingPlan(self):
        '''测试获取指定月份直播列表'''
        teacherId = Configuration.teacherId
        month = Configuration.month
        year  =  Configuration.year
        self.params = {
            "month":month,
            "teacherId":teacherId,
            "year":year
                            }
        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        s.close()
        self.assertEqual(0, returnObj['code'], "返回态码错误")
        self.assertEqual("success", returnObj['message'])
        ExpectKeys = ['sectionDescipt','start_time','status','class_id','thumb','type','class_name','section_name','teacher_name','course_id','userTotal','num','title',
                'plan_id','course_type']
        for key in returnObj['result']:
            if returnObj['result'][key]['flag'] == 1:
                CompareObj = returnObj['result'][key]['data'][0]
                self.assertTrue(Confirm.VerifyDataStucture(ExpectKeys, CompareObj),'获取排课json与实际不符')
                break

        format = ["course_name","class_name","section_name","section_desc","course_type","plan_id","start_time","totaltime","teacher_id","teacher_real_name"]
        query = {"start_time":"2018-03-01,2018-03-31","teacher_id":teacherId,"status":"1,2,3"}
        ob = {"start_time":"asc"}
        planList,ss = Seek.seekPlan(format, query,ob)
        ss.close()
        dataList = planList['data']
        print(dataList)
        plan = []
        for v in returnObj['result'].values():
            for m in v['data']:
                plan.append(m)
        for i in range(len(dataList)):
            self.assertEqual(int(plan[i]['plan_id']),dataList[i]['plan_id'],'与中间层信息不符合')

if __name__ == "__main__":
    unittest.main()