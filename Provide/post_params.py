#-*- coding:utf-8 -*-
'''
Updated on Mar 29 2018

@update by: LT
'''

from Provide import Configuration
import time,requests,json
from Provide import TestProvide

class Post_Params:
    def __init__(self,v,url,params):
        self.v = v
        self.url = url
        self.params = params
        self.s = requests.session()
    def psot_params_returnObj(self):
        s = TestProvide.login(self.s,Configuration.mobile,Configuration.password)
        token = s.cookies.get('token_test')
        params = {}
        timeStamp = int(time.time())
        params['u'] = 'p'
        params['v'] = self.v
        params['time'] = timeStamp
        params['token'] = token
        params['params'] = self.params
        params['key'] = TestProvide.generateKey(timeStamp, params['params'])
        print("Url: {} \nParameter:{}".format(self.url,
                                               json.dumps(params, separators=(',', ':'), ensure_ascii=False)))
        response = self.s.post(self.url, data=json.dumps(params, separators=(',', ':')))
        response.encoding = "utf-8"
        returnObj = json.loads(response.text)
        print('result:{}'.format(returnObj))
        return returnObj,s


        '''def get_token(s,mobile,password):
        s = TestProvide.login(s,mobile,password)
        token = s.cookies.get('token_test')
        return token'''
