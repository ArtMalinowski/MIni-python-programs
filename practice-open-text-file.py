# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 12:17:10 2016

@author: Artur
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 12:12:04 2016

@author: Artur
"""

try:
    f = open('someText.txt')
    for line in f.readlines():
        print(line)
except IOError as e:
        print("somthing bad happened({})".format(e))

        print("aftter badness")