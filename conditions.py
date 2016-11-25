# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 15:28:35 2016

@author: Artur
"""

def condition1():
    a,b = 0,1
    if False: 
        print ('this is true')
    else:
        print('isn not true')

def condition2():
    v = 'seven'
    if v =='one':print('v is one')
    elif v == 'two': print('v is two')
    elif v == 'three': print('v is three')
    else:print('v is some oter string')
def condition3():
    a,b =0,1
    v = 'this is true' if a < b else 'this is not true '
    print (v)
condition1()
condition2()
condition3()