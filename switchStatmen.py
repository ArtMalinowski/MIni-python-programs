# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 15:40:15 2016

@author: Artur
"""

def main():
    choices = dict(
        one = 'first',
        two = 'second',
        three = 'third',
        four = 'fourth',
        five = 'fifth'
        )
    v = 'two'
    print(choices.get(v,'other'))
    
if __name__ == "__main__":main()