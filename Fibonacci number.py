# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 15:52:30 2016

@author: Artur
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
 
class Fibonacci():
    def __init__(self,a,b):
        self.a = b
        self.b = b
        
    def series(self):
        while(True):
            yield(self.b)
            self.a,self.b = self.b,self.a + self.b
        
f = Fibonacci(0,1)
for r in f.series():
    if r > 1000:break 
    print(r,end=' ')