#-*- coding:utf-8 -*-
'''
Updated on Mar 29 2018

@update by: LT
'''

import unittest
from Provide import Confirm
from Provide import Configuration
import pymysql
import pymysql.cursors
from Provide.post_params import Post_Params

class Test_GetQuestion(unittest.TestCase):
    """测试快速出题接口/interface/plan/getQuestionId"""
    
    @classmethod
    def setUpClass(cls):
        print('test class start')
        connect_url = {"host":Configuration.db_host,"user":"michael", "passwd":"michael", "db":"db_course", "charset":"utf8", "cursorclass":pymysql.cursors.DictCursor}
        cls.connect = pymysql.connect(**connect_url)
        cls.connect.autocommit(True)
        cls.cursor = cls.connect.cursor()
    
    def setUp(self):
        print('test start')
        self.url = Configuration.HostUrl +"/interface/plan/getQuestionId"
        self.v = Configuration.version
        
    #快速出题
    def test_CreateQuestionA(self):
        """测试快速出题1个选项单选选题"""
        answer = "A"
        self.params = {"answerRight":answer,
                                 "phraseId":1,
                                 "planId":Configuration.Plan_Id
                            }

        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        self.assertEqual(0, returnObj['code'], '返回状态码不正确')
        self.assertEqual("success", returnObj['message'])
        #t_course_plan_phrase表验证
        sql = "SELECT * FROM  t_course_plan_phrase WHERE pk_plan_phrase={}".format(returnObj['result']['questId'])
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        print(result['fk_plan'],result['fk_phrase'])
        self.assertEqual(answer,result['answer_right'],"数据库表里不存在此条记录")
        s.close()

    def test_CreateQuestionB(self):
        """测试快速出题2个选项多选题"""
        answer = "A,B"
        self.params = {"answerRight":answer,
                                 "phraseId":2,
                                 "planId":Configuration.Plan_Id
                            }

        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        self.assertEqual(0, returnObj['code'], '返回状态码不正确')
        self.assertEqual("success", returnObj['message'])
        #t_course_plan_phrase表验证
        sql = "SELECT * FROM  t_course_plan_phrase WHERE pk_plan_phrase={}".format(returnObj['result']['questId'])
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        print(result['fk_plan'],result['fk_phrase'])
        self.assertEqual(answer,result['answer_right'],"数据库表里不存在此条记录")
        s.close()

    def test_CreateQuestionC(self):
        """测试快速出题3个选项多选题"""
        answer = "A,B,C"
        self.params = {"answerRight":answer,
                                 "phraseId":3,
                                 "planId":Configuration.Plan_Id
                            }

        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        self.assertEqual(0, returnObj['code'], '返回状态码不正确')
        self.assertEqual("success", returnObj['message'])
        #t_course_plan_phrase表验证
        sql = "SELECT * FROM  t_course_plan_phrase WHERE pk_plan_phrase={}".format(returnObj['result']['questId'])
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        print(result['fk_plan'],result['fk_phrase'])
        self.assertEqual(answer,result['answer_right'],"数据库表里不存在此条记录")
        s.close()

    def test_CreateQuestionD(self):
        """测试快速出题4个选项多选题"""
        answer = "A,B,C,D"
        self.params = {"answerRight":answer,
                                 "phraseId":4,
                                 "planId":Configuration.Plan_Id
                            }

        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        self.assertEqual(0, returnObj['code'], '返回状态码不正确')
        self.assertEqual("success", returnObj['message'])
        #t_course_plan_phrase表验证
        sql = "SELECT * FROM  t_course_plan_phrase WHERE pk_plan_phrase={}".format(returnObj['result']['questId'])
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        print(result['fk_plan'],result['fk_phrase'])
        self.assertEqual(answer,result['answer_right'],"数据库表里不存在此条记录")
        s.close()

    def test_CreateQuestionE(self):
        """测试快速出题5个选项多选题"""
        answer = "A,B,C,D,E"
        self.params = {"answerRight":answer,
                                 "phraseId":5,
                                 "planId":Configuration.Plan_Id
                            }

        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        self.assertEqual(0, returnObj['code'], '返回状态码不正确')
        self.assertEqual("success", returnObj['message'])
        #t_course_plan_phrase表验证
        sql = "SELECT * FROM  t_course_plan_phrase WHERE pk_plan_phrase={}".format(returnObj['result']['questId'])
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        print(result['fk_plan'],result['fk_phrase'])
        self.assertEqual(answer,result['answer_right'],"数据库表里不存在此条记录")
        s.close()

    def test_CreateQuestionF(self):
        """测试快速出题6个选项多选题"""
        answer = "A,B,C,D,E,F"
        self.params = {"answerRight":answer,
                                 "phraseId":6,
                                 "planId":Configuration.Plan_Id
                            }

        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        self.assertEqual(0, returnObj['code'], '返回状态码不正确')
        self.assertEqual("success", returnObj['message'])
        #t_course_plan_phrase表验证
        sql = "SELECT * FROM  t_course_plan_phrase WHERE pk_plan_phrase={}".format(returnObj['result']['questId'])
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        print(result['fk_plan'],result['fk_phrase'])
        self.assertEqual(answer,result['answer_right'],"数据库表里不存在此条记录")
        s.close()

    def test_CreateQuestionG(self):
        """测试快速出题7个选项多选题"""
        answer = "A,B,C,D,E,F,G"
        self.params = {"answerRight":answer,
                                 "phraseId":7,
                                 "planId":Configuration.Plan_Id
                            }

        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        self.assertEqual(0, returnObj['code'], '返回状态码不正确')
        self.assertEqual("success", returnObj['message'])
        #t_course_plan_phrase表验证
        sql = "SELECT * FROM  t_course_plan_phrase WHERE pk_plan_phrase={}".format(returnObj['result']['questId'])
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        print(result['fk_plan'],result['fk_phrase'])
        self.assertEqual(answer,result['answer_right'],"数据库表里不存在此条记录")
        s.close()

    def test_CreateQuestionH(self):
        """测试快速出题8个选项多选题"""
        answer = "A,B,C,D,E,F,G,H"
        self.params = {"answerRight":answer,
                                 "phraseId":8,
                                 "planId":Configuration.Plan_Id
                            }

        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        self.assertEqual(0, returnObj['code'], '返回状态码不正确')
        self.assertEqual("success", returnObj['message'])
        #t_course_plan_phrase表验证
        sql = "SELECT * FROM  t_course_plan_phrase WHERE pk_plan_phrase={}".format(returnObj['result']['questId'])
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        print(result['fk_plan'],result['fk_phrase'])
        self.assertEqual(answer,result['answer_right'],"数据库表里不存在此条记录")
        s.close()

    def test_CreateQuestionI(self):
        """测试快速出题判断题"""
        answer = "A"
        self.params = {"answerRight":answer,
                                 "phraseId":9,
                                 "planId":Configuration.Plan_Id
                            }

        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        self.assertEqual(0, returnObj['code'], '返回状态码不正确')
        self.assertEqual("success", returnObj['message'])
        #t_course_plan_phrase表验证
        sql = "SELECT * FROM  t_course_plan_phrase WHERE pk_plan_phrase={}".format(returnObj['result']['questId'])
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        print(result['fk_plan'],result['fk_phrase'])
        self.assertEqual(answer,result['answer_right'],"数据库表里不存在此条记录")
        s.close()

    def test_CreateQuestionJ(self):
        """测试快速出题填空题"""
        answer = "好/Abｑｂ大。"
        self.params = {"answerRight":answer,
                                 "phraseId":14,
                                 "planId":Configuration.Plan_Id
                            }

        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        self.assertEqual(0, returnObj['code'], '返回状态码不正确')
        self.assertEqual("success", returnObj['message'])
        #t_course_plan_phrase表验证
        sql = "SELECT * FROM  t_course_plan_phrase WHERE pk_plan_phrase={}".format(returnObj['result']['questId'])
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        print(result['fk_plan'],result['fk_phrase'])
        self.assertEqual(answer,result['answer_right'],"数据库表里不存在此条记录")
        s.close()

    #互动问答
    def test_CreateQuestionK(self):
        """测试询问需要"""
        answer = "A"
        self.params = {"answerRight":answer,
                                 "phraseId":10,
                                 "planId":Configuration.Plan_Id
                            }

        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        self.assertEqual(0, returnObj['code'], '返回状态码不正确')
        self.assertEqual("success", returnObj['message'])
        #t_course_plan_phrase表验证
        sql = "SELECT * FROM  t_course_plan_phrase WHERE pk_plan_phrase={}".format(returnObj['result']['questId'])
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        print(result['fk_plan'],result['fk_phrase'])
        self.assertEqual(answer,result['answer_right'],"数据库表里不存在此条记录")
        s.close()


    def test_CreateQuestionL(self):
        """测试询问明白"""
        answer = "A"
        self.params = {"answerRight": answer,
                       "phraseId": 11,
                       "planId": Configuration.Plan_Id
                       }

        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        self.assertEqual(0, returnObj['code'], '返回状态码不正确')
        self.assertEqual("success", returnObj['message'])
        # t_course_plan_phrase表验证
        sql = "SELECT * FROM  t_course_plan_phrase WHERE pk_plan_phrase={}".format(returnObj['result']['questId'])
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        print(result['fk_plan'], result['fk_phrase'])
        self.assertEqual(answer, result['answer_right'], "数据库表里不存在此条记录")
        s.close()

    def test_CreateQuestionM(self):
        """测试询问可以"""
        answer = "A"
        self.params = {"answerRight":answer,
                                 "phraseId":12,
                                 "planId":Configuration.Plan_Id
                            }

        returnObj, s = Post_Params(self.v, self.url, self.params).psot_params_returnObj()
        self.assertEqual(0, returnObj['code'], '返回状态码不正确')
        self.assertEqual("success", returnObj['message'])
        #t_course_plan_phrase表验证
        sql = "SELECT * FROM  t_course_plan_phrase WHERE pk_plan_phrase={}".format(returnObj['result']['questId'])
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        print(result['fk_plan'],result['fk_phrase'])
        self.assertEqual(answer,result['answer_right'],"数据库表里不存在此条记录")
        s.close()


    def tearDown(self):
        print('test case end')
    
    
    @classmethod
    def tearDownClass(cls):
        print('test class end')
        cls.cursor.close()
        cls.connect.close()
        
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()