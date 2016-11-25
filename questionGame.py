# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 10:34:03 2016

@author: Artur
"""
from random import randint


def main():
    x = 1
    print('Welcome at my question game')
    my_random_number = randint(0,9)
    while True:
        user_exit = input("if you want exit enter exit")
        user_exit = user_exit.upper()
        if user_exit == 'EXIT':break
        guess_number = int(input("guess the number"))
        
        if guess_number < my_random_number:print('the number is too small try bigger')
        elif guess_number > my_random_number:print('the number is too big try smaller')
        else :
            print('bravo you gues the number in {} round'.format(x))
            False 
        
        x+=1
if __name__ == "__main__":main()