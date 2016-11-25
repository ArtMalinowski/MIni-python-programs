# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 11:15:27 2016

@author: Artur
"""
from random import randint
import random, string
def random_generator(size=6, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for x in range(size))

def main():
    x = 0
    print('Welcome at my password generator')
    How_Long = int(input('How long would you like to have password'))
    password = [0]*How_Long
    print(len(password))
    for s in range(len(password)):
        randomNumber = str(randint(0,9))
        if x == 2 :
            password[s]=random_generator(1)
            x = 0
        elif x == 1 :
            password[s]=random_generator(1).lower()
            x = x +1
        else:
            password[s] = randomNumber
            x = x +1
         
    finished_Password = "".join(password)
    print(finished_Password)
        
if __name__ == "__main__":main()