# -*- coding:UTF-8 -*-
#!/usr/bin/env python3
'''
Updated on Mar 29 2018

@update by: LT
'''

import time
from datetime import datetime
import calendar


salt = "gn1002015"
HostUrl = "http://test.gn100.com"
version = "1.16.1"
#版本信息

#db 建立连接信息
db_host= "121.42.232.104"
db_user = "michael"
db_password = "michael"

db_name = "db_course"

#教师用户名和密码
mobile="17600117243"
password= "117243"
teacherId = 42

#开始上课/继续上课PlanID
Plan_Id= 6899

#学生列表
course_id = 275 #课程Id
class_id  = 353 #班级Id

#助教课程
assitant_course= 11223
assitant_course_class = 112

#获取当前时间直播列表时间
nowtime = time.localtime()
month = nowtime.tm_mon
year = nowtime.tm_year
print(month,year)
wday, monthRange = calendar.monthrange(nowtime.tm_year, nowtime.tm_mon)   # 得到本月的天数 第一返回为月第一日为星期几（0-6）, 第二返回为此月天数
querytime1 = '{}-{}-1'.format(year,month)
querytime2 = '{}-{}-{}'.format(year,month,monthRange)

