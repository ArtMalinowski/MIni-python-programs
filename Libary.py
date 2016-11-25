# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 17:31:45 2016

@author: Artur
"""
class create_events():
    n = 'name'
    p = 'place'
    d = 'date'
    t = 'time of day'
    event = dict(
           name = n ,
           place = p ,
           date = d,
           time_of_day = t ,
    )



def main():
    
    number_of_events = int(input("how many events would you like to crete"))
    for x in range(number_of_events):
        event = "event" + str(x)
        event = create_events()
        event.n = input("Please enter a name")
        event.p = input("Plaesae enter a place of event")
        event.d = input("Please enter date of")
        event.t = input("please enter time of day")
        print(event.n,event.p,event.d,event.t)
     
        
    


if __name__ == "__main__": main();
