#-*- coding:utf-8 -*-
'''
Created on 2017年3月29日

@author: lsh
'''
import pymysql
from pymysql import cursors
from Provide import Configuration

#建立数据库连接
def Generate_DB_Connect():
    connect_url = {"host":Configuration.db_host,"user":Configuration.db_user,"passwd":Configuration.db_password,
                   "db":Configuration.db_name,"charset":"utf8","cursorclass":cursors.DictCursor}
    connect = pymysql.connect(**connect_url)
    connect.autocommit(True)
    return connect  

def fetchone_fromDB(cursor,sql):
    cursor.execute(sql)
    result = cursor.fetchone()
    return result


def fetchall_fromDB(cursor,sql):
    cursor.execute(sql)
    result = cursor.fetchall()
    return result
    
def close_DB_Connect(connect):
    connect.close()
