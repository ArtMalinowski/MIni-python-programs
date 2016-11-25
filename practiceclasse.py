# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 16:00:04 2016

@author: Artur
"""

class AnimalAcitons:
    def bark(self): return self._doActiom('bark')
    def fur(self): return self._doActiom('fur')
    def quack(self): return self._doActiom('quack')
    def feathers(self): return self._doActiom('feathers')
    
    
    def _doActiom(self,action):
        if action in self.strings:
            return self.strings[action]
        else:
            return 'the {} has no {}'.format(self.animalName(),action)
    
    def animalName(self):
        return self.__class__.__name__.lower()
                
class duck(AnimalAcitons):
    strings = dict(
                  quack = "quack!!!",
                  feathers = "the duck has gray feathers"
                  )
    
class Person(AnimalAcitons):
     strings = dict(
                   bark = "tjer person say wolf",
                   fur = "the person puts on a fur coat",
                   quakc = "the person quack",
                   feathers = "ther person find feathers"
                   )
class dog(AnimalAcitons):
    strings = dict(
                  bark = "whoaf whaof",
                  fur = "the dog has whie fur "
                  )
def in_the_dogHouse(dog):
    print(dog.bark())
    print(dog.fur())
    
def in_the_forest(duck):
    print(duck.quack())
    print(duck.feathers())
    
    
def main():
    donald = duck()
    john = Person()
    fido = dog()
    
    print("... in the foest:")
    for o in (donald,john,fido):
        in_the_forest(o)
    
    print("...int the dogHouse:")
    for o in (donald,john,fido):
            in_the_dogHouse(o)
            
artmain()