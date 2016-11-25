# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 13:30:27 2016

@author: Artur
"""
import numpy as np


height = np.random.uniform(1/2,5,100)
mean = 0
for n in height:
    mean = mean + n


meanHeight = mean / height.size 
meanHeight=round(meanHeight,5)
print(meanHeight)

def mean(height):
    height = np.random.uniform(1/2,5,100)

    mean = 0
    for n in height:
        mean = mean + n


    meanHeight = mean / height.size 
    return(meanHeight)


forest_means = []


for x in range(0,1000,1):
   height1 = np.random.uniform(1/2,5,100)
   m = [mean(height1)]
   forest_means += m


sortForest = forest_means
sortForest.sort()
print(sortForest)
bad_trees = []
for m in sortForest:
    if round(m,1) == 2.5:bad_trees+=[m]
if len(bad_trees) / len(sortForest) >= 1/20 :
    print("We have big problem with {} forests".format(len(bad_trees)))
    
