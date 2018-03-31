#-*- coding:UTF-8 -*-
#!/usr/bin/env python3
'''
Created on 2016年9月26日

@author: lsh
'''

def objIsInList(obj,compareList):
    if obj in compareList:
        return True
    
    else:
        return False


def VerifyDataStucture(Expect,actual):
    for key in actual:
        if key not in Expect:
            return False
    return True

def VerifyDictEqual(comp1,comp2):
    keys = comp1.keys()
    for key in keys:
        if comp1[key] !=comp2[key]:
            return False
    
    return True         
                

